"""Replay a deterministic synthetic telemetry sequence through KORDEX Core."""
import json

from kordex_core import Genesis, RecordedTelemetryConnector, TelemetryPacket


SIGNALS = {
    "motor_temperature": "C", "ambient_temperature": "C", "battery_level": "%",
    "battery_voltage": "V", "battery_current": "A", "battery_temperature": "C",
    "power_consumption": "W", "voltage_drop": "V", "workload": "%",
}


def main():
    packets = []
    for index, motor_temperature in enumerate((40.0, 41.2, 53.0), start=1):
        packets.append(TelemetryPacket(
            robot_id="synthetic-demo-01", source="recorded-synthetic-example",
            timestamp=float(index), sequence_number=index,
            signals={
                "motor_temperature": motor_temperature, "ambient_temperature": 22.0,
                "battery_level": 84.0, "battery_voltage": 24.0, "battery_current": 2.1,
                "battery_temperature": 27.0, "power_consumption": 48.0,
                "voltage_drop": 0.2, "workload": 35.0, "robot_state": "working",
            },
            units=SIGNALS,
            provenance={"kind": "synthetic_example", "record_index": index},
            limitations=("Synthetic demonstration only; not robot telemetry.",),
        ))

    connector = RecordedTelemetryConnector(packets, connector_id="recorded-synthetic-example")
    connector.connect()
    try:
        records = []
        while (packet := connector.read()) is not None:
            records.append(packet.to_genesis_record(connector_id=connector.connector_id))
    finally:
        connector.disconnect()

    result = Genesis().investigate(records)
    synthesis = result.get("evidence_synthesis") or {}
    view = {
        "robot": result.get("robot"),
        "observation_quality": result.get("observation_quality"),
        "evidence_summary": synthesis.get("summary"),
        "supporting_evidence": synthesis.get("observations", []),
        "missing_evidence": synthesis.get("missing_evidence", []),
        "uncertainty_and_limitations": result.get("limitations", []),
        "recommendation_for_human_review": result.get("recommendation"),
        "latest_source_metadata": records[-1].get("source_metadata"),
    }
    print(json.dumps(view, indent=2, ensure_ascii=False, allow_nan=False))


if __name__ == "__main__":
    main()