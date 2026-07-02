"""Examples using match-case statements."""

from __future__ import annotations


def handle_command(command: str) -> str:
    """Execute a simple command using match-case.

    Args:
        command: The command name.

    Returns:
        A descriptive response.
    """
    match command:
        case "start":
            return "Starting the workflow."
        case "stop":
            return "Stopping the workflow."
        case "pause":
            return "Pausing the workflow."
        case _:
            return "Unknown command."
