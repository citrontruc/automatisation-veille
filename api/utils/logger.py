"""
An object to log actions and errors.
"""

from datetime import datetime
import logging
from pathlib import Path
import structlog


class Logger:
    def __init__(self):
        structlog.configure(
            processors=[
                structlog.contextvars.merge_contextvars,
                structlog.processors.add_log_level,
                structlog.processors.StackInfoRenderer(),
                structlog.dev.set_exc_info,
                structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=False),
                structlog.dev.ConsoleRenderer(),
                structlog.processors.JSONRenderer()
            ],
            wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
            context_class=dict,
            logger_factory=structlog.WriteLoggerFactory(
                file=Path(f"{datetime.today().strftime('%Y-%m-%d')}_logs").with_suffix(".log").open("wt")
            ),
            cache_logger_on_first_use=False
        )
        self.logger = structlog.get_logger()
    
    def log_info(self, message):
        """
        Method to log an information.
        input:
            message (str)
        """
        self.logger.info(message)

    def log_error(self, message):
        """
        Method to log an error message.
        input:
            message (str)
        """
        self.logger.error(message)
