<div align="center">

# lost-and-found

**Small skills for the moment you and your AI lose each other.**

Eight skills for Claude. A skill is a saved instruction that Claude follows for you. No coding needed.<br>
Install them once, or copy a single sentence and paste it into any AI chat.

[![Works in Claude Code, Cowork and Claude Desktop](https://img.shields.io/badge/works_in-Claude_Code_%C2%B7_Cowork_%C2%B7_Claude_Desktop-d97757)](#install)
[![Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdavebream%2Flost-and-found%2Fmain%2Fplugins%2Flost-and-found%2F.claude-plugin%2Fplugin.json&query=%24.version&label=version&color=4c8bf5)](plugins/lost-and-found/.claude-plugin/plugin.json)
[![Licence: MIT](https://img.shields.io/badge/licence-MIT-2ea44f)](LICENSE)

[Pick a skill](#pick-a-skill) ·
[The problem](#the-problem) ·
[No install? Copy a sentence](#no-install-copy-a-sentence) ·
[Install](#install) ·
[Limits](#what-these-skills-cannot-do)

</div>

---

## Pick a skill

Start from what just happened to you.

| What just happened | Use | What you get |
|---|---|---|
| The chat went in circles and you no longer know what was decided | `regroup` | One ordered list: what was decided, what is open, what was assumed |
| The answer is probably right but too dense to take in | `clarify` | The same answer in plain language, with every caveat kept |
| You are about to give the AI a task, and it usually guesses wrong | `ask-me-first` | The questions only you can answer, one at a time, each with a recommendation |
| You have a plan and want it tested before you commit | `grill` | Your plan challenged, worst concern first |
| Correcting the chat no longer works and you want to start over | `hand-over` | A checked summary you can carry into a fresh chat |
| You are starting a new chat from a summary | `pick-up` | The AI says what is unclear or missing before it does any work |
| You are about to send a document to someone who was not there | `cold-read` | A reader with no context lists what only makes sense to the authors |
| Your text sounds machine-written | `humanize` | Text that reads like a person wrote it |

> [!TIP]
> You do not have to install anything. Every skill has a one-sentence version you can paste
> into Claude, ChatGPT or any other AI chat. See
> [No install? Copy a sentence](#no-install-copy-a-sentence).

## The problem

When you work with an AI assistant, context gets lost in both directions. Then it travels.

| Step | What goes wrong | Skills that help |
|:---:|---|---|
| 1 | The AI writes more than you can read, so **you get lost in its output**. | `regroup`, `clarify` |
| 2 | You correct it bit by bit, so **it gets lost in your conversation**. Models tend to guess early, commit to the guess, and not recover ([Laban et al., 2025](https://arxiv.org/abs/2505.06120)). | `ask-me-first`, `grill`, `hand-over`, `pick-up` |
| 3 | Between you, you produce a document. **Neither of you checks** whether it makes sense to someone who was not there. | `cold-read` |
| 4 | You send it to a colleague. They had none of the context, and **now it is their problem**. | `humanize` |

Each skill cuts that chain at one point:

- `regroup` puts everything in one ordered list, so you can stop holding it in your head.
  `clarify` makes a dense answer smaller without losing a caveat.
- `ask-me-first` and `grill` make the AI ask or challenge before it guesses.
- `hand-over` and `pick-up` work as a pair. Together they move a derailed chat into a clean
  one, and the new chat reads the handover cold before it starts.
- `cold-read` means someone finally reads the document without the context.
- `humanize` helps because text that reads as machine-written gets skimmed or distrusted.
  Your colleague pays less to read it.

## No install? Copy a sentence

Each block below is one skill in a single message. Click a name to open it, then use the copy
button in the corner of the grey box and paste it into your chat.

<details>
<summary><b><code>regroup</code></b>: the panic button for a chat that has lost the thread</summary>

Re-reads the whole chat three times, then reports what was decided, what is open and what
was assumed, grouped by importance.

```text
Stop. Don't answer anything new. Go back through this whole conversation
twice more, looking for what got buried early and what was said in passing.
Then list what we've decided, what's still open, and what you assumed without
checking, grouped by how much it matters, most important first.
```

</details>

<details>
<summary><b><code>clarify</code></b>: a dense answer, again, in plain language</summary>

Re-explains a dense answer without dropping a caveat.

```text
Explain that again in plain language. First list every caveat in your answer.
Then rewrite it: what it means, how it works, one example, caveats last.
Don't lose anything from your list.
```

</details>

<details>
<summary><b><code>ask-me-first</code></b>: questions before guesses</summary>

Asks what only you can answer, one question at a time, each with a recommendation.

```text
Before you start, ask me the questions only I can answer, one at a time, each
with your recommendation. Anything you can work out yourself, work out.
```

</details>

<details>
<summary><b><code>grill</code></b>: test a plan before you commit to it</summary>

Challenges a plan, design, proposal or decision.

```text
Interrogate this before I commit. One concern at a time, worst first, only
concerns that could change the outcome, each with the risk and what you would
do instead. Wait for my answer before the next one.
```

</details>

<details>
<summary><b><code>hand-over</code></b>: leave a derailed chat with a summary you can trust</summary>

Summarises a chat so you can continue in a fresh one. Checks the summary for completeness,
then has a fresh reader check that it stands alone.

```text
Summarise everything that matters so I can continue in a new chat. Check it
against our conversation: is anything I told you missing? Then mark every
phrase that only makes sense if you were here. You cannot fully judge that,
so I will check those in a fresh chat.
```

</details>

<details>
<summary><b><code>pick-up</code></b>: start the new chat from that summary</summary>

The other half of `hand-over`. Says what is unclear or missing before doing anything. Paste
your summary into a new chat, followed by this:

```text
Before we start, and before you do any work: what is unclear or missing in
this? Do not guess, and do not look anything up.
```

</details>

<details>
<summary><b><code>cold-read</code></b>: find out what only makes sense to the authors</summary>

Gets a document read by someone with no context. Use this one in a **new** chat, ideally an
incognito or temporary one, and paste your document after it:

```text
You have never seen the conversation that produced this. Do not search past
chats or memory. Quote every phrase that only makes sense with context you
don't have, and tell me what to add.
```

</details>

<details>
<summary><b><code>humanize</code></b>: make it read like a person wrote it</summary>

```text
Rewrite this so it sounds like a person wrote it. Cut filler and praise, use
plain words, vary sentence length, say the thing directly.
```

</details>

## Install

A skill is a saved set of instructions that Claude can follow for you. Claude uses it on its
own when the task matches, or you type `/` and pick it. A plugin is the package that installs
all eight skills at once. It is free.

### Claude Desktop and claude.ai

For paid plans. There are two parts: tell Claude where this project lives, then install the
plugin from it.

Two words you will see on the way. A **repository** is the folder of files this project lives
in on GitHub, which is the page you are reading now. You only give Claude its address. You do
not download or run anything yourself. A **marketplace** is Claude's word for a source it can
get plugins from. Nothing is for sale.

1. Open the **Customize** menu and go to the **Plugins** tab.
2. In **Personal plugins**, click **+**, then **Add marketplace**.
3. Choose **Add from a repository** and enter `https://github.com/davebream/lost-and-found`.
4. Find `lost-and-found` in the list and click **Install**.

Anthropic's guide has screenshots:
[Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

> [!NOTE]
> On a Team or Enterprise plan, if the skills do not show up, ask an owner whether skills are
> switched on for the organisation.

### Claude Code

Inside a Claude Code session, run:

```
/plugin marketplace add davebream/lost-and-found
/plugin install lost-and-found@lost-and-found
```

### After installing

Type `/` in a chat to see the skills, or just describe what you want. Claude picks the
matching skill on its own.

### Anything else

Use the sentences in [No install? Copy a sentence](#no-install-copy-a-sentence). They work
anywhere you can paste text.

## Good to know

**`hand-over` and `pick-up` can skip the copy and paste.** Where files can be written, as in
Claude Code, `hand-over` saves to `.claude/handover.md` and `pick-up` finds it there. In a
plain chat you copy the block across yourself.

**`cold-read` never does the reading in the chat where the text was written.** There, the AI
already knows everything the text leaves out, so it cannot see the gaps. In Claude Code and
Cowork the skill starts the plugin's `cold-reader`, a fresh copy of Claude that has never
seen your conversation and is given only the text. Where Claude cannot start such a fresh copy, as in Claude Desktop chat, the
skill says so and gives you a block to paste into a new incognito chat.

> [!IMPORTANT]
> Incognito matters. A normal new chat can still search your past conversations, so it is not
> a truly fresh reader.

**Long chats get summarised behind your back.** When a conversation grows too long, most AI
tools quietly replace the early part with a summary, and a summary loses rules and reasons
first. `hand-over`, `regroup`, `clarify` and `ask-me-first` check for that. Where the full
record can still be reached, as in Claude Code, they search it and do not trust the summary
alone. Where it cannot, they tell you, so you can add what you remember.

## One setting worth changing

Add this to your assistant's standing instructions. In Claude: **Settings**, then the
instructions for Claude.

```text
Don't agree with me to be polite. If I'm wrong, say so and say why. If you don't
know something, say "unknown" instead of guessing.
```

## What these skills cannot do

- **They are instructions, not programs.** Nothing here enforces a step or stops the AI from
  skipping one. They make the right behaviour the default. They do not guarantee it.
- **Two of them are conversations by design.** `ask-me-first` and `grill` are back and
  forth, and long conversations are exactly where models lose the thread. Both carry a
  stopping rule for that reason.
- **The idea underneath `cold-read` is a design bet.** A fresh context catches what the
  authoring context cannot: that fits how context works, and it matches the author's
  experience. It is not something the papers below prove.
- **No skill replaces reading what you are about to send.**

## Background

<details>
<summary>The research behind it</summary>

- [LLMs Get Lost In Multi-Turn Conversation](https://arxiv.org/abs/2505.06120). The same
  task scored 39% lower on average when the information arrived over several turns instead
  of all at once. Most of that drop is unreliability, not lost ability: the same model on
  the same task varies far more from run to run. The authors' advice (section 7.4): try
  again in a new chat, and consolidate what you have said into one message first.
  `hand-over` is that advice as a skill.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).
  Why more context is not better context.
- [LLM as a Broken Telephone](https://arxiv.org/abs/2502.20258). Information distorts as it
  passes through repeated rounds of generation.

</details>

## Licence

MIT. See [LICENSE](LICENSE).
