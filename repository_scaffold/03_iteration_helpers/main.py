"""
Main entry point for the Iteration Helpers module.
"""

from any_all.demo import run_demo as any_all_demo
from enumerate_module.demo import run_demo as enumerate_demo
from range_module.demo import run_demo as range_demo
from reversed_module.demo import run_demo as reversed_demo
from sorted_module.demo import run_demo as sorted_demo
from zip_module.demo import run_demo as zip_demo


def main():
    print('=' * 80)
    print('PYTHON ITERATION HELPERS MODULE')
    print('=' * 80)

    any_all_demo()
    enumerate_demo()
    range_demo()
    reversed_demo()
    sorted_demo()
    zip_demo()

    print('
All Iteration Helpers demonstrations completed successfully.')


if __name__ == '__main__':
    main()
