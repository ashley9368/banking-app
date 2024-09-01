# Banking App
![Bank App Deployed](/images/banking-app-deployed.png)

This is a basic banking app that lets users create accounts, deposit money, withdraw money, and check their balance. The app is easy to use and is designed to help you manage your money.

The deployed project live link is [HERE](https://banking-app-python-d549d2afb12c.herokuapp.com/)

## Contents

- [Introduction](#introduction)
- [Project](#project)
  - [User goals:](#user-goals)
  - [Site owner goals](#site-owner-goals)
- [Pre development](#pre-development)
- [Development](#development)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Resources](#resources)
  - [Libraries](#libraries)
- [Testing](#testing)
- [Future Updates](#future-updates)  
- [Validation](#validation)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Branching the GitHub Repository using GitHub Desktop and Visual Studio Code](#branching-the-github-repository-using-github-desktop-and-visual-studio-code)
- [Bugs](#bugs)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

## Introduction

This banking app allows users to create an account by entering their name and a secure PIN. Once logged in, users can easily manage their finances by checking their account balance, depositing funds (up to a maximum of $500 at a time), and withdrawing money (up to $500 per transaction). All transactions are handled within the app, and account details are saved for future access. The app is designed to be user-friendly and provides basic banking functions to help users manage their money.

## Project 

The aim of this project is to:

- Provide a simple way for users to manage their finances through a user-friendly banking app.
- Limit the amount that can be deposited and withdrawn in each transaction to encourage responsible money management.
- Allow users to easily create and access their accounts with a username and PIN.
- Automatically save account details, so users can return to their account at any time without losing their data.
- Offer clear and straightforward options for checking balances, making deposits, and withdrawing funds, ensuring a smooth user experience.

### User goals:

Users should be able to quickly set up their account by entering a username and secure PIN, without any confusion.
Users want clear and easy-to-understand instructions on how to check their balance, deposit funds, and withdraw money within the app.
Users should be able to deposit up to $500 per transaction and withdraw up to $500 per transaction, with clear feedback on their actions.
Users want to easily view their account balance without hassle, providing them with up to date information on their finances.
Users expect their account information to be saved automatically so that they can access it later without losing any details.


### Site owner goals

Ensure the banking app is simple for users to navigate and clearly commented so it can be maintained or developed further with ease.
Design the app so that users receive clear instructions at each step, minimizing confusion and making a better user experience.


### Pre development
Before I started coding, I made a mental note of what the app should do, like creating accounts, deposits, and withdrawals. This helped me stay on track while building the app.

### Development

I began by setting up the basic parts of the banking app and adding options for users.

Next, I worked on letting users create accounts, making sure they used 4-digit PINs and followed username rules. As I added more features, I went back and updated this code to keep it clean and working well.

After that, I added the ability for users to deposit money into their accounts. I made sure the app could handle mistakes and set a $500 limit for deposits. I also revisited and improved this part of the code as I continued developing other features.

Then, I added the withdrawal feature, allowing users to take money out of their accounts. I included checks to prevent withdrawing more than what’s available and set a $500 limit. I had to go back and adjust this code to ensure it worked with the rest of the app.

I also worked on saving and loading account data using JSON files. This way, users could log in or create new accounts, and their information would be saved properly. I refined this code several times to make sure it was functional.

Finally, I cleaned up the entire codebase and added comments to make it easier to understand. I made sure everything was working correctly and was free of issues before finishing the project.

I didn’t write the code in a perfect, step-by-step order. Instead, I kept going back and changing different parts of the code as I added new features and made improvements.

## Features

Account creation and login:
Users can create a new bank account by entering a username up to 8 characters, and using only letters, setting a 4-digit PIN. Each account gets a unique ID automatically.

Users can access their existing accounts by entering their username and PIN. The app checks the PIN to make sure only the right person can log in.

![banking app account creation or login](/images/banking-app-deployed.png)

Check balance:
Users can see their current balance. The app shows both the account ID and the balance.

![check balance](/images/check-balance.png)

Deposit:
Users can add money to their account. They can deposit up to $500, and the app makes sure the input is correct before updating the balance.

![deposit](/images/deposit.png)

Withdraw:
Users can take money out of their account. Withdrawals are limited to $500, and users can only withdraw if they have enough money.

![withdraw](/images/withdraw.png)

Load and save account data:
The app saves user account details to a JSON file and loads it when they log in, so their data is safe and available later.

![load and save accoutn data](/images/load-account-and-save-data.png)

User interface:
The app provides clear menus and instructions, making it easy to navigate and use all the features.

![user interface](/images/user-interface.png)

## Technologies Used

The only technology i used to create this program is Python

### Resources

- Gitpod
- GitHub 
- Heroku

## Testing

The banking app has been tested and the results can be viewed [here - TESTING](https://github.com/ashley9368/banking-app/blob/main/TESTING.md)

## Future Updates

Transaction History:
In the future, I plan to add a transaction history feature so users can see a detailed record of all their deposits, withdrawals, and balance checks. This would make it easier for users to track their spending and manage their money better.

User Interface Improvements:
I want to improve the user interface by creating a more appealing look using Python. This would make the app look nicer.

Account Types and Services:
I would like to add different account types, like savings accounts, or business accounts. Each type would have its own features, like higher interest for savings accounts or special services for business accounts.

## Validation

PEP8 - I added an extension called flake 8 to validate my code - https://flake8.pycqa.org/en/latest/

All code has been reviewed, and lines longer than the recommended length have been adjusted where possible.

## Deployment

### Heroku
   
The deployed project link is [HERE](https://banking-app-python-d549d2afb12c.herokuapp.com/)

## Bugs

File Overwriting:
When saving account data, if two users pick the same username, the file from the first user will be replaced by the second user’s file. This means one user’s data could be lost.

PIN Validation:
The app doesn’t check if a PIN is already in use when creating a new account. So, multiple accounts can have the same PIN, which could be a problem.

Username Validation:
The app only checks if the username is made of letters and not too long. It doesn’t check for special characters or spaces, which could cause problems.


## Credits

![This video served as a helpful resource during my project](https://www.youtube.com/watch?v=8aW3tkIul-8)

![This cheat sheet was a handy reference during my project](https://images.datacamp.com/image/upload/v1694526244/Marketing/Blog/Python_Basics_Cheat_Sheet-updated.pdf)

![understanding json a little more](https://codeinstitute.net/blog/working-with-json-in-python/)

## Acknowledgements

I want to thank my mentor, Jubril Akolade, for his support and guidance throughout this project. His help was key for me to know which direction to go in.