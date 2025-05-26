from typing import Optional
class BankInfo:
    """
    Dummy class for bank information

    Responsible for:
        1. Stores card information
        2. Manages metadata for accounts
    """
    card = None
    accounts = None

    @classmethod
    def reset_states(cls):
        cls.card = None
        cls.accounts = None

    @classmethod
    def update_cardInfo(cls, card_info):
        """
        TODO: This needs to properly check the data and return success state.
        """
        cls.card = card_info
    
    @classmethod
    def update_accounts(cls, accounts):
        """
        TODO: This needs to properly check the data and return success state.
        """
        cls.accounts = accounts

    @classmethod
    def get_accounts(cls, account: Optional[int]):
        """
        Returns accounts metadata
        """
        if account is None:
            return cls.accounts
        else:
            return cls.accounts[account]
