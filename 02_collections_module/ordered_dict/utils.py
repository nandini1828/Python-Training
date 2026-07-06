from collections import OrderedDict


def build_cache():

    cache = OrderedDict()

    cache["A"] = 100
    cache["B"] = 200
    cache["C"] = 300

    cache.move_to_end("A")

    return cache