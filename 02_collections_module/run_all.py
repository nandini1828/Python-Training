import subprocess
import sys

modules = [
    "counter.demo",
]

for module in modules:
    print("=" * 60)
    print(f"Running: {module}")
    print("=" * 60)

    subprocess.run(
        [sys.executable, "-m", module],
        check=True,
    )