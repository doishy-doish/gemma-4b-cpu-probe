# e4b-gguf
~~~
/home/runner/work/_temp/6d28ba25-7334-41b9-97f2-e38b9982a4b7.sh: line 1: kaggle: command not found
ls: cannot access 'e4b/': No such file or directory
GGUF_FILES []
Traceback (most recent call last):
  File "/home/runner/work/gemma-4b-cpu-probe/gemma-4b-cpu-probe/smoke.py", line 5, in <module>
    llm = Llama(model_path=fs[0], n_ctx=4096, verbose=False)
                           ~~^^^
IndexError: list index out of range
~~~
