"""BankAccount — business logic for Lab 2.1 (pytest fundamentals)."""

from __future__ import annotations


class BankAccount:
    """Simple bank account: deposit, withdraw, interest, balance checks."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner name must be a non-empty string")
        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise TypeError("Balance must be a number")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner.strip()
        self.balance = float(balance)

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += float(amount)
        return self.balance

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= float(amount)
        return self.balance

    def apply_interest(self, rate_percent: float) -> float:
        """Add interest as percent of current balance (e.g. 5 -> +5%)."""
        if not isinstance(rate_percent, (int, float)) or isinstance(rate_percent, bool):
            raise TypeError("Rate must be a number")
        if rate_percent < 0:
            raise ValueError("Interest rate cannot be negative")
        self.balance += self.balance * (float(rate_percent) / 100.0)
        return self.balance

    def get_balance(self) -> float:
        return self.balance
