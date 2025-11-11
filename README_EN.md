# AIBash

AI-driven Shell Command Generation Tool

## Introduction

AIBash is an intelligent command-line tool that generates corresponding Shell commands based on natural language descriptions. It supports both OpenAI API and local Ollama models.

**Note**: All command-line prompts are in English to avoid character encoding issues. The documentation is available in both English and Chinese.

## Features

- 🤖 **AI Command Generation**: Generate Shell commands from natural language descriptions
- 🔄 **Interactive Selection**: Supports execution, modification, or abandonment of generated commands
- 📝 **History**: Saves command execution history and outputs for contextual support
- ⚙️ **Flexible Configuration**: Supports various configuration options (model, key, system info, etc.)
- 🌐 **Cross-platform Support**: Supports macOS, Windows, and Linux
- 🔌 **Multiple Model Support**: Supports OpenAI API and Ollama local models
- 🧠 **Automation**: Automatically plans multi-step commands with `-a` and executes them step by step
- 🪟 **New Terminal Execution**: Run commands in a new terminal window with `-new` to keep the current window clean
- 🌏 **Bilingual Interface**: Supports both English and Chinese prompts; can be switched at any time

## Installation

### From Source

```bash
git clone https://github.com/W1412X/aibash.git
cd aibash
pip install -e .
```

### Using pip

```bash
pip install aibash-wx
```

## Quick Start

### 1. Configuration

Before using for the first time, you need to configure the model connection information. The configuration file is located at `~/.aibash/config.yaml`.

#### OpenAI API Configuration Example

```yaml
model:
  provider: openai
  api_base: https://api.openai.com/v1
  api_key: your-api-key-here
  model_name: gpt-3.5-turbo

history:
  enabled: true
  max_records: 50
  include_output: true

system_info: "Linux 5.15.0 (x86_64)"
use_default_prompt: true
```

#### Ollama Configuration Example

```yaml
model:
  provider: ollama
  api_base: http://localhost:11434
  api_key: ""  # Ollama doesn't require an API key
  model_name: llama2

history:
  enabled: true
  max_records: 50
  include_output: true

system_info: "Linux 5.15.0 (x86_64)"
use_default_prompt: true
```

### 2. Usage

```bash
# Basic usage
aibash -l "List all files in the current directory"

# Specify a configuration file
aibash --config /path/to/config.yaml -l "Find files containing 'test'"

# Auto mode example (step-by-step completion with confirmation)
aibash -a "Check current project dependencies and generate requirements.txt"

# Auto/Analysis mode read task descriptions from a file (requires -a or --analyze)
aibash -a "" -p /path/to/task_description.txt
aibash --analyze "Perform code review" -p /path/to/task_description.txt

# Execute command in a new terminal window
aibash -new -l "Run test cases in the current directory"

# Project analysis mode (generate project summary and then execute)
aibash --analyze "Outline project modules and provide refactoring suggestions"

# View help
aibash -h

# Initialize configuration (for first-time use)
aibash --init

# View command history
aibash --history

# Clear command history
aibash --clear-history

# Test AI connection
aibash --test
```

- `-l, --lang QUERY`: Natural language description to generate Shell commands
- `-a, --auto QUERY`: Auto mode to plan and execute multi-step operations based on natural language descriptions (up to 30 steps by default, no project summary generated)
- `--analyze QUERY`: Project analysis mode, generates a project summary before executing steps, suitable for large projects
- `-p, --plan-file PATH`: Specify a file for task description input (must be used with `-a/--auto` or `-A/--analyze`)
- `--auto-approve-all`: Automatically approve all actions in auto mode (no confirmation)
- `--auto-approve-commands`: Automatically approve command execution in auto mode
- `--auto-approve-files`: Automatically approve file reading in auto mode
- `--auto-approve-web`: Automatically approve web requests in auto mode
- `--auto-max-steps N`: Limit the maximum number of steps in auto mode (default is 30)
- `--ui-language {en,zh}`: Temporarily switch the interface language (default reads from configuration, English if not set)
- `--config PATH`: Specify a custom configuration file path (default is `~/.aibash/config.yaml`)
- `-new, --new-terminal`: Execute commands in a new terminal window (defaults to the current terminal if not specified)
- `--init`: Interactive initialization of the configuration file
- `--history`: View command execution history
- `--clear-history`: Clear command execution history
- `--test`: Test AI connection
- `-h, --help`: Display help information
- `-v, --version`: Display version information

After generating a command, you can choose to:

- `[e]` Execute the command
- `[c]` Copy the command to clipboard
- `[m]` Modify the command before executing
- `[s]` Skip/Abandon the command
- `[h]` Display help

When a command fails, AIBash will automatically request the AI to generate a new command suggestion based on the latest history and error output, providing a helpful Chinese prompt for quick iteration.

### Auto Mode (`-a`)

In Auto Mode, AIBash acts as an "execution agent," planning and executing tasks step by step based on your natural language descriptions:

- The model will plan one action at a time (running commands, reading files, accessing the network, asking questions, or finishing the task)
- Every command, file read, or web request will first ask for your confirmation before execution
- Execution results are fed back to the model to help it decide the next step
- Ideal for tasks requiring multiple steps of cooperation, like "pull the latest code, install dependencies, and run tests"
- You can use `--auto-approve-*` parameters to fine-tune which operations do not require confirmation, and limit the number of steps with `--auto-max-steps`
- If any step fails, Auto Mode will feed the error details back to the model and automatically replan new commands or strategies
- Auto Mode will not generate a project summary by default, focusing solely on executing your tasks. Use `--analyze` for project structure analysis first
- Project analysis mode will generate a summary of key files in the directory before executing the task, which helps the model quickly understand the project structure
- Auto Mode and Project Analysis Mode both support reading task descriptions from a configuration file, and support caching and concurrency for efficient execution

You can combine `-new` to execute the commands in a new terminal window, ensuring the auto mode interface remains clean.

## Configuration Description

### Model Configuration

- `provider`: Model provider (`openai` or `ollama`)
- `api_base`: API base URL
- `api_key`: API key (Ollama does not require an API key)
- `model_name`: Model name

### History Configuration

- `enabled`: Whether to enable command history
- `max_records`: Maximum number of history records
- `include_output`: Whether to include command output in history
- `history_file`: Path for storing history records (automatically set)

### Other Configuration

- `system_info`: System information (for generating more accurate commands)
- `custom_prompt`: Custom prompt template
- `use_default_prompt`: Whether to use the default prompt
- `ui.language`: Interface language (`en` or `zh`, default is `en`)
- `automation`: Default behavior configuration for auto mode (e.g., auto confirmation, max steps, concurrent project summaries)

```yaml
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
  language: en
```

You can set the language permanently in the configuration file by modifying `ui.language`.

## Custom Prompt

You can customize the prompt template to better control the AI's behavior. Set `custom_prompt` in the configuration file and use the following placeholders:

- `{system_info}`: System information
- `{history_context}`: History context
- `{user_query}`: User query

Example:

```yaml
custom_prompt: |
  You are a professional command-line assistant.
  System: {system_info}
  {history_context}
  User Request: {user_query}
  Please generate the corresponding shell command:
use_default_prompt: false
```

## Project Structure

```
aibash/
├── aibash/
│   ├── __init__.py
│   ├── main.py            # Main program entry
│   ├── automation.py      # Auto mode executor
│   ├── agents/            # Agents for different models
│   ├── config.py          # Configuration loading and validation
│   ├──