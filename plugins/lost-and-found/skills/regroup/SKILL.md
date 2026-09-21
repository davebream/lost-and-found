---
name: regroup
description: Panic button for a long chat that has lost the thread, when you want to take stock and stay. Reads back for what got buried, then reports decisions, open items and assumptions by importance.
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

Organising does include saying what to do next and which way out you recommend. It does
not include solving the open question, or raising an option this conversation never raised.

## Steps

### 1. Freeze

Stop pushing the problem forward. No "one more try". From here you only organise.

### 2. Say what you can actually see

If earlier parts of this conversation were summarised or dropped, say so first. You are
then reading a summary, not the conversation, and the user may remember things it lost.

**Go past the summary if you can.** A summary of a conversation is not the conversation. It
keeps the outcome and loses the rules, the reasons and the things said once. So before you
write anything, try to reach the real record:

- The summary may name the full transcript file. If it does and you can read files, that
  file is the record. Use it.
- In Claude Code, this session's transcript is a `.jsonl` file named after the session id,
  in the `projects` folder of the Claude config directory (`~/.claude/projects/` unless
  `CLAUDE_CONFIG_DIR` points somewhere else). Open only the one that is this session's.
- Anywhere else: notes or an earlier handover the user pointed at, or a tool for searching
  past chats if you have one.

A transcript can be many times larger than the room you have left. Never read it whole.
Search it. Start with the user's own messages, because they hold the rules, the decisions
and the corrections. Then search for the names and terms you are unsure about, and read only
around the hits. If you can start a sub-agent, let it do the searching and bring back only
what it found, so the transcript does not fill this conversation.

Only reach for a record the user pointed at, or one that is plainly this conversation's own.
In a plain chat there is usually no such record, and that is fine. Say what you read. Mark
anything that comes from a summary you could not check as "recovered, not re-read".

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

Do not present the final result yet, but do write down what each pass finds as you go.
Work you only did in your head cannot be checked, by the user or by you. A first pass over
a long conversation favours what is recent and what was loud. Go back through it, and the
fuller record if you have one, **two more times**, each with a different question:

- **Pass two, the beginning and the middle.** What was set early and then buried: the
  original goal, standing constraints, preferences stated once, things the user said
  they would come back to. Early material is exactly what gets lost.
- **Pass three, the quiet items.** Small corrections, side remarks, "also" and "by the
  way", things agreed in half a sentence, items that were deferred and never picked up.

Each pass ends with a written list of what it found, quoted from the conversation. Write
both before you sort anything. If a pass finds nothing new, write "nothing new". That is a
result too. Then add what you found to the lists.

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
Read: <this conversation / a summary plus the transcript, searched / a summary only / notes>
Gaps in what I could see: <none / earlier parts were summarised, those items are marked>
From early on, easy to miss: <quote it, or "nothing the first pass had missed">
Said in passing, never closed: <quote it, or "nothing the first pass had missed">

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
  message for a fresh chat. It copies the user's constraints word for word and records
  what was rejected, so the new chat does not propose the same ideas again.

## Do not

- Do not pad. If a list or a group is empty, write "none".
- Do not cut real items to make the result look short. Order them instead.
- Do not hide an assumption because it is embarrassing. Finding it is why the user asked.
