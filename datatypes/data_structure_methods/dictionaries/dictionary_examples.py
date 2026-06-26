"""
Dictionary Examples

Practical dictionary usage examples.
"""


class DictionaryExamples:
    """Practical dictionary usage examples."""
    
    @staticmethod
    def configuration_management() -> dict:
        """Using dictionaries for configuration."""
        config = {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "mydb",
            },
            "api": {
                "timeout": 30,
                "retries": 3,
            },
            "debug": True,
        }
        
        return {
            "db_host": config["database"]["host"],
            "api_timeout": config["api"]["timeout"],
            "debug_mode": config["debug"],
        }
    
    @staticmethod
    def json_like_data() -> dict:
        """Working with JSON-like dictionary data."""
        import json
        
        data = {
            "users": [
                {"id": 1, "name": "Alice", "email": "alice@example.com"},
                {"id": 2, "name": "Bob", "email": "bob@example.com"},
            ],
            "total": 2,
        }
        
        json_string = json.dumps(data)
        parsed = json.loads(json_string)
        
        return {
            "original": data,
            "json_string": json_string,
            "parsed_back": parsed,
            "first_user": parsed["users"][0],
        }
    
    @staticmethod
    def word_frequency() -> dict:
        """Counting word frequency."""
        text = "hello world hello python hello"
        words = text.split()
        
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        
        return {
            "text": text,
            "frequency": frequency,
            "most_frequent": max(frequency, key=frequency.get),
        }
