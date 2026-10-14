---
name: Bug report
description: Report a reproducible KORDEX Core defect
title: "[Bug]: "
labels: [bug]
body:
  - type: textarea
    id: summary
    attributes:
      label: What happened?
      description: Do not include private telemetry, credentials, or security-sensitive details.
    validations:
      required: true
  - type: textarea
    id: reproduce
    attributes:
      label: Minimal reproducible example
      description: Use synthetic or rights-cleared data and redact source identifiers.
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected behavior
    validations:
      required: true
  - type: input
    id: environment
    attributes:
      label: Python version and operating system