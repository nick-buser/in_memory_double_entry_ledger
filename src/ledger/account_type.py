#!/usr/bin/env python3
from enum import Enum

# In a production system I'd lean away from sequential account numbers to avoid guessing threat vectors
n_consumer_checking_accounts = 1
n_consumer_savings_accounts = 1
n_consumer_credit_accounts = 1

class AccountType(Enum):
    # accounts are a simplification for restricted implementation and not a claim for how I'd design a complete business ledger
    ASSETS          = 3_000_001
    PAYMENTS        = 4_000_001
    OPERATING       = 5_000_001
    CONSUMER_CHECKING  = 6_000_000 + n_consumer_checking_accounts
    CONSUMER_SAVINGS  = 7_000_000 + n_consumer_savings_accounts
    CONSUMER_CREDIT = 8_000_000 + n_consumer_credit_accounts
