
import ollama


def calculate(input1, input2, operation):
    if operation == "+":
        return input1 + input2
    elif operation == "-":
        return input1 - input2
    elif operation == "*":
        return input1 * input2
    elif operation == "/":
        if input2 == 0:
            return "Error: Cannot divide by zero"
        return input1 / input2
    else:
        return "Error: Operation not supported"


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input1": {
                        "type": "number"
                    },
                    "input2": {
                        "type": "number"
                    },
                    "operation": {
                        "type": "string",
                        "enum": ["+", "-", "*", "/"]
                    }
                },
                "required": ["input1", "input2", "operation"]
            }
        }
    }
]


user_input = input("You: ")

messages = [
    {
        "role": "system",
        "content": "You are a concise assistant. Answer directly and avoid unnecessary explanations."
    },
    {
        "role": "user",
        "content": user_input
    }
]


response = ollama.chat(
    model="qwen3:4b",
    messages=messages,
    tools=tools
)


if response.message.tool_calls:
    tool_call = response.message.tool_calls[0]

    arguments = tool_call.function.arguments

    result = calculate(
        arguments["input1"],
        arguments["input2"],
        arguments["operation"]
    )

    messages.append(response.message)

    messages.append({
        "role": "tool",
        "content": str(result),
        "tool_name": tool_call.function.name
    })

    final_response = ollama.chat(
        model="qwen3:4b",
        messages=messages,
        tools=tools
    )

    print("Qwen:", final_response.message.content)

else:
    print("Qwen:", response.message.content)

