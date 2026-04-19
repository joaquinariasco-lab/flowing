# Security Policy

## Supported Versions

Security updates are provided only for the latest stable release.

| Version | Supported          |
|---------|-------------------|
| latest  | ✅ Yes            |
| < latest | ❌ No            |

If you are using an older version, you are expected to upgrade before reporting issues unless the issue is critical and reproducible on the latest version.

---

## Reporting a Vulnerability

If you discover a security vulnerability, **do not open a public issue**.

Instead, report it privately:

- Email: joaquin.arias.co@gmail.com
- Or use a private security advisory (if GitHub enabled)

Please include:

- Description of the vulnerability
- Steps to reproduce
- Affected versions
- Potential impact
- Any suggested fix (if available)

---

## Response Time

We aim to:

- Acknowledge reports within **48 hours**
- Provide an initial assessment within **5 business days**
- Release a fix as soon as possible depending on severity

Critical vulnerabilities may trigger immediate hotfix releases.

---

## Scope

The following are considered in scope:

- Core repository code
- Official packages published by this project
- Default configurations and integrations

Out of scope:

- Third-party dependencies
- User-custom modifications
- External integrations not maintained by this project

---

## Disclosure Policy

- Vulnerabilities are handled privately until a fix is released
- We may credit reporters unless anonymity is requested
- After resolution, a security advisory may be published

---

## Security Best Practices for Users

To reduce risk:

- Always use the latest stable version
- Avoid exposing internal APIs publicly
- Validate all external inputs when integrating this tool
- Run in restricted environments when handling untrusted data

---

## Final Note

Security is a core priority of this project. We treat vulnerabilities as high-severity issues and respond accordingly to ensure the tool remains safe for production-scale usage.
