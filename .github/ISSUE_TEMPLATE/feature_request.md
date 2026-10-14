---
name: Feature request
description: Suggest a focused improvement
title: "[Feature]: "
labels: [enhancement]
body:
  - type: textarea
    id: problem
    attributes:
      label: Engineering problem
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed behavior
      description: Explain how this preserves read-only operation, provenance, uncertainty, and human review.
    validations:
      required: true