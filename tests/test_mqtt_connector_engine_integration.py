import json
import unittest
from types import SimpleNamespace

from genesis import Genesis
from genesis_system.adapters.telemetry_connector import investigate_packet
from mqtt_telemetry_connector import MQTTTelemetryConnector


class FakeMQTTClient:
    def connect(self, *args):
        pass

    def loop_start(self):
        self.on_connect(self, None, {}, 0)

    def loop_stop(self):
        pass

    def subscribe(self, topic, qos=0):
        self.subscription = (topic, qos)

    def disconnect(self):
        pass

    def send(self, payload):
        self.on_message(self, None, SimpleNamespace(payload=payload, topic="robot/robot-01/telemetry"))


class MQTTConnectorEngineIntegrationTests(unittest.TestCase):
    def test_mqtt_packet_uses_same_genesis_investigation_pipeline(self):
        client = FakeMQTTClient()
        connector = MQTTTelemetryConnector(
            host="localhost", topic="robot/+/telemetry", client_factory=lambda: client,
        )
        connector.connect()
        client.send(json.dumps({
            "robot_id": "robot-01",
            "timestamp": 100.0,
            "sequence_number": 1,
            "signals": {"motor_temperature": 41.0},
            "units": {"motor_temperature": "C"},
        }).encode())
        packet = connector.read(timeout=0.1)
        record, result = investigate_packet(packet, Genesis(), connector_id=connector.connector_id)
        self.assertEqual(record["identity"]["robot_id"], "robot-01")
        self.assertEqual(record["telemetry"]["motor_temperature"], 41.0)
        self.assertEqual(record["source_metadata"]["connector_id"], "mqtt")
        self.assertEqual(result["robot"]["robot_id"], "robot-01")
        self.assertEqual(result["processing"]["observation_count"], 1)
        connector.disconnect()

    def test_mqtt_declared_fahrenheit_is_canonicalized_before_genesis(self):
        client = FakeMQTTClient()
        connector = MQTTTelemetryConnector(
            host="localhost", topic="robot/+/telemetry", client_factory=lambda: client,
        )
        connector.connect()
        client.send(json.dumps({
            "robot_id": "robot-01",
            "timestamp": 101.0,
            "sequence_number": 2,
            "signals": {"motor_temperature": 104.0},
            "units": {"motor_temperature": "F"},
            "provenance": {"controller": "drive-unit"},
        }).encode())
        packet = connector.read(timeout=0.1)
        record, result = investigate_packet(packet, Genesis(), connector_id=connector.connector_id)
        self.assertAlmostEqual(record["telemetry"]["motor_temperature"], 40.0)
        self.assertEqual(record["source_metadata"]["units"], {"motor_temperature": "C"})
        self.assertEqual(record["source_metadata"]["source_units"], {"motor_temperature": "F"})
        self.assertEqual(record["source_metadata"]["source_values"], {"motor_temperature": 104.0})
        self.assertEqual(record["source_metadata"]["provenance"]["controller"], "drive-unit")
        self.assertAlmostEqual(result["processing"]["telemetry"][-1]["motor_temperature"], 40.0)
        connector.disconnect()

    def test_rejected_mqtt_units_do_not_mutate_genesis_session(self):
        client = FakeMQTTClient()
        connector = MQTTTelemetryConnector(
            host="localhost", topic="robot/+/telemetry", client_factory=lambda: client,
        )
        engine = Genesis()
        connector.connect()
        for units in ({}, {"motor_temperature": "mV"}):
            client.send(json.dumps({
                "robot_id": "robot-01",
                "timestamp": 100.0,
                "signals": {"motor_temperature": 40.0},
                "units": units,
            }).encode())
            packet = connector.read(timeout=0.1)
            with self.assertRaisesRegex(ValueError, "missing or unsupported unit"):
                investigate_packet(packet, engine, connector_id=connector.connector_id)
            self.assertEqual(engine._records_by_robot, {})

        client.send(json.dumps({
            "robot_id": "robot-01",
            "timestamp": 101.0,
            "signals": {"motor_temperature": 104.0},
            "units": {"motor_temperature": "F"},
        }).encode())
        packet = connector.read(timeout=0.1)
        record, result = investigate_packet(packet, engine, connector_id=connector.connector_id)
        self.assertAlmostEqual(record["telemetry"]["motor_temperature"], 40.0)
        self.assertEqual(result["processing"]["observation_count"], 1)
        connector.disconnect()


if __name__ == "__main__":
    unittest.main()
