# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

The Unofficial Guide is a document retrieval and question-answering tool built on the `campus_life` corpus. It indexes 88 student-authored documents covering course workloads, housing reviews, dining recommendations, and administrative advice that isn't plainly stated on official university sites. Users can ask natural-language questions about surviving day-to-day campus life, and the system retrieves the most relevant excerpts, evaluates semantic relevance, and generates an answer strictly grounded in those documents with citations.

## Chunking Strategy

**Chunk size:** 800 characters
**Overlap:** 100 characters

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

     When reading the `campus_life` documents in Milestone 1, the indexer reported that all 88 documents averaged approximately 317 characters, with the longest document topping out at 549 characters. Because each document is already a concise, single-topic student tip or review, setting the chunk size to 800 characters guarantees that an entire post remains intact as a single thought rather than being severed mid-sentence. An overlap of 100 characters ensures that any future, longer multi-paragraph posts maintain sentence context across chunk boundaries.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

======================================================================
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

"is the housing lottery random?"

The housing lottery is not entirely random in the way most people assume. While rising sophomores get a number drawn at random, juniors and seniors are ordered by accumulated credit hours first, with random tie-breaking used only for ties. 
```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Is the housing lottery actually random? | Yes | 0.412 |
| What is the issue with Aldridge Hall? | Yes | 0.394 |
| Which dining hall is worth the walk? | Yes | 0.458 |
| How reliable is the campus shuttle? | Yes | 0.512 |
| How do students save money on textbooks? | Yes | 0.536 |
| How do I fix a leaky kitchen faucet? | No | 0.842 |
| What was the score of the 1998 World Cup final? | No | 0.865 |
| How do I calculate the eigenvalues of a 3x3 matrix? | No | 0.798 |
| What is the standard treatment for acute bronchitis? | No | 0.738 |
| Who won the Academy Award for Best Actor in 2012? | No | 0.811 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

"I had gemini help me specifically refine my answers to individual questions, as well as help me work with git and whatnot."

**2.**

When formulating my acceptance criteria for `criteria.md`, I asked Gemini to review my draft ideas to ensure they met the course rubric's requirement for testable, measurable outcomes. The AI suggested checking chunk length boundaries and latency. 

**3. (Unit 2)**

I asked Claude Code to finish the unit 2 write-up from my partial run logs. It
caught two things I'd missed. First, a `time.sleep(4)` I'd added to `generate.py` to
dodge rate limits would have added 4 s to every answer, and it was a second change
to the system. Second, my "before" runs weren't actually identical, as I'd claimed:
the 23:29 file has the shuttle question passing twice. It also spotted the pattern
in my failures: my `expects` words ("priority", "mold", "schedule") appear in zero
corpus documents, and the dining question ranks housing buildings named "Hall"
above Kestrel Commons. It wrote `chunk_check.py`, ran the after timing and the
fresh after eval, and drafted the unit 2 sections. I kept the strict MISSED call
on criterion 2 after it argued the opposite reading (that a refusal isn't an
answer).

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

System as submitted in unit 1: cutoff 0.6, top-k 5, chunk size 800, overlap 120.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer (original, scored by `scorer.py`) | 4 of 5 | 1/5 | 1/5 | 1/5 | MISSED |
| 1. Revised: the answer's source file is among the 5 retrieved | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 4/5 | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. ≥90% of chunks 150–600 chars, 0 under 50 | 90%, 0 | 100%, 0 | 100%, 0 | 100%, 0 | MET |
| 5. All 5 questions answered in under 4.0 s | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Where the numbers come from.**

- Criteria 1–3: `results/run_2026-09-30_2333_before.md`, produced by `run_eval.py::main`.
  Each `run_eval.py` file holds three runs with caching off.
- Criterion 1 (original) is the pass/fail column from `scorer.py::judge`. Criterion 1
  (revised) is read off the "Sources retrieved" line for each question (the revision and
  the expected file per question are in `criteria.md`).
- Criterion 2 is counted by hand from the answer text: an answer passes if it names a
  `.txt` file.
- Criterion 3 is one deterministic pass (`run_eval.py::check_out_of_scope`), so the same
  number goes in all three columns.
- Criterion 4: `results/chunk_lengths.txt`, from `chunk_check.py`. Chunking is
  deterministic, so it is one measurement in all three columns.
- Criterion 5: `results/timing_before.txt`, from `time_check.py` (three timed passes, cache off).

**A correction to what I wrote earlier.** I ran `run_eval.py --label before` three times back
to back with no changes (23:29, 23:30, 23:33). I first wrote that they were identical. They
weren't: in the 23:29 file the shuttle question passed the scorer in runs 1 and 3 (the
model happened to write "schedule"), so that file reads 2/5, 1/5, 2/5 for original
criterion 1. It's a miss either way. The table uses the 23:33 file.

`results/run_2026-10-01_0137_before.md` is mislabeled. It was run after the cutoff had
already been raised to 0.7 (its header says "relevance cutoff: 0.7"), so it is really an
"after" run. I've left the file alone rather than rename evidence.

### Real output (run 1 of `results/run_2026-09-30_2333_before.md` unless noted)

**Criterion 1, original** — `scorer.py::judge` checks the `expects` word against the answer:

```
| Is the housing lottery actually random? | fail | fail | fail |
| Which dining hall is considered the best or worth the walk? | fail | fail | fail |
| What is the issue with Aldridge Hall? | fail | fail | fail |
| How reliable is the campus shuttle? | fail | fail | fail |
| How do students save money on textbooks? | pass | pass | pass |
```

**Criterion 1, revised** — `store.py::search`, the "Sources retrieved" line per question:

```
lottery:   admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_morrow_house.txt, housing_tamsin_court.txt   -> admin_housing_lottery.txt present
dining:    dining_halden_hall.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_aldridge_hall.txt, housing_innisfree_hall.txt   -> dining_kestrel_commons.txt MISSING
Aldridge:  dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_aldridge_hall_noise.txt   -> housing_aldridge_hall.txt present
shuttle:   dining_the_ridgeway_cafe.txt, dining_verrill_street_grill.txt, housing_aldridge_hall.txt, housing_tamsin_court.txt, transit_shuttle.txt   -> transit_shuttle.txt present
textbooks: admin_printing_quota.txt, course_cs_210.txt, course_cs_340.txt, money_textbooks.txt, study_group_rooms.txt   -> money_textbooks.txt present
```

**Criterion 2** — `generate.py::answer_from_chunks`. Four answers cite a file, e.g.:

```
Q: How reliable is the campus shuttle?
A: The campus shuttle runs a loop every 20 minutes from 7am to 11pm on weekdays and every
   40 minutes on weekends. Its published timetable is optimistic by about five minutes in
   the morning and accurate for the rest of the day (transit_shuttle.txt).
```

The one that doesn't (`gate.py::check` refused it, so the model was never called):

```
Q: What is the issue with Aldridge Hall?
- Best distance: 0.6559 (refused by the gate)
A: I don't have enough information about that.
```

**Criterion 3** — `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5:

```
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844 | refused |
| How do I write a for loop in Rust? | 0.896 | refused |
```

**Criterion 4** — `chunk_check.py`, using `chunker.py::split_documents` (`results/chunk_lengths.txt`):

```
chunks: 88
150-600 chars: 88 (100.0%)
under 50 chars: 0
shortest: 178  longest: 549
documents the chunker split into more than one chunk: 0
```

**Criterion 5** — `time_check.py` (`results/timing_before.txt`), run 3, the slowest pass:

```
cutoff 0.6, top-k 5. Warm-up call (not counted): 2.02s
run 3   0.64s  answered  Is the housing lottery actually random?
run 3   2.11s  answered  Which dining hall is considered the best or worth the walk?
run 3   0.05s  refused by gate  What is the issue with Aldridge Hall?
run 3   0.81s  answered  How reliable is the campus shuttle?
run 3   0.70s  answered  How do students save money on textbooks?
run 3: 5/5 under 4.0s, slowest 2.11s
```

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | Original: MISSED. Revised: MET | Original: 1/5 in all three runs against a target of 4. Revised: 4/5 in all three runs, so it holds every time, not just once. Only the dining question misses. I wrote the revised check after seeing my first run, so it isn't a blind test. |
| 2 | Every answer names a source | MISSED | 4/5 in every run against 5 of 5. The Aldridge Hall refusal names no source. You could argue a refusal isn't "an answer the system produces", which would make it 4/4 and MET. I didn't take that reading, because the user still gets a reply with no source on it and my criterion says "every answer". |
| 3 | Gate stops out-of-corpus questions | MET | 5/5 against 4 of 5. The closest out-of-scope question was 0.825, well clear of 0.6, so this wasn't close. |
| 4 | Chunk lengths | MET | 88/88 chunks (100%) are 150–600 chars and the shortest is 178, so 0 are under 50. It passes, but see Diagnoses: it was never going to fail. |
| 5 | Response time | MET | All 15 timed answers came in under 4.0 s, and the slowest was 2.11 s. The warm-up call isn't counted. Including it wouldn't change this run (2.02 s), but it does matter after the fix (see What's Still Broken). |

## Diagnoses

**Criterion 1 (original), lottery, shuttle and Aldridge: the test, not the pipeline.**
`scorer.py::judge` passes an answer only if it contains my `expects` word. "priority",
"mold" and "schedule" appear in **zero** of the 88 corpus documents (checked with grep),
so those three questions could never pass, however good retrieval and generation were.
The answers themselves were right. The lottery answer says juniors and seniors are
ordered by "credit hours", and the shuttle answer says the "timetable is optimistic by
about five minutes". I picked the `expects` words from what I assumed the documents said
instead of what they actually say. This is why I revised criterion 1 (see `criteria.md`).

**Criterion 1, dining: embedding/retrieval stage, matching on the word "Hall".**
The question asks which "dining hall" is worth the walk. I expected Kestrel Commons. The
top 5 were Pellew Dining Hall (twice), Halden Hall, and two *housing* buildings,
Innisfree Hall (0.552) and Aldridge Hall (0.558). Those housing docs say nothing about
dining. They rank above four of the seven dining venues because their titles contain
"Hall". Kestrel Commons doesn't have "Hall" in its name. It ranks **25th** at 0.704, and
the gate would refuse it on its own. Every dining document follows the same template
("Wait times … The thing worth going for is …"), so the bodies barely separate them. The
title word is what the embedding latches onto.

There is a second problem underneath. No dining document calls any hall "the best", so
this question has no single right answer in the corpus. "Commons" was my opinion, not
something the documents say.

**Criterion 2, the Aldridge refusal: the relevance gate, at the retrieval stage.**
`housing_aldridge_hall.txt` *was* retrieved. The answer (the elevator is out a week per
semester, and the washer/dryer ratio is wrong) is in it and in
`housing_aldridge_hall_laundry.txt`. But the best distance was 0.656, over the 0.6 cutoff,
so `gate.py::check` refused before the model saw anything, and a refusal names no
source. The question is short and vague ("what is the issue"), while the documents are a
list of specifics, so even the right document only gets to 0.656. My unit 1 cutoff table
lists 0.394 for this question, but every run this unit measured 0.656. None of the five
in-scope distances in that table match what the system returns now (lottery 0.248,
dining 0.492, Aldridge 0.656, shuttle 0.575, textbooks 0.337). So the 0.6 cutoff was
calibrated against numbers that don't describe this system. That is the real reason it
was too tight.

**Pattern.** Every miss traces back to a decision I made *about* the corpus without
checking it against the corpus: `expects` words that aren't in it, a "best dining hall"
it never names, and a cutoff set from distances that don't match it. The pipeline's own
failure is the dining retrieval, where the embedding over-weights a title word.

**Criteria I met but set too low.** Criterion 4 can't fail on this corpus. The longest
document is 549 chars and the chunk size is 800, so the chunker never splits anything
("documents the chunker split into more than one chunk: 0"). The criterion measures how
long the documents are, not anything my chunking did. Criterion 3 is also safe: the
out-of-scope questions are from completely different worlds (Mongolia, diesel engines)
and sit 0.2 or more past the cutoff. Next time I'd tighten criterion 3 to near-miss
questions the corpus doesn't cover, like "What's the gym schedule?" or "How much is
parking for visitors?".

## The Improvement

**What I changed:** the relevance cutoff in `config.py`, `THRESHOLD = 0.6` → `THRESHOLD = 0.7`.
That is the only change to the system. I also took out a `time.sleep(4)` I'd added to
`generate.py::generate` to dodge rate limits, and a chunk-overlap edit (120 → 100).
Neither was part of the improvement, and the overlap edit did nothing since no document
gets split. For the after run I stayed under Gemini's free-tier limit (15 requests per
minute) by setting `config.REQUESTS_PER_MINUTE = 12` from the command line for that one
run, without editing any file.

**Why I picked it:** the Aldridge Hall question was refused at 0.656 even though the right
document was retrieved, and that one refusal is the entire criterion 2 miss. 0.7 lets
0.656 through and still sits below the closest out-of-scope question (0.825). So it
should fix criterion 2 without breaking criterion 3. It won't touch the dining miss,
because the gate doesn't change *which* chunks come back, only whether they're used.

### Run Log — After

Cutoff 0.7, everything else unchanged. Criteria 1–3 come from
`results/run_2026-10-18_2123_after.md` (run on the final code). The two earlier after
runs, `run_2026-09-30_2355_after.md` and `run_2026-10-01_0005_after.md`, agree on every
criterion except one: original criterion 1 reads 1/5 in all of their runs. Criterion 4 is
`results/chunk_lengths.txt` and criterion 5 is `results/timing_after.txt`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer (original, scored by `scorer.py`) | 4 of 5 | 1/5 | 2/5 | 1/5 | MISSED |
| 1. Revised: the answer's source file is among the 5 retrieved | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. ≥90% of chunks 150–600 chars, 0 under 50 | 90%, 0 | 100%, 0 | 100%, 0 | 100%, 0 | MET |
| 5. All 5 questions answered in under 4.0 s | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

Before and after, side by side:

| Criterion | Before (runs 1/2/3) | After (runs 1/2/3) | Change |
|---|---|---|---|
| 1 original | 1/5, 1/5, 1/5 | 1/5, 2/5, 1/5 | none (run 2's extra pass is the model writing "schedule" once) |
| 1 revised | 4/5, 4/5, 4/5 | 4/5, 4/5, 4/5 | none |
| 2 | 4/5, 4/5, 4/5 | 5/5, 5/5, 5/5 | **MISSED → MET** |
| 3 | 5/5 | 5/5 | none (closest out-of-scope 0.825 vs cutoff 0.7) |
| 4 | 100%, 0 under 50 | 100%, 0 under 50 | none |
| 5 | 15/15, slowest 2.11 s | 15/15, slowest 0.90 s | none (still MET) |

The Aldridge answer that used to be a refusal, after the fix (run 1, `generate.py::answer_from_chunks`):

```
Q: What is the issue with Aldridge Hall?
- Best distance: 0.6559 (passed the gate)
A: Based on the provided documents, the issues with Aldridge Hall are:
- The elevator is out roughly one week per semester (`housing_aldridge_hall.txt`).
- The ratio of eight washers to six dryers is wrong, which causes the dryers to back up on
  Sunday evenings (`housing_aldridge_hall_laundry.txt`).
```

**Did it help?** Yes, for the thing it was aimed at. Criterion 2 went from 4/5 in every run to
5/5 in every run, because the Aldridge answer now passes the gate and cites two files.
Criterion 3 didn't get worse: all five out-of-scope questions are still refused. It did
nothing for original criterion 1. Aldridge is now answered correctly, but the answer
still doesn't contain "mold" because "mold" isn't in the corpus. It also did nothing for
the dining miss, as expected. The cost is a thinner safety margin: the gap between the
cutoff and the nearest out-of-scope question shrank from 0.225 to 0.125.

## What's Still Broken

- **Criterion 1 (original), still 1/5.** The `expects` words for lottery, Aldridge and
  shuttle aren't in the corpus. Swapping them now ("credit hours", "elevator",
  "timetable") would be loosening the test after seeing the answers, so I left them and
  revised the criterion instead. Next time I'd pick `expects` words by grepping the
  corpus *before* writing the criteria.
- **Dining retrieval, the one miss under revised criterion 1.** The embedding ranks
  buildings named "Hall" above Kestrel Commons, which sits 25th. Hybrid BM25 wouldn't save
  this question, because "Kestrel" and "Commons" aren't in it, and "hall" would match the
  same wrong documents. The honest fix is the question, not the pipeline: nothing in the
  corpus says which hall is best. I'd replace it with one the corpus does answer, like
  "Which dining hall has the shortest lunch wait?", and test that blind. I stopped here
  because the rule is one change per unit, and changing a test question isn't an
  improvement to the system.
- **Cold start (criterion 5's blind spot).** `time_check.py` doesn't count its warm-up call,
  and after the fix that call took **5.24 s** (`results/timing_after.txt`), over the 4.0 s
  target. A real user's first question would miss the target. I'd fix it by loading the
  embedding model and API client when the server starts, in `serve.py`, not on the first
  question.
- **The gate cutoff is still a guess on 5 + 5 questions.** At 0.7 it is 0.044 above the
  Aldridge question and 0.125 below the nearest out-of-scope one. With only ten data
  points I can't say where the real gap is. I'd want 20 or more in-scope and near-miss
  out-of-scope questions before trusting it.

## What I'd Do Differently

- **Criterion 1:** I'd write it as the source-file check from the start ("the file that holds
  the answer is in the top 5"), with the expected file per question written down
  *before* any run, so the revision wouldn't have to be a non-blind test.
- **Criterion 4:** I'd make it about chunking, not document length. With 800-char chunks and
  no document longer than 563 chars, it can't fail. Something like "for questions whose answer
  spans two documents (an original post and its follow-up), both appear in the top 5"
  would actually test retrieval over this corpus's post/reply structure.
- **Criterion 5:** I'd count the first call, because "under 4 seconds" should mean what a
  user actually waits.
- **Criterion 3:** I'd use near-miss questions instead of other-world questions, so the gate
  is actually tested.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     None attempted this unit.
     ───────────────────────────────────────────────────────────────────────── -->
