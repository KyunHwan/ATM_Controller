# ATM Controller

A simple ATM controller implementation that demonstrates the core functionality of an ATM system without UI integration.

## Project Structure

```
.
├── src/
│   └── atm_controller/
│       ├── controller/
│       │   └── atm_controller.py
│       └── future_integration_classes/
│           ├── atm_device.py
│           ├── bank/
│           │   └── bank_system.py
│           └── ui_controller.py
├── tests/
│   └── test_atm_controller.py
├── pyproject.toml
└── README.md
```

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd ATM_Controller
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

## Future Integration Points

The system is designed to be integrated with:
- Real bank systems
- ATM hardware (card reader, cash bin)
- User interface (console or GUI)

# Assumptions
1. Assume user does not take out the card once the card is in unless prompted.
2. Assume that the device will not be turned off.
3. Assume that the card is read correctly every time for now.
4. Assume that the card information exists in the bank system for now.
5. Bank pin number has to be 4 digits. Assume only single digits are possible to be input to the system.
6. Pin number is automatically submitted once 4 digits have been reached
7. Assume information retrieval always succeeds from the bank system
8. Assume that once bank system has checked the pin against the system, it remembers the user at the particular ATM device, until explicitly reset. This is to ensure that the user doesn't need to input their pin number again. 
9. Assume the user places the right amount of cash into the device. 
10. Assume there's no user whose action of withdrawing can make the balance for an account to go below 0.
11. Assume there's enough cash in the cash bin for every interaction
12. Assume that once an action (withdraw or deposit) has been made, the user does not need to do additional action, and therefore will retrieve their card.


## Test Structure

The test suite is implemented in `test_atm_controller.py` and covers:

1. Device state management
2. Card reading flow
3. PIN verification
4. Deposit and withdrawal operations

The tests use simple Python assertions and print statements to verify the behavior. External dependencies (bank system, UI) are replaced with simple mock classes.

## Running Tests

To run the tests:

```bash
python tests/test_atm_controller.py
```

Test Note:

When the test has reached "Testing PIN verification" section, press 4 numbers without Enter (This doesn't check whether the user has input characters or numbers since it's written in the assumption that the user will not have the option of pressing any other value other than a single digit number).
