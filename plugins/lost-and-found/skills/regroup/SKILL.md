---
name: regroup
description: Panic button for a long conversation that has lost the thread. Stops, lists what was decided, what is open and what was assumed, forces a top three, and offers a clean restart.
---

# Regroup

The user pulls this by hand when a long conversation has too many open threads and they
can no longer hold it in their head. It is manual on purpose: a model that is lost cannot
reliably tell that it is lost.

## The one rule: subtract, never add

This skill reduces load. A long recap floods the user again and defeats the purpose. Keep
every list short, capped and plain.

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
Mark anything you are reconstructing from a summary as "recovered, not re-read".

### 3. Five short lists

Draw only from this conversation. At most seven items per list. If a list would run past
seven, summarise it in one line instead.

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

### 4. Drift check

Re-read the last two lists and ask:

- Which of these did I conclude on my own, and would I still conclude it now?
- Which of these did I accept because the user said so, and not because the evidence
  supported it? Agreement is not evidence.

Flag anything that later turns may have been bent to fit. This decides step 7.

### 5. Top three

Sort every open item into **now, later, hand to someone else, or drop**. Then force
**exactly three** items into "now". If there are four, one moves. The cut is the point:
it lets the user put the rest down.

### 6. Write it down

Give the result as one block the user can copy out of the chat, in this shape:

```
Regroup, <date and time>

Top 3 (do these, ignore the rest for now)
1.
2.
3.

Open threads
now: ...   later: ...   hand off: ...   drop: ...

Decisions made (with why)
- ...

Assumptions the assistant made   <- scan for the wrong one
- ...

Conclusions taken from the user   <- scan for the one never checked
- ...

Next concrete action
<one line: where we stopped, and the literal next step>
```

If you can write files here, offer to save it as well. Either way, tell the user to keep
a copy outside this chat. A checkpoint that scrolls away is not a checkpoint.

### 7. Offer two ways out

Tell the user plainly which one you recommend, and why.

- **Carry on here.** The assumptions hold. Resume from the top three and the next action.
- **Restart clean.** An early assumption looks wrong, and later work was built on it. Do
  not keep arguing in this thread. Use the `hand-over` skill to write one self-contained
  message for a fresh chat, with two additions:
  - copy the user's constraints **word for word**. Standing rules are the first thing a
    summary loses.
  - list the ideas already rejected, and why. Without that, the new chat proposes them
    again.

## Do not

- Do not pad. If a list is empty, write "none".
- Do not hide an assumption because it is embarrassing. Finding it is why the user asked.
