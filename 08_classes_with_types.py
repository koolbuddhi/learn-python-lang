# Classes with Type Hints in Python
# ============================

from typing import List, Dict, Optional, ClassVar
from dataclasses import dataclass
from datetime import datetime

# Basic Class with Type Hints
# ------------------------
class BankAccount:
    interest_rate: ClassVar[float] = 0.02  # Class variable with type hint
    
    def __init__(self, account_number: str, balance: float = 0.0) -> None:
        self.account_number: str = account_number
        self.balance: float = balance
        self.transaction_history: List[Dict[str, Union[str, float, datetime]]] = []

    def deposit(self, amount: float) -> float:
        self.balance += amount
        self._record_transaction("deposit", amount)
        return self.balance

    def withdraw(self, amount: float) -> Optional[float]:
        if amount <= self.balance:
            self.balance -= amount
            self._record_transaction("withdrawal", amount)
            return self.balance
        return None

    def _record_transaction(self, transaction_type: str, amount: float) -> None:
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "timestamp": datetime.now()
        })

# Inheritance with Type Hints
# ------------------------
class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, balance: float = 0.0, 
                 minimum_balance: float = 100.0) -> None:
        super().__init__(account_number, balance)
        self.minimum_balance: float = minimum_balance

    def withdraw(self, amount: float) -> Optional[float]:
        if self.balance - amount >= self.minimum_balance:
            return super().withdraw(amount)
        return None

# DataClass with Type Hints
# ----------------------
@dataclass
class Customer:
    id: str
    name: str
    email: str
    accounts: List[BankAccount]
    
    def get_total_balance(self) -> float:
        return sum(account.balance for account in self.accounts)

# Generic Class with Type Hints
# --------------------------
from typing import TypeVar, Generic

T = TypeVar('T')

class TransactionLog(Generic[T]):
    def __init__(self) -> None:
        self.transactions: List[T] = []

    def add_transaction(self, transaction: T) -> None:
        self.transactions.append(transaction)

    def get_transactions(self) -> List[T]:
        return self.transactions

# Abstract Base Class with Type Hints
# -------------------------------
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

    @abstractmethod
    def refund_payment(self, amount: float) -> bool:
        pass

# Concrete Implementation
class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number: str) -> None:
        self.card_number: str = card_number

    def process_payment(self, amount: float) -> bool:
        # Simulate payment processing
        print(f"Processing ${amount} with card {self.card_number}")
        return True

    def refund_payment(self, amount: float) -> bool:
        # Simulate refund
        print(f"Refunding ${amount} to card {self.card_number}")
        return True

# Example Usage
def main() -> None:
    # Create a bank account
    account: BankAccount = BankAccount("1234567890")
    account.deposit(1000.0)
    account.withdraw(500.0)

    # Create a savings account
    savings: SavingsAccount = SavingsAccount("9876543210", 2000.0)
    savings.withdraw(1000.0)

    # Create a customer
    customer: Customer = Customer(
        id="C001",
        name="John Doe",
        email="john@example.com",
        accounts=[account, savings]
    )
    
    # Create a transaction log
    log: TransactionLog[Dict[str, Union[str, float]]] = TransactionLog()
    log.add_transaction({"type": "deposit", "amount": 1000.0})

    # Process a payment
    processor: PaymentProcessor = CreditCardProcessor("4111-1111-1111-1111")
    processor.process_payment(100.0)

    # Print results
    print(f"Customer total balance: ${customer.get_total_balance()}")
    print(f"Transaction history: {account.transaction_history}")
    print(f"Transaction log: {log.get_transactions()}")

if __name__ == "__main__":
    main()

# Practice Exercises:
# 1. Create a generic Shopping Cart class that can hold items of any type
# 2. Implement an abstract base class for different types of bank accounts
# 3. Create a dataclass for representing a product with inventory tracking
# 4. Implement a class hierarchy for different types of payment methods with appropriate type hints
