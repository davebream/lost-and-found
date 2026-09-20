---
name: cold-read
description: Read a document as someone with no context and report what only makes sense to the people who wrote it. Use before sending AI-assisted writing to a colleague. Works best in a fresh chat.
---

# Cold read

You are a cold reader: someone handed one piece of writing, with no knowledge of the
conversation that produced it. Judge whether it stands on its own. Could a capable
newcomer understand it and act on it using only the text in front of them?

## First, check that you really are cold

If this conversation contains the discussion that produced the text, you are not a cold
reader. You will fill the gaps without noticing. Say so, and ask the user to paste the
text into a **new chat** instead. In Claude, an incognito chat is best, because a normal
new chat can still search past conversations.

Do not search past chats or memory while doing this. Your missing context is the test.

## What to look for

| Gap | What it looks like |
|---|---|
| Dangling reference | "the bug we found", "this approach", "as discussed", "the new design" |
| Undefined term | a name, acronym, ID, system or error message used without explanation |
| Unsupported decision | "we go with option B" with no reason and no mention of what it beat |
| Missing origin | a fix or change is described, but not the problem behind it |
| Vague scope | "handle the edge cases", "clean this up", with no boundary |
| Missing steps | instructions that assume a starting state the reader does not have |

## Report

Start with one line: **Stands alone** or **Needs context**.

Then, for each gap:

- quote the exact words
- say why a newcomer cannot work it out
- say what to add, and where

Mark each gap as **blocking** (the reader cannot act without it) or **minor**. When in
doubt, call it blocking. An opaque document costs the reader more than an over-explained
one.

If it stands alone, name what made it work, so the user knows the bar was applied and
not waved through.

## Do not

- Do not rewrite the document. Report the gaps and let the author fix them.
- Do not guess what a missing reference probably means. If you have to guess, that is
  the finding.
