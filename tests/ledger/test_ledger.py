#!/usr/bin/env python3

from transactions.transaction_type import TransactionType
from ledger.ledger import CONSUMER_CREDIT_ACCOUNT_ID_START
from ledger.ledger import CONSUMER_SAVINGS_ACCOUNT_ID_START
from ledger.ledger import CONSUMER_CHECKING_ACCOUNT_ID_START
from ledger.account_type import AccountType
from ledger.ledger import OPERATING_ACCOUNT_ID
from ledger.ledger import PAYMENTS_ACCOUNT_ID
from ledger.ledger import ASSETS_ACCOUNT_ID
from ledger.ledger import Ledger

def test_ledger_account_creation():
    ledger = Ledger()
    assert ASSETS_ACCOUNT_ID in ledger.accounts
    assert PAYMENTS_ACCOUNT_ID in ledger.accounts
    assert OPERATING_ACCOUNT_ID in ledger.accounts

    # All successful account creations should return True to indicate it was created
    consumer_checking_balance = 100
    consumer_savings_balance = 200
    default_balance = 0
    assert ledger.create_account(AccountType.CONSUMER_CHECKING, consumer_checking_balance)
    assert ledger.create_account(AccountType.CONSUMER_SAVINGS, consumer_savings_balance)
    assert ledger.create_account(AccountType.CONSUMER_CREDIT)

    consumer_checking_account = ledger.accounts[CONSUMER_CHECKING_ACCOUNT_ID_START + ledger.n_checking_accounts]
    consumer_savings_account = ledger.accounts[CONSUMER_SAVINGS_ACCOUNT_ID_START + ledger.n_savings_accounts]
    consumer_credit_account = ledger.accounts[CONSUMER_CREDIT_ACCOUNT_ID_START + ledger.n_credit_accounts]

    assert consumer_checking_account.balance == consumer_checking_balance
    assert consumer_savings_account.balance == consumer_savings_balance
    assert consumer_credit_account.balance == default_balance

    assert consumer_checking_account.account_type == AccountType.CONSUMER_CHECKING
    assert consumer_savings_account.account_type == AccountType.CONSUMER_SAVINGS
    assert consumer_credit_account.account_type == AccountType.CONSUMER_CREDIT

def test_a_few_transactions():
    assets_starting_balance = 1_000
    payments_starting_balance = 500
    operating_starting_balance = 2_000
    ledger = Ledger(assets_starting_balance=assets_starting_balance, payments_starting_balance= payments_starting_balance, operating_starting_balance=operating_starting_balance)

    assets_account = ledger.accounts[ASSETS_ACCOUNT_ID]
    assert assets_account.balance == assets_starting_balance

    payments_account = ledger.accounts[PAYMENTS_ACCOUNT_ID]
    assert payments_account.balance == payments_starting_balance

    operating_account = ledger.accounts[OPERATING_ACCOUNT_ID]
    assert operating_account.balance == operating_starting_balance

    assets_to_operating_transaction_amount = 100
    ledger.issue_transaction(TransactionType.TRANSFER_ASSETS_TO_OPERATING, ASSETS_ACCOUNT_ID, OPERATING_ACCOUNT_ID, assets_to_operating_transaction_amount)
    assert assets_account.balance == assets_starting_balance - assets_to_operating_transaction_amount
    assert operating_account.balance == operating_starting_balance + assets_to_operating_transaction_amount

    consumer_checking_starting_balance = 100
    assert ledger.create_account(AccountType.CONSUMER_CHECKING, consumer_checking_starting_balance)
    consumer_checking_account = ledger.accounts[CONSUMER_CHECKING_ACCOUNT_ID_START + ledger.n_checking_accounts]

    debit_purchase_transaction_amount = 50
    previous_operating_account_balance = operating_account.balance
    ledger.issue_transaction(TransactionType.DEBIT_PURCHASE, consumer_checking_account.account_id, OPERATING_ACCOUNT_ID, debit_purchase_transaction_amount)
    assert consumer_checking_account.balance == consumer_checking_starting_balance - debit_purchase_transaction_amount
    assert operating_account.balance == previous_operating_account_balance + debit_purchase_transaction_amount
