---
name: hand-over
description: Capture a conversation so it can continue in a fresh chat or be passed to someone else. Checks the summary for completeness, then has a fresh-context cold reader check that it stands alone.
---

# Hand over

A chat that has taken a wrong turn rarely recovers by being corrected. Starting fresh
with a good summary works better. This skill writes that summary and puts it through two
checks before it leaves. Its partner, `pick-up`, receives it on the other side.

## Steps

### 1. Say what you can see

If earlier parts of this conversation have been summarised or dropped, say so first. You
are then working from a summary, and the user may remember things you cannot see. Ask
them to add anything important.

If there is nothing meaningful to hand over, say so and stop.

### 2. Draft it, and hold it

Write for a reader with no memory of this conversation. Cover, in this order:

- the goal, in one or two sentences
- what has been decided, and why
- what was tried and rejected, and why
- what is still open, and anything blocking it
- exactly one most useful next step

Leave out the back-and-forth. Keep the names, numbers, file names and exact wording that
matter. Copy the user's standing constraints word for word: rules are the first thing a
summary loses.

Do not deliver the draft yet. The two checks below patch it first.

### 3. Check A, completeness. Yours to do

You can see the conversation. The cold reader cannot. So this check is yours alone.

| Must be in the draft | Passes when |
|---|---|
| The work in progress | What was being worked on, and why, is stated |
| What got done | It is listed, with references where they exist |
| What is pending | Everything still open is there, not only the interesting parts |
| Blockers | Each one is recorded, with what it blocks |
| Next step | Exactly one is named |

Anything present in the conversation but absent from the draft is a gap. Patch it.

### 4. Check B, does it stand alone. Not yours to do

You cannot judge this yourself. You already know everything the draft leaves out.

**If you can start sub-agents** (Claude Code, Cowork): you must start this plugin's
`cold-reader` agent. Pass it **only** a title of the form `Session handover: <topic>`, the
full draft, and the kind of document, `session handover`. Do not pass this conversation
or anything about it. That would defeat the test.

Apply its blocking findings. Take the facts from this conversation, never from
imagination. If a gap cannot be filled from what is known, say so in the draft ("reason
not recorded"). If there were blocking findings, run the agent **once more** on the
patched draft, and no more than that. If the agent cannot be started or returns nothing,
retry once, then deliver anyway with a first line saying the cold read did not run.

**If you cannot start sub-agents** (for example Claude Desktop chat): reread the draft
and rewrite every phrase that leans on this conversation, such as "the earlier approach"
or "as discussed". Then tell the user plainly that this check is weaker than a real cold
read, and that `pick-up` in the new chat does the real one.

### 5. Deliver

Give the final handover as one block the user can copy. If you can write files here,
offer to save it too, and say where you saved it.

Then report the gate in one line, for example: "Completeness: 2 gaps patched. Cold read:
NEEDS_CONTEXT, 3 blocking findings fixed, second pass STANDS_ALONE."

### 6. Point to the other side

Tell the user to open a new chat and start it with the `pick-up` skill, or, without this
plugin, to paste the block with this as the first message:

> Before we start: what is unclear or missing in this?

## Do not

- Do not solve the open problem while summarising. Organising is the job.
- Do not invent a reason for a decision the conversation never explained.
- Do not skip Check B because the draft looks fine to you. It always looks fine to you.
