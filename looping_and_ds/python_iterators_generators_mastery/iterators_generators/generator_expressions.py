
def build_square_generator(numbers: list[int]):
    """
    Returns a generator expression that yields squared values.


    Parameters
    ----------
    numbers : list[int]
        Input numbers.

    Returns
    -------
    generator
        Generator expression of squared numbers.
    """
    return (number ** 2 for number in numbers)


def build_even_generator(numbers: list[int]):
    """
    Returns a generator expression that yields only even numbers.

    Parameters
    ----------
    numbers : list[int]
        Input numbers.

    Returns
    -------
    generator
        Generator expression of even numbers.
    """
    return (number for number in numbers if number % 2 == 0)


def build_scaled_generator(numbers: list[int], factor: int = 1, offset: int = 0):
    """
    Returns a generator expression that scales values and applies an offset.

    Parameters
    ----------
    numbers : list[int]
        Input numbers.
    factor : int
        Multiplier applied to each value.
    offset : int
        Constant added after scaling.

    Returns
    -------
    generator
        Generator expression of transformed numbers.
    """
    return (number * factor + offset for number in numbers)


def run_debug_demo(numbers: list[int], factor: int = 1, offset: int = 0):
    """
    Demonstrates stepping through generator-style operations while changing
    variables and tracking a running total.

    Parameters
    ----------
    numbers : list[int]
        Input numbers to process.
    factor : int
        Multiplier applied to each value.
    offset : int
        Constant added after scaling.

    Returns
    -------
    tuple[list[dict[str, int]], int]
        A list of step snapshots and the final running total.
    """
    steps = []
    running_total = 0

    for value in numbers:
        adjusted = value * factor + offset
        running_total += adjusted
        steps.append(
            {
                "value": value,
                "factor": factor,
                "offset": offset,
                "adjusted": adjusted,
                "running_total": running_total,
            }
        )

    return steps, running_total