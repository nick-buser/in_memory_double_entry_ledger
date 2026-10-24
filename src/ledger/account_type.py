#!/usr/bin/env python3
from enum import StrEnum, auto


class AccountType(Enum):
    # accounts are a simplification for restricted implementation and not a claim for how I'd design a complete business ledger
    ASSETS            = auto()
    PAYMENTS          = auto()
    OPERATING         = auto()
    CONSUMER_CHECKING = auto()
    CONSUMER_SAVINGS  = auto()
    CONSUMER_CREDIT   = auto()
