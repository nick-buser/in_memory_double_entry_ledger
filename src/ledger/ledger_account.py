#!/usr/bin/env python3
from ledger.account_type import AccountType
import time

class LedgerAccount:
    def __init__(self, account_type: AccountType):
        self.account_type: AccountType = account_type
        self.account_id: int             = account_type.value
        self.balance: int                = 0
        self.creation_time: int          = int(time.time())
