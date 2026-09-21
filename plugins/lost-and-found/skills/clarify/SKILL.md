---
name: clarify
description: Re-explain something correct but too dense, in plain language, without dropping a caveat. Use when the user says they don't follow, asks for it simpler, or asks you to explain again.
---

# Clarify

Re-render a correct but dense explanation so a confused reader can absorb it, **without
dumbing it down**. Change the wording and the structure. Never delete a fact, a caveat or
a boundary condition that matters. Plain language is for experts too.

## Steps

1. **Find the target.** With no other instruction, clarify your previous explanation. If
   the user pointed at a text or topic, clarify that. If it is unclear which part they
   mean, ask one short question first.

   If the original may have been summarised or dropped from this conversation, say so.
   Then try to get the original back before you rewrite: the summary may name the full
   transcript file, and in Claude Code the session's transcript is a `.jsonl` file under
   the `projects` folder of the Claude config directory. Search it for the explanation,
   never read it whole. Caveats are the first thing a summary loses. Never present a
   rewrite of a summary as a clarification of the original.

2. **List the caveats first.** Before rewriting anything, list every caveat, condition,
   exception and "only when" in the original, and number them. **Show the numbered list
   in the chat.** It does not stay in your head: a list you did not write down is a
   feeling again. This list is the contract for step 6.

   Do this before the rewrite, not after. Asked afterwards "does this look complete?",
   the same model that just compressed the text will say yes. A list written beforehand
   is something the rewrite can be checked against. That is the difference between a
   check and a feeling.

3. **Name what made it hard.** Undefined jargon? Facts the reader needs together
   scattered apart? Too many new ideas per sentence? Edge cases before the main idea?

4. **Rewrite in this order.** The order is not optional.
   1. **The outcome first:** what it does or means, in plain words.
   2. **The mechanism:** why and how it works underneath.
   3. **One concrete example or analogy.** For an analogy, say which part maps, and say
      where it breaks down.
   4. **Caveats last,** clearly marked as caveats.

5. **Plain-language rules.**
   - One idea per sentence. One topic per paragraph. Around twenty words a sentence.
   - Attach each new idea to one already explained.
   - Active voice. The common word over the rare one.
   - Keep a technical term only when it is needed, and define it in plain words first.
   - Mark caveats out loud: "The exception:", "This only holds when".

6. **Check against the list.** Go through the numbered caveats from step 2 and find each
   one in your rewrite. Any caveat you cannot point to is a defect. Put it back. Cut only
   detail that does not change the conclusion.

7. **Before you show it:** every caveat accounted for? No undefined jargon left? No
   analogy stretched past where it fits? Outcome before mechanism?

## Do not

- Do not drop a caveat to make it read cleaner. That is the worst failure here, because
  it looks like success.
- Do not skip a step because it feels obvious to you. It was not obvious to the reader.
- Do not put exceptions before the main idea.
- Do not change the accuracy, soften a real limitation, or pad.
- If `humanize` also applies to the same text, clarify first, then humanize.
