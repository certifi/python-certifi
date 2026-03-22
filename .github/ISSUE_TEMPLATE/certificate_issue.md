---
name: Bug Report or Feature Request
about: Report a bug or suggest a feature for certifi
title: ''
labels: ''
assignees: ''
---

**Important:** Certifi is a repackaging of the [Mozilla CA Certificate Program](https://wiki.mozilla.org/CA) root certificates. It does not add, remove, or modify certificates. If you are looking to:

- **Add a custom or organizational certificate**: See the [Requests documentation on SSL certificates](https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification) or set the `REQUESTS_CA_BUNDLE` environment variable to point to your custom bundle.
- **Fix a missing intermediate certificate error**: This is typically a server-side configuration issue. See [this StackOverflow answer](https://stackoverflow.com/a/66111417) for guidance.
- **Add a certificate to the Mozilla bundle**: File a bug with [Mozilla's CA Certificate Program](https://bugzilla.mozilla.org/enter_bug.cgi?product=CA%20Certificates&component=CA%20Certificate%20Root%20Program).
- **Report a missing/revoked root certificate**: File a bug with [Mozilla](https://bugzilla.mozilla.org/enter_bug.cgi?product=CA%20Certificates&component=CA%20Certificate%20Root%20Program) since certifi tracks their bundle.

---

**Description**
<!-- A clear description of your bug report or feature request. -->
