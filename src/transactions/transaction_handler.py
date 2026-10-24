#!/usr/bin/env python3
from ledger.ledger_account import LedgerAccount
from ledger.ledger_account import AccountType
from transactions.transaction import Transaction
from transactions.transaction_type import TransactionType


def handle_transaction(
    transaction_type: TransactionType,
    credited_account: LedgerAccount,
    debited_account : LedgerAccount,
    amount          : int
) -> Transaction | None:
    match transaction_type:
        case TransactionType.CREDIT_PURCHASE:
            credit_type = AccountType.CONSUMER_CREDIT
            debit_type = AccountType.OPERATING

        case TransactionType.DEBIT_PURCHASE:
            credit_type = AccountType.OPERATING
            debit_type = AccountType.CONSUMER_CHECKING

        case TransactionType.TRANSFER_CHECKING_TO_CHECKING:
            credit_type = AccountType.CONSUMER_CHECKING
            debit_type = AccountType.CONSUMER_CHECKING

        case TransactionType.TRANSFER_CHECKING_TO_SAVINGS:
            credit_type = AccountType.CONSUMER_SAVINGS
            debit_type = AccountType.CONSUMER_CHECKING

        case TransactionType.TRANSFER_CHECKING_TO_PAYMENTS:
            credit_type = AccountType.PAYMENTS
            debit_type = AccountType.CONSUMER_CHECKING

        case TransactionType.TRANSFER_SAVINGS_TO_CHECKING:
            credit_type = AccountType.CONSUMER_CHECKING
            debit_type = AccountType.CONSUMER_SAVINGS

        case TransactionType.TRANSFER_PAYMENTS_TO_OPERATING:
            credit_type = AccountType.OPERATING
            debit_type = AccountType.PAYMENTS

        case TransactionType.TRANSFER_OPERATING_TO_ASSETS:
            credit_type = AccountType.ASSETS
            debit_type = AccountType.OPERATING

        case TransactionType.TRANSFER_ASSETS_TO_OPERATING:
            credit_type = AccountType.OPERATING
            debit_type = AccountType.ASSETS

        case _:
            raise ValueError(f"transaction type {transaction_type} is not implemented")

    if not validate_transaction(credit_type, debit_type, credited_account, debited_account, transaction_type, amount):
        return None

    credited_account.credit_account(amount)
    debited_account.debit_account(amount)
    return Transaction(credited_account.account_id, debited_account.account_id, amount, transaction_type)


def validate_transaction(credit_type, debit_type, credited_account, debited_account, transaction_type, amount) -> bool:
    """
    This is written intentionally to throw exceptions for invalid transactions
    and to return False for a no-op for a case where the isssed transaction is valid but the state
    doesn't permit it. Thinking is that the prior sounds like an implementation bug
    and the latter a possible case occurring in properly implemented operation
    """
    if not credited_account or credited_account.account_type != credit_type:
        raise ValueError(f"credited account for {transaction_type} must be {credit_type}")
    if debited_account.account_type != debit_type:
        raise ValueError(f"debited account for {transaction_type} must be {debit_type}")
    if credited_account.account_id == debited_account.account_id:
        raise ValueError(f"An account cannot issue a transaction from itself to itself")

    if amount <= 0 or not isinstance(amount, int):
        # Arguable whether this should be considered a bug indication and throw an exception
        return False

    if debited_account.balance < amount:
        return False
    return True
