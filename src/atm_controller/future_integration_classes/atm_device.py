from src.atm_controller.future_integration_classes.bank.bank_system import BankSystemWrapper
from typing import Tuple

class ATMDevice:
    """
    This is the dummy ATM device class.
    
    Tasks it's responsible for:
        1. Talks to ATMController class
        2. Talks to BankSystemWrapper to check data validity and to update BankInfo.

    This will simulate a singleton class since an ATM device only deals with a single user interaction.
    """

    device_on = True # ATM device state of wehther or not the device is on.
    card_inserted = False # ATM device keeps track of the state of whether a card has been inserted

    @classmethod
    def device_on(cls) -> bool:
        return cls.device_on

    @classmethod
    def reset_states(cls):
        cls.device_on = True
        cls.card_inserted = False
        BankSystemWrapper.reset_states()

    @classmethod
    def remove_card(cls):
        """
        TODO: This should remove the card if there is a card.
        """
        return 
    
    @classmethod
    def waitForCashDeposit(cls, amount: int):
        """
        TODO: Waits for the user to place the right amount of cash into the machine
        and checks.
        """
        return 
    
    @classmethod
    def waitForCashRemoval(cls):
        """
        TODO: Waits for the user to withdraw the cash from the machine
        """
        return

    @classmethod
    def _card_read(cls) -> bool:
        """
        This method reads the card information and updates the BankInfo. If it fails, return false.

        TODO: This needs to be implemented. For now, assume that the card is read correctly every time.
        
        This should update the BankInfo class, within which card info is contained
        This returns True for now
        """
        card_info = {}
        success = BankSystemWrapper.update_cardInfo(card_info)
        return success
    
    @classmethod
    def _card_in_bank(cls) -> bool:
        """
        This method checks the read card information against the bank system. 
        The card information must have been read.
        """
        
        return BankSystemWrapper.card_exists()

    @classmethod
    def card_inserted(cls) -> bool:
        """
        TODO: This method checks whether a user has inserted his/her card. Waits until card has been inserted.
        This returns true for now.

        TODO: Need to check whether a user as inserted his / her card.
        """
        cls.card_inserted = True
        return cls.card_inserted

    @classmethod
    def card_read_success(cls) -> Tuple[bool, str]:
        """
        If the card is read correctly and the read information is checked against the bank system, it returns true.
        """
        if cls._card_read():
            if cls._card_in_bank():
                return (True, "Card read successfully.")
            else:
                return (True, "Card info not registered with bank system.")
        else:
            return (False, "Failed to read card. Please take out your card and try again.")

    @classmethod
    def pin_correct(cls, pin: str="", retry: bool=False) -> Tuple[bool, str]:
        """
        Once correct, populate the BankInfo with appropriate metadata for accounts connected to the card.
        """
        
        if not retry:
            return (False, "Failed to put correct PIN. Please take out your card.")

        if BankSystemWrapper.check_pin_update_accounts(pin):
            return (True, "PIN Correct")
        else:
            return (False, "Incorrect PIN.")
        
    @classmethod
    def get_bankinfo_accounts(cls, account=None):
        """
        This returns the accounts recorded in BankInfo
        """
        return BankSystemWrapper.get_bankinfo_accounts(account)
    
    @classmethod
    def deposit(cls, amount: int, account_idx: int) -> bool:
        """
        TODO: deposits amount to account indexed at account_idx in BankInfo
        """
        return BankSystemWrapper.deposit(amount, account_idx)
    
    @classmethod
    def withdraw(cls, amount: int, account_idx: int) -> bool:
        """
        TODO: withdraws amount from account indexed at account_idx in BankInfo
        """
        return BankSystemWrapper.withdraw(amount, account_idx)