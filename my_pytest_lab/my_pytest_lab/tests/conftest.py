import pytest

from src.main import BankAccount


@pytest.fixture
def account():
    """Prepare a BankAccount and clear state after the test (yield teardown)."""
    acc = BankAccount(owner="Іван", balance=1000.0)
    yield acc
    # TEARDOWN
    acc.balance = 0.0


@pytest.fixture
def empty_account():
    acc = BankAccount(owner="Марія", balance=0.0)
    yield acc
    acc.balance = 0.0
