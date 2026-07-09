import os


def calculate_running_total(values: list[int]) -> int:
    """Sum the list while showing where a debugger breakpoint can pause."""
    total = 0
    for index, value in enumerate(values):
        total += value
        if os.getenv("ENABLE_BREAKPOINT") == "1" and index == 2:
            breakpoint()  # pause here in debugger when ENABLE_BREAKPOINT=1
    return total


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    print("Values:", values)
    print("Use ENABLE_BREAKPOINT=1 to stop at the third item in a debugger.")
    result = calculate_running_total(values)
    print("Total:", result)
