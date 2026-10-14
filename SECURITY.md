# Security policy

This is an unpublished release candidate; it has no active GitHub repository or private vulnerability intake channel yet.

Before inviting contributions or publishing a repository, the owner must enable GitHub private vulnerability reporting. Once enabled, report privately from the repository's Security/Advisories page using **Report a vulnerability**. GitHub's private reporting flow is documented at https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately . Do not report vulnerabilities in a public issue. Until the repository and private route exist, do not send vulnerability details through public channels; there is no verified project email address to provide.

The prototype processes telemetry locally and is not a hardened network service. MQTT authentication and TLS settings do not authenticate the physical origin or correctness of observations. Do not expose experimental services to untrusted networks.