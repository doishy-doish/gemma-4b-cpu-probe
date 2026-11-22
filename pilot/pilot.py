import time
from llama_cpp import Llama
t0 = time.time()
llm = Llama.from_pretrained(repo_id="Qwen/Qwen2.5-3B-Instruct-GGUF", filename="qwen2.5-3b-instruct-q4_k_m.gguf", n_ctx=8192, verbose=False)
print("LOAD_S", round(time.time() - t0, 1), flush=True)
task = open("pilot/task.md").read()
for rnd, temp in [(1, 0.0), (2, 0.7), (3, 0.7)]:
    for tag in ["sys-r2", "sys-r3"]:
        sysp = open("pilot/" + tag + ".md").read()
        t2 = time.time()
        o = llm.create_chat_completion(messages=[{"role": "system", "content": sysp}, {"role": "user", "content": task}], max_tokens=512, temperature=temp)
        dt = round(time.time() - t2, 1)
        c = o["choices"][0]["message"]["content"]
        print("=== r" + str(rnd) + " " + tag + " GEN_S " + str(dt) + " CHARS " + str(len(c)) + " ===", flush=True)
        print(c[:1200], flush=True)
        print("SCORE r" + str(rnd) + " " + tag + " diff=" + str("@@" in c) + " file=" + str("utils.py" in c) + " strip=" + str("strip" in c), flush=True)
