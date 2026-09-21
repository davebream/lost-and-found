---
name: pick-up
description: Start a fresh chat from a handover written elsewhere. Reads it cold, says what is unclear or missing before doing anything, then confirms the goal and the next step. Pairs with hand-over.
---

# Pick up

You are starting from a handover: a summary written in another conversation, by another
session or another person. If this chat has no memory of that conversation, you are the
best cold reader this document will ever get. Use that before it wears off.

## Steps

1. **Find the handover.** If the user pasted one, use that. Otherwise, if you can read
   files, look in the two places `hand-over` saves to: `.claude/handover.md`, then
   `handover.md` in the working folder. Read only that file. If the user points at a
   different file, read that one. If there is no handover at all, say so, and ask what
   they would like to work on. Do not invent context, and do not go looking through other
   files to make up for a missing handover.

2. **Say how cold you are.** If this chat has memory, or can search past conversations,
   say so in one line. Your read is then worth less, and the user should know. Do not use
   those to fill gaps.

3. **Read it cold, and report first.** Before doing any work, list what is unclear or
   missing:
   - references to things the text never introduces ("the earlier approach", "as agreed")
   - names, acronyms or systems that are not explained
   - decisions with no reason given
   - a next step you could not actually carry out from the text alone

   If you would have to guess, do not guess. Ask. Keep it short: only what would stop
   you or send you the wrong way. Give the gaps as a short list the user can paste back
   into the original chat. If a gap can only be filled from that conversation, say so,
   and send the user back to it.

4. **Play it back in three lines:** the goal, where things stand, and the next step as
   you understand it.

5. **Check it is still current.** If the handover carries a date and is more than a
   couple of days old, or mentions things that may have moved on, say so.
   Look for its "Written from:" line too. If it says the handover came from a summary only,
   tell the user: parts of the old conversation were never re-read, so rules and reasons
   may be missing, and the old chat or its transcript is where to look.

6. **Ask how to proceed:** continue from the next step, go through the full handover
   together, or start something different. Wait for the answer.

7. **Then work.** Once the user confirms, begin with the next step. Treat the constraints
   in the handover as standing rules for this whole conversation.

8. **Tidy up, if it came from a file.** Ask whether to delete the handover file now that
   it has been picked up. A stale handover left in place gets picked up again by mistake.
   Delete it only if the user says yes.

## Do not

- Do not start working before step 6 is answered. The next step written in the handover
  is a proposal until the user confirms it.
- Do not fill a gap with a plausible guess. The gaps you notice now are invisible to
  everyone who was in the original conversation. That is what makes them worth reporting.
- Do not search past chats or memory to fill the gaps on your own. If the handover needs
  the old conversation to make sense, the handover is what needs fixing.
