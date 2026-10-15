# KORDEX Core publication checklist

**Status: repository created; public visibility and release readiness not independently verified.** Repository: <https://github.com/Wale394/kordex-core>. Complete the remaining checks before announcing a public release.

- [x] A dedicated `kordex-core` repository has been created, according to the project owner.
- [x] The candidate was uploaded to the dedicated repository, according to the project owner.
- [ ] Verify that GitHub displays the reviewed README, Apache 2.0 `LICENSE`, and expected source files.
- [ ] Confirm the repository visibility and public URL directly on GitHub; a configured remote does not prove public access.
- [ ] Review `FILE_INVENTORY.md` against the exact repository files; exclude temporary environments, caches, private data, generated reports, and local research artifacts.
- [ ] Confirm the owner has authority to license all included source and tests, including any employment, contractor, earlier-contributor, third-party, or AI-assisted material obligations.
- [ ] From a clean environment, install the package, run the synthetic recorded-data example, and run the focused tests against the current checkout.
- [ ] Generate a release-specific resolved dependency inventory or SBOM and verify direct, transitive, and build dependency licenses from authoritative metadata.
- [ ] Enable GitHub private vulnerability reporting where available and verify the private reporting flow.
- [ ] Establish a real, monitored security/community contact route; do not publish an invented or unmonitored address.
- [ ] Review collaborator permissions, branch rules/protection, dependency alerts, secret scanning, and push protection where available.
- [ ] Confirm the Genesis/KORDEX naming and trademark strategy before public release.
- [ ] Resolve the blockers in `RELEASE_GATE_REPORT.md` and `DEPENDENCIES_AND_PROVENANCE.md` before describing the package as cleared for release.
- [ ] Verify that the public URL loads and points to the reviewed repository before using it in a Reddit post or other announcement.

The checked items above record repository creation and upload as reported by the owner. They do not independently verify the remote state. This checklist does not assert that any GitHub security setting, monitored contact route, legal clearance, or public release is complete.
