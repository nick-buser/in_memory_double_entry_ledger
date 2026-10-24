#!/usr/bin/env python3
from transactions.transaction_handler import handle_transaction
from transactions.transaction_type import TransactionType
from transactions.transaction import Transaction
from ledger.account_type import AccountType
from ledger.ledger_account import LedgerAccount

ASSETS_ACCOUNT_ID                  = 1_000_001
PAYMENTS_ACCOUNT_ID                = 2_000_001
OPERATING_ACCOUNT_ID               = 3_000_001
CONSUMER_CHECKING_ACCOUNT_ID_START = 4_000_000
CONSUMER_SAVINGS_ACCOUNT_ID_START  = 5_000_000
CONSUMER_CREDIT_ACCOUNT_ID_START   = 6_000_000

class Ledger:
    def __init__(self, assets_starting_balance = 0, payments_starting_balance = 0, operating_starting_balance = 0):
        self.n_checking_accounts   = 0
        self.n_savings_accounts    = 0
        self.n_credit_accounts     = 0

        # in a double entry system you ought to be able to sum to 0. This is a cheaper way to enforce the invariant
        # without issuing a transaction to an account going negative every time a new account starts with a positive balance
        self.starting_balances     = assets_starting_balance + payments_starting_balance + operating_starting_balance

        self.accounts: dict[int, LedgerAccount] = {
            ASSETS_ACCOUNT_ID: LedgerAccount(AccountType.ASSETS, ASSETS_ACCOUNT_ID, assets_starting_balance),
            PAYMENTS_ACCOUNT_ID: LedgerAccount(AccountType.PAYMENTS, PAYMENTS_ACCOUNT_ID, payments_starting_balance),
            OPERATING_ACCOUNT_ID: LedgerAccount(AccountType.OPERATING, OPERATING_ACCOUNT_ID, operating_starting_balance),
        }
        self.transactions: dict[int, Transaction] = {}

    def create_account(self, account_type: AccountType, starting_balance = 0) -> bool:
        """
        boolean response indicates whether the account was created
        """

        if account_type in [AccountType.ASSETS, AccountType.PAYMENTS, AccountType.OPERATING]:
            # cannot have more than one of these core business accounts
            return False

        if account_type == AccountType.CONSUMER_CHECKING:
            account_id = CONSUMER_CHECKING_ACCOUNT_ID_START  + self.n_checking_accounts + 1
            self.n_checking_accounts += 1

        elif account_type == AccountType.CONSUMER_SAVINGS:
            account_id = CONSUMER_SAVINGS_ACCOUNT_ID_START  + self.n_savings_accounts + 1
            self.n_savings_accounts += 1

        elif account_type == AccountType.CONSUMER_CREDIT:
            account_id = CONSUMER_CREDIT_ACCOUNT_ID_START  + self.n_credit_accounts + 1
            self.n_credit_accounts += 1

        else:
            raise ValueError(f"unrecognized account type {account_type} is not supported")

        self.accounts[account_id] = LedgerAccount(account_type, account_id, starting_balance)
        return True

    def issue_transaction(
            self,
            transaction_type: TransactionType,
            debited_account_id: int,
            credited_account_id: int,
            amount : int
    )-> bool:
        if credited_account_id not in self.accounts:
            raise ValueError(f"target credited account {credited_account_id} does not exist in the system")
        if debited_account_id not in self.accounts:
            raise ValueError(f"target debited account {debited_account_id} does not exist in the system")

        credited_account = self.accounts[credited_account_id]
        debited_account = self.accounts[debited_account_id]

        transaction = handle_transaction(transaction_type, credited_account, debited_account, amount)
        if not transaction:
            return False
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = transaction
        return True
