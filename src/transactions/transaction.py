#!/usr/bin/env python3
import time

class Transaction:
    def __init__(self, credited_account_id, debited_account_id, amount, transaction_type):
        self.credited_account_id   = credited_account_id
        self.debited_account_id    = debited_account_id
        self.transaction_amount    = amount
        self.transaction_type      = transaction_type
        self.creation_time         = int(time.time())
