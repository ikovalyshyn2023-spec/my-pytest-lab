import sys

import pytest

from src.main import BankAccount


# --- positive scenarios ---

def test_initial_balance(account):
    assert account.get_balance() == 1000.0
    assert account.owner == "Іван"


def test_deposit_increases_balance(account):
    new_balance = account.deposit(250.0)
    assert new_balance == 1250.0
    assert account.get_balance() == 1250.0


def test_withdraw_decreases_balance(account):
    new_balance = account.withdraw(200.0)
    assert new_balance == 800.0


def test_apply_interest(account):
    # 5% of 1000 = 50
    result = account.apply_interest(5)
    assert result == pytest.approx(1050.0)


# --- exceptions ---

def test_deposit_negative_raises():
    acc = BankAccount("Test", 100)
    with pytest.raises(ValueError, match="positive"):
        acc.deposit(-10)


def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError, match="Insufficient"):
        account.withdraw(5000)


def test_withdraw_zero_raises(account):
    with pytest.raises(ValueError, match="positive"):
        account.withdraw(0)


def test_invalid_owner_raises():
    with pytest.raises(ValueError, match="Owner"):
        BankAccount("", 0)


def test_negative_initial_balance_raises():
    with pytest.raises(ValueError, match="negative"):
        BankAccount("Test", -1)


def test_deposit_non_numeric_raises(account):
    with pytest.raises(TypeError, match="number"):
        account.deposit("100")  # type: ignore[arg-type]


# --- parametrize (≥3 datasets) ---

@pytest.mark.parametrize(
    "deposit, expected",
    [
        (100.0, 1100.0),
        (500.0, 1500.0),
        (0.01, 1000.01),
        (999.99, 1999.99),
    ],
)
def test_deposit_parametrized(account, deposit, expected):
    account.deposit(deposit)
    assert account.get_balance() == pytest.approx(expected)


@pytest.mark.parametrize(
    "start, rate, expected",
    [
        (1000.0, 10, 1100.0),
        (200.0, 0, 200.0),
        (50.0, 100, 100.0),
    ],
)
def test_interest_parametrized(start, rate, expected):
    acc = BankAccount("Param", start)
    acc.apply_interest(rate)
    assert acc.get_balance() == pytest.approx(expected)


# --- markers ---

@pytest.mark.smoke
def test_smoke_create_and_balance():
    acc = BankAccount("Smoke", 42)
    assert acc.get_balance() == 42


@pytest.mark.skipif(
    sys.version_info < (3, 8),
    reason="Requires Python 3.8+ for this environment check demo",
)
def test_skipif_python_version(account):
    assert account.get_balance() >= 0


@pytest.mark.xfail(reason="Demo: intentional expected failure for Lab 2.1 marker requirement")
def test_xfail_demo():
    assert 1 == 2
