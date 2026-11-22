# pilot-r2r3
~~~
/home/runner/.local/lib/python3.14/site-packages/huggingface_hub/utils/_validators.py:205: UserWarning: The `local_dir_use_symlinks` argument is deprecated and ignored in `hf_hub_download`. Downloading to a local directory does not use symlinks anymore.
  warnings.warn(
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
LOAD_S 13.9
=== r1 sys-r2 GEN_S 25.4 CHARS 591 ===
```diff
diff --git a/fastapi/security/utils.py b/fastapi/security/utils.py
--- a/fastapi/security/utils.py
+++ b/fastapi/security/utils.py
@@ -1,4 +1,4 @@
-from typing import Optional
+from typing import Optional, Tuple
+
 def get_authorization_scheme_param(
     authorization_header_value: Optional[str],
 ) -> Tuple[str, str]:
-    if not authorization_header_value:
-        return "", ""
+    if not authorization_header_value or authorization_header_value.isspace():
+        return "", ""
     scheme, _, param = authorization_header_value.partition(" ")
     return scheme, param
```
SCORE r1 sys-r2 diff=True file=True strip=False
=== r1 sys-r3 GEN_S 65.9 CHARS 2686 ===
```diff
diff --git a/fastapi/security/utils.py b/fastapi/security/utils.py
--- a/fastapi/security/utils.py
+++ b/fastapi/security/utils.py
@@ -1,4 +1,4 @@
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typing import Optional
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typing import Optional
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typing import Optional
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typing import Optional
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typing import Optional
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typing import Optional
-from typing import Optional
+from typing import Optional, Tuple
 from typing import Optional
 from typing import Optional
 from typi
SCORE r1 sys-r3 diff=True file=True strip=False
=== r2 sys-r2 GEN_S 64.9 CHARS 2889 ===
```diff
diff --git a/fastapi/security/utils.py b/fastapi/security/utils.py
--- a/fastapi/security/utils.py
+++ b/fastapi/security/utils.py
@@ -1,5 +1,5 @@
 from typing import Optional
-from typing import str
+from typing import str, Sequence
 from typing import Tuple
 
 from fastapi import HTTPException
 from fastapi.security.base import SecurityBase
 from fastapi.security.base import BaseAuth
 from fastapi.security.base import HTTPAuthorizationCredentials
 from fastapi.security.base import HTTPAuthorization
 from fastapi.security.base import BaseAuthCredentials
 from fastapi.security.base import SecurityCredentials
 from fastapi.security.base import HTTPAuthorizationCredentials
 from fastapi.security.base import HTTPAuthorization
 from fastapi.security.base import BaseAuth
 from fastapi.security.base import HTTPAuthorizationCredentials
 from fastapi.security.base import HTTPAuthorization
 from fastapi.security.base import BaseAuthCredentials
 from fastapi.security.base import SecurityCredentials
 from fastapi.security.base import HTTPAuthorizationCredentials
 from fastapi.security.base import HTTPAuthorization
 from fastapi.security.base import BaseAuth
 from fastapi.security.base
SCORE r2 sys-r2 diff=True file=True strip=False
=== r2 sys-r3 GEN_S 65.8 CHARS 2860 ===
```diff
diff --git a/fastapi/security/utils.py b/fastapi/security/utils.py
--- a/fastapi/security/utils.py
+++ b/fastapi/security/utils.py
@@ -1,4 +1,4 @@
-from typing import Optional
+from typing import Optional, Pattern
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import Optional
 from typing import O
SCORE r2 sys-r3 diff=True file=True strip=False
=== r3 sys-r2 GEN_S 21.8 CHARS 540 ===
```diff
diff --git a/fastapi/security/utils.py b/fastapi/security/utils.py
--- a/fastapi/security/utils.py
+++ b/fastapi/security/utils.py
@@ -1,4 +1,4 @@
-from typing import Optional
+from typing import Optional, str
 ...
-    if not authorization_header_value:
+    if not authorization_header_value or authorization_header_value.isspace():
         return "", ""
-    scheme, _, param = authorization_header_value.partition(" ")
+    scheme, param = authorization_header_value.partition(" ")
     return scheme, param
```

Patch Size: 16
SCORE r3 sys-r2 diff=True file=True strip=False
=== r3 sys-r3 GEN_S 19.5 CHARS 430 ===
```diff
diff --git a/fastapi/security/utils.py b/fastapi/security/utils.py
@@ -22,7 +22,7 @@
     if not authorization_header_value:
         return "", ""
     scheme, _, param = authorization_header_value.partition(" ")
-    return scheme, param
+    return scheme.strip(), param.strip()
```

This diff removes the whitespace characters from the extracted credential parameter by applying `strip()` to both `scheme` and `param`.
SCORE r3 sys-r3 diff=True file=True strip=True
~~~
