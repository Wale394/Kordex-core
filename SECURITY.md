# Security policy

KORDEX Core is an early-stage research prototype. The repository exists at <https://github.com/Wale394/kordex-core>, but this document does not assume that GitHub private vulnerability reporting is enabled or that a monitored security contact has been configured.

**Do not disclose vulnerability details in a public issue.** Before reporting a vulnerability, check the repository's **Security** tab for GitHub's private vulnerability reporting option. If it is enabled, use the repository's private **Report a vulnerability** flow. See GitHub's [private vulnerability reporting documentation](https://docs.github.com/en/code-security/how-tos/report-and-fix-vulnerabilities/report-privately). If that option is unavailable, do not post exploit details publicly; contact the repository owner through an independently verified private route.

Repository maintainers should enable and test private reporting and publish a monitored contact route before inviting external contributions.

The prototype processes telemetry locally and is not a hardened network service. MQTT authentication and TLS do not authenticate the physical origin or correctness of observations. Do not expose experimental services to untrusted networks or rely on this prototype as the sole basis for safety-critical decisions.
