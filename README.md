# KORDEX Core

KORDEX is the reliability-investigation system within Genesis. This release candidate packages the existing Genesis investigation engine as a local, read-only Python library. It accepts recorded observations and transport-adapted packets, then returns an investigation containing observation quality, evidence, uncertainty, and human-reviewed recommendations.

## Status and boundaries

This is an **unpublished release candidate** and a research prototype. It has not been validated on physical hardware or representative field telemetry. It does not establish a live robot connection by itself, issue robot commands, or autonomously control equipment. An unusual measurement is not proof of a sensor or mechanical failure, root cause, or causality. Declared provenance and units are carried through the interface but are not independently authenticated.

The ROS 2 module adapts ROS-like diagnostic message objects. It does not subscribe to a live ROS 2 graph. MQTT is a read-only optional subscriber, not a command/control path. Recorded replay remains available for reproducible investigations.

## Requirements and installation

Python 3.11 or later is required. Core analysis uses the Python standard library.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

For MQTT support, install the optional extra:

```powershell
python -m pip install -e ".[mqtt,test]"
```

The MQTT connector lazily imports `paho-mqtt`; it is not bundled. No native ROS 2 dependency is required for the payload adapter.

## Recorded investigation example

Run this deterministic, synthetic packet replay from the candidate root:

```powershell
python examples/recorded_investigation.py
```

The script uses the public `kordex_core` API (`Genesis`, `TelemetryPacket`, and `RecordedTelemetryConnector`), converts declared source units to the contract's canonical units at the shared packet boundary, and passes the resulting records into the existing analysis engine. It prints the engine's observation-quality, evidence summary, limitations, and recommendation. No external data or robot is used.

Python API outline:

```python
from kordex_core import Genesis, TelemetryPacket

packet = TelemetryPacket(
    robot_id="demo-01",
    source="recorded-file",
    timestamp=1.0,
    signals={"motor_temperature": 40.0},
    units={"motor_temperature": "C"},
    provenance={"kind": "recorded_example"},
)
record = packet.to_genesis_record()
result = Genesis().investigate(record)
```

Physical signals require explicit supported units; see `genesis_system/adapters/telemetry_connector.py` for the canonical unit contract. Source values, source units, connector identity, timestamp, and provenance are retained in `source_metadata` where the packet contract supports them. A nonnumeric source timestamp is preserved, while the existing engine may use its ingestion-order fallback; this candidate does not alter timestamp semantics.

## What results mean

The result includes a reliability state, observation-quality status and groups, evidence synthesis, missing evidence/limitations, uncertainty, and a recommendation for human review. The pipeline does not provide a validated probability of failure when a model artifact is unavailable. Missing telemetry is not evidence that an asset is healthy. Do not use the prototype as the sole basis for safety-critical maintenance or operation.

## Focused tests

Install the test extra, then run:

```powershell
python -m pytest -q tests/test_observation_quality.py tests/test_telemetry_pattern_engine.py tests/test_telemetry_connector_contract.py tests/test_ros2_telemetry_adapter.py tests/test_mqtt_telemetry_connector.py tests/test_mqtt_connector_engine_integration.py tests/test_evidence_synthesis.py tests/test_decision_pipeline.py
```

`CONTRIBUTING.md` describes the focused test set. Tests use deterministic data and MQTT client mocks; they do not require a real broker or robot.

## Included components and provenance

The candidate contains selected existing Genesis engine, telemetry-contract, MQTT and ROS payload-adapter, focused test, and synthetic example files. It excludes the browser UI, field-agent/control-facing modules, local datasets, ABB-labeled fixtures, external predictive-maintenance data, research experiments/results, generated reports, and KORDEX SVG mark. `DEPENDENCIES_AND_PROVENANCE.md` records the selection and known provenance limits.

## Community

- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security reporting](SECURITY.md)
- [Dependency and provenance inventory](DEPENDENCIES_AND_PROVENANCE.md)
- [Bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- [Feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- [Pull request template](.github/pull_request_template.md)

This candidate has no GitHub repository yet, so those are local contribution guidance files rather than active issue links. The Apache 2.0 license is included for material the project owner is authorized to license; ownership and distribution rights must be cleared before public publication. Apache 2.0 does not grant rights to Genesis/KORDEX trademarks or marks.