# Lab 2.1 — Pytest fundamentals (BankAccount)

## Setup

```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
# source .venv/bin/activate

python -m pip install -r requirements.txt
pytest -v
```

## Coverage

- BankAccount: deposit, withdraw, interest, exceptions
- pytest.raises, parametrize, approx
- conftest fixture with yield teardown
- markers: smoke, skipif, xfail
