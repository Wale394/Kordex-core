# KORDEX Core

**A Python toolkit for investigating robot telemetry.**

KORDEX Core is an early-stage reliability project within Genesis. It takes recorded observations and supported telemetry inputs and organizes them into a structured investigation: data quality, patterns, available evidence, uncertainty, and recommendations for a person to review.

The aim is to make it easier to inspect what the data supports—and what it does not. KORDEX does not replace an engineer or establish a fault simply because a reading looks unusual.

## What is implemented

- Observation-quality checks and rule-based telemetry pattern analysis.
- A shared telemetry contract with validation and supported physical-unit normalization.
- Evidence synthesis, limitations, and recommendations for human review.
- Recorded telemetry replay for repeatable investigations.
- An optional, read-only MQTT subscriber.
- An adapter for supported ROS 2-style diagnostic payloads.

KORDEX Core does not publish robot commands or autonomously control equipment. The ROS 2 adapter translates payload objects; it does **not** subscribe to a live ROS 2 graph. MQTT support is optional and does not establish live-broker interoperability by itself.

## Try it locally

Python 3.11 or later is required. Core runtime dependencies are from the Python standard library.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[test]"
```

Run the synthetic recorded-data example from the repository root:

```powershell
python examples/recorded_investigation.py
```

The example generates its observations in memory. It needs no robot, external dataset, MQTT broker, or ROS 2 installation.

### Optional MQTT support

Install the MQTT extra when you want the connector available:

```powershell
python -m pip install -e ".[mqtt,test]"
```

The connector imports `paho-mqtt` lazily. No MQTT client library is bundled in the repository.

## Run the focused tests

After installing the test extra, run:

```powershell
python -m pytest -q tests/test_observation_quality.py tests/test_telemetry_pattern_engine.py tests/test_telemetry_connector_contract.py tests/test_ros2_telemetry_adapter.py tests/test_mqtt_telemetry_connector.py tests/test_mqtt_connector_engine_integration.py tests/test_evidence_synthesis.py tests/test_decision_pipeline.py
```

The MQTT tests use a mock client. These tests do not establish interoperability with a real broker or validate behavior on physical robots.

## How to interpret results

The investigation output can include observation-quality findings, evidence summaries, missing evidence, limitations, uncertainty, and a recommendation for human review. Missing telemetry is not proof that an asset is healthy, and a pattern is not by itself proof of root cause or causality. The current rule-based pipeline does not establish validated real-world failure-prediction accuracy.

**This is a research prototype, not a production reliability platform.** It has not been validated on physical robots or representative field telemetry. Do not use it as the sole basis for safety-critical maintenance or operational decisions.

## Project status

The dedicated repository is `https://github.com/Wale394/kordex-core`. Repository creation and a configured remote do not by themselves confirm that the repository is public or that GitHub security settings are enabled; check those settings on GitHub before announcing a public release.

Genesis is the broader project; KORDEX is its reliability-intelligence system; KORDEX Core is the selected Python core. The current work is focused on making telemetry investigations inspectable and repeatable. Feedback on the telemetry contract, evidence handling, architecture, and evaluation methods is welcome.

## Project documentation

- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security policy](SECURITY.md)
- [Dependencies and provenance](DEPENDENCIES_AND_PROVENANCE.md)
- [Release gate report](RELEASE_GATE_REPORT.md)
- [Publication checklist](PUBLICATION_CHECKLIST.md)
- [File inventory](FILE_INVENTORY.md)

## License

The repository includes the Apache License 2.0 text in [LICENSE](LICENSE). Its inclusion does not independently establish that every file is cleared for distribution. Review [DEPENDENCIES_AND_PROVENANCE.md](DEPENDENCIES_AND_PROVENANCE.md) and [RELEASE_GATE_REPORT.md](RELEASE_GATE_REPORT.md) for outstanding provenance, dependency, and release checks. Apache 2.0 does not grant rights to Genesis/KORDEX trademarks or marks.
