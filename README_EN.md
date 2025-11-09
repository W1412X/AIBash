# AIBash

AI-powered Shell Command Generator

## Introduction

AIBash is an intelligent command-line tool that generates corresponding Shell commands based on natural language descriptions. It supports OpenAI API and local Ollama models.

## Features

- 🤖 **AI Command Generation**: Generate Shell commands from natural language descriptions
- 🔄 **Interactive Selection**: Support executing, modifying, or canceling generated commands
- 📝 **History Records**: Save command execution history and output, providing context support
- ⚙️ **Flexible Configuration**: Support multiple configuration options (model, keys, system info, etc.)
- 🌐 **Multi-platform Support**: Support macOS, Windows, Linux
- 🔌 **Multi-model Support**: Support OpenAI API and Ollama local models

## Installation

### Install from Source

```bash
git clone https://github.com/W1412X/aibash.git
cd aibash
pip install -e .
```

### Install using pip

```bash
pip install aibash
```

## Quick Start

### 1. Configuration

Before first use, you need to configure model connection information. The configuration file is located at `~/.aibash/config.yaml`.

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
  api_key: ""  # Ollama doesn't require a key
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
aibash -l "list all files in current directory"

# Specify config file
aibash --config /path/to/config.yaml -l "find files containing test"

# View help
aibash -h

# Initialize configuration (first use)
aibash --init

# View command history
aibash --history

# Clear command history
aibash --clear-history

# Test AI connection
aibash --test
```

## Command Line Options

- `-l, --lang QUERY`: Natural language description to generate shell command
- `--config PATH`: Specify config file path (default: ~/.aibash/config.yaml)
- `--init`: Interactive configuration initialization
- `--history`: View command execution history
- `--clear-history`: Clear command execution history
- `--test`: Test AI connection
- `-h, --help`: Show help information
- `-v, --version`: Show version information

After generating a command, you can choose:

- `[e]` Execute command - Execute the generated command directly
- `[c]` Copy to clipboard - Copy command to clipboard
- `[m]` Modify command - Modify command before execution
- `[s]` Skip/Cancel - Do not execute command
- `[h]` Show help - Show help information

## Configuration

### Model Configuration

- `provider`: Model provider (`openai` or `ollama`)
- `api_base`: API base URL
- `api_key`: API key (can be empty for Ollama)
- `model_name`: Model name

### History Configuration

- `enabled`: Whether to enable history records
- `max_records`: Maximum number of records
- `include_output`: Whether to include command output
- `history_file`: History file path (automatically set)

### Other Configuration

- `system_info`: System information (for generating more accurate commands)
- `custom_prompt`: Custom prompt template
- `use_default_prompt`: Whether to use default prompt

## Custom Prompt

You can customize the prompt template to better control AI behavior. Set `custom_prompt` in the configuration file and use the following placeholders:

- `{system_info}`: System information
- `{history_context}`: History context
- `{user_query}`: User query

Example:

```yaml
custom_prompt: |
  You are a professional command-line assistant.
  System: {system_info}
  {history_context}
  User request: {user_query}
  Please generate the corresponding shell command:
use_default_prompt: false
```

## Project Structure

```
aibash/
├── aibash/
│   ├── __init__.py
│   ├── config.py          # Configuration management
│   ├── ai_client.py       # AI model client
│   ├── history.py         # History management
│   ├── interactive.py     # Interactive selection
│   ├── prompt.py          # Prompt management
│   └── main.py            # Main program entry
├── setup.py
├── requirements.txt
└── README.md
```

## Development

### Run Tests

```bash
python -m aibash.main -l "test command"
```

### Build Distribution Package

```bash
python setup.py sdist bdist_wheel
```

## License

MIT License

## Author

github/W1412X

## Contributing

Issues and Pull Requests are welcome!

