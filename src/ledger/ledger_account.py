#!/usr/bin/env python3
from ledger.account_type import AccountType
import time

class LedgerAccount:
    def __init__(self, account_type: AccountType, account_id: int, starting_balance = 0):
        self.account_type: AccountType = account_type
        self.account_id: int             = account_id
        self.balance: int                = starting_balance
        self.creation_time: int          = int(time.time())

    def debit_account(self, debit_amount):
        self.balance -= debit_amount

    def credit_account(self, credit_amount):
        self.balance += credit_amount
