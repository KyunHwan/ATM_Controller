from atm_controller.future_integration_classes.bank.helper_classes.bank_info import BankInfo

class BankSystemWrapper:
    """
    This is the dummy BankSystemWrapper class.
    
    Task it's responsible for:
        1. Interacts with the bank system API.
        2. Interacts with BankInfo 
    
    This will simulate a singleton class since an ATM device only deals with a single user interaction.
    """
    pin_checked = False

    @classmethod
    def reset_states(cls):
        """
        TODO: This should reset the states of the bank system (ie. forget the particular user)
        """
        cls.pin_checked = False
        BankInfo.reset_states()

        return


    @classmethod
    def card_exists(cls) -> bool:
        """
        TODO: This should check the bank system against the read & recorded card information and return True if card exists.
        
        Return True for now
        """

        return True

    @classmethod
    def update_cardInfo(cls, card_info) -> bool:
        """
        TODO: This should update the BankInfo with read card information.
        
        Return whether or not the update has been successful
        """

        BankInfo.update_cardInfo(card_info)
        return bool

    @classmethod
    def pin_correct(cls, pin) -> bool:
        """
        TODO: This should talk with the Bank System API. It should check the system against BankInfo and pin given
        
        This will return True for now.
        """
        cls.pin_checked = True
        return True
    
    @classmethod
    def check_pin_update_accounts(cls, pin) -> bool:
        """
        TODO: This should check the pin for correctness and retrieve account metadata from the bank system.
              Then BankInfo should be updated to contain the necessary metadata.
        """
        success = cls.pin_correct(pin)
        if success:
            # this is where the accounts should be retrieved using the pin and Card info
            accounts = [{}, {}] # dummy data for now
            BankInfo.update_accounts(accounts)

        return success
    
    @classmethod
    def get_bankinfo_accounts(cls, account=None):
        """
        This should get accounts from the BankInfo
        """
        return BankInfo.get_accounts(account)
    
    @classmethod
    def deposit(cls, amount, account_idx):
        """
        TODO: This should deposit the ammount to the account at account_idx in BankInfo
        via the bank system.
        """
        return True
    
    @classmethod
    def withdraw(cls, amount, account_idxc):
        """
        TODO: This should withdraw the ammount from the account at account_idx in BankInfo
        via the bank system.
        """
        return True
