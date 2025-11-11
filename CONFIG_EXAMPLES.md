# AIBash 个性化配置示例

本文档提供了各种个性化配置示例，帮助您根据需求定制 AIBash。

## 目录

1. [基础配置](#基础配置)
2. [OpenAI 配置](#openai-配置)
3. [Ollama 配置](#ollama-配置)
4. [自定义 API 配置](#自定义-api-配置)
5. [UI 个性化配置](#ui-个性化配置)
6. [高级配置](#高级配置)
7. [搭配计划文件运行自动/分析模式](#搭配计划文件运行自动分析模式)

---

## 基础配置

### 最小配置（仅必需项）

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: your-api-key-here
  model_name: gpt-3.5-turbo
```

### 完整配置示例

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: sk-xxxxxxxxxxxxx
  model_name: gpt-3.5-turbo

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 30

history:
  enabled: true
  max_records: 50
  include_output: true
  history_file: ""

ui:
  enable_colors: true
  single_key_mode: true

system_info: ""
custom_prompt: ""
use_default_prompt: true
```

---

## OpenAI 配置

### GPT-3.5 Turbo（推荐，性价比高）

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: sk-xxxxxxxxxxxxx
  model_name: gpt-3.5-turbo

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 30
```

### GPT-4（更强大，但更贵）

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: sk-xxxxxxxxxxxxx
  model_name: gpt-4

model_params:
  temperature: 0.2  # GPT-4 建议使用更低的温度
  max_tokens: 1000
  timeout: 60
```

### GPT-4 Turbo（最新版本）

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: sk-xxxxxxxxxxxxx
  model_name: gpt-4-turbo-preview

model_params:
  temperature: 0.2
  max_tokens: 1000
  timeout: 60
```

### 使用代理或自定义端点

```yaml
model:
  provider: openai
  api_base: https://your-proxy.com/v1  # 自定义 API 端点
  api_key: sk-xxxxxxxxxxxxx
  model_name: gpt-3.5-turbo

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60  # 代理可能需要更长的超时时间
```

---

## Ollama 配置

### Llama 2（推荐）

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""  # Ollama 不需要密钥
  model_name: llama2

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60  # 本地模型可能需要更长时间
```

### Mistral（轻量级，速度快）

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""
  model_name: mistral

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60
```

### Llama 3（最新版本）

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""
  model_name: llama3

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60
```

### CodeLlama（专用于代码生成）

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""
  model_name: codellama

model_params:
  temperature: 0.2  # 代码生成建议使用较低温度
  max_tokens: 1000
  timeout: 90
```

### 远程 Ollama 服务器

```yaml
model:
  provider: ollama
  api_base: http://192.168.1.100:11434  # 远程服务器地址
  api_key: ""
  model_name: llama2

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60
```

---

## 自定义 API 配置

### 兼容 OpenAI API 的服务（如 Azure OpenAI）

```yaml
model:
  provider: openai
  api_base: https://your-resource.openai.azure.com/v1
  api_key: your-azure-key
  model_name: gpt-35-turbo  # Azure 的模型名称可能不同

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 30
```

### 其他兼容服务

```yaml
model:
  provider: openai
  api_base: https://api.your-service.com/v1
  api_key: your-api-key
  model_name: your-model-name

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 30
```

---

## UI 个性化配置

### 启用彩色输出和单键模式（推荐）

```yaml
ui:
  enable_colors: true
  single_key_mode: true
```

### 禁用彩色输出（兼容性更好）

```yaml
ui:
  enable_colors: false
  single_key_mode: true
```

### 传统输入模式（需要回车确认）

```yaml
ui:
  enable_colors: true
  single_key_mode: false
```

### 纯文本模式（最大兼容性）

```yaml
ui:
  enable_colors: false
  single_key_mode: false
```

---

## 高级配置

### 禁用历史记录（节省空间）

```yaml
history:
  enabled: false
  max_records: 0
  include_output: false
```

### 仅保存命令，不保存输出

```yaml
history:
  enabled: true
  max_records: 100
  include_output: false  # 不保存输出，节省空间
```

### 保存更多历史记录

```yaml
history:
  enabled: true
  max_records: 200  # 保存更多记录
  include_output: true
```

### 自定义历史记录位置

```yaml
history:
  enabled: true
  max_records: 50
  include_output: true
  history_file: /path/to/custom/history.json
```

### 自定义 Prompt（更精确的控制）

```yaml
custom_prompt: |
  你是一个专业的命令行助手，专门为 {system_info} 系统生成命令。
  
  要求：
  1. 只输出命令，不要任何解释
  2. 优先使用系统内置命令
  3. 确保命令安全可靠
  4. 考虑跨平台兼容性
  
  {history_context}
  
  用户需求：{user_query}
  
  命令：
use_default_prompt: false
```

### 针对特定系统的 Prompt

```yaml
system_info: "Linux Ubuntu 22.04 (x86_64)"

custom_prompt: |
  你是一个 Ubuntu Linux 系统的命令行助手。
  请生成适合 Ubuntu 22.04 的命令。
  
  系统信息：{system_info}
  {history_context}
  
  用户需求：{user_query}
  
  命令：
use_default_prompt: false
```

### 高精度模式（低温度）

```yaml
model_params:
  temperature: 0.1  # 非常低的温度，输出更确定
  max_tokens: 500
  timeout: 30
```

### 创造性模式（高温度）

```yaml
model_params:
  temperature: 0.7  # 较高的温度，输出更有创造性
  max_tokens: 500
  timeout: 30
```

### 长命令支持

```yaml
model_params:
  temperature: 0.3
  max_tokens: 1000  # 支持更长的命令
  timeout: 60
```

### 快速响应模式

```yaml
model_params:
  temperature: 0.3
  max_tokens: 300  # 减少 token 数，加快响应
  timeout: 15  # 减少超时时间
```

---

## 组合配置示例

### 开发环境配置（快速、本地）

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""
  model_name: mistral

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60

history:
  enabled: true
  max_records: 100
  include_output: true

automation:
  auto_confirm_all: false
  auto_confirm_commands: false
  auto_confirm_files: false
  auto_confirm_web: false
  max_steps: 30
  allow_silence: true
  enable_auto_summary: false
  summary_workers: 4

ui:
  enable_colors: true
  single_key_mode: true

system_info: ""
use_default_prompt: true
```

### 生产环境配置（稳定、云端）

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: sk-xxxxxxxxxxxxx
  model_name: gpt-3.5-turbo

model_params:
  temperature: 0.2
  max_tokens: 500
  timeout: 30

history:
  enabled: true
  max_records: 50
  include_output: true

automation:
  auto_confirm_all: false
  auto_confirm_commands: true
  auto_confirm_files: false
  auto_confirm_web: false
  max_steps: 30
  allow_silence: true
  enable_auto_summary: true
  summary_workers: 6

ui:
  enable_colors: true
  single_key_mode: true

system_info: ""
use_default_prompt: true
```

### 隐私优先配置（本地、无历史）

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""
  model_name: llama2

model_params:
  temperature: 0.3
  max_tokens: 500
  timeout: 60

history:
  enabled: false  # 不保存历史记录
  max_records: 0
  include_output: false

automation:
  auto_confirm_all: false
  auto_confirm_commands: false
  auto_confirm_files: false
  auto_confirm_web: false
  max_steps: 30
  allow_silence: true
  enable_auto_summary: false
  summary_workers: 2

ui:
  enable_colors: true
  single_key_mode: true

system_info: ""
use_default_prompt: true
```

---

## 搭配计划文件运行自动/分析模式

除了在配置文件中预设自动化策略外，你也可以将复杂任务描述写入独立文件，并在运行时与自动模式或项目分析模式结合使用：

```bash
# 自动模式读取 plan 文件（-a 仍需提供参数，可留空字符串）
aibash -a "" -p ~/.aibash/plans/upgrade-deps.txt

# 项目分析模式读取 plan 文件
aibash --analyze "占位描述" -p ~/.aibash/plans/full-review.txt
```

> 提示：`-p/--plan-file` 必须与 `-a/--auto` 或 `-A/--analyze` 搭配，文件内容会覆盖命令行中的任务描述。

## 配置验证

配置完成后，可以使用以下命令验证配置：

```bash
# 测试连接
aibash --test

# 查看配置
cat ~/.aibash/config.yaml
```

---

## 常见问题

### Q: 如何切换不同的配置？

A: 使用 `--config` 参数指定不同的配置文件：

```bash
aibash --config ~/.aibash/config-openai.yaml -l "某个操作"
aibash --config ~/.aibash/config-ollama.yaml -l "某个操作"
```

### Q: 配置错误怎么办？

A: 删除配置文件，重新运行 `aibash --init` 进行初始化。

### Q: 如何备份配置？

A: 配置文件位于 `~/.aibash/config.yaml`，直接复制即可。

### Q: 配置不生效？

A: 检查 YAML 语法是否正确，确保缩进使用空格而不是制表符。

