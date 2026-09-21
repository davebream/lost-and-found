---
name: one-by-one
description: When questions pile up, ask them one at a time, each with context and a recommendation. Before a task, mid-task or after a review. Only asks what the user alone can answer.
---

# One by one

Models tend to guess early, commit to the guess, and struggle to recover when it turns
out wrong. It is cheaper to ask. But a wall of ten questions is its own kind of overload:
the user answers the easy ones, skips the hard ones, and nobody can tell which answer
belongs to which question. So ask one at a time, and ask well.

## When to use it

- Before a task, when the request leaves choices open and a wrong guess would be costly.
- In the middle of work, when two or more decisions have piled up and you are about to
  list them.
- After a review or a report, when several findings each need the user's call.

A single question does not need this skill. Just ask it.

## Steps

1. **Collect.** Write down every open question, without showing the list yet. If you were
   started with no task at all, then which task to work on is the first question. Offer
   the candidates you can see in the conversation.

2. **Sort them by who can answer.**
   - **Only the user knows:** a preference, a priority, a trade-off they own, a fact
     about their situation. These get asked.
   - **You can find out:** the answer is in the conversation, the files, or something
     you can look up. Go and find out. Do not ask. If earlier parts of this conversation
     were summarised, the answer may have been given there and lost. Where you can reach
     the full transcript (the summary may name the file; in Claude Code it is a `.jsonl`
     file under the `projects` folder of the Claude config directory), search the user's
     messages in it before you ask. Asking twice what was already answered is the most
     expensive question there is.
   - **Does not matter yet:** a sensible default exists. Take it, and note which default
     you took for the summary at the end.

3. **Order by impact.** The first question is whatever would change the most work if
   answered differently. Stop asking as soon as you know enough to act. Three good
   questions beat ten thorough ones.

4. **Ask one question at a time,** in this shape:

   ```
   Question <n> of <total>: <topic>

   <The decision, in one plain sentence.>

   So far: <one to three sentences: why this needs deciding now, and what changes with
   the answer. Write as if the user just came back from an hour away.>
   Options: <two to four, each saying what it would mean in practice>
   Already ruled out: <ideas dropped earlier, and why. Leave this line out if none.>
   I would pick: <option>, because <one sentence>. The cost: <what you give up>.
   ```

   Then stop and wait. The user can take your pick, take another option, skip the
   question for now, or ask to talk it through. A skipped question goes to the summary
   as still open. Do not ask it again unless the user brings it back.

   Answers change the queue. One may settle a later question, another may raise a new
   one. Say so when the total moves: "Question 3 of 4 (was 5, your last answer settled
   one)."

   If you have a tool for asking structured questions, use it for one question at a
   time, never for a batch.

5. **Sum up, then act.** After the last answer, and before doing anything:

   ```
   Decided
   1. <topic>: <answer>
   Defaults I took
   - <topic>: <default>
   Skipped, still open
   - <topic>
   Next: <what you will do now, in one line>
   ```

   Then begin. If an answer sounded like a standing preference, true next time as well
   and not only a call about this task, point it out, so the user can save it wherever
   they keep instructions for you.

## Do not

- Do not ask anything you could have answered yourself.
- Do not ask several questions in one message. That means exactly one question mark. A
  trailing "and would you also prefer" is a second question.
- Do not ask without a recommendation. "What would you like?" pushes the thinking back
  onto the user.
- Do not lean on the previous question. Each one must make sense on its own, to someone
  who has forgotten everything before it.
- If the user asks for all the questions at once, say in one line that one at a time is
  easier to answer well, then do what they asked: a numbered list, each item still with
  its recommendation.
