You are fixing a real bug in the fastapi repository.

ISSUE (fastapi #14786, problem + reproduction only):
## Description

Fixes whitespace handling in authorization header parameter extraction to comply with [RFC 6750](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1).

## Problem

The current implementation preserves leading/trailing whitespace in the extracted credential parameter. While RFC 6750 allows one or more spaces (`1*SP`) between "Bearer" and the token, the token definition (`b64token`) doesn't include whitespace characters, meaning spaces should be treated as separators only.

This causes the extracted credentials to include extraneous whitespace, which can lead to authentication failures.

REPO FILE fastapi/security/utils.py (exact current content):
```python
from typing import Optional


def get_authorization_scheme_param(
    authorization_header_value: Optional[str],
) -> tuple[str, str]:
    if not authorization_header_value:
        return "", ""
    scheme, _, param = authorization_header_value.partition(" ")
    return scheme, param

```

TASK: Reply with ONLY a unified diff (diff --git format) that fixes the issue. No explanation.
