"""Times the full pipeline per question for criterion 5. Measures only; changes nothing."""
import argparse
import time

import config
import gate
import questions as qs
from generate import answer_from_chunks
from store import search

p = argparse.ArgumentParser()
p.add_argument("--label", default="timing")
p.add_argument("--runs", type=int, default=3)
p.add_argument("--threshold", type=float, default=None)
args = p.parse_args()
threshold = config.THRESHOLD if args.threshold is None else args.threshold


def one(question):
    start = time.perf_counter()
    results = search(question, top_k=config.TOP_K, corpus=config.CORPUS, variant="default")
    decision = gate.check(results, threshold=threshold)
    if decision.passed:
        answer_from_chunks(question, results, cache=False)
    return time.perf_counter() - start, decision.passed


items = qs.answered()
warm, _ = one(items[0]["question"])
out = [f"cutoff {threshold}, top-k {config.TOP_K}. Warm-up call (not counted): {warm:.2f}s"]
for run in range(1, args.runs + 1):
    times = []
    for item in items:
        secs, passed = one(item["question"])
        times.append(secs)
        out.append(f"run {run}  {secs:5.2f}s  {'answered' if passed else 'refused by gate'}  {item['question']}")
    under = sum(t < 4.0 for t in times)
    out.append(f"run {run}: {under}/{len(times)} under 4.0s, slowest {max(times):.2f}s")
text = "\n".join(out)
print(text)
open(f"results/timing_{args.label}.txt", "w").write(text + "\n")
