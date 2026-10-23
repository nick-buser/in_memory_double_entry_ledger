#!/usr/bin/env python3
from enum import Enum

# In a production system I'd lean away from sequential account numbers to avoid guessing threat vectors
n_consumer_debit_accounts = 1
n_consumer_credit_accounts = 1

class AccountType(Enum):
    PAYMENTS        = 4_000_001
    OPERATING       = 5_000_001
    CONSUMER_DEBIT  = 6_000_000 + n_consumer_debit_accounts
    CONSUMER_CREDIT = 7_000_000 + n_consumer_credit_accounts

class LedgerAccount:
    def __init__(self, account_type: AccountType):
        self.account_type: AccountType = account_type
        self.account_id: int =
