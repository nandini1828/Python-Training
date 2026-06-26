"""
Section 4: Dictionaries & JSON
"""

import json


class DictionaryOperations:

    @staticmethod
    def get_value(data, key, default=None):
        return data.get(key, default)

    @staticmethod
    def set_default(data, key, default_value):
        return data.setdefault(key, default_value)

    @staticmethod
    def get_keys(data):
        return list(data.keys())

    @staticmethod
    def get_values(data):
        return list(data.values())

    @staticmethod
    def get_items(data):
        return list(data.items())

    @staticmethod
    def update_dictionary(data, other_dictionary):
        data.update(other_dictionary)
        return data

    @staticmethod
    def pop_key(data, key, default=None):
        return data.pop(key, default)

    @staticmethod
    def pop_last_item(data):
        return data.popitem()

    @staticmethod
    def clear_dictionary(data):
        data.clear()
        return data

    @staticmethod
    def copy_dictionary(data):
        return data.copy()

    @staticmethod
    def create_from_keys(keys, value=None):
        return dict.fromkeys(keys, value)


class JsonOperations:

    @staticmethod
    def json_to_dictionary(json_string):
        return json.loads(json_string)

    @staticmethod
    def dictionary_to_json(dictionary):
        return json.dumps(dictionary, indent=4)

    @staticmethod
    def is_valid_json(json_string):

        try:
            json.loads(json_string)
            return True

        except json.JSONDecodeError:
            return False