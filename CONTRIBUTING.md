# Contributing to KORDEX Core

KORDEX Core is an early-stage reliability-investigation prototype. Before accepting outside contributions, maintainers must confirm the licensing and provenance of the existing source and establish a monitored contribution and private security-reporting process. The repository is available at <https://github.com/Wale394/kordex-core>; its visibility and security settings must be checked on GitHub.

## Contribution expectations

- Keep KORDEX read-only. Do not add robot-command publication, automatic control, or autonomous actuation.
- Preserve canonical-unit validation, source identity, timestamp meaning, provenance, data quality, uncertainty, and the distinction between an observation and a confirmed fault.
- Keep changes focused and add deterministic tests for behavior changes.
- Do not add private telemetry, real-robot datasets, credentials, generated reports, or unverified research outputs.
- State when data or code is generated or derived and document its source and license.
- Avoid claims of field validation, failure-prediction accuracy, or integration that the implementation and evidence do not support.

## Development setup and checks

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
python -m pytest -q tests/test_observation_quality.py tests/test_telemetry_pattern_engine.py tests/test_telemetry_connector_contract.py tests/test_ros2_telemetry_adapter.py tests/test_mqtt_telemetry_connector.py tests/test_mqtt_connector_engine_integration.py tests/test_evidence_synthesis.py tests/test_decision_pipeline.py
python examples/recorded_investigation.py
```

The MQTT tests use mocks and do not need a broker. The ROS 2 adapter tests do not require a ROS installation. Report unavailable optional dependencies and do not claim hardware validation when none was performed.

## Contribution rights and sign-off

Contributors should review the repository license and ensure they have the right to submit their work under it. A Developer Certificate of Origin sign-off (`Signed-off-by:`) may be adopted as a lightweight provenance practice; it does not establish rights to existing files, transfer copyright, or authorize relicensing. No CLA is introduced by this candidate. Contributors retain copyright in their contributions, subject to the applicable project license grant.

Do not disclose security vulnerabilities in public issues. Follow [SECURITY.md](SECURITY.md) and use a verified private reporting route.
