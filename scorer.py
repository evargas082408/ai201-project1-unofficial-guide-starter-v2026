import questions

# Criterion 1, revised in unit 2 (see criteria.md): a question passes when the
# file holding its answer is among the retrieved chunks. The original version
# checked `expects` against the generated answer, which measured my word
# choice rather than retrieval.
SOURCES = {q["question"]: q.get("source", "") for q in questions.QUESTIONS}


def judge(question: str, expects: str, answer: str, results) -> bool:
    source = SOURCES.get(question)
    if source:
        return source in {r.source for r in results}
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()
