def count_truthy_falsy(items):
    result = {
        "truthy": 0,
        "falsy": 0
    }

    for item in items:
        if item:
            result["truthy"] += 1
        else:
            result["falsy"] += 1

    return result