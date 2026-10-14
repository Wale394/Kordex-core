# Dependencies and provenance inventory

## Included code

The candidate contains the existing Genesis source needed for the public `Genesis.investigate` API and shared telemetry contract:

- `genesis_system/core/`: quality checks, normalization, evidence, uncertainty, history, memory, and incident/investigation utilities.
- `genesis_system/robotics/`: feature, reliability-state, fusion, and recommendation components used by the analysis path.
- `genesis_system/runtime/`: Genesis facade and decision pipeline.
- `genesis_system/adapters/telemetry_connector.py`, `mqtt_telemetry_connector.py`, and `ros2_telemetry_adapter.py`.
- Top-level compatibility modules listed in `pyproject.toml`, including the evidence timeline and fleet-registry imports, retained because the existing engine imports those names.
- Focused copied tests under `tests/` and the synthetic example under `examples/`.

The project owner states they authored the project code with AI assistance. That is an owner-provided provenance statement, not an independent authorship or title review. The existing source tree contained no license file or source-level copyright/SPDX notices in the selected paths. No individual copyright notice is added because the owner's legal name and the rightsholder entity/year were not established here. Before publication, confirm the owner has authority to license all included files and that no employment, contractor, or earlier-contributor rights apply.

### Owner declarations recorded for Task 05E

The owner has stated that they wrote the included code with AI assistance; that no other person's code or employer-owned work is knowingly included; and that they created the Genesis/KORDEX names and logo and know of no conflicting rights. These statements are recorded as owner declarations only. They are not independently verified, do not establish chain of title, and are not legal clearance. The KORDEX SVG mark remains excluded from this candidate.

### Lineage findings and limits

- **Technical finding:** included engine/adapters are selected copies from the Genesis source tree; the package candidate does not carry a complete source-repository history that independently establishes authorship or rights. Included tests are copied project tests. The lack of copyright headers or third-party attribution in the selected paths is an observation, not proof of original authorship or permission.
- **Technical finding:** the included recorded example generates observations in memory. The candidate scan identified no bundled third-party source, real-data directory, generated investigation report, ABB fixture, or external dataset. This scan cannot detect all copied/generated snippets or determine rights from content alone.
- **Owner declaration:** project code was written by the owner with AI assistance. No independent record of the AI tools, prompts, sources, or code-level contribution boundaries was available in the candidate.
- **Unresolved:** confirm whether any included code or tests were contributed under employment, contractor, assignment, prior collaboration, or other terms; identify any third-party or AI-generated material incorporated into them; and verify the owner/rightsholder has authority to grant Apache 2.0 rights.

The checklist below is a request for owner evidence and decisions, not a conclusion that any item is cleared.

## Excluded material

Not copied: `data/`, `real_data/`, the external predictive-maintenance dataset and derived outputs, research/experiment workflows and result CSVs, generated reports/caches, local artifacts, `GENESIS_FIELD_TEST/`, root research/demo scripts, ABB-labeled fixtures, the KORDEX SVG mark, `genesis_interface/`, field-agent/robot-action-facing modules, and the real-robot dataset adapter. The local interface was omitted so the installable Core does not depend on its prototype HTTP/server packaging.

## Runtime/build/test dependencies

- Runtime Core: Python standard library only; `pyproject.toml` declares no runtime dependencies.
- Build: `setuptools>=68` through PEP 517 build isolation. The lower bound is declared; the exact build version resolved for a future release is not pinned here.
- Tests: optional `pytest` extra. No exact version is pinned in project metadata, and its resolved version/license must be checked for the release environment.
- MQTT: optional `paho-mqtt>=1.6` extra. The lower bound is declared; no exact version is pinned. The connector lazily imports this package and no third-party source is bundled in this candidate. The MQTT tests included here use a mock client; broker interoperability is not claimed.
- ROS 2: payload translation only, with no `rclpy` dependency and no native subscription.

### Targeted license-evidence inventory

This inventory distinguishes declared constraints from resolved distributions. No lockfile or release-specific resolved dependency list is included, so exact installed versions cannot be established from this candidate's metadata alone.

| Component | Evidence in candidate | Version evidence | License evidence | Status |
|---|---|---|---|---|
| Python standard library | Core imports and `dependencies = []` in `pyproject.toml` | Runtime floor `>=3.11`; exact interpreter is environment-specific | Supplied with the selected Python distribution; distribution-specific licensing was not audited here | No third-party Python runtime package declared |
| setuptools | `[build-system].requires = ["setuptools>=68"]` | Lower bound only; no lock/pin | No release-environment package metadata or license text recorded in this candidate | Must verify resolved build version and license |
| pytest | Optional `test = ["pytest"]` | Unbounded constraint; no exact version | No release-environment package metadata or license text recorded in this candidate | Must verify if tests are distributed/run as a supported extra |
| paho-mqtt | Optional `mqtt = ["paho-mqtt>=1.6"]`; lazy import in connector | Lower bound only; no exact version | No release-environment package metadata or license text recorded in this candidate | Must verify resolved optional version and license before offering MQTT extra |

The previous Task 05B install/smoke report does not provide a retained lockfile or dependency-license manifest. Do not treat package names, common upstream licensing, or a successful install as license evidence. Generate a release-specific resolved dependency/SBOM and inspect authoritative package metadata and license texts before release. Transitive dependencies, including build-backend dependencies, also need review. No dependency-license conclusion is asserted here.

#### Task 05E isolated resolution attempt

The candidate metadata was re-read for this task. The isolated-environment attempt was blocked: an initial command was rejected before process startup with Windows access denied / `os error 5`; when shell execution later started, `python --version` failed because `python` was not recognized. No usable Python command or venv was available in this task environment. Therefore no fresh environment was created and no 05E dependency installation, resolved-version inventory, metadata/license inspection, import check, example run, optional-dependency check, or MQTT integration test was performed. This is an environment/tooling limitation, not a package-install failure. The earlier Task 05B successful temporary installation and example run remain prior results only and do not supply exact resolved dependency versions or licenses.

## License and third-party notices

`LICENSE` contains the Apache License 2.0 text. There were no discovered third-party source files, attribution notices, or bundled libraries in this selected subset. A clean scan is not proof that every file is original or that all historical rights are clear. Apache licensing applies only to material the project owner is authorized to license. The license does not grant rights to Genesis/KORDEX names or marks; the SVG mark is excluded.

## Data and example provenance

`examples/recorded_investigation.py` generates all observations in memory and labels them as synthetic. No dataset is distributed. Tests use deterministic inline fixtures and copied project tests. No ABB-labeled fixture or derived research result is included.

## Known release blockers

1. The owner must verify ownership and license authority for all included code and copied tests, including historic contributions and employment/contractor obligations.
2. Configure an actual private security report channel and conduct-policy contact before inviting external contributions. `SECURITY.md` currently documents that no channel exists yet.
3. Resolve exact dependencies and verify their licenses for a published/supported release, including transitive and build dependencies.
4. Decide whether names may be used in a public repository; Apache 2.0 does not grant trademark rights.

## Owner-confirmation checklist (not legal clearance)

- [ ] Confirm authority to license every included source and copied test under Apache License 2.0; check employment, contractor, prior contributor, and other assignment obligations.
- [ ] Confirm which code was AI-assisted, what tools or inputs were used where relevant, and that no third-party prompts, generated snippets, or source material with incompatible terms were incorporated. AI assistance alone does not establish ownership or clear third-party rights.
- [ ] Confirm no omitted third-party code, fixtures, generated content, data, or attribution obligations remain in the selected files; provide evidence for any newly identified material.
- [ ] Decide whether Genesis/KORDEX names may be used for the public project and whether any marks are owned or licensed by another party. `LICENSE` grants no trademark rights.
- [ ] Establish an owner-approved, monitored security and community contact before accepting outside reports or contributions.

For an Apache-2.0-only project, the simplest starting contribution policy is to accept contributions under the repository's Apache-2.0 license and require no CLA. A DCO sign-off may be adopted as a lightweight provenance attestation, but it is not proof of title and cannot cure uncertainty in existing code. Do not introduce a CLA unless the owner has a concrete relicensing/dual-licensing need and obtains appropriate legal advice. Contributors retain their copyright while granting the permissions specified by Apache 2.0; the project must not imply that contribution transfers ownership.

## GitHub setup after repository creation

These actions cannot be completed in this local candidate:

1. Enable GitHub private vulnerability reporting in repository Security settings, submit a test/verification using GitHub's supported private reporting flow, and ensure an owner is assigned to monitor incoming reports.
2. Choose and publish a real, monitored contact route for community issues and the Code of Conduct; do not add an unmonitored or invented address.
3. Verify repository visibility and security settings before release: branch protections/rules, secret scanning and push protection availability, dependency graph/alerts, access and collaborator permissions, and the configured security policy. Record settings appropriate to the chosen GitHub plan and repository.

Private reporting and contact setup require a created repository and owner action; the candidate does not claim these settings are active.
