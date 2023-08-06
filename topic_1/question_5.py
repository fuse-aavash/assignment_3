
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Process a payment for the given amount.

        Args:
            amount (float): The amount to be paid.

        Returns:
            None
        """
        pass


class PaymentWithRefundProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """
        Process a payment for the given amount.

        Args:
            amount (float): The amount to be paid.

        Returns:
            None
        """
        pass

    @abstractmethod
    def process_refund(self, amount: float) -> None:
        """
        Process a refund for the given amount.

        Args:
            amount (float): The amount to be refunded.

        Returns:
            None
        """
        pass


class OnlinePaymentProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        """
        Process a payment for online transactions.

        Args:
            amount (float): The amount to be paid.

        Returns:
            None
        """
        print(f"Processing online payment of ${amount}")


class OnlinePaymentWithRefundProcessor(PaymentWithRefundProcessor):
    def process_payment(self, amount: float) -> None:
        """
        Process a payment for online transactions.

        Args:
            amount (float): The amount to be paid.

        Returns:
            None
        """
        print(f"Processing online payment of ${amount}")

    def process_refund(self, amount: float) -> None:
        """
        Process a refund for online transactions.

        Args:
            amount (float): The amount to be refunded.

        Returns:
            None
        """
        print(f"Processing online refund of ${amount}")


# Test the classes
online_processor = OnlinePaymentProcessor()
online_processor.process_payment(100)

online_refund_processor = OnlinePaymentWithRefundProcessor()
online_refund_processor.process_payment(150)
online_refund_processor.process_refund(50)
