# prompt_utils.py
# Handles prompt creation for LLM

SYSTEM_PROMPT = """
You are a senior Python engineer. Produce a single, self-contained pytest file.
Rules:
- Output only Python test code (no prose, no markdown fences).
- Use plain pytest tests (functions), no classes unless unavoidable.
- Deterministic: avoid network/IO; seed randomness if used.
- Import the target module by module name only.
- Cover every public function and method with at least one tiny test.
- Prefer straightforward, fast assertions.
"""


def create_test_prompt(code: str, module_name: str) -> str:
    """
    Create user prompt for generating tests
    """

    prompt = f"""Please generate comprehensive unit tests for the following Python code.
        
    Guidelines:
    - Use appropriate testing framework for Python
    - Do not insert in the response the function for the tests.
    - Create tests for all functions and methods
    - Include both positive and negative test cases
    - Test edge cases and error conditions
    - Use meaningful test names that describe what is being tested
    - Include setup and teardown methods if needed
    - Add mock objects for external dependencies (like database connections)
    - Follow testing best practices for Python
    - Import as: `import {module_name}`

    Here's the code to test:

    {code}

    Please return only the unit test code without any additional explanation or markdown formatting."""

    return prompt


def build_messages(code, module_name):
    """
    Build messages for Claude API
    """

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": create_test_prompt(code, module_name)}
    ]
