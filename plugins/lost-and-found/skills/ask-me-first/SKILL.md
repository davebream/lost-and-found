---
name: ask-me-first
description: Before starting a task, ask the questions only the user can answer, one at a time, each with a recommendation. Use when a request is underspecified and guessing would be costly.
---

# Ask me first

Models tend to guess early, commit to the guess, and struggle to recover when it turns
out wrong. It is cheaper to ask. But a wall of ten questions is its own kind of
overload, so ask well.

## Steps

1. **List what you do not know.** Work out every open question about the task, without
   showing the list yet.

2. **Sort them.**
   - **Only the user knows:** a preference, a priority, a trade-off they own, a fact
     about their situation. These get asked.
   - **You can find out:** the answer is in the conversation, the files, or something
     you can look up. Go and find out. Do not ask.
   - **Does not matter yet:** a sensible default exists. Take it and say which default
     you took.

3. **Order by impact.** The first question is whatever would change the most work if
   answered differently. Stop asking as soon as you know enough to start. Three good
   questions beat ten thorough ones.

4. **Ask one question at a time.** For each one:
   - give one or two sentences of context, as if the user had just walked in
   - offer two to four concrete options when you can
   - say which you would pick, and why
   - then stop and wait for the answer

   If you have a tool for asking structured questions, use it for one question at a
   time, never for a batch.

5. **Play it back.** Before starting, restate the task in a few lines with the answers
   folded in, and the defaults you chose. Then begin.

## Do not

- Do not ask anything you could have answered yourself.
- Do not ask several questions in one message. That means exactly one question mark. A
  trailing "and would you also prefer" is a second question.
- Do not ask without a recommendation. "What would you like?" pushes the thinking back
  onto the user.
