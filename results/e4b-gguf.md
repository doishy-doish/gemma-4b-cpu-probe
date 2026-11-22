# e4b-gguf
~~~
usage: kaggle models get [-h] [-p FOLDER] model

options:
  -h, --help         show this help message and exit
  model              Model URL suffix in format <owner>/<model-name>
  -p, --path FOLDER  Folder containing the special model-metadata.json file (https://github.com/Kaggle/kaggle-cli/blob/main/docs/models_metadata.md).
usage: kaggle models instances get [-h] [-p FOLDER] model_instance

options:
  -h, --help         show this help message and exit
  model_instance     Model variation URL suffix in format <owner>/<model-name>/<framework>/<instance-slug>
  -p, --path FOLDER  Folder for downloading the special model-instance-metadata.json file (https://github.com/Kaggle/kaggle-cli/blob/main/docs/models_metadata.md#model-instance). 
usage: kaggle models instances files [-h] [-v | --format OUTPUT_FORMAT]
                                     [--page-size PAGE_SIZE]
                                     [--page-token PAGE_TOKEN]
                                     model_instance

options:
  -h, --help            show this help message and exit
  model_instance        Model variation URL suffix in format <owner>/<model-name>/<framework>/<instance-slug>
  -v, --csv             Print results in CSV format (if not set print in table format)
  --format OUTPUT_FORMAT
                        Print results in selected format (csv, table, json). For details on advanced options, see
                        https://github.com/Kaggle/kaggle-cli/blob/main/docs/output_format.md
  --page-size PAGE_SIZE
                        Number of items to show on a page. Default size is 20, max is 200
  --page-token PAGE_TOKEN
                        Page token for results paging.
404 Client Error: Not Found for url: https://api.kaggle.com/v1/models.ModelApiService/DownloadModelInstanceVersion

The resource was not found. Check the spelling of the reference you passed.
References are usually '<owner>/<slug>', which you can find in the resource's URL.
To search for one, try 'kaggle search <query>'.
ls: cannot access 'e4b/': No such file or directory
GGUF_FILES []
Traceback (most recent call last):
  File "/home/runner/work/gemma-4b-cpu-probe/gemma-4b-cpu-probe/smoke.py", line 5, in <module>
    llm = Llama(model_path=fs[0], n_ctx=4096, verbose=False)
                           ~~^^^
IndexError: list index out of range
~~~
