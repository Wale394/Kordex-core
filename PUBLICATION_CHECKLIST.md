# KORDEX Core publication checklist

**Status: preparation only. No repository has been created or published.** Complete the checks below before announcing a public URL.

- [ ] Review `FILE_INVENTORY.md` against the exact candidate files to be uploaded; exclude temporary environments, caches, private data, generated reports, and local research artifacts.
- [ ] Confirm the intended GitHub repository name is `kordex-core` and confirm owner authorization for public use of the Genesis/KORDEX names. The logo remains excluded.
- [ ] Create a dedicated GitHub repository. Do not import the GenesisLab repository, its Git history, working tree, or uncommitted artifacts.
- [ ] Upload only the reviewed candidate files from this directory.
- [ ] Verify GitHub displays the candidate's Apache 2.0 `LICENSE` and the expected README.
- [ ] Follow the README installation instructions and run the synthetic recorded-data example from a clean environment.
- [ ] Enable private vulnerability reporting where available and verify the private reporting flow works for repository maintainers.
- [ ] Establish a real, monitored contact route for security reports and community/Code of Conduct issues. Do not publish an invented or unmonitored address.
- [ ] Review repository visibility, collaborator permissions, branch protection/rules, and available security settings, including dependency alerts and secret scanning/push protection where available.
- [ ] Verify the public repository URL loads and points to the reviewed repository before using it in any Reddit post or other announcement.
- [ ] Before release, resolve the dependency versions/license evidence and ownership/provenance blockers in `RELEASE_GATE_REPORT.md` and `DEPENDENCIES_AND_PROVENANCE.md`.

This checklist does not assert that any GitHub setting, contact route, repository, or public URL currently exists.
