# test_runner.py
# Creates temp files and runs pytest

import os
import subprocess
import tempfile


def save_and_run_tests(code, tests, module_name):
    """
    Save code + tests into temp folder and run pytest
    """

    with tempfile.TemporaryDirectory() as temp_dir:

        # Create module file
        module_path = os.path.join(temp_dir, f"{module_name}.py")

        with open(module_path, "w") as f:
            f.write(code)

        # Create test file
        test_path = os.path.join(temp_dir, f"test_{module_name}.py")

        with open(test_path, "w") as f:
            f.write(tests)

        # Run pytest
        command = ["pytest", temp_dir]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        output = result.stdout + "\n" + result.stderr

        return output
