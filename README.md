# lost-and-found

Small skills for the moment you and your AI lose each other.

Works in Claude Code, Cowork and Claude Desktop chat. If you use something else, the
one-line versions below work anywhere you can paste text.

## The problem

Working with an AI assistant, context gets lost in both directions, and then it travels:

1. The model writes more than you can read, so you get lost in its output.
2. You correct it bit by bit, so it gets lost in your conversation. Models tend to guess
   early, commit to the guess, and not recover
   ([Laban et al., 2025](https://arxiv.org/abs/2505.06120)).
3. Between you, you produce a document. Neither of you checks whether it makes sense to
   someone who was not there.
4. You send it to a colleague. They had none of the context, and now it is their problem.

Each skill here cuts that chain at one point:

- `regroup` and `clarify` cut step 1. `regroup` puts everything in one ordered list so you can stop holding it in your head. `clarify` makes a dense answer smaller without losing a caveat.
- `ask-me-first` and `grill` cut step 2. The model asks or challenges before it guesses.
- `hand-over` and `pick-up` cut step 2 as well. Together they move a derailed chat into a clean one, and the new chat reads the handover cold before it starts.
- `cold-read` cuts step 3. Someone finally reads the document without the context.
- `humanize` cuts step 4. Text that reads as machine-written gets skimmed or distrusted, so your colleague pays less to read it.

## The skills

| Skill | What it does | If you only have one sentence |
|---|---|---|
| `hand-over` | Summarises a chat so you can continue in a fresh one. Checks the summary for completeness, then has a fresh-context reader check that it stands alone | "Summarise everything that matters so I can continue in a new chat. Check it against our conversation: is anything I told you missing? Then mark every phrase that only makes sense if you were here. You cannot fully judge that, so I will check those in a fresh chat." |
| `pick-up` | The other half: starts a fresh chat from a handover. Says what is unclear or missing before doing anything | In the new chat: "Before we start, and before you do any work: what is unclear or missing in this? Do not guess, and do not look anything up." |
| `cold-read` | Gets a document read by a fresh-context reader and reports what only makes sense to its authors | In a **new** chat: "You have never seen the conversation that produced this. Do not search past chats or memory. Quote every phrase that only makes sense with context you don't have, and tell me what to add." |
| `ask-me-first` | Asks what only you can answer, one question at a time, each with a recommendation | "Before you start, ask me the questions only I can answer, one at a time, each with your recommendation. Anything you can work out yourself, work out." |
| `grill` | Challenges a plan, design, proposal or decision before you commit to it | "Interrogate this before I commit. One concern at a time, worst first, only concerns that could change the outcome, each with the risk and what you would do instead. Wait for my answer before the next one." |
| `regroup` | Panic button for a chat that has lost the thread. Re-reads it three times, then reports what was decided, what is open and what was assumed, grouped by importance | "Stop. Don't answer anything new. Go back through this whole conversation twice more, looking for what got buried early and what was said in passing. Then list what we've decided, what's still open, and what you assumed without checking, grouped by how much it matters, most important first." |
| `clarify` | Re-explains a dense answer in plain language without dropping a caveat | "Explain that again in plain language. First list every caveat in your answer. Then rewrite it: what it means, how it works, one example, caveats last. Don't lose anything from your list." |
| `humanize` | Rewrites text so it reads like a person wrote it | "Rewrite this so it sounds like a person wrote it. Cut filler and praise, use plain words, vary sentence length, say the thing directly." |

Where files can be written, as in Claude Code, `hand-over` saves to `.claude/handover.md`
and `pick-up` finds it there, so nothing needs pasting. In a plain chat you copy the block
across yourself.

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

**Claude Desktop and claude.ai** (paid plans). Two parts: add the repository, then install
the plugin from it.

1. Open the **Customize** menu and go to the **Plugins** tab.
2. In **Personal plugins**, click **+**, then **Add marketplace**.
3. Choose **Add from a repository** and enter `https://github.com/davebream/lost-and-found`.
4. Find `lost-and-found` in the list and click **Install**.

Anthropic's guide has screenshots: [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).
If the skills do not show up on a Team or Enterprise plan, ask an owner whether skills are
switched on for the organisation.

Once installed, type `/` in a chat to see the skills, or just describe what you want.
Claude picks the matching skill on its own.

**Anything else:** copy a sentence from the table above.

## One setting worth changing

Add this to your assistant's standing instructions (in Claude: Settings, then the
instructions for Claude):

> Don't agree with me to be polite. If I'm wrong, say so and say why. If you don't know
> something, say "unknown" instead of guessing.

## What these skills cannot do

They are instructions, not programs. Nothing here enforces a step or stops the model from
skipping one. They make the right behaviour the default. They do not
guarantee it.

`ask-me-first` and `grill` are conversations by design, and long conversations are
exactly where models lose the thread. Both carry a stopping rule for that reason.

The idea underneath `cold-read`, that a fresh context catches what the authoring context
cannot, is a design bet. It fits how context works, and it matches the author's
experience. It is not something the papers below prove.

And no skill replaces reading what you are about to send.

## Background

- [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120). The
  same task scored 39% lower on average when the information arrived over several turns
  instead of all at once. Most of that drop is unreliability, not lost ability: the same
  model on the same task varies far more from run to run. The authors' advice (section
  7.4): try again in a new chat, and consolidate what you have said into one message
  first. `hand-over` is that advice as a skill.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  Why more context is not better context.
- [LLM as a Broken Telephone](https://arxiv.org/abs/2502.20258). Information distorts as
  it passes through repeated rounds of generation.

## Licence

MIT. See [LICENSE](LICENSE).
