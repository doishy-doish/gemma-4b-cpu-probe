# pilot-r2r3
~~~
/home/runner/.local/lib/python3.14/site-packages/huggingface_hub/utils/_validators.py:205: UserWarning: The `local_dir_use_symlinks` argument is deprecated and ignored in `hf_hub_download`. Downloading to a local directory does not use symlinks anymore.
  warnings.warn(
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
LOAD_S 11.7
=== sys-r2 GEN_S 25.6 CHARS 591 ===
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
SCORE sys-r2 diff=True file=True strip=False
=== sys-r3 GEN_S 64.9 CHARS 2686 ===
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
-from typing import O
SCORE sys-r3 diff=True file=True strip=False
~~~
