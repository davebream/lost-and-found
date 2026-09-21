# lost-and-found

Small skills for the moment you and your AI lose each other.

Works in Claude Code and in Claude Desktop chat. If you use something else, the
one-line versions below work anywhere you can paste text.

## The problem

Working with an AI assistant, people get lost in two directions at once:

1. The model writes more than you can read, so you get lost in its output.
2. You correct it bit by bit, so it gets lost in your conversation. Models tend to guess
   early, commit to the guess, and not recover
   ([Laban et al., 2025](https://arxiv.org/abs/2505.06120)).
3. Between you, you produce a document. Neither of you checks whether it makes sense to
   someone who was not there.
4. You send it to a colleague. They had none of the context, and now it is their problem.

Each skill here cuts that chain at one point:

- `regroup` and `clarify` cut step 1. They shrink what you have to hold in your head, without losing the caveats.
- `ask-me-first` and `grill` cut step 2. The model asks or challenges before it guesses.
- `hand-over` and `pick-up` cut step 2 as well. Together they move a derailed chat into a clean one, and the new chat reads the handover cold before it starts.
- `cold-read` cuts step 3. Someone finally reads the document without the context.
- `humanize` cuts step 4. Text that reads as machine-written gets skimmed or distrusted, so your colleague pays less to read it.

## The skills

| Skill | What it does | If you only have one sentence |
|---|---|---|
| `hand-over` | Summarises a chat so you can continue in a fresh one. Checks the summary for completeness, then has a fresh-context reader check that it stands alone | "Summarise everything that matters so I can continue in a new chat. Then review it for completeness (is anything I told you missing?) and for sufficiency (could someone who never saw this chat carry on from it alone?). Fix what you find." |
| `pick-up` | The other half: starts a fresh chat from a handover. Says what is unclear or missing before doing anything | In the new chat: "Before we start: what is unclear or missing in this?" |
| `cold-read` | Gets a document read by a fresh-context reader and reports what only makes sense to its authors | In a **new** chat: "You have never seen the conversation that produced this. Quote every phrase that only makes sense with context you don't have, and tell me what to add." |
| `ask-me-first` | Asks what only you can answer, one question at a time, each with a recommendation | "Before you start, ask me the questions only I can answer, one at a time, each with your recommendation. Anything you can work out yourself, work out." |
| `grill` | Challenges a plan, design, proposal or decision before you commit to it | "Interrogate this before I commit. One concern at a time, only concerns that could change the outcome, each with the risk and what you would do instead." |
| `regroup` | Panic button for a chat that has lost the thread. Re-reads it three times, then reports what was decided, what is open and what was assumed, grouped by importance | "Stop. Don't answer anything new. Go back through this whole conversation twice more, looking for what got buried early and what was said in passing. Then list what we've decided, what's still open, and what you assumed without checking, grouped by how much it matters, most important first." |
| `clarify` | Re-explains a dense answer in plain language without dropping a caveat | "Explain that again in plain language. First list every caveat in your answer. Then rewrite it: what it means, how it works, one example, caveats last. Don't lose anything from your list." |
| `humanize` | Rewrites text so it reads like a person wrote it | "Rewrite this so it sounds like a person wrote it. Cut filler and praise, use plain words, keep sentences short, say the thing directly." |

`cold-read` never does the reading in the chat where the text was written. There, the
model already knows everything the text leaves out, so it cannot see the gaps. In Claude
Code and Cowork the skill starts the plugin's `cold-reader` agent, which runs in its own
context and is handed only the text. Where sub-agents are not available, such as Claude
Desktop chat, the skill says so and gives you a block to paste into a new incognito chat.
Incognito matters: a normal new chat can still search your past conversations.

## Install

A skill is a saved set of instructions that Claude can follow for you, either on its own
when the task matches or when you type `/` and pick it.

**Claude Code.** Inside a Claude Code session, run:

```
/plugin marketplace add davebream/lost-and-found
/plugin install lost-and-found@lost-and-found
```

**Claude Desktop** (paid plans). Open Customize, go to the Plugins tab, choose to add from
a repository, and enter `davebream/lost-and-found`. Anthropic's guide has the exact
clicks: [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).
On Team and Enterprise plans an owner has to have code execution and skills switched on
for the organisation.

Once installed, type `/` in a chat to see the skills, or just describe what you want.
Claude picks the matching skill on its own.

**Anything else:** copy a sentence from the table above.

## One setting worth changing

Add this to your assistant's standing instructions (in Claude: Settings, then the
instructions for Claude):

> Don't agree with me to be polite. If I'm wrong, say so and say why. If you don't know
> something, say "unknown" instead of guessing.

## What these skills cannot do

They are instructions, not enforcement. Nothing here runs code, writes files or stops the
model from skipping a step. They make the right behaviour the default. They do not
guarantee it.

And no skill replaces reading what you are about to send.

## Background

- [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120). The
  same task scored 39% lower on average when the information arrived over several turns
  instead of all at once. The authors' advice: start a new chat with everything in one
  message. `hand-over` is that advice as a skill.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  Why more context is not better context.
- [LLM as a Broken Telephone](https://arxiv.org/abs/2502.20258). Information distorts as
  it passes through repeated rounds of generation.

## Licence

MIT. See [LICENSE](LICENSE).
