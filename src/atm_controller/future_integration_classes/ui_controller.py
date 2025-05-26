from enum import Enum
import sys
import tty
import termios

class ATMState(Enum):
    INSERT_CARD = 1
    READ_CARD = 2
    PIN_NUMBER = 3
    SELECT_ACCOUNT = 4
    CHOOSE_ACCOUNT_ACTION = 5
    CHOOSE_ACTION_AMOUNT = 6
    IMPLEMENT_ACTION = 7
    ACTION_COMPLETE = 8
    


class AccountInteraction(Enum):
    WITHDRAW = 1
    DEPOSIT = 2


class UIControllerWrapper:
    """
    Dummy class for UIController Wrapper

    Responsible for:
        1. Talks with the UI controller 
        2. Talks with ATMController
    """

    @classmethod
    def setStateTo(cls, state: ATMState, data):
        """
        TODO: This should update the UI to the specificed state (ex. page)
        """
        return
    
    @classmethod
    def message(cls, state: ATMState, message: str):
        """
        TODO: This should give the user an appropriate message at the specified state.

        For now, it simply prints the desired output message
        """
        print(message)
        return
    
    @classmethod
    def error_message(cls, state: ATMState, error_message: str):
        """
        TODO: This should give the user an appropriate error message at the specified state.

        For now, it simply prints the error
        """

        print(error_message)
        return
    
    @classmethod 
    def prompt_pin_digit(cls, state: ATMState, pin: str):
        """
        TODO: This should check that the state is at the correct state and interact with the UI
              to update the pin. 
              
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)  # read one character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch
    
    @classmethod
    def select_account(cls):
        """
        TODO: This should wait until the account has been selected correctly.
              The UI had previously been updated to select_account state.
              UI has also been given accounts data in a list form.
              So each interactive UI element related to each account has index information.

              Returns index information of the accounts list of BankInfo
        Returns index 0 for now.
        """

        return 0
    
    @classmethod
    def get_user_action(cls) -> AccountInteraction:
        """
        TODO: Gets action from the user (withdraw or deposit)
        """

        return AccountInteraction.WITHDRAW
    
    @classmethod
    def get_action_amount(cls) -> int:
        """
        TODO: Gets the amount to either withdraw or deposit.

        Return 100 for now
        """

        return 100
