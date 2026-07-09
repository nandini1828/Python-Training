from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class Phone:
    number: str
    type: str = "mobile"

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"Phone(number={self.number!r}, type={self.type!r})"


class Person:
    """Simple Person model that can hold multiple `Phone` objects."""
    name: str
    _phones: List[Phone]

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._phones: List[Phone] = []

    def add_phone(self, number: str, type: str = "mobile") -> Phone:
        """Add a phone by number and optional type and return the Phone."""
        phone = Phone(number=number, type=type)
        self._phones.append(phone)
        return phone

    def remove_phone(self, number: str) -> bool:
        """Remove the first phone matching `number`. Returns True if removed."""
        for i, p in enumerate(self._phones):
            if p.number == number:
                del self._phones[i]
                return True
        return False

    def get_phones(self) -> List[Phone]:
        """Return a shallow copy of the phone list."""
        return list(self._phones)

    def find_phones_starting_with(self, prefix: str) -> List[Phone]:
        """Return phones whose number starts with `prefix`."""
        return [p for p in self._phones if p.number.startswith(prefix)]

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"Person(name={self.name!r}, phones={self._phones!r})"


"""
Examples: equivalent representations of a Person with multiple phones

Python (in-memory objects):
    # Person object with two Phone entries
    p = Person("Alice")
    p.add_phone("12345")
    p.add_phone("98765", type="home")

MongoDB (document-oriented storage):
    # A single document holds nested phone objects
    db.people.insertOne({
        "name": "Alice",
        "phones": [
            {"number": "12345", "type": "mobile"},
            {"number": "98765", "type": "home"}
        ]
    })

JSON (serialization / transport):
    {
        "name": "Alice",
        "phones": [
            {"number": "12345", "type": "mobile"},
            {"number": "98765", "type": "home"}
        ]
    }

Relational (RDBMS) - normalized tables:
    -- persons table
    CREATE TABLE person (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL
    );

    -- phones table with foreign key to person
    CREATE TABLE phone (
        id SERIAL PRIMARY KEY,
        person_id INTEGER REFERENCES person(id),
        number TEXT NOT NULL,
        type TEXT
    );

    -- insert example (pseudo-SQL):
    -- 1) create person, get id
    -- 2) insert phones referencing person_id
    INSERT INTO person (name) VALUES ('Alice');
    INSERT INTO phone (person_id, number, type) VALUES (1, '12345', 'mobile');
    INSERT INTO phone (person_id, number, type) VALUES (1, '98765', 'home');

Notes:
    - MongoDB/JSON store nested arrays naturally and match the `Person`+`Phone` shape directly.
    - RDBMS requires normalization (separate tables and joins) but allows efficient queries on phones.
    - Choose representation based on query patterns, consistency and transactional needs.
"""

# --- RDBMS SQL + Python (sqlite3) examples ---------------------------------
#
# SQL (Postgres / generic SQL) - create tables and demonstrate inserts/joins
# ---------------------------------------------------------------------------
# CREATE TABLE person (
#     id SERIAL PRIMARY KEY,
#     name TEXT NOT NULL
# );
#
# CREATE TABLE phone (
#     id SERIAL PRIMARY KEY,
#     person_id INTEGER REFERENCES person(id) ON DELETE CASCADE,
#     number TEXT NOT NULL,
#     type TEXT
# );
#
# -- Insert person and phones (pseudo-SQL):
# INSERT INTO person (name) VALUES ('Alice');
# -- assume returned id = 1
# INSERT INTO phone (person_id, number, type) VALUES (1, '12345', 'mobile');
# INSERT INTO phone (person_id, number, type) VALUES (1, '98765', 'home');
#
# -- Query to fetch person with phones (join):
# SELECT p.id, p.name, ph.number, ph.type
# FROM person p
# LEFT JOIN phone ph ON ph.person_id = p.id
# WHERE p.name = 'Alice';
# ---------------------------------------------------------------------------

# Example: equivalent operations using Python's `sqlite3` (runnable example)
# This illustrates the normalized RDBMS approach: one person row, many phone rows.
def example_sqlite_operations(db_path: str = ":memory:") -> None:
    """Create tables, insert a person and phones, then query with JOIN.

    db_path: path to sqlite database (":memory:" for in-memory DB).
    """
    import sqlite3

    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        # Create tables
        cur.execute("""
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            person_id INTEGER NOT NULL,
            number TEXT NOT NULL,
            type TEXT,
            FOREIGN KEY(person_id) REFERENCES person(id) ON DELETE CASCADE
        )
        """)
        conn.commit()

        # Insert a person
        cur.execute("INSERT INTO person (name) VALUES (?)", ("Alice",))
        person_id = cur.lastrowid

        # Insert multiple phones for that person
        phones = [(person_id, "12345", "mobile"), (person_id, "98765", "home")]
        cur.executemany("INSERT INTO phone (person_id, number, type) VALUES (?, ?, ?)", phones)
        conn.commit()

        # Query person with phones using JOIN
        cur.execute(
            "SELECT p.id, p.name, ph.number, ph.type "
            "FROM person p LEFT JOIN phone ph ON ph.person_id = p.id "
            "WHERE p.id = ?",
            (person_id,)
        )
        rows = cur.fetchall()
        # rows: list of tuples (person_id, name, phone_number, phone_type)
        for r in rows:
            print(r)
    finally:
        conn.close()


# --- Pandas perspective ----------------------------------------------------
#
# Pandas is useful when you want tabular, in-memory analysis of normalized
# or denormalized data. Below are a few small examples showing common patterns:
def example_pandas_operations() -> None:
    """Demonstrate pandas usage for Person/Phone data.

    - create two DataFrames (persons, phones)
    - join them to view one-row-per-phone
    - aggregate phones per person into lists
    """
    try:
        import pandas as pd
    except Exception:  # pragma: no cover - optional dependency in examples
        print("pandas is not installed; install with: pip install pandas")
        return

    # Source data (could also come from SQL, JSON, or MongoDB)
    persons = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
    ]
    phones = [
        {"id": 1, "person_id": 1, "number": "12345", "type": "mobile"},
        {"id": 2, "person_id": 1, "number": "98765", "type": "home"},
        {"id": 3, "person_id": 2, "number": "55500", "type": "work"},
    ]

    df_person = pd.DataFrame(persons)
    df_phone = pd.DataFrame(phones)

    # 1) Simple join: one row per phone with person columns available
    df_joined = df_phone.merge(df_person, left_on="person_id", right_on="id", how="left")
    print("Joined (phone rows):")
    print(df_joined[['name', 'number', 'type']])

    # 2) Aggregate phones per person into a list (denormalize)
    df_agg = (
        df_phone.groupby('person_id')
        .agg(phones_list=pd.NamedAgg(column='number', aggfunc=lambda s: list(s)))
        .reset_index()
        .merge(df_person, left_on='person_id', right_on='id', how='left')
    )
    print('\nAggregated phones per person:')
    print(df_agg[['name', 'phones_list']])

    # 3) Pivot-style view (phones as columns) - useful for small, fixed-size phone sets
    df_pivot = df_phone.assign(rn=df_phone.groupby('person_id').cumcount()+1)
    df_pivot = df_pivot.pivot_table(index='person_id', columns='rn', values='number', aggfunc='first')
    df_pivot = df_pivot.merge(df_person, left_on='person_id', right_on='id', how='left')
    print('\nPivot (phone columns):')
    print(df_pivot)


