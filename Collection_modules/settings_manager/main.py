from collections import ChainMap

# Three configuration layers
default_settings = {"Theme": "Light", "Language": "English", "Timeout": 30}
environment_settings = {"Timeout": 60}
user_settings = {"Theme": "Dark"}

settings = ChainMap(user_settings, environment_settings, default_settings)


def view_effective_settings():
    """Display the effective settings after applying ChainMap precedence."""
    print("Effective settings:")
    for key, value in settings.items():
        print(f"- {key}: {value}")


def update_user_setting():
    """Update or add a setting in the user layer."""
    key = input("Enter setting name to update: ").strip()
    value = input("Enter new value: ").strip()
    user_settings[key] = value
    print(f"Updated user setting: {key} = {value}")


def remove_user_setting():
    """Remove a setting from the user layer."""
    key = input("Enter setting name to remove from user settings: ").strip()
    if key in user_settings:
        del user_settings[key]
        print(f"Removed {key} from user settings.")
    else:
        print(f"{key} not found in user settings.")


def view_individual_configurations():
    """Display each individual configuration dictionary."""
    print("Default settings:", default_settings)
    print("Environment settings:", environment_settings)
    print("User settings:", user_settings)


def reset_user_settings():
    """Reset the user settings back to an empty dictionary."""
    user_settings.clear()
    print("User settings reset to empty.")


def main():
    """Run the settings manager menu."""
    while True:
        print("\n=== Settings Manager ===")
        print("1. View Effective Settings")
        print("2. Update User Setting")
        print("3. Remove User Setting")
        print("4. View Individual Configurations")
        print("5. Reset User Settings")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_effective_settings()
        elif choice == "2":
            update_user_setting()
        elif choice == "3":
            remove_user_setting()
        elif choice == "4":
            view_individual_configurations()
        elif choice == "5":
            reset_user_settings()
        elif choice == "6":
            print("Exiting Settings Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
