# ATM_Controller

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

