---
puppeteer:
  format: "A4"
  scale: 0.9
  landscape: false
  printBackground: true
  displayHeaderFooter: true
  headerTemplate: |
    <div style="font-size:9px; color:#888; text-align:center; width:100%; border-bottom:1px solid #ddd; padding-bottom:4px;">
      Cursor 终端粘贴中文乱码——深度根因分析与完整排查报告
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

# Cursor 终端粘贴中文乱码——深度根因分析与完整排查报告

> **作者**：Fishcool123
> **日期**：2026-06-24
> **环境**：Windows 11 + Cursor 3.8.23 + Claude Code 2.1.187
>
> 折腾了整整一晚上，从改系统编码到装 PowerShell 7、从终端换壳到退版本，最终定位出一个可复现的 workaround。本文既是踩坑记录，也希望能帮到同样被这个 Bug 折磨的人。

---

## 一、问题表现

在 Cursor IDE（Windows 11）的内置终端里，**Ctrl+V 粘贴中文会变成乱码**。乱码规律极其一致——UTF-8 多字节序列被逐字节当成 Latin-1（ISO-8859-1）单字节字符显示：

| 输入原文 | 终端显示为 |
|----------|-----------|
| `大学物理资料` | `å¤§å­¦ç©çèµæ` |
| `建议` | `å»ºè®®` |
| `粘贴中文测试` | `ç²è´´ä¸­ææµè¯` |

**五条关键特征**：

1. ✅ 键盘打字中文**完全正常**——只有粘贴出问题
2. ✅ Cursor 编辑器里粘贴中文**完全正常**——剪贴板本身没问题
3. ❌ 影响**所有 Shell**——Git Bash、PowerShell 5/7、CMD 全部中招
4. ❌ Windows 系统 UTF-8 Beta **已开启仍无效**
5. ⚠️ Cursor 3.8.x 更新后才出现——之前一个多月完全正常

---

## 二、环境与版本时间线

| 项目 | 最初正常期 | 故障出现期 | 当前（最新） |
|------|-----------|-----------|-------------|
| Cursor | ≤ 3.7.x | **3.8.22（6/22 更新）** | 3.8.23 |
| Claude Code 扩展 | ≤ 2.1.184 | **2.1.185（6/21）** | 2.1.187 |
| Claude Code CLI | ≤ 2.1.185 | **2.1.186（6/21）** | 2.1.187 |

**触发窗口**：6月21-22日，Cursor 和 Claude Code 扩展几乎同时更新。回退 Cursor 到 3.7.42 **无效**，说明问题并非单纯跟随 Cursor 版本，而是更深层的依赖（Electron、xterm.js、node-pty）或 Claude Code 扩展内部改动。

| 环境项 | 值 |
|--------|-----|
| OS | Windows 11 Home China 10.0.26200 |
| 终端 Shell | Git Bash 5.3.9 (MSYS2 3.6.7) |
| 系统区域 | zh-CN |
| 系统 UTF-8 Beta | ✅ ACP/OEMCP 均已变为 65001 |

---

## 三、终极 workaround：反复英文粘贴热身法 🔥

**这是目前唯一可复现的临时解决方案。**

### 操作步骤

每个新开的终端会话中：

1. **反复 Ctrl+V 粘贴纯英文**——每次几个单词即可（如 `hello world`）
2. 某一次粘贴后，管线的 UTF-8 处理被"激活"
3. **此后粘贴中文**——正常 ✅

### 关键发现（2026-06-24 修正）

> **不是"第一次英文就行"**，也不是"先贴英文再贴中文"的固定两步。

实际行为是：终端的粘贴管线初始化是一个**概率事件**。每次英文粘贴都有一定概率触发初始化，但不是 100%。有时一次就激活了，有时要贴三四次才激活。一旦激活（即某次英文粘贴后，管线进入正常 UTF-8 模式），**整个终端会话期间**粘贴中文都正常。

### 为什么英文能激活而中文不能？

| 粘贴内容 | 字节特征 | 单字节模式下 | 能否激活管线 |
|----------|---------|-------------|-------------|
| 纯英文 | 全部 ≤ 0x7F（ASCII） | 正确渲染 | ✅ 同时触发初始化 |
| 中文 | 含 ≥ 0x80 多字节序列 | 乱码（Latin-1 逐字节） | ❌ 初始化被破坏 |

英文的好处是：即使在"未初始化"的单字节模式下，ASCII 字节的显示也是正确的，所以你在激活过程中看到的都是正常英文，某个瞬间激活悄然完成——表面无感。

### 触发条件严格度

| 操作 | 能否触发激活 |
|------|-------------|
| 键盘输入英文 | ❌（走键盘事件通道，不触发粘贴管线） |
| `printf '\e[200~ok\e[201~'` 模拟粘贴序列 | ❌（绕过剪贴板 API） |
| `clip.exe` 预置英文后按 Ctrl+V | ❌（需真正从剪贴板取） |
| **真实 Ctrl+V 从剪贴板粘贴英文** | ✅（唯一方式，但需反复） |

---

## 四、13 项已证实的无效方案

| # | 方案 | 简要操作 | 结果 |
|---|------|---------|------|
| 1 | 终端字体配置 | `terminal.integrated.fontFamily` 加中文字体 | ❌ |
| 2 | 禁用 bracketed paste | `enableBracketedPaste: false` | ❌ |
| 3 | PowerShell chcp 65001 | 启动参数强制 UTF-8 | ❌ |
| 4 | Reload Window | `Ctrl+Shift+P` → 重载 | ⚠️ 偶尔好转，不持久 |
| 5 | Windows 系统 UTF-8 Beta | 区域设置 → Unicode UTF-8 → 重启 | ❌ |
| 6 | MSYS=disable_pcon | 终端环境变量禁用 ConPTY | ❌ |
| 7 | Panel ↔ Terminal 切换 | `claudeCode.preferredLocation` | ❌ |
| 8 | PowerShell 7（pwsh） | winget 安装，原生 UTF-8 | ❌ |
| 9 | 改用 CMD | 默认终端改 CMD + chcp 65001 | ❌（更差） |
| 10 | 回退 Cursor 版本 | 装 3.7.42 | ❌（Bug 仍在） |
| 11 | PYTHONUTF8=1 | 终端环境变量 | ❌ |
| 12 | printf 模拟粘贴序列 | `\e[200~ok\e[201~` | ❌（未触发粘贴事件） |
| 13 | clip.exe 自动预放英文 | `.bashrc` 加 `echo -n "ok" \| clip.exe` | ❌ |

**核心结论**：问题不在 Shell 层、不在 Windows 系统编码层、不在字体层，而在 **Cursor 终端（xterm.js）→ node-pty → ConPTY** 这条输入管线的粘贴事件处理中。

---

## 五、根因深度分析

### 5.1 排除法定位

```
剪贴板 UTF-16 ✅
    ↓ Electron clipboard.readText()
正确的文本 ✅
    ↓ xterm.js paste handler
【问题高发区】← 粘贴管线初始化时序 Bug
    ↓ node-pty WriteFile
ConPTY 输入管道
    ↓ conhost.exe → KEY_EVENT record
Shell stdin（接收到的字节已损坏）
```

逐一排除：
- 编辑器粘贴正常 → 剪贴板、Electron clipboard API 正常
- 所有 Shell 都受影响 → 不是特定 Shell 的问题
- 系统 UTF-8 Beta 开启仍无效 → 不是传统"Windows 编码不对"
- PowerShell 7（原生 UTF-8）也无效 → 不是 PowerShell 5.1 的编码缺陷
- CMD 比 Git Bash 更差 → 说明 MSYS2 层不是唯一相关

### 5.2 核心假设：粘贴管线的非确定性"冷启动"问题

我们推测定位于 **ConPTY 输入管的代码页读取存在竞态条件**：

```
终端会话创建
    ↓
ConPTY 伪控制台初始化
    ├── 代码页缓存 = 启动时的"原始值"（可能是 Latin-1 或未设置）
    ├── 首个粘贴事件到来时，尝试读取控制台代码页
    │       ↓
    │   读取操作存在时序不确定性（竞态/缓存未刷新）
    │       ↓
    │   ┌── 时序 A：成功读到 65001 (UTF-8) → 激活 ✅
    │   │
    │   └── 时序 B：读到旧值（Latin-1）
    │       → 多字节序列被逐字节解释 → 乱码 ❌
    │       → 代码页缓存未刷新
    │       → 需再次触发粘贴事件来重新读取
    │
    └── 不断重复粘贴 → 某次时序对齐 → 读到 65001 → 激活 ✅
```

这个模型解释了所有观察到的现象：

| 观察 | 模型如何解释 |
|------|-------------|
| 键盘输入正常 | 键盘走 `KEY_EVENT` 直通路径，不触发这段代码页读取逻辑 |
| 所有 Shell 都受影响 | 代码页读取发生在 ConPTY 层，与 Shell 无关 |
| 系统 UTF-8 开启仍无效 | 系统设置是 65001 没错，但 ConPTY 初始化阶段读到的缓存值是旧值 |
| CMD 更差 | CMD 的 conhost 不走 ConPTY 的同一代码页读取路径 |
| 反复贴英文才能激活 | 每次粘贴都触发代码页重读，概率性命中正确值 |
| 激活后全会话稳定 | 代码页缓存一旦正确写入，不会被后续操作改变 |
| 贴中文永远不行 | 首次中文粘贴触发的是"读到旧值"路径，破坏了初始化状态 |
| 回退 Cursor 版本无效 | 问题出在 Electron/node-pty/xterm.js 的依赖版本，不是 Cursor 自身代码 |

### 5.3 技术栈各层分析

**xterm.js 粘贴层**
- `Terminal.paste()` → 从 Clipboard API 读取 UTF-16 → 转 UTF-8 → 写入 node-pty
- 此层**行为正确**——编辑器粘贴（不经过 PTY）完全正常
- 问题在**下游**（写入 PTY 后）

**node-pty（Windows ConPTY 后端）**
- 通过 `CreatePseudoConsole` 创建 ConPTY
- 通过 `WriteFile` 将 UTF-8 字节写入输入管道
- ConPTY 初始化时，控制台代码页的读取可能存在竞态

**ConPTY（conhost.exe）**
- 将输入管道字节转换为 `KEY_EVENT_RECORD`
- 依赖 `GetConsoleCP()` 或等效内部变量来确定字节→Unicode 的转换编码
- 首次读取时，内部缓存的代码页可能尚未与系统设置（65001）同步

### 5.4 为什么 2026 年 6 月 21-22 日突然出现？

两个更新的交集：
1. **Cursor 3.8.22**：可能升级了 Electron 版本（VS Code 上游合并），连带更新了 xterm.js 和 node-pty 的实现
2. **Claude Code 扩展 2.1.185/2.1.186**：可能调整了终端会话的管理方式（创建/销毁 PTY 的生命周期），影响了 ConPTY 的初始化时序

之前一个多月完全正常，说明老版本依赖链没有这个竞态条件。

---

## 六、给受影响的用户

### 立即可用的 workaround

1. **反复英文粘贴热身**：新终端 → 反复贴英文（3~5 次）→ 直到某次贴完后中文正常
2. **键盘打字替代粘贴**：键盘输入中文不受影响，急用时打字代替
3. **外部 Windows Terminal**：`Win+R` → `wt` → 运行 `claude`，粘贴完全正常（绕过 Cursor 终端）
4. **Claude Code Panel 模式**：`Ctrl+Shift+P` → `Claude Code: Open in Panel`，Panel 的 webview 输入框粘贴中文正常

### 持续关注

5. 在 Cursor 论坛相关帖子里跟踪进度：
   - [Chinese text copied from terminal is garbled](https://forum.cursor.com/t/chinese-text-copied-from-terminal-is-garbled-utf-8-mojibake/161982)
   - [Windows: Cursor Hooks corrupt Chinese UTF-8 characters in stdin](https://forum.cursor.com/t/windows-cursor-hooks-corrupt-chinese-utf-8-characters-in-stdin-replaced-with-question-marks/142878)
6. 关注 xterm.js 和 node-pty 的 GitHub Issues

---

## 七、给 Cursor 开发团队的建议

1. **检查 3.8.22 引入的 Electron / xterm.js / node-pty 版本变更**——哪个依赖的升级触发了这个竞态？
2. **审查 ConPTY 初始化时的代码页设置时机**——`CreatePseudoConsole` 之后、首次 `WriteFile` 之前，是否已确认代码页为 65001？
3. **考虑在 PTY 创建后立即执行一次"热身写入"**：一个 ≤ 1 字节的 ASCII 写入，强制触发代码页缓存刷新。这本质上就是本文 workaround 的自动化实现。
4. **对比 VS Code 同版本 xterm.js 的终端粘贴行为**——如果 VS Code 没有此 Bug，则差异在 Cursor 的 fork 改动中。

---

## 八、附录：当前配置快照

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

> **最后的话**
>
> 这一晚上，从怀疑字体到改 Windows 系统编码再到重装操作系统设置，从换终端换 Shell 到退版本，最后发现一个"反复贴英文直到激活"的土办法，心态确实崩过。
>
> 但说实话，排查过程让我对 Cursor/Electron/xterm.js/node-pty/ConPTY 这条链路有了深刻的理解——多字节字符在每个环节都可能被搞坏，而 Windows ConPTY 的"伪控制台"在现代终端生态里依然是个薄弱环节。
>
> 如果你也在被这个 Bug 折磨，希望这篇报告能让你少走弯路。
>
> 如果你有新的解法或发现，请在 Cursor 论坛接力——这个 Bug 从 2025 年 11 月就有人报了，至今仍未修复。更多的声音和细节才能让它被真正重视。
>
> —— Fishcool123，2026-06-24
