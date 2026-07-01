from collections import OrderedDict

MAX_HISTORY_SIZE = 10
recent_files = OrderedDict()


def open_file():
    """Open a file and move it to the most recent position in the history."""
    file_name = input("Enter file name to open: ").strip()
    if not file_name:
        print("File name cannot be empty.")
        return

    if file_name in recent_files:
        recent_files.move_to_end(file_name)
    else:
        recent_files[file_name] = True
        if len(recent_files) > MAX_HISTORY_SIZE:
            recent_files.popitem(last=False)

    print(f"Opened: {file_name}")


def view_recent_files():
    """Display the recent file history in order from oldest to newest."""
    if not recent_files:
        print("No recent files.")
        return

    print("Recent Files History:")
    for file_name in recent_files:
        print(f"- {file_name}")


def remove_file():
    """Remove a file from the history."""
    file_name = input("Enter file name to remove: ").strip()
    if file_name in recent_files:
        del recent_files[file_name]
        print(f"Removed {file_name} from history.")
    else:
        print("File not found in recent history.")


def clear_history():
    """Clear all recent files."""
    recent_files.clear()
    print("Recent file history cleared.")


def main():
    """Run the recent files manager menu."""
    while True:
        print("\n=== Recent Files Manager ===")
        print("1. Open File")
        print("2. View Recent Files")
        print("3. Remove File")
        print("4. Clear History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            open_file()
        elif choice == "2":
            view_recent_files()
        elif choice == "3":
            remove_file()
        elif choice == "4":
            clear_history()
        elif choice == "5":
            print("Exiting Recent Files Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
