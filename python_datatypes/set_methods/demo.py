"""Demo Program for Set Methods"""

from set_methods.set_utils import union, intersection


def main() -> None:
    a = {"Python", "Docker"}
    b = {"Docker", "Kubernetes"}
    print("Union:", union(a, b))
    print("Intersection:", intersection(a, b))


if __name__ == "__main__":
    main()