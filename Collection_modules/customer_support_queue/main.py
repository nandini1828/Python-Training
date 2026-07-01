from collections import deque

queue = deque()


def add_customer():
    """Add a normal customer to the back of the queue."""
    name = input("Enter customer name: ").strip()
    if name:
        queue.append(name)
        print(f"{name} added to the queue.")
    else:
        print("Customer name cannot be empty.")


def add_vip_customer():
    """Add a VIP customer to the front of the queue."""
    name = input("Enter VIP customer name: ").strip()
    if name:
        queue.appendleft(name)
        print(f"VIP {name} added to the front of the queue.")
    else:
        print("VIP customer name cannot be empty.")


def serve_customer():
    """Serve the next customer using popleft."""
    if not queue:
        print("No customers waiting.")
    else:
        customer = queue.popleft()
        print(f"Serving: {customer}")


def view_waiting_queue():
    """Display all customers in the queue."""
    if not queue:
        print("The queue is empty.")
    else:
        print("Waiting queue:")
        for index, customer in enumerate(queue, start=1):
            print(f"{index}. {customer}")


def view_queue_length():
    """Show how many customers are currently waiting."""
    print(f"Queue length: {len(queue)}")


def main():
    """Run the customer support queue menu."""
    while True:
        print("\n=== Customer Support Queue ===")
        print("1. Add Customer")
        print("2. Add VIP Customer")
        print("3. Serve Customer")
        print("4. View Waiting Queue")
        print("5. View Queue Length")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_vip_customer()
        elif choice == "3":
            serve_customer()
        elif choice == "4":
            view_waiting_queue()
        elif choice == "5":
            view_queue_length()
        elif choice == "6":
            print("Exiting Customer Support Queue. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
