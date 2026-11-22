# smoke-25
~~~
/home/runner/.local/lib/python3.14/site-packages/huggingface_hub/utils/_validators.py:205: UserWarning: The `local_dir_use_symlinks` argument is deprecated and ignored in `hf_hub_download`. Downloading to a local directory does not use symlinks anymore.
  warnings.warn(
Warning: You are sending unauthenticated requests to the HF Hub. Please set a HF_TOKEN to enable higher rate limits and faster downloads.
LOAD_S 10.2
GEN1_S 2.6 CHARS 25
REPLY1-BEGIN
more_itertools/chunked.py
REPLY1-END
GEN2_S 7.6 CHARS 256
REPLY2-BEGIN
```
diff --git a/script.py b/script.py
@@ -1,6 +1,6 @@
 def chunked(seq, size):
-    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
+    return (seq[pos:pos + size] for pos in range(0, len(seq) - size, size) if pos + size <= len(seq))
```
REPLY2-END
~~~
