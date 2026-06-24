from __future__ import annotations

import logging
from logging import Logger


def configure_logging(level: int = logging.INFO) -> Logger:
    logger = logging.getLogger("python_datatypes")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s %(name)s %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger
