# Testing

After running the program, I proceeded to test it thoroughly to identify and handle any potential errors.

The deployed project live link is [HERE](https://banking-app-python-d549d2afb12c.herokuapp.com/) 


The following tests were carried out to ensure the portal is working correctly

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Welcome Screen | User is greeted and given options | Intro screen with options is presented | Works as expected |
| Username Input | User is asked to enter their username | Username is entered| Works as expected | 
| Username Input | User inputs a number, or long name | Error message appears | Works as expected | 
| PIN Input | User sets a 4-digit PIN | PIN is accepted | Works as expected | 
| PIN Input | User enters incorrect PIN format | Error message appears | Works as expected | 
| Account Creation | User creates a new account | Account created with unique ID | Works as expected |
| Load Account | User attempts to log in with correct details | Account loaded successfully | Works as expected |
| Load Account | User attempts to log in with incorrect PIN | Error message appears | Works as expected |
| Balance Check | User checks account balance | Correct balance is displayed | Works as expected |
| Deposit Funds  | User deposits a valid amount | Balance updated accordingly | Works as expected |
| Deposit Funds | User tries to deposit over the $500 limit | Error message appears | Works as expected |
| Withdraw Funds | User withdraws a valid amount | Balance updated accordingly | Works as expected |
| Withdraw Funds | User tries to withdraw more than available funds | Error message appears | Works as expected |
| Exit App | User chooses to exit the app | Account data saved, exit message displayed | Works as expected |

## Testing Browsers

- Chrome

It worked without issues.


### [BACK TO README](https://github.com/ashley9368/banking-app/blob/main/README.md)