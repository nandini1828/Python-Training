"""
==================================================
Module: List Utilities
Topic: Python List Methods
Author: Sagar

Description:
Demonstrates commonly used Python list methods
using a movie collection example.
==================================================
"""


def demonstrate_list_methods():
    """
    Demonstrates Python list methods.

    Returns:
        None
    """

    print("\n========== LIST METHODS ==========\n")

    # ----------------------------------------
    # append()
    # ----------------------------------------

    movies = ["Inception", "Interstellar"]

    print("Original Movies:")
    print(movies)

    movies.append("Oppenheimer")

    print("\nappend('Oppenheimer')")
    print(movies)

    # ----------------------------------------
    # extend()
    # ----------------------------------------

    movies.extend(["Tenet", "Dunkirk"])

    print("\nextend(['Tenet', 'Dunkirk'])")
    print(movies)

    # ----------------------------------------
    # insert()
    # ----------------------------------------

    movies.insert(1, "Memento")

    print("\ninsert(1, 'Memento')")
    print(movies)

    # ----------------------------------------
    # remove()
    # ----------------------------------------

    movies.remove("Tenet")

    print("\nremove('Tenet')")
    print(movies)

    # ----------------------------------------
    # pop()
    # ----------------------------------------

    removed_movie = movies.pop()

    print("\npop()")
    print("Removed Movie:", removed_movie)
    print(movies)

    # ----------------------------------------
    # index()
    # ----------------------------------------

    print("\nindex('Interstellar')")
    print(movies.index("Interstellar"))

    # ----------------------------------------
    # count()
    # ----------------------------------------

    ratings = [5, 4, 5, 3, 5, 4]

    print("\ncount(5)")
    print(ratings.count(5))

    # ----------------------------------------
    # sort()
    # ----------------------------------------

    durations = [148, 169, 106, 181]

    durations.sort()

    print("\nsort()")
    print(durations)

    # ----------------------------------------
    # reverse()
    # ----------------------------------------

    durations.reverse()

    print("\nreverse()")
    print(durations)

    # ----------------------------------------
    # copy()
    # ----------------------------------------

    backup_durations = durations.copy()

    print("\ncopy()")
    print(backup_durations)

    # ----------------------------------------
    # clear()
    # ----------------------------------------

    backup_durations.clear()

    print("\nclear()")
    print(backup_durations)

    print("\n==================================")