import sqlite3

class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.conn = sqlite3.connect('bank.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS accounts (account_number INTEGER PRIMARY KEY, balance REAL)")
        self.conn.commit()

    def deposit(self, amount):
        self.cursor.execute(
            "UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно зачислены на счет {self.account_number}"

    def withdraw(self, amount):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        balance = self.cursor.fetchone()[0]
        self.cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_number = ?", (amount, self.account_number))
        self.conn.commit()
        return f"{amount} средств успешно сняты с счета {self.account_number}"

    def check_balance(self):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_number = ?", (self.account_number,))
        result = self.cursor.fetchone()
        if result is not None:
            balance = result[0]
            return balance
        else:
            return 0

    def close_account(self):
        self.cursor.execute(
            "DELETE FROM accounts WHERE account_number = ?", (self.account_number,))
        self.conn.commit()
        return f"Счет {self.account_number} закрыт"

    def create_account(self, balance):
        self.cursor.execute(
            "INSERT INTO accounts (account_number, balance) VALUES (?, ?)", (self.account_number, balance))
        self.conn.commit()
        return f"Счет {self.account_number} успешно создан"

from hypothesis import given
from hypothesis.strategies import floats
import pytest

@given(amount=floats(min_value=0))
def test_deposit(amount):
    account = BankAccount(1)
    initial_balance = account.check_balance()
    account.deposit(amount)
    new_balance = account.check_balance()
    assert new_balance == f"Баланс счета 1: {initial_balance + amount}"

# тестирование метода withdraw
@given(amount=floats(min_value=0))
def test_withdraw(amount):
    account = BankAccount(1)
    account.deposit(amount)
    initial_balance = account.check_balance()
    account.withdraw(amount)
    new_balance = account.check_balance()
    assert new_balance == f"Баланс счета 1: {initial_balance - amount}"


def test_check_balance():
    account = BankAccount(1)
    balance = account.check_balance()
    assert balance == "Баланс счета 1: 0.0"


def test_close_account():
    account = BankAccount(1)
    account.create_account(100)
    result = account.close_account()
    assert result == "Счет 1 закрыт"