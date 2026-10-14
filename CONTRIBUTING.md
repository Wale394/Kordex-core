# Contributing to KORDEX Core

This repository is an unpublished release candidate. Before accepting outside contributions, the project owner must confirm the release license, rights to the existing source, and a private security-reporting channel.

## Contribution expectations

- Keep KORDEX read-only. Do not add robot command publication, automatic control, or autonomous actuation.
- Preserve canonical-unit validation, source identity, timestamp meaning, provenance, data quality, uncertainty, and the distinction between an observation and a confirmed fault.
- Keep changes focused and add deterministic tests for behavior changes.
- Do not add private telemetry, real-robot datasets, credentials, generated reports, or unverified research outputs.
- State when data or code is generated or derived and document its source and license.

## Development setup and checks

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
python -m pytest -q tests/test_observation_quality.py tests/test_telemetry_pattern_engine.py tests/test_telemetry_connector_contract.py tests/test_ros2_telemetry_adapter.py tests/test_mqtt_telemetry_connector.py tests/test_mqtt_connector_engine_integration.py tests/test_evidence_synthesis.py tests/test_decision_pipeline.py
python examples/recorded_investigation.py
```

The MQTT tests use mocks and do not need a broker. The ROS 2 adapter tests do not require a ROS installation. Report any unavailable optional dependency and do not claim hardware validation.

## Submission rights and sign-off

The project recommends adopting Developer Certificate of Origin 1.1 sign-off (`Signed-off-by:`) for future contributions after maintainers publish the project contribution process. A DCO records a contributor's certification for that contribution; it does not establish rights to existing files, transfer copyright, or authorize relicensing. No CLA is introduced by this candidate. Contributors retain copyright in their own contributions, subject to the project license grant that applies to accepted submissions.

Until a repository and contribution workflow exist, do not submit a pull request or disclose security vulnerabilities publicly.