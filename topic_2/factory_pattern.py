from abc import ABC, abstractmethod

# Logger interface
class Logger(ABC):
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
    def log(self, message: str) -> None:
        """
        Log the message to a file.

        Args:
            message (str): The message to be logged.

        Returns:
            None
        """
        with open("logs.txt", "a") as file:
            file.write(f"File Logger: {message}\n")
        print(f"Logged to File: {message}")

# ConsoleLogger class
class ConsoleLogger(Logger):
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
    def create_logger(self, logger_type: str) -> Logger:
        """
        Create a logger based on the logger type.

        Args:
            logger_type (str): The type of logger to be created.

        Returns:
            Logger: An instance of the specified logger type.
        """
        if logger_type == "file":
            return FileLogger()
        elif logger_type == "console":
            return ConsoleLogger()
        elif logger_type == "database":
            return DatabaseLogger()
        else:
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
