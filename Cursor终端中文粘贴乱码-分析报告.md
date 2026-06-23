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

> 作者注：折腾了整整一晚上，把几乎所有能试的方案都试了，最后发现一个可复现的临时 workaround。本文既是踩坑记录，也是抛砖引玉，希望帮助后来者不至于像我一样浪费一晚上。

---

## 一、问题表现

在 Cursor IDE（Windows 11）的内置终端里，**Ctrl+V 粘贴中文会变成乱码**。乱码模式非常规律——UTF-8 多字节序列被逐字节当成 Latin-1（ISO-8859-1）显示：

| 输入 | 显示为 |
|------|--------|
| `大学物理资料` | `å¤§å­¦ç©çèµæ` |
| `建议` | `å»ºè®®` |
| `粘贴中文` | `ç²è´´ä¸­æ` |

**关键特征**：
- ✅ 键盘打字中文**完全正常**
- ✅ Cursor 编辑器里粘贴中文**完全正常**  
- ❌ 只有**终端里粘贴中文**会乱码
- ❌ 影响**所有 Shell**（Git Bash、PowerShell 5/7、CMD 均受影响）
- ❌ **Clipboard 本身正常**（同一份剪贴板内容在编辑器粘贴正常）

---

## 二、环境信息

| 项目 | 值 |
|------|-----|
| OS | Windows 11 Home China 10.0.26200 |
| Cursor 版本 | 3.8.22（6月22日更新后触发） |
| Claude Code 扩展 | 2.1.186（6月21日更新） |
| 终端 | Git Bash 5.3.9 / MSYS2 3.6.7 / PowerShell 7 / CMD |
| 系统区域 | zh-CN |
| 系统 UTF-8 Beta | ✅ 已开启（ACP/OEMCP = 65001） |

---

## 三、终极 workaround：英文粘贴热身法 🔥

**这是目前唯一可复现的临时解决方案。**

### 操作步骤

每个新终端会话中：
1. **先 Ctrl+V 粘贴一段纯英文**（任意几个单词都可以，比如 `hello world`）
2. **再 Ctrl+V 粘贴中文** → 正常了 ✅

### 触发条件

| 操作 | 能否触发修复 |
|------|-------------|
| 在终端里**键盘输入**英文 | ❌ 不行 |
| `printf` 模拟粘贴转义序列 | ❌ 不行 |
| `clip.exe` 预放英文到剪贴板 | ❌ 不行 |
| **真正的 Ctrl+V 粘贴英文** | ✅ 可以 |

**结论：必须是真实的剪贴板粘贴事件（Ctrl+V），且内容为纯 ASCII，才能激活终端的中文粘贴能力。**

---

## 四、已证实的无效方案（13项全部失败）

| # | 方案 | 结果 |
|---|------|------|
| 1 | `terminal.integrated.fontFamily` 配中文字体 | ❌ |
| 2 | `terminal.integrated.enableBracketedPaste: false` | ❌ |
| 3 | 终端启动参数加 `chcp 65001` | ❌ |
| 4 | `Developer: Reload Window` | ⚠️ 偶尔有效，不稳定 |
| 5 | Windows 系统 UTF-8 Beta | ❌ |
| 6 | `terminal.integrated.env` 设 `MSYS=disable_pcon` | ❌ |
| 7 | Claude Code Panel ↔ Terminal 切换 | ❌ |
| 8 | 安装并使用 PowerShell 7 | ❌ |
| 9 | 改用 CMD + `chcp 65001` | ❌（更差） |
| 10 | 回退 Cursor 到 3.7.42 | ❌ |
| 11 | `terminal.integrated.env` 设 `PYTHONUTF8=1` | ❌ |
| 12 | `printf '\e[200~ok\e[201~'` 模拟粘贴序列 | ❌ |
| 13 | `clip.exe` 自动放英文到剪贴板 | ❌ |

**特别值得注意：系统 UTF-8 Beta 已经启用，但还是不行**——说明这不是传统的"Windows 编码不对"问题，问题出在更底层。

---

## 五、根因深度分析

### 5.1 排除法定位

通过上述排除，可以精确锁定问题位置：

```
剪贴板（正常） → Electron 剪贴板 API（正常） → Cursor webview（正常）
    → xterm.js paste handler ← 问题很可能在这里
    → node-pty → Windows ConPTY → Shell stdin
```

- 编辑器粘贴正常 → 排除剪贴板和 Cursor 全局编码问题
- 所有 Shell 都有问题 → 排除特定 Shell 编码配置
- 系统 UTF-8 开启无效 → 排除 Windows 系统级编码问题
- PowerShell 7 也无效 → 排除 PowerShell 特定问题
- CMD 更差 → 说明问题甚至不限于 MSYS2/ConPTY

### 5.2 核心假设：粘贴管线的"懒初始化"Bug

xterm.js 的粘贴处理和 ConPTY 的输入管之间存在**初始化时序问题**：

```
终端启动
    ↓
ConPTY 输入管线创建，但 UTF-8 多字节解码器处于 "未热身" 状态
    ↓                       ↓
第一个粘贴 = 纯 ASCII    第一个粘贴 = 中文
    ↓                       ↓
ASCII 字节 0x00-0x7F     UTF-8 多字节序列 E5 A4 A7...
在所有编码中一致           解码器尚未准备好处理多字节
    ↓                       ↓
通过正常 ✅                 逐字节当成 Latin-1 处理 ❌
    ↓                       ↓
粘贴管线完成初始化         乱码产生
    ↓
后续粘贴 — 无论中英文 — 全部正常 ✅
```

### 5.3 技术细节推测

从 xterm.js、node-pty、ConPTY 三层的源码行为推断：

1. **xterm.js** 的粘贴处理调用 `Terminal.paste()`，将剪贴板内容（UTF-16）转换为 UTF-8 字节后写入 `node-pty`
2. **node-pty** 在 Windows 上通过 `WriteFile` 将字节写入 ConPTY 的输入管道
3. **ConPTY** (conhost.exe) 需要将这些字节转换为 `KEY_EVENT` 记录。这个转换依赖于控制台代码页的设置
4. 在**首次写入时**，ConPTY 的代码页缓存可能尚未正确初始化（即使系统已设为 UTF-8），使用的可能是启动时的默认值（Latin-1/CP-1252）
5. **首次写入纯 ASCII 时**：因为 ASCII 在所有编码下字节值一致，转换正确，同时触发了代码页缓存更新
6. **首次写入包含多字节字符时**：多字节序列被错误地按单字节编码（Latin-1）逐字节解释，产生乱码

这也能解释为什么 `clip.exe` 自动放剪贴板没用——粘贴热身的本质不是"剪贴板里有英文"，而是 **ConPTY 的输入管经历了至少一次完整的写入-处理-回显周期**，完成了编码缓存的初始化。

### 5.4 为什么最近才出现？

- **Cursor 3.8.22**（6月22日更新）和 **Claude Code 扩展 2.1.186**（6月21日更新）几乎同时发布
- 可能是 Cursor 更新了 Electron 版本或 xterm.js 版本，改变了粘贴处理的初始化时序
- 也可能是 node-pty 的 Windows 实现有改动，影响了 ConPTY 的初始化行为
- 之前用一个多月完全正常，说明老版本（大概率 Cursor 3.7.x + 旧版 Claude Code 扩展）没有这个问题

---

## 六、给受影响的用户

### 立即可用
1. **英文热身法**：新终端→先贴一段英文→再贴中文（确认可复现 ✅）
2. **键盘打字**：打中文不受影响，急用时打字代替粘贴
3. **Windows Terminal 外部终端**：`Win+R` → `wt` → 运行 `claude`，粘贴完全正常

### 持续关注
4. **等 Cursor 官方修复**：论坛已有多个相关帖子，团队已标记为 "high priority"
5. **关注 xterm.js / node-pty 上游更新**：如果根因在上游组件，更新会一起带过来

---

## 七、给 Cursor 开发团队的建议

如果 Cursor 团队成员看到这篇帖子，以下是我的建议排查方向：

1. **检查 3.8.x 更新的 Electron/xterm.js/node-pty 版本变更**
2. **检查 ConPTY 初始化时的代码页设置时机**——首次写入前是否已确保代码页为 UTF-8？
3. **对比 3.7.x 和 3.8.x 的粘贴处理管线实现差异**
4. **考虑在终端创建后立即写入一个无害的 ASCII 字节序列作为"热身"**（类似本文发现的 workaround 的自动化实现）
5. **参考 VS Code 的终端粘贴实现**——VS Code 的集成终端是否有同样问题？还是 Cursor 特有的 fork 变动？

---

## 八、附录：完整配置文件快照

### Cursor settings.json (`%APPDATA%\Cursor\User\settings.json`)
```json
{
    "window.autoDetectColorScheme": true,
    "claudeCode.preferredLocation": "panel",
    "markdown-preview-enhanced.chromePath": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
}
```

### .bashrc (`C:\Users\<user>\.bashrc`)
```bash
PS1='\[\033[1;32m\]\u@\h\[\033[0m\]:\[\033[1;34m\]\w\[\033[0m\]\[\033[1;31m\]$(__git_ps1 " (%s)")\[\033[0m\]\n\$ '
```

### .claude/settings.json (`C:\Users\<user>\.claude\settings.json`)
```json
{
  "model": "deepseek-v4-pro[1M]",
  "language": "中文"
}
```

---

> **最后的话**：折腾了一整晚，从改系统设置到装 PowerShell 7，从换终端到退版本，最后发现一个"先贴英文再贴中文"的土办法居然管用，心态崩了但至少能用了。  
>   
> 如果你也遇到同样问题，希望这篇文章能让你少走弯路。如果你有其他解法或新发现，欢迎在 Cursor 论坛分享——这个 Bug 从 2025 年 11 月就开始有人报了，到现在还没修，需要更多声音让它被重视。
