import re

from typing import Any, Optional, Dict, List



class NestedJSONQueryEngine:

    """

    A robust, lightweight query engine for navigating nested Python dictionaries and lists (JSON-like structures).

    

    Supports:

      - Dot notation for keys: "store.book"

      - Array index selection: "store.books[0]"

      - Key-value filters: "store.books[author=Nishant]" or "users[role=admin]"

    """



    def __init__(self, data: Any):

        self.data = data



    def query(self, path: str, default: Any = None) -> Any:

        """

        Query the nested data structure.

        

        Args:

            path: A string path representing the query (e.g., "store.books[0].title")

            default: The fallback value to return if the path does not exist.

            

        Returns:

            The matched value or the default value.

        """

        if not path:

            return self.data



        # Split path by dot notation

        tokens = path.split('.')

        current = self.data



        for token in tokens:

            if current is None:

                return default



            # Check if token contains array bracket navigation/filtering, e.g., "books[0]" or "users[role=admin]"

            if '[' in token and token.endswith(']'):

                # Extract key and the contents of brackets

                match = re.match(r"^(\w+)\[(.*)\]$", token)

                if not match:

                    return default

                

                key = match.group(1)

                selector = match.group(2).strip()



                # 1. Access the dictionary key first

                if isinstance(current, Dict) and key in current:

                    current = current[key]

                else:

                    return default



                # 2. Process the selector inside brackets

                if current is None:

                    return default



                # Scenario A: Numeric Index (e.g., "books[0]")

                if selector.isdigit():

                    idx = int(selector)

                    if isinstance(current, List) and 0 <= idx < len(current):

                        current = current[idx]

                    else:

                        return default



                # Scenario B: Filter Query (e.g., "books[author=Nishant]")

                elif '=' in selector:

                    filter_key, filter_val = selector.split('=', 1)

                    filter_key = filter_key.strip()

                    filter_val = filter_val.strip()



                    # We expect current to be a list of dictionaries to apply a filter

                    if isinstance(current, List):

                        matched_items = []

                        for item in current:

                            if isinstance(item, Dict) and str(item.get(filter_key)) == filter_val:

                                matched_items.append(item)

                        

                        # Return the list of matched items (or first item depending on design choice)

                        # We return the list of matched items. If empty, return default.

                        if matched_items:

                            current = matched_items

                        else:

                            return default

                    else:

                        return default

                else:

                    # Unsupported bracket format

                    return default

            else:

                # Standard dictionary key navigation

                if isinstance(current, Dict) and token in current:

                    current = current[token]

                else:

                    return default



        return current



# Demonstration example if run directly

if __name__ == "__main__":

    sample_data = {

        "store": {

            "name": "Tech Books",

            "books": [

                {"title": "Automate the Boring Stuff", "author": "Al Sweigart", "price": 29.99},

                {"title": "Learning Python", "author": "Mark Lutz", "price": 45.00},

                {"title": "Fluent Python", "author": "Luciano Ramalho", "price": 55.00}

            ],

            "staff": [

                {"name": "Alice", "role": "manager"},

                {"name": "Bob", "role": "cashier"},

                {"name": "Charlie", "role": "cashier"}

            ]

        }

    }



    engine = NestedJSONQueryEngine(sample_data)



    print("--- Nested JSON Query Engine Demo ---")

    print("Store Name:     ", engine.query("store.name"))

    print("First Book Title:", engine.query("store.books[0].title"))

    print("Luciano's Book: ", engine.query("store.books[author=Luciano Ramalho]"))

    print("All Cashiers:   ", engine.query("store.staff[role=cashier]"))

    print("Non-existent:   ", engine.query("store.books[5].title", "N/A"))

 