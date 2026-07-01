from collections import Counter

# Sample data to demonstrate the analyzer
website_logs = [
    "/home", "/login", "/profile", "/orders", "/home",
    "/login", "/profile", "/checkout", "/orders", "/home",
    "/profile", "/login", "/support", "/orders", "/profile"
]


def get_log_counter(logs):
    """Return a Counter object for the list of logged pages."""
    return Counter(logs)


def display_total_requests(logs):
    """Show how many total requests were recorded."""
    print(f"Total requests: {len(logs)}")


def show_most_visited_page(logs):
    """Display the single most visited page using Counter."""
    page_counter = get_log_counter(logs)
    if not page_counter:
        print("No logs available.")
        return

    page, count = page_counter.most_common(1)[0]
    print(f"Most visited page: {page} ({count} visits)")


def show_top_3_pages(logs):
    """Display the top 3 most visited pages."""
    page_counter = get_log_counter(logs)
    top_pages = page_counter.most_common(3)

    if not top_pages:
        print("No logs available.")
        return

    print("Top 3 most visited pages:")
    for page, count in top_pages:
        print(f"- {page}: {count} visits")


def search_visits_for_page(logs):
    """Ask the user for a page and show how many times it was seen."""
    page = input("Enter the page to search (for example, /login): ").strip()
    page_counter = get_log_counter(logs)
    print(f"{page} was visited {page_counter.get(page, 0)} times.")


def display_complete_analytics(logs):
    """Show a full analytics report for the logs."""
    page_counter = get_log_counter(logs)
    top_pages = page_counter.most_common(3)

    print("===== Complete Analytics Report =====")
    print(f"Total Requests: {len(logs)}")
    print(f"Unique Pages: {len(page_counter)}")

    if top_pages:
        most_visited_page, most_visited_count = top_pages[0]
        print(f"Most Visited Page: {most_visited_page} ({most_visited_count} visits)")
    else:
        print("Most Visited Page: None")

    print("Top 3 Pages:")
    for page, count in top_pages:
        print(f"- {page}: {count} visits")

    print("Visit count for every page:")
    for page, count in sorted(page_counter.items()):
        print(f"- {page}: {count}")


def main():
    """Run the website log analyzer menu."""
    while True:
        print("\n=== Website Log Analyzer ===")
        print("1. Display Total Requests")
        print("2. Show Most Visited Page")
        print("3. Show Top 3 Most Visited Pages")
        print("4. Search Visits for a Specific Page")
        print("5. Display Complete Analytics Report")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_total_requests(website_logs)
        elif choice == "2":
            show_most_visited_page(website_logs)
        elif choice == "3":
            show_top_3_pages(website_logs)
        elif choice == "4":
            search_visits_for_page(website_logs)
        elif choice == "5":
            display_complete_analytics(website_logs)
        elif choice == "6":
            print("Exiting Website Log Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
