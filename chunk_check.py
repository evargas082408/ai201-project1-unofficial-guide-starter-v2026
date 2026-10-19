"""Measures chunk lengths for criterion 4. Measures only; changes nothing."""
from chunker import split_documents
from ingest import load_documents

chunks = split_documents(load_documents())
lengths = sorted(len(c.text) for c in chunks)
in_range = sum(150 <= n <= 600 for n in lengths)
out = [
    f"chunks: {len(lengths)}",
    f"150-600 chars: {in_range} ({in_range / len(lengths):.1%})",
    f"under 50 chars: {sum(n < 50 for n in lengths)}",
    f"shortest: {lengths[0]}  longest: {lengths[-1]}",
    f"documents the chunker split into more than one chunk: {len(chunks) - len(load_documents())}",
]
text = "\n".join(out)
print(text)
open("results/chunk_lengths.txt", "w").write(text + "\n")
