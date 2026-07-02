"""Data Practice with Comprehensions"""


def even_numbers(numbers):
    """Return even numbers using a list comprehension."""
    return [number for number in numbers if number % 2 == 0]


def odd_numbers(numbers):
    """Return odd numbers using a list comprehension."""
    return [number for number in numbers if number % 2 != 0]


def squares_dictionary(numbers):
    """Create a dictionary with numbers as keys and squares as values."""
    return {number: number * number for number in numbers}


def unique_email_domains(emails):
    """Collect unique email domains using a set comprehension."""
    return {email.split("@")[-1] for email in emails}


def word_frequency(text):
    """Count words with a dictionary comprehension."""
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}


def flatten_matrix(matrix):
    """Flatten a matrix using a nested comprehension."""
    return [value for row in matrix for value in row]


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    emails = ["anna@example.com", "bob@example.org", "anna@sample.net", "carol@example.org"]
    sample_text = "python python is fun fun for beginners"
    matrix = [[1, 2, 3], [4, 5], [6]]

    print("Even numbers:", even_numbers(numbers))
    print("Odd numbers:", odd_numbers(numbers))
    print("Squares dictionary:", squares_dictionary(numbers))
    print("Unique domains:", unique_email_domains(emails))
    print("Word frequency:", word_frequency(sample_text))
    print("Flattened matrix:", flatten_matrix(matrix))


if __name__ == "__main__":
    main()
