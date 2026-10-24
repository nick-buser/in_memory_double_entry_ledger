#!/usr/bin/env python3
from enum import StrEnum, auto

class TransactionType(StrEnum):
    # simplified set of transactions to limit implementation scope
    CREDIT_PURCHASE                = auto()
    DEBIT_PURCHASE                 = auto()
    TRANSFER_CHECKING_TO_CHECKING  = auto()
    TRANSFER_CHECKING_TO_SAVINGS   = auto()
    TRANSFER_CHECKING_TO_PAYMENTS  = auto()
    TRANSFER_SAVINGS_TO_CHECKING   = auto()
    TRANSFER_PAYMENTS_TO_OPERATING = auto()
    TRANSFER_OPERATING_TO_ASSETS   = auto()
    TRANSFER_ASSETS_TO_OPERATING   = auto()
