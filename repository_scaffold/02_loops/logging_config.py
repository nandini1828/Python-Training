"""
Central logging configuration for the Loops module.
"""

import logging


def configure_logging(level=logging.INFO):
    """Configure logging for the module."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    return logging.getLogger(__name__)
