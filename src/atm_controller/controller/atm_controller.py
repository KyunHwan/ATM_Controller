from atm_controller.future_integration_classes.atm_device import ATMDevice
from atm_controller.future_integration_classes.ui_controller import UIControllerWrapper, ATMState, AccountInteraction


class ATMController:
    """
    This is the controller class for the ATM system.
    It will be responsible for handling the control flow for the ATM system.

    This will simulate a singleton class since an ATM device only deals with a single user interaction.
    """

    _num_pin_try_limit = 3 # this is the limit of times the user can try to enter the pin
    _pin_length = 4

    @classmethod
    def _reset_states(cls):
        """
        Resets states of the ATM device and the BankInfo that has retrieved from the bank system.
        """
        ATMDevice.reset_states()

    @classmethod
    def _remove_card(cls):
        """
        Removes the card from the ATM device
        """
        ATMDevice.remove_card()

    @classmethod
    def _set_ui_state(cls, state: ATMState, data = None):
        """
        Sets UI state to state with appropriate data for the corresponding state
        """
        UIControllerWrapper.setStateTo(state, data)
        
    @classmethod
    def _deviceOn(cls) -> bool:
        """
        Implemented as a condition for having the controller on.
        """
        return ATMDevice.is_device_on()

    @classmethod
    def _wait_card_insertion(cls):
        """
        Prompts the device to wait until it detects card insertion.
        It is assumed that card has been inserted henceforth
        """
        ATMDevice.card_inserted()

    @classmethod 
    def _card_read_success(cls) -> bool:
        """
        Prompts the device to read the inserted card.
        """
        success, message = ATMDevice.card_read_success()
        if success:
            UIControllerWrapper.message(ATMState.READ_CARD, message)
        else:
            UIControllerWrapper.error_message(ATMState.READ_CARD, message)
        return success

    @classmethod
    def _enter_pin_success(cls) -> bool:
        """
        This prompts the user to input 4 digit number. If it doesn't match that stored in the system,
        prompts the user again to input the pin until it reaches the limit. 
        """
        for i in range(cls._num_pin_try_limit):
            pin = ""
            while len(pin) < cls._pin_length:
                pin += UIControllerWrapper.prompt_pin_digit(ATMState.PIN_NUMBER, pin)

            success, message = ATMDevice.pin_correct(pin, (i < cls._num_pin_try_limit))

            if success:
                UIControllerWrapper.message(ATMState.PIN_NUMBER, message)
                return success
            else:
                UIControllerWrapper.message(ATMState.PIN_NUMBER, message)
        
        success, message = ATMDevice.pin_correct()
        UIControllerWrapper.error_message(ATMState.PIN_NUMBER, message)

        return success
    
    @classmethod
    def _select_account(cls) -> int:
        """
        Waits for the user to choose an account connected to the card.
        On the UI side, it already has UI elements displayed to show accounts 
        retrieved from the system with index associated with each element. 
        """
        selected_account = UIControllerWrapper.select_account()
        return selected_account

    @classmethod
    def _deposit(cls, amount: int, account: int) -> bool:
        """
        Waits for the right amount to be deposited to the machine.
        Then the amount is digitally deposited to the account in the bank system.
        """
        ATMDevice.waitForCashDeposit(amount) # Waits for the cash to be placed in the ATM
        return ATMDevice.deposit(amount, account)

    @classmethod
    def _withdraw(cls, amount: int, account: int) -> bool:
        """
        Digitally withdraws amount from the bank account.
        Cash is withdrawn from the cash bin.
        Waits for the user to retrieve the cash from the device. 
        """
        success = ATMDevice.withdraw(amount, account)
        ATMDevice.waitForCashRemoval() # Waits for the cash to be removed from the ATM
        return success 

    @classmethod
    def _account_interaction(cls) -> AccountInteraction:
        """
        Waits for the user to choose an action (ie. withdraw or deposit)
        """
        return UIControllerWrapper.get_user_action()
        
    @classmethod
    def _choose_action_amount(cls) -> int:
        """
        Waits for the user to write the amount for the action chosen.
        """
        return UIControllerWrapper.get_action_amount()

    @classmethod
    def start(cls):
        """
        This is the main control flow for the ATM system.
        """
        while cls._deviceOn():
            # Checks if there's an inserted card and removes it if it exists.
            cls._remove_card()

            # reset the states
            cls._reset_states()

            # wait until the card has been inserted
            cls._set_ui_state(ATMState.INSERT_CARD)
            cls._wait_card_insertion()
            
            # read the inserted card and check against the bank system
            cls._set_ui_state(ATMState.READ_CARD)
            if not cls._card_read_success():
                continue
            
            # enter the pin
            cls._set_ui_state(ATMState.PIN_NUMBER)
            if not cls._enter_pin_success():
                continue

            # displays the accounts and waits for the user to select the account
            cls._set_ui_state(ATMState.SELECT_ACCOUNT, ATMDevice.get_bankinfo_accounts())
            selected_account = cls._select_account()

            # displays the metadata of the selected account with options of withdraw & deposit
            cls._set_ui_state(ATMState.CHOOSE_ACCOUNT_ACTION, ATMDevice.get_bankinfo_accounts(selected_account))
            action = cls._account_interaction()

            # displays the action page (depending on whether it's withdraw or deposit)
            # gets the amount to either withdraw or deposit
            cls._set_ui_state(ATMState.CHOOSE_ACTION_AMOUNT)
            cash_amount = cls._choose_action_amount()

            # either withdraw or deposit the cash_amount. 
            # No need to update the local account metadata in BankInfo
            # since it is assumed that user will no longer need additional action,
            cls._set_ui_state(ATMState.IMPLEMENT_ACTION, (action, cash_amount))
            if action == AccountInteraction.DEPOSIT:
                cls._deposit(cash_amount, selected_account)
            else:
                cls._withdraw(cash_amount, selected_account)
            
            # Action completed. Not going back to the initial phase
            cls._set_ui_state(ATMState.ACTION_COMPLETE)
