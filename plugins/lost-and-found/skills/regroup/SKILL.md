---
name: regroup
description: Panic button for a long conversation that has lost the thread. Stops, re-reads it three times, then reports what was decided, what is open and what was assumed, grouped by importance.
---

# Regroup

The user pulls this by hand when a long conversation has too many open threads and they
can no longer hold it in their head. It is manual on purpose: a model that is lost cannot
reliably tell that it is lost.

## The one rule: organise, never add

This skill reduces load. It does that by sorting, not by hiding. Report everything that
matters, however much there is, but make it easy to take in: one line per item, grouped
by importance, most important first. A long conversation can hold ten important things.
Dropping seven of them to look tidy is a loss, not a simplification.

Two things you must not do, without exception:

- **Do not answer the open question.** Organising is the job. Solving is not.
- **Do not propose new ideas or new analysis.** Write down what already exists in this
  conversation, then stop.

## Steps

### 1. Freeze

Stop pushing the problem forward. No "one more try". From here you only organise.

### 2. Say what you can actually see

If earlier parts of this conversation were summarised or dropped, say so first. You are
then reading a summary, not the conversation, and the user may remember things it lost.

If you have access to the fuller record, use it: a transcript file, saved notes, a
handover, the project's files or history. Say which of these you read. Mark anything you
are reconstructing from a summary as "recovered, not re-read".

### 3. First pass: collect

Draw only from this conversation and its record. One line per item. Do not cap the lists.

| List | What goes in it |
|---|---|
| Open threads | Unresolved things still in flight |
| Decisions made | Each with its one-line reason |
| Pending questions | Things still truly unanswered |
| Assumptions I made | What you concluded on your own and kept building on |
| Conclusions I took from you | What you treated as settled because the user said it |

The last two are the point. They fail in different ways. The first is you believing your
own inference. The second is you deferring to the user: it never felt like a
disagreement, so nobody checked it.

### 4. Second and third pass: go back and look again

Do not show anything yet. A first pass over a long conversation favours what is recent
and what was loud. Go back through the conversation, and the fuller record if you have
it, **two more times**, each with a different question:

- **Pass two, the beginning and the middle.** What was set early and then buried: the
  original goal, standing constraints, preferences stated once, things the user said
  they would come back to. Early material is exactly what gets lost.
- **Pass three, the quiet items.** Small corrections, side remarks, "also" and "by the
  way", things agreed in half a sentence, items that were deferred and never picked up.

Add what you find to the lists. If a pass finds nothing new, say so. That is a result too.

### 5. Drift check

Re-read the last two lists and ask:

- Which of these did I conclude on my own, and would I still conclude it now?
- Which of these did I accept because the user said so, and not because the evidence
  supported it? Agreement is not evidence.

Flag anything that later turns may have been bent to fit. This decides step 8.

### 6. Group by importance

Sort every open item into one of these, most important first. Put in each group whatever
belongs there. There is no quota.

| Group | What belongs here |
|---|---|
| **Matters now** | Blocks other things, has a deadline, or is wrong and being built on |
| **Matters soon** | Real and needed, but nothing breaks if it waits a little |
| **Can wait** | Worth keeping, no urgency |
| **Hand off or drop** | Someone else's, or no longer worth doing. Say which |

Within "Matters now", order the items and say in a few words why each is there. If that
group is long, say so plainly, and name the one to start with.

### 7. Write it down

Give the result as one block the user can copy out of the chat, in this shape:

```
Regroup, <date and time>
Read: <this conversation / transcript / notes>. Passes: 3. <what passes two and three added>

Matters now
1. <item>, <why now>
...

Matters soon
- ...

Can wait
- ...

Hand off or drop
- ...

Decisions made (with why)
- ...

Pending questions
- ...

Assumptions the assistant made   <- scan for the wrong one
- ...

Conclusions taken from the user   <- scan for the one never checked
- ...

Start here
<one line: where we stopped, and the literal next step>
```

If you can write files here, offer to save it as well. Either way, tell the user to keep
a copy outside this chat. A checkpoint that scrolls away is not a checkpoint.

### 8. Offer two ways out

Tell the user plainly which one you recommend, and why.

- **Carry on here.** The assumptions hold. Resume from "Start here".
- **Restart clean.** An early assumption looks wrong, and later work was built on it. Do
  not keep arguing in this thread. Use the `hand-over` skill to write one self-contained
  message for a fresh chat, with two additions:
  - copy the user's constraints **word for word**. Standing rules are the first thing a
    summary loses.
  - list the ideas already rejected, and why. Without that, the new chat proposes them
    again.

## Do not

- Do not pad. If a list or a group is empty, write "none".
- Do not cut real items to make the result look short. Order them instead.
- Do not hide an assumption because it is embarrassing. Finding it is why the user asked.
