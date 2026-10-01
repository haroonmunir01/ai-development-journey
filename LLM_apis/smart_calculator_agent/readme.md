# Smart Calculator Agent

A simple local AI agent built with **Python, Ollama, and Qwen3** that demonstrates how an LLM can use a Python tool to perform calculations.

## Current Version

**v1 — Basic Tool-Calling Agent**

The agent can:

* Accept a natural-language user request
* Send the request to a local Qwen3 LLM
* Let the LLM decide when to use the calculator tool
* Extract the tool name and arguments
* Execute the Python calculator function
* Send the tool result back to the LLM
* Generate a final natural-language response

## Architecture

```text
User
 ↓
Python
 ↓
Qwen3 via Ollama
 ↓
Tool Call
 ↓
Python calculate()
 ↓
Tool Result
 ↓
Qwen3
 ↓
Final Response
```

## Technologies

* Python
* Ollama
* Qwen3 4B
* Ollama Python Library

## Requirements

* Python 3.x
* Ollama
* Qwen3 4B
* `ollama` Python package

## Setup

Install the Python package:

```bash
pip install ollama
```

Download the Qwen3 model:

```bash
ollama pull qwen3:4b
```

Make sure Ollama is running, then run:

```bash
python main.py
```

## Example

```text
You: What is 25 multiplied by 40?

Qwen: 25 multiplied by 40 is 1000.
```

The important part is that Qwen does not directly execute the calculation.

It requests the Python tool:

```text
calculate(25, 40, "*")
```

Python executes the function and returns the result to Qwen.

## Project Structure

```text
smart-calculator-agent/
│
└── main.py
```

## What This Project Demonstrates

This project is intentionally simple. Its purpose is to demonstrate the basic architecture behind tool-using AI agents:

```text
LLM
 ↓
Tool Decision
 ↓
Tool Call
 ↓
Tool Execution
 ↓
Tool Result
 ↓
LLM Response
```

## Future Improvements

Planned improvements include:

* Robust agent loop
* Multiple tool calls
* Tool argument validation
* Error handling
* Multiple tools
* Better conversation handling
* Logging
* Testing
* Cleaner project structure

## Status

🚧 **In development**

This is the first version of a larger AI-agent learning project. The project will be progressively expanded with more tools and agent capabilities.
