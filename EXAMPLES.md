# AIBash 使用示例

## 基本使用

### 1. 初始化配置

首次使用时，需要先配置 AI 模型连接：

```bash
aibash --init
```

按照提示输入：
- AI 模型提供商（OpenAI 或 Ollama）
- API 地址和密钥
- 模型名称
- 历史记录配置等

### 2. 生成命令

```bash
# 列出文件
aibash -l "列出当前目录下的所有文件"

# 查找文件
aibash -l "查找包含test的文件"

# 系统操作
aibash -l "显示当前系统内存使用情况"

# 网络操作
aibash -l "查看当前网络连接"
```

### 3. 交互式操作

生成命令后，会显示交互式菜单：

```
============================================================
生成的命令:
------------------------------------------------------------
  ls -la
============================================================

请选择操作:
  [e] 执行命令
  [m] 修改命令
  [s] 跳过/放弃
  [h] 显示帮助

请输入选项: 
```

- 输入 `e` 执行命令
- 输入 `m` 修改命令后再执行
- 输入 `s` 放弃执行
- 输入 `h` 查看帮助

### 4. 查看历史记录

```bash
# 查看所有历史记录
aibash --history

# 清空历史记录
aibash --clear-history
```

### 5. 测试连接

```bash
# 测试 AI 连接是否正常
aibash --test
```

## 高级配置

### 自定义 Prompt

编辑配置文件 `~/.aibash/config.yaml`：

```yaml
custom_prompt: |
  你是一个专业的命令行助手。
  系统: {system_info}
  {history_context}
  用户需求: {user_query}
  请生成对应的shell命令：
use_default_prompt: false
```

### 配置多个模型

可以通过 `--config` 参数使用不同的配置文件：

```bash
# 使用 OpenAI
aibash --config ~/.aibash/config-openai.yaml -l "某个操作"

# 使用 Ollama
aibash --config ~/.aibash/config-ollama.yaml -l "某个操作"
```

## 常见问题

### Q: 如何配置 Ollama？

A: 确保 Ollama 服务正在运行，然后运行 `aibash --init` 选择 Ollama，配置如下：
- API Base URL: `http://localhost:11434`
- API Key: 留空
- 模型名称: 你安装的模型名称（如 `llama2`, `mistral` 等）

### Q: 历史记录保存在哪里？

A: 默认保存在 `~/.aibash/history.json`，可以在配置文件中修改。

### Q: 如何禁用历史记录？

A: 编辑配置文件，设置 `history.enabled: false`

### Q: Windows 上如何使用？

A: AIBash 完全支持 Windows，安装后直接使用即可。配置文件位置在 `%USERPROFILE%\.aibash\config.yaml`

