---
name: cold-read
description: Get a document read by someone with no context, to find what only makes sense to its authors. Starts a fresh-context cold-reader agent, or prepares a paste-ready check for a new chat.
---

# Cold read

A cold read only works if the reader is actually cold. You are not: if this conversation
produced the text, you already know everything it leaves out, and you will fill the gaps
without noticing. So **never do the cold read yourself in this conversation.** Your job is
to get the text in front of a reader with a fresh context, and then help fix what that
reader finds.

## Steps

1. **Get the text.** Ask for it if the user has not given it. Note what kind of document
   it is (email, ticket, spec, summary, handover) and who will receive it.

2. **Do the one check only you can do: completeness.** You can see the conversation and
   the cold reader cannot. Is anything that was decided or asked for here missing from
   the text? Fix that first, or tell the user what is missing.

3. **Hand it to a cold reader.**

   **If you can start sub-agents** (Claude Code, Cowork): start this plugin's
   `cold-reader` agent. Pass it **only** three things: a title, the full text, and the
   kind of document. Do not pass this conversation, a summary of it, the recipient's
   background, or any hint about what to look for. Anything extra defeats the test.

   **If you cannot start sub-agents** (for example Claude Desktop chat): say so plainly.
   Tell the user you cannot cold-read it here because you have the context. Then give
   them the block below, filled in, to paste into a **new incognito chat**. In Claude that
   is the ghost icon. A normal new chat can still search past conversations.

   ```
   You have never seen the conversation that produced the text below. Do not search past
   chats or memory. Read it as the person who will receive it.

   First line of your answer: STANDS ALONE or NEEDS CONTEXT.

   Then, for every phrase that only makes sense with context you do not have, give:
   - the exact words, quoted
   - why a newcomer cannot work it out
   - what should be added, and where
   Mark each as blocking or minor. Look for: references to things never introduced ("as
   discussed", "the new approach"), unexplained names or acronyms, decisions with no
   reason, fixes with no stated problem, instructions that assume a starting point, and
   vague scope. Do not rewrite the text. If you have to guess what something means, that
   is a finding.

   Kind of document: <kind>
   Text:
   <the text>
   ```

   Ask the user to bring the answer back here.

4. **Fix what was found.** Apply the blocking findings, using facts from this
   conversation and never invented ones. If a gap cannot be filled from what is known,
   say so in the text ("reason not recorded") instead of papering over it.

5. **Check once more, at most.** If there were blocking findings, run the cold read one
   more time on the fixed text. Do not loop beyond that.

6. **Report in a line or two:** the verdict, and what changed.

## Do not

- Do not play the cold reader yourself, even if asked to "just pretend". Explain why it
  does not work and offer step 3.
- Do not tell the cold reader what the document is supposed to achieve. If the text does
  not say, that is a finding.
