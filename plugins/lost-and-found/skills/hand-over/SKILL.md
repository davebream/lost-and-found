---
name: hand-over
description: Capture this whole conversation so it can continue in a fresh chat. Use when a chat has gone off the rails or is too long. Checks it for completeness, then a cold reader checks it stands alone.
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

If there is nothing meaningful to hand over, say so and stop. If the user wants to take
stock and carry on here, not leave, use the `regroup` skill instead.

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

Go through the table row by row and write down the row and what you found, before you
patch anything. Anything present in the conversation but absent from the draft is a gap.
Patch it.

### 4. Check B, does it stand alone. Not yours to do

You cannot judge this yourself. You already know everything the draft leaves out. Never
write the cold reader's answer yourself.

**Which branch you are in.** Look at the tools you actually have in this session. If one
of them starts a sub-agent or a task, you can run Check B. If no such tool is in your
list, you cannot. Decide this from your tool list only, not from the product name. **If
you are not sure, assume you cannot.**

**If you can start a sub-agent:** you must start this plugin's `cold-reader` agent. Its
full name is `lost-and-found:cold-reader`. Pass it **only** a title of the form `Session
handover: <topic>`, the full draft, and the kind of document, `session handover`. Do not
pass this conversation or anything about it. That would defeat the test.

For a long draft, do not retype it into the prompt, where small differences creep in.
Save the draft alone in a new, empty folder and pass that one path in place of the text.
The folder must be empty because the agent can read files, and anything else in there is
context it was not meant to have.

Apply its blocking findings. Take the facts from this conversation, never from
imagination. If a gap cannot be filled from what is known, say so in the draft ("reason
not recorded"). If there were blocking findings, run the agent **once more** on the
patched draft, and no more than that. Start a **new** agent for the second pass. Do not
continue the first one: it has read the earlier draft and is no longer cold. Minor
findings from the final pass are yours to judge: apply the cheap ones, skip the rest, and
do not run a third pass for them. If the agent cannot be started or returns nothing,
retry once, then deliver anyway with a first line saying the cold read did not run.
**Never report a verdict you did not receive.**

**If you cannot:** you cannot run Check B. Do a self-reference sweep instead, which is a
different and weaker thing. Search the draft for phrases such as: as discussed, as agreed,
the earlier, the new, this approach, that fix, the issue, the file, we decided. For each
hit, replace the phrase with the thing itself. Then tell the user plainly: "Check B did not
run. I cannot judge this draft cold, because I wrote it. The new chat is the real check."

### 5. Deliver

Do not deliver until Check B has either run or been reported as not run. The draft always
looks fine to you.

If you can write files here, save the handover, so the new session can find it without
any pasting. Then show the user the path and the gate line below, not the whole text: the
file is the delivery, and a long block in the chat only repeats it. Print the text if they
ask. If you cannot write files, give the final handover as one block the user can copy.

Where to save it: use `.claude/handover.md` in the project folder when you are in Claude Code or
the folder already has a `.claude` directory. Otherwise use `handover.md` in the working
folder. Put the date and time on the first line. Overwrite an older handover at that path
instead of adding a second file. Tell the user where you saved it, and that the file is
not hidden from git unless they ignore it, in case it holds something private.

Then report the gate in one line, quoting a real finding. If the cold reader said project
instructions or memory were in its context, pass that on. Counts are easy to invent; a
quote is not. For example: "Completeness: 2 gaps patched. Cold read: NEEDS_CONTEXT.
Biggest finding: 'the earlier approach' had no referent. Second pass: STANDS_ALONE."

### 6. Point to the other side

Tell the user to open a new chat and start it with the `pick-up` skill. If you saved a
file, `pick-up` finds it by itself. If not, they paste the block. Without this plugin,
they paste the block with this as the first message:

> Before we start, and before you do any work: what is unclear or missing in this?

**Ask them to keep this chat open** until the new one confirms the handover stands alone.
If the new chat finds gaps, the answers are here, not there.

## Do not

- Do not solve the open problem while summarising. Organising is the job.
- Do not invent a reason for a decision the conversation never explained.
- Do not skip Check B because the draft looks fine to you. It always looks fine to you.
