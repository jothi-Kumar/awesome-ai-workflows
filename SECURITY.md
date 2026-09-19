# Security Policy

## Supported versions

Security fixes are applied to the current default branch unless a release-specific support policy is announced.

## Reporting a vulnerability

Do not disclose exploitable security vulnerabilities in a public issue.

Use GitHub's private vulnerability reporting/security advisory mechanism when available. If that mechanism is unavailable, contact the repository maintainer privately through the contact method published in the repository profile.

Include:

- Affected file or component
- Description of the vulnerability
- Reproduction steps or proof of concept
- Potential impact
- Suggested mitigation, if known

Please do not include real credentials, customer data, or other secrets in a report.

## Secrets

Never commit:

- API keys
- Access tokens
- Passwords
- Private certificates
- Cloud credentials
- Production configuration containing secrets

If a secret is accidentally committed, revoke or rotate it immediately. Removing the file from the latest commit does not necessarily remove it from Git history.
