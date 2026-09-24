def judge(question: str, expects: str, answer: str, results: str) -> bool: 
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()

