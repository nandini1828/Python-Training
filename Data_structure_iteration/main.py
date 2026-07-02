"""Simple Contact Book"""


class Contact:
    """A simple contact record."""

    def __init__(self, name, phone, city, favorite=False):
        self.name = name
        self.phone = phone
        self.city = city
        self.favorite = favorite


class ContactBook:
    """Store contacts in a list and track favorites as a set."""

    def __init__(self):
        self.contacts = []
        self.favorite_names = set()


def safe_input(prompt, default=""):
    """Read input, but return a default when no input is available."""
    try:
        value = input(prompt).strip()
    except EOFError:
        print("No input provided. Using the default value.")
        return default
    return value if value else default

    def add_contact(self, contact):
        self.contacts.append(contact)
        if contact.favorite:
            self.favorite_names.add(contact.name)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def delete_contact(self, name):
        safe_copy = list(self.contacts)
        for contact in safe_copy:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                self.favorite_names.discard(contact.name)
                return True
        return False

    def display_contacts(self):
        if not self.contacts:
            print("No contacts yet.")
            return
        for contact in self.contacts:
            marker = "★" if contact.favorite else "-"
            print(f"{marker} {contact.name}: {contact.phone} ({contact.city})")

    def favorite_contacts(self):
        return [contact for contact in self.contacts if contact.name in self.favorite_names]

    def unique_cities(self):
        return {contact.city for contact in self.contacts}


def main():
    book = ContactBook()

    print("Simple Contact Book")
    while True:
        print("\nChoose an option:")
        print("1. Add contact")
        print("2. Search contact")
        print("3. Delete contact")
        print("4. Show contacts")
        print("5. Show favorites")
        print("6. Show unique cities")
        print("7. Quit")

        choice = safe_input("Enter your choice: ", "7")

        if choice == "1":
            name = safe_input("Name: ", "Sample")
            phone = safe_input("Phone: ", "000")
            city = safe_input("City: ", "Unknown")
            favorite = safe_input("Favorite? (y/n): ", "n").lower() == "y"
            book.add_contact(Contact(name, phone, city, favorite))
        elif choice == "2":
            name = safe_input("Name to search: ", "")
            contact = book.search_contact(name)
            if contact:
                print(contact.name, contact.phone, contact.city)
            else:
                print("Contact not found.")
        elif choice == "3":
            name = safe_input("Name to delete: ", "")
            removed = book.delete_contact(name)
            print("Deleted." if removed else "Contact not found.")
        elif choice == "4":
            book.display_contacts()
        elif choice == "5":
            for contact in book.favorite_contacts():
                print(contact.name)
        elif choice == "6":
            print(book.unique_cities())
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
