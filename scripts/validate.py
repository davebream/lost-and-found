#!/usr/bin/env python3
"""Repo checks for lost-and-found. No dependencies beyond python3 and git.

  python3 scripts/validate.py                 # structure checks
  python3 scripts/validate.py --base origin/main   # also: content changed => version bumped
"""
import json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "lost-and-found"
errors = []


def fail(msg):
    errors.append(msg)


def frontmatter(path):
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


# 1. Versions agree. plugin.json is compared with its marketplace entry.
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
manifest = json.loads((PLUGIN / ".claude-plugin" / "plugin.json").read_text())
entry = next((p for p in market["plugins"] if p["name"] == manifest["name"]), None)
if entry is None:
    fail("marketplace.json has no entry for the plugin")
elif entry.get("version") != manifest.get("version"):
    fail(f"version mismatch: plugin.json {manifest.get('version')} != marketplace {entry.get('version')}")

# 2. Skills: name matches its folder, limits that Claude Desktop enforces on upload.
skills = sorted(p.parent.name for p in PLUGIN.glob("skills/*/SKILL.md"))
for s in skills:
    fm = frontmatter(PLUGIN / "skills" / s / "SKILL.md")
    if fm.get("name") != s:
        fail(f"skills/{s}: frontmatter name {fm.get('name')!r} does not match the folder")
    if len(fm.get("name", "")) > 64:
        fail(f"skills/{s}: name is over 64 characters")
    d = fm.get("description", "")
    if not d:
        fail(f"skills/{s}: description is missing")
    elif len(d) > 200:
        fail(f"skills/{s}: description is {len(d)} characters, the limit is 200")

# 3. Agents: name matches its file, and every agent a skill relies on exists.
agents = sorted(p.stem for p in PLUGIN.glob("agents/*.md"))
for a in agents:
    if frontmatter(PLUGIN / "agents" / f"{a}.md").get("name") != a:
        fail(f"agents/{a}.md: frontmatter name does not match the file")
for s in skills:
    text = (PLUGIN / "skills" / s / "SKILL.md").read_text(encoding="utf-8")
    for ref in set(re.findall(r"`([a-z][a-z0-9-]+)`\s+agent", text)):
        if ref not in agents:
            fail(f"skills/{s}: relies on agent `{ref}`, which does not exist")
    for ref in set(re.findall(r"the `([a-z][a-z0-9-]+)` skill", text)):
        if ref not in skills:
            fail(f"skills/{s}: points to skill `{ref}`, which does not exist")

# 4. README and manifests describe what is actually there.
readme = (ROOT / "README.md").read_text(encoding="utf-8")
for s in skills:
    if f"`{s}`" not in readme:
        fail(f"README.md does not mention the skill `{s}`")
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
for label, desc in (("plugin.json", manifest.get("description", "")), ("marketplace.json", (entry or {}).get("description", ""))):
    m = re.match(r"(\w+) instruction-only skills", desc)
    if m and m.group(1).lower() in words and words.index(m.group(1).lower()) != len(skills):
        fail(f"{label} says {m.group(1)} skills, there are {len(skills)}")

# 5. House style: no em or en dashes anywhere in the prose. humanize promises it.
for path in list(ROOT.glob("*.md")) + list(PLUGIN.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    for ch, label in (("—", "em dash"), ("–", "en dash")):
        if ch in text:
            fail(f"{path.relative_to(ROOT)}: contains an {label}")

# 6. A public repo needs a licence.
if not (ROOT / "LICENSE").exists():
    fail("LICENSE is missing")

# 7. Anthropic's own validator, when the claude CLI is on this machine.
if shutil.which("claude"):
    for target in (ROOT, PLUGIN):
        r = subprocess.run(["claude", "plugin", "validate", str(target)], capture_output=True, text=True)
        if r.returncode != 0:
            fail(f"claude plugin validate failed for {target.relative_to(ROOT) or '.'}:\n{r.stdout}{r.stderr}")
else:
    print("note: claude CLI not found, skipped `claude plugin validate`")

# 8. Versions are cache keys. If plugin content changed since --base and the version did
#    not, people who already installed the plugin never receive the change.
if "--base" in sys.argv:
    base = sys.argv[sys.argv.index("--base") + 1]
    def git(*a):
        return subprocess.run(["git", "-C", str(ROOT), *a], capture_output=True, text=True)
    if git("rev-parse", "--verify", base).returncode != 0:
        print(f"note: base ref {base} not found, skipped the version-bump check")
    else:
        changed = [p for p in git("diff", "--name-only", base, "--", "plugins/").stdout.split() if p]
        changed += [p for p in git("ls-files", "--others", "--exclude-standard", "plugins/").stdout.split() if p]
        manifest_rel = "plugins/lost-and-found/.claude-plugin/plugin.json"
        content = [p for p in changed if p != manifest_rel]
        old = git("show", f"{base}:{manifest_rel}")
        old_version = json.loads(old.stdout).get("version") if old.returncode == 0 else None
        if content and old_version == manifest.get("version"):
            fail(f"plugin content changed since {base} but the version is still {old_version}. Bump it in plugin.json and marketplace.json.")

if errors:
    print("FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print(f"ok: {len(skills)} skills, {len(agents)} agent(s), version {manifest.get('version')}")
