# KORDEX Core release gate report

**Gate result: NOT READY FOR PUBLIC RELEASE.** This report records a candidate audit only; it does not authorize publication or establish legal clearance.

## Checks performed

- Candidate contained 108 files before this report. The inventory was reviewed and updated to list this report.
- `LICENSE` SHA-256 matches the official Apache License 2.0 text at `https://www.apache.org/licenses/LICENSE-2.0.txt` byte-for-byte: `CFC7749B96F63BD31C3C42B5C471BF756814053E847C10F3EB003417BC523D30` (202 lines).
- README commands, example path, test command, optional MQTT extra, and ROS 2 payload-adapter limitation were checked against `pyproject.toml` and the candidate tree. The README explicitly states that ROS 2 does not subscribe to a live graph.
- Metadata declares Python `>=3.11`, no runtime dependencies, `pytest` as the test extra, and `paho-mqtt>=1.6` as the optional MQTT extra. This matches the documented lazy MQTT import and no native ROS 2 dependency. The build requirement is `setuptools>=68`.
- The candidate metadata supplies lower bounds or unpinned requirements, not exact resolved versions. There is no lockfile/resolved dependency list in the candidate. The dependency inventory now records the declaration and marks version/license evidence as unverified where no retained authoritative package metadata or license text exists. No dependency license is inferred from its name.
- File scan found no environment/credential/private-key-named files, cache/build/install folders, local absolute user paths, or excluded data/research/field-test directories. ABB references are explanatory exclusions in documentation; no ABB fixture is present. No bundled third-party source was identified. This is a scan, not proof of complete provenance.
- README and example describe synthetic recorded data; no real-broker or physical-robot validation is claimed.
- Candidate-focused tests and packaging/example smoke checks were run during Task 05B, not rerun for this gate. Recorded results: the README's focused pytest command completed with `116 passed`; package installation to a temporary target succeeded; the installed-package example exited successfully. No live broker or hardware test was performed.

## Release blockers and owner/legal review

1. **Chain of title:** the provenance statement is owner-provided and not independently verified. The owner must confirm authority to license every included file and copied test, including historic contributions and employment/contractor obligations. Seek qualified legal advice if ownership or rights are uncertain.
2. **Security intake:** no repository or private vulnerability-reporting channel exists yet. Configure and test a private route before external release or contributions.
3. **Project names:** Apache 2.0 does not grant trademark rights. Confirm authorization and naming strategy for Genesis/KORDEX before public release; legal advice may be appropriate.
4. **Dependencies:** exact release dependency versions and their licenses, including transitive/build dependencies, remain unverified. `DEPENDENCIES_AND_PROVENANCE.md` now records metadata constraints and evidence gaps; resolve and review the release dependency set before release.
5. **Community contact:** the Code of Conduct and security guidance need a real, monitored contact/intake route before inviting external contributors.

## Owner decisions and GitHub actions

The owner must complete the chain-of-title, AI-assisted development/third-party material, and Genesis/KORDEX name/mark checklist in `DEPENDENCIES_AND_PROVENANCE.md`. Qualified legal advice is appropriate for uncertain employment/contributor rights, third-party licensing, and trademark rights. This technical review cannot resolve those questions.

For Task 05E, the owner additionally declared that they wrote the included code with AI assistance, knowingly included no other person's code or employer-owned work, and created the Genesis/KORDEX names and logo with no known conflicting rights. These are owner declarations, not independently verified legal findings; the SVG logo remains excluded.

After repository creation, an owner must enable and verify private vulnerability reporting, establish a monitored community/security contact, and review repository access and security settings. Those settings cannot be verified in this local candidate. `DEPENDENCIES_AND_PROVENANCE.md` contains the checklist and recommends Apache-2.0-only contributions without a CLA; optional DCO sign-off is a separate lightweight provenance practice, not title clearance.

No release blocker is resolved by the metadata review alone. The candidate remains **NOT READY FOR PUBLICATION**.

## Task 05E verification status

An initial execution attempt was rejected before process startup with Windows access denied / `os error 5`. On a later shell invocation, `python --version` returned that `python` was not recognized. No usable Python interpreter or venv was available, so no isolated environment, dependency installation, resolved version/license inventory, import check, example run, MQTT optional-dependency check, or MQTT integration test was completed for Task 05E. The prior Task 05B results remain historical and were not rerun. The exact technical dependency review therefore remains blocked; see `DEPENDENCIES_AND_PROVENANCE.md`.

The attempted version check was exactly `python --version`; it failed with “The term 'python' is not recognized”. The planned isolated install command (`python -m venv <temporary-venv>` followed by `<temporary-venv>\Scripts\python -m pip install "<candidate-copy>[test,mqtt]"`) could not be run. No test command was run for Task 05E.

`PUBLICATION_CHECKLIST.md` records the repository creation and verification procedure. No remote repository or active GitHub security/contact setting exists as a result of this task.

The existing review ZIP was preserved and not refreshed; it predates the Task 05E documentation additions. Review the current candidate directory, not that earlier archive, for the owner declarations and publication checklist added in this task.

No individual copyright ownership is asserted here. The Apache license text itself is complete and unmodified; its presence does not clear rights to the candidate contents. Resolve the blockers above before describing the package as cleared for public release.

## Scope limitations

This is a local read-only analysis prototype. It does not issue robot commands or autonomously control equipment. MQTT support is an optional read-only subscriber. ROS 2 support translates payload objects and is not a native ROS 2 graph subscription. Synthetic/replay checks are not live telemetry, broker interoperability, or hardware validation.
