# KORDEX Core release gate report

**Gate result: NOT READY FOR PUBLIC RELEASE.** The dedicated repository has been created and the candidate uploaded, according to the project owner. This local report does not independently verify repository visibility, remote contents, GitHub settings, legal clearance, or the state of the current remote branch.

## What the candidate contains

The candidate packages selected Genesis investigation-engine modules, the shared telemetry contract, an optional MQTT subscriber, a ROS 2-style payload adapter, focused tests, and a synthetic recorded-data example. The Core has no declared runtime dependencies beyond the Python standard library. The optional dependency groups are `test = ["pytest"]` and `mqtt = ["paho-mqtt>=1.6"]`; the build requirement is `setuptools>=68`.

The included example generates observations in memory. MQTT tests use a mock client. ROS 2 support translates supported payload objects and does not subscribe to a live ROS 2 graph. No physical-robot validation, representative field-telemetry validation, real-broker interoperability, or validated real-world failure-prediction accuracy is established.

## Evidence recorded in the candidate

- The `LICENSE` file contains the Apache License 2.0 text. Its presence does not establish authority to license every included file.
- The metadata declares Python `>=3.11`, no runtime dependencies, an optional `pytest` extra, an optional `paho-mqtt>=1.6` extra, and `setuptools>=68` for building.
- The candidate's dependency constraints are not a release lockfile. Exact resolved versions, license texts, and transitive/build dependency evidence remain to be collected and reviewed.
- Prior Task 05B records reported 116 focused tests passing, a successful temporary package installation, and a successful synthetic example. Those results are historical and were not rerun as part of the original Task 05E check. Do not treat them as verification of a later GitHub checkout.
- The previous Task 05E execution attempt could not run Python in its Windows environment. That limitation explains why that attempt did not produce fresh test or dependency-resolution results; it does not establish that the package itself failed.
- A local file scan is not proof of complete provenance or legal clearance.

## Release blockers

1. **Ownership and provenance:** the owner's authorship and rights statements are owner declarations, not independent verification. Confirm authority to license every included source file and copied test, including employment, contractor, earlier-contributor, third-party, and AI-assisted material considerations.
2. **Dependencies:** resolve and review exact direct, transitive, and build dependencies and their licenses for the intended release environment. Retain a release-specific resolved inventory or SBOM.
3. **Security intake:** verify repository security settings, enable private vulnerability reporting where available, and test the reporting route. Establish a monitored contact for security and community concerns.
4. **Repository state:** verify current remote contents, visibility, collaborator permissions, branch rules, and relevant security features directly on GitHub.
5. **Names and marks:** Apache 2.0 does not grant trademark rights. Confirm the intended Genesis/KORDEX naming and mark strategy before public release.
6. **Current-checkout verification:** run installation, the synthetic example, and the focused tests against the exact checkout intended for release. Record observed results, not historical results.

## Owner decisions and GitHub actions

The owner must resolve the provenance and naming questions, and verify repository visibility and security settings. Qualified legal advice may be appropriate where ownership, employment/contributor rights, third-party licensing, or trademark rights are uncertain. This technical report is not legal advice or legal clearance.

`PUBLICATION_CHECKLIST.md` tracks the remaining tasks. Repository creation and upload are recorded as owner-reported facts; private reporting, a monitored contact route, dependency-license clearance, and public visibility are not claimed to be complete.

## Scope limitations

KORDEX Core is a local, read-only analysis prototype. It does not issue robot commands or autonomously control equipment. MQTT support is an optional read-only subscriber. ROS 2 support translates payloads and is not a native live graph subscription. Synthetic and replay checks do not establish field performance, broker interoperability, or hardware validation.
