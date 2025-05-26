import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.atm_controller.controller.atm_controller import ATMController
from src.atm_controller.future_integration_classes.atm_device import ATMDevice
from src.atm_controller.future_integration_classes.ui_controller import ATMState, AccountInteraction

class MockBankSystem:
    def __init__(self):
        self.card_info = {}
        self.accounts = ["Account1", "Account2"]
        self.pin_correct = True

    def update_cardInfo(self, card_info):
        self.card_info = card_info
        return True

    def card_exists(self):
        return True

    def check_pin_update_accounts(self, pin):
        return self.pin_correct

    def deposit(self, amount, account_idx):
        return True

    def withdraw(self, amount, account_idx):
        return True

    def waitForCashRemoval(self):
        return True

    def waitForCashDeposit(self, amount):
        return True

class MockUIController:
    def __init__(self):
        self.current_state = None
        self.current_data = None
        self.pin_digits = ["1", "2", "3", "4"]
        self.pin_index = 0
        self.selected_account = 0
        self.action = AccountInteraction.DEPOSIT
        self.amount = 100

    def setStateTo(self, state, data=None):
        self.current_state = state
        self.current_data = data

    def prompt_pin_digit(self, state, current_pin):
        digit = self.pin_digits[self.pin_index]
        self.pin_index = (self.pin_index + 1) % len(self.pin_digits)
        return digit

    def select_account(self):
        return self.selected_account

    def get_user_action(self):
        return self.action

    def get_action_amount(self):
        return self.amount

    def message(self, state, message):
        print(f"UI Message ({state}): {message}")

    def error_message(self, state, message):
        print(f"UI Error ({state}): {message}")

def test_device_on():
    print("\nTesting device state...")
    ATMDevice.reset_states()
    assert ATMController._deviceOn() is True, "Device should be on by default"
    print("✓ Device state test passed")

def test_card_read_success():
    print("\nTesting card read success...")
    ATMDevice.reset_states()
    ATMDevice.card_inserted = True
    success = ATMController._card_read_success()
    assert success is True, "Card read should succeed"
    print("✓ Card read success test passed")

def test_pin_verification():
    print("\nTesting PIN verification...")
    ATMDevice.reset_states()
    ATMDevice.card_inserted = True
    success = ATMController._enter_pin_success()
    assert success is True, "PIN verification should succeed"
    print("✓ PIN verification test passed")

def test_deposit_flow():
    print("\nTesting deposit flow...")
    ATMDevice.reset_states()
    success = ATMController._deposit(100, 0)
    assert success is True, "Deposit should succeed"
    print("✓ Deposit flow test passed")

def test_withdraw_flow():
    print("\nTesting withdraw flow...")
    ATMDevice.reset_states()
    success = ATMController._withdraw(100, 0)
    assert success is True, "Withdraw should succeed"
    print("✓ Withdraw flow test passed")

def run_all_tests():
    print("Starting ATM Controller Tests...")
    
    # Replace the real dependencies with mocks
    global BankSystemWrapper
    global UIControllerWrapper
    
    BankSystemWrapper = MockBankSystem()
    UIControllerWrapper = MockUIController()
    
    try:
        test_device_on()
        test_card_read_success()
        test_pin_verification()
        test_deposit_flow()
        test_withdraw_flow()
        print("\n✓ All tests passed successfully!")
        return 0
    except AssertionError as e:
        print(f"\n✗ Test failed: {str(e)}")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {str(e)}")
        return 1

if __name__ == '__main__':
    sys.exit(run_all_tests()) 