---
puppeteer:
  format: "A4"
  scale: 0.9
  landscape: false
  printBackground: true
  displayHeaderFooter: true
  headerTemplate: |
    <div style="font-size:9px; color:#888; text-align:center; width:100%; border-bottom:1px solid #ddd; padding-bottom:4px;">
      Cursor Terminal Chinese Paste Corruption — Root Cause Analysis & Complete Investigation Report
    </div>
  footerTemplate: |
    <div style="font-size:9px; color:#888; text-align:center; width:100%; border-top:1px solid #ddd; padding-top:4px;">
      <span class="pageNumber"></span> / <span class="totalPages"></span>
    </div>
  margin:
    top: "1.2cm"
    bottom: "1.2cm"
    left: "1.2cm"
    right: "1.2cm"
---

# Cursor Terminal Chinese Paste Corruption — Root Cause Analysis & Complete Investigation Report

> **Author**: Fishcool123
> **Date**: 2026-06-24
> **Environment**: Windows 11 + Cursor 3.8.23 + Claude Code 2.1.187
>
> After an entire night of troubleshooting — from tweaking system locale settings to installing PowerShell 7, from switching terminal shells to downgrading Cursor versions — I eventually discovered a reproducible workaround. This post is both a record of that journey and a resource for others suffering from the same bug.

---

## 1. Problem Description

In Cursor IDE's integrated terminal on Windows 11, **pasting Chinese text via Ctrl+V produces garbled (mojibake) output**. The corruption pattern is extremely consistent — UTF-8 multi-byte sequences are interpreted byte-by-byte as Latin-1 (ISO-8859-1):

| Original Input | Terminal Output |
|---------------|-----------------|
| `大学物理资料` (University Physics Materials) | `å¤§å­¦ç©çèµæ` |
| `建议` (Suggestion) | `å»ºè®®` |
| `粘贴中文测试` (Paste Chinese Test) | `ç²è´´ä¸­ææµè¯` |

**Five key characteristics**:

1. ✅ **Typing** Chinese via keyboard works **perfectly** — only pasting is broken
2. ✅ Pasting Chinese in Cursor's **code editor** works **perfectly** — the clipboard itself is fine
3. ❌ Affects **all shells** — Git Bash, PowerShell 5/7, and CMD are all impacted
4. ❌ Enabling Windows **system-wide UTF-8 Beta** does **not** fix it
5. ⚠️ The issue appeared **after the Cursor 3.8.x update** — it worked flawlessly for over a month prior

---

## 2. Environment & Version Timeline

| Component | Pre-Bug (Working) | Bug Introduced | Current (Latest) |
|-----------|-------------------|----------------|-------------------|
| Cursor | ≤ 3.7.x | **3.8.22 (June 22 update)** | 3.8.23 |
| Claude Code extension | ≤ 2.1.184 | **2.1.185 (June 21)** | 2.1.187 |
| Claude Code CLI | ≤ 2.1.185 | **2.1.186 (June 21)** | 2.1.187 |

**Trigger window**: June 21–22, 2026. Both Cursor and the Claude Code extension updated almost simultaneously. Downgrading Cursor to 3.7.42 did **not** resolve the issue, suggesting the root cause lies in deeper dependencies (Electron, xterm.js, node-pty) rather than Cursor's own code.

| System Detail | Value |
|---------------|-------|
| OS | Windows 11 Home China 10.0.26200 |
| Default Shell | Git Bash 5.3.9 (MSYS2 3.6.7) |
| System Locale | zh-CN (Chinese Simplified) |
| System UTF-8 Beta | ✅ Enabled (ACP/OEMCP = 65001) |

---

## 3. The Workaround: Repeated English Paste "Warm-Up" 🔥

**This is the only reproducible workaround discovered so far.**

### Steps

For every new terminal session:

1. **Paste pure English text repeatedly** via Ctrl+V — a few words each time (e.g., `hello world`)
2. At some iteration, the paste pipeline's UTF-8 handling gets "activated"
3. **Paste Chinese** — it now works normally ✅

### Critical Refinement (2026-06-24)

> This is **not** a simple "paste English once, then Chinese forever" pattern.

The actual behavior is: the terminal's paste pipeline initialization is **non-deterministic**. Each English paste has a probability of triggering initialization, but not 100%. Sometimes it activates on the first attempt; other times it takes 3–4 pastes. Once activated, Chinese pasting remains functional for the entire terminal session.

### Why English Works but Chinese Doesn't

| Paste Content | Byte Characteristics | Behavior in Single-Byte Mode | Can Activate Pipeline? |
|---------------|---------------------|------------------------------|------------------------|
| Pure English | All ≤ 0x7F (ASCII) | Renders correctly | ✅ Activation succeeds silently |
| Chinese text | Contains ≥ 0x80 multi-byte sequences | Garbled (byte-by-byte Latin-1) | ❌ Initialization corrupted |

English has the advantage: even in the "uninitialized" single-byte mode, ASCII bytes display correctly. You see normal English text while the activation quietly completes behind the scenes — invisible to you.

### Trigger Condition Strictness

| Action | Can Trigger Activation? |
|--------|------------------------|
| Keyboard-typing English | ❌ (different event channel — keyboard, not paste) |
| `printf '\e[200~ok\e[201~'` simulated paste sequence | ❌ (bypasses clipboard API) |
| `clip.exe` to pre-populate clipboard, then Ctrl+V | ❌ (must originate from a real clipboard read) |
| **Real Ctrl+V paste of English from clipboard** | ✅ (the only way — but requires repetition) |

---

## 4. Thirteen Failed Attempts

| # | Approach | Brief Operation | Result |
|---|----------|----------------|--------|
| 1 | Terminal font config | `terminal.integrated.fontFamily` with CJK fonts | ❌ |
| 2 | Disable bracketed paste | `enableBracketedPaste: false` | ❌ |
| 3 | PowerShell chcp 65001 | Force UTF-8 via startup args | ❌ |
| 4 | Reload Window | `Ctrl+Shift+P` → Developer: Reload | ⚠️ Occasionally helped, not persistent |
| 5 | Windows system UTF-8 Beta | Region settings → Unicode UTF-8 → Reboot | ❌ |
| 6 | MSYS=disable_pcon | Terminal env var to disable ConPTY | ❌ |
| 7 | Panel ↔ Terminal switch | `claudeCode.preferredLocation` toggle | ❌ |
| 8 | PowerShell 7 (pwsh) | winget install, native UTF-8 shell | ❌ |
| 9 | Switch to CMD | Default terminal to CMD + chcp 65001 | ❌ (worse — every paste broken) |
| 10 | Downgrade Cursor | Install 3.7.42 | ❌ (bug persists) |
| 11 | PYTHONUTF8=1 | Terminal environment variable | ❌ |
| 12 | Simulated paste sequence | `\e[200~ok\e[201~` in `.bashrc` | ❌ (didn't trigger paste event) |
| 13 | clip.exe auto seed | `echo -n "ok" \| clip.exe` in `.bashrc` | ❌ |

**Key takeaway**: The problem is neither in the shell layer, nor in the Windows system encoding, nor in the font. It lies in the **paste event handling pipeline** within: **Cursor terminal (xterm.js) → node-pty → ConPTY**.

---

## 5. Root Cause Analysis

### 5.1 Pinpointing via Elimination

```
Clipboard UTF-16 ✅
    ↓ Electron clipboard.readText()
Correct text string ✅
    ↓ xterm.js paste handler
【HIGH SUSPICION ZONE】← Paste pipeline initialization timing bug
    ↓ node-pty WriteFile
ConPTY input pipe
    ↓ conhost.exe → KEY_EVENT records
Shell stdin (receives corrupted bytes)
```

One-by-one elimination:
- Editor paste works → clipboard and Electron clipboard API are fine
- All shells affected → not a specific shell's encoding configuration
- Windows UTF-8 Beta enabled, still broken → not a "Windows code page" issue
- PowerShell 7 (native UTF-8) also broken → not PowerShell 5.1's encoding quirk
- CMD worse than Git Bash → MSYS2 layer is not the sole culprit

### 5.2 Core Hypothesis: Non-Deterministic "Cold Start" in ConPTY

We hypothesize a **race condition in ConPTY's codepage reading during paste initialization**:

```
Terminal session created
    ↓
ConPTY pseudo-console initialized
    ├── Internal codepage cache = "raw" value at startup (possibly Latin-1 or unset)
    ├── First paste event arrives → attempts to read console codepage
    │       ↓
    │   Read operation has timing non-determinism (race / stale cache)
    │       ↓
    │   ┌── Timing A: successfully reads 65001 (UTF-8) → ACTIVATION ✅
    │   │
    │   └── Timing B: reads stale/old value (Latin-1)
    │       → Multi-byte sequences interpreted byte-by-byte → GARBLED ❌
    │       → Codepage cache NOT refreshed
    │       → Requires another paste event for a fresh read attempt
    │
    └── Repeated pasting → eventually timing aligns → reads 65001 → ACTIVATED ✅
```

This model explains every observation:

| Observation | How the Model Explains It |
|-------------|--------------------------|
| Keyboard input works fine | Keyboard events go through `KEY_EVENT` directly, bypassing this codepage read logic |
| All shells affected | Codepage reading happens at the ConPTY layer, shell-agnostic |
| System UTF-8 Beta enabled, still broken | System setting IS 65001, but ConPTY's initialization reads a stale cache value |
| CMD is worse | CMD's conhost doesn't go through the same ConPTY codepage read path |
| Repeated English pasting eventually works | Each paste triggers a fresh codepage read; probabilistically hits the correct value |
| Once activated, stable for entire session | Once the codepage cache is correctly set, no subsequent operation changes it |
| Pasting Chinese never works first | First Chinese paste triggers the "read stale value" path, corrupting initialization |
| Downgrading Cursor doesn't help | Bug is in Electron/node-pty/xterm.js dependency layer, not Cursor's own code |

### 5.3 Layer-by-Layer Technical Analysis

**xterm.js Paste Layer**
- `Terminal.paste()` → reads from Clipboard API (UTF-16) → converts to UTF-8 → writes to node-pty
- This layer **behaves correctly** — editor paste (which doesn't go through PTY) works perfectly
- The problem is **downstream** (after writing to PTY)

**node-pty (Windows ConPTY Backend)**
- Creates ConPTY via `CreatePseudoConsole`
- Writes UTF-8 bytes to the input pipe via `WriteFile`
- During ConPTY initialization, the read of the console codepage may encounter a race condition

**ConPTY (conhost.exe)**
- Converts input pipe bytes to `KEY_EVENT_RECORD` structures
- Relies on `GetConsoleCP()` or equivalent internal variable to determine byte→Unicode conversion encoding
- On first read, the internally cached codepage may not yet be synchronized with the system setting (65001)

### 5.4 Why Did This Suddenly Appear in June 2026?

The intersection of two updates:
1. **Cursor 3.8.22**: likely upgraded the Electron version (upstream VS Code merge), bringing updated xterm.js and node-pty implementations
2. **Claude Code extension 2.1.185/2.1.186**: may have adjusted terminal session lifecycle management (PTY creation/destruction timing), altering ConPTY initialization sequencing

The fact that it worked flawlessly for over a month prior confirms that the old dependency chain lacked this race condition.

---

## 6. For Affected Users

### Immediate Workarounds

1. **Repeated English paste warm-up**: New terminal → paste English repeatedly (3–5×) → Chinese paste works
2. **Type instead of paste**: Keyboard-typed Chinese is unaffected — use this when in a hurry
3. **External Windows Terminal**: `Win+R` → `wt` → run `claude`, paste works perfectly (bypasses Cursor terminal entirely)
4. **Claude Code Panel mode**: `Ctrl+Shift+P` → `Claude Code: Open in Panel`, the panel's webview input box handles Chinese paste correctly

### Stay Updated

5. Track these Cursor forum threads:
   - [Chinese text copied from terminal is garbled](https://forum.cursor.com/t/chinese-text-copied-from-terminal-is-garbled-utf-8-mojibake/161982)
   - [Windows: Cursor Hooks corrupt Chinese UTF-8 characters in stdin](https://forum.cursor.com/t/windows-cursor-hooks-corrupt-chinese-utf-8-characters-in-stdin-replaced-with-question-marks/142878)
6. Watch xterm.js and node-pty GitHub Issues for related fixes

---

## 7. Recommendations for the Cursor Development Team

1. **Audit the Electron / xterm.js / node-pty version changes introduced in 3.8.22** — which dependency upgrade triggered this race condition?
2. **Review ConPTY codepage setup timing** — between `CreatePseudoConsole` and the first `WriteFile`, is the codepage guaranteed to be 65001?
3. **Consider performing a "warm-up write" immediately after PTY creation**: a single ASCII byte write to force codepage cache refresh. This is essentially the automated version of the workaround discovered in this investigation.
4. **Compare with VS Code's terminal paste behavior at the same xterm.js version** — if VS Code does not exhibit this bug, the difference lies in Cursor's fork modifications.

---

## 8. Appendix: Current Configuration Snapshots

### Cursor settings.json
`%APPDATA%\Cursor\User\settings.json`
```json
{
    "window.autoDetectColorScheme": true,
    "claudeCode.preferredLocation": "panel",
    "markdown-preview-enhanced.chromePath": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
}
```

### .bashrc
`C:\Users\<user>\.bashrc`
```bash
PS1='\[\033[1;32m\]\u@\h\[\033[0m\]:\[\033[1;34m\]\w\[\033[0m\]\[\033[1;31m\]$(__git_ps1 " (%s)")\[\033[0m\]\n\$ '
```

### .claude/settings.json
`C:\Users\<user>\.claude\settings.json`
```json
{
  "model": "deepseek-v4-pro[1M]",
  "language": "中文"
}
```

---

> **Final Words**
>
> Over the course of this marathon debugging session, I went from suspecting font issues, to changing Windows system encoding, to switching terminal shells, to downgrading Cursor versions. The solution — "paste English repeatedly until it works" — is the kind of workaround that makes you laugh and cry at the same time.
>
> But honestly, the investigation gave me a deep appreciation for how fragile multi-byte character handling can be across the entire stack: Electron → xterm.js → node-pty → ConPTY. Windows' ConPTY remains a weak link in the modern terminal ecosystem — and CJK users bear the cost.
>
> If you're also suffering from this bug, I hope this report saves you hours of frustration.
>
> If you have new findings or solutions, please chime in on the Cursor forum — this bug has been reported since November 2025 and remains unfixed. More voices and detailed reproduction cases are the only way to get it prioritized.
>
> — Fishcool123, 2026-06-24
