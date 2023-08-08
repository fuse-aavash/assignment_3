from abc import ABC, abstractmethod

# Logger interface
class Logger(ABC):
    """
    Abstract Base Class for representing different types of loggers.
    """

    @abstractmethod
    def log(self, message: str) -> None:
        """
        Log the message to the respective destination.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        pass


# FileLogger class
class FileLogger(Logger):
    """
    Represents a logger that logs messages to a file.
    """

    def log(self, message: str) -> None:
        """
        Log the message to a file.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        with open("logs.txt", "a", encoding="utf-8") as file:
            file.write(f"File Logger: {message}\n")
        print(f"Logged to File: {message}")


# ConsoleLogger class
class ConsoleLogger(Logger):
    """
    Represents a logger that logs messages to the console.
    """

    def log(self, message: str) -> None:
        """
        Log the message to the console.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        print(f"Console Logger: {message}")


# DatabaseLogger class
class DatabaseLogger(Logger):
    """
    Represents a logger that logs messages to the database.
    """

    def log(self, message: str) -> None:
        """
        Log the message to the database.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        # Code to log the message to the database
        print(f"Logged to Database: {message}")


# LoggerFactory class
class LoggerFactory:
    """
    Factory class to create different types of loggers.
    """

    loggers = {
        "file": FileLogger,
        "console": ConsoleLogger,
        "database": DatabaseLogger,
    }

    def create_logger(self, logger_type: str) -> Logger:
        """
        Create a logger based on the logger type.

        Args:
            logger_type (str): The type of logger to be created.

        Returns:
            Logger: An instance of the specified logger type.
        """
        logger_class = self.loggers.get(logger_type)
        if logger_class:
            return logger_class()
        raise ValueError("Invalid logger type")


# Client code
if __name__ == "__main__":
    logger_factory = LoggerFactory()

    file_logger = logger_factory.create_logger("file")
    file_logger.log("This message will be logged to the file.")

    console_logger = logger_factory.create_logger("console")
    console_logger.log("This message will be logged to the console.")

    database_logger = logger_factory.create_logger("database")
    database_logger.log("This message will be logged to the database.")
