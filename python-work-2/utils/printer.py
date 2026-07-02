def title(text: str) -> None:
    """Print a formatted main title."""
    width = 60
    print("\n" + "=" * width)
    print(text.center(width).upper())
    print("=" * width)


def subtitle(text: str) -> None:
    """Print a formatted subtitle."""
    width = 60
    print("\n" + "-" * width)
    print(text.center(width))
    print("-" * width)