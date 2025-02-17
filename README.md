# Page Object Model Framework for Website Testing

This repository contains a Page Object Model (POM) framework for testing the website https://www.qa-practice.com/. It is built using Python, Selenium, and pytest to provide a structured and maintainable approach to automate the testing of web applications.

Requirements
To use this framework, you'll need to have the following dependencies installed:

- Python 3.x
- Selenium
- pytest
- webdriver-manager
- dotenv
- httpx

Install the required dependencies using the following:

~~~bash
pip install -r requirements.txt
~~~


## Base Classes
The framework uses base classes for different types of elements, such as buttons, inputs, checkboxes, select elements, and textareas. These base classes handle common interactions for each type of element, reducing redundancy in the code.

- Buttons: `BaseButtonPage` handles common button interactions like clicking the button. Locators for buttons are stored in data classes for easy reuse.
- Inputs: `BaseInputPage` manages interaction with input fields. It simplifies actions like entering text into text boxes.
- Checkboxes: `BaseCheckboxPage` provides methods to interact with checkbox elements (e.g., selecting or deselecting them).


## Data Classes
Data classes are used to group locators for various elements on the page. For example, BaseButtonPageLocator groups all button locators into a single, immutable object. This approach:

- Keeps related locators organized and easy to reference.
- Reduces boilerplate code by automatically generating __init__() and __repr__() methods.
- Ensures immutability, preventing accidental changes to the locators.

## Fixtures
`options`
provides the Chrome browser options, including running in headless mode.

`service`
instantiates the ChromeDriver service using webdriver-manager.

`browser`
sets up a Chrome browser instance with the specified options and service. The browser is closed after each test function.

## Utility Functions

`TelegramClient` - This class sends the test results to a Telegram chat. It uses the Telegram Bot API to send a message with the total number of tests, failed tests, and their statuses.

- Notification after testing: The `TelegramClient` sends a message with the results at the end of the test session. The message includes:
    - Total number of tests executed
    - Number of failed tests
    - Overall status (successful or failed)
    - A link to the detailed report (will be updated)

You can configure the bot by setting up the .env file with your Telegram bot token and chat ID.

## Running the Tests
To run the tests using pytest, use the following command:

~~~bash
pytest -s -v tests/
~~~

This will execute all tests and provide output in the terminal. If the TelegramClient is configured, you will receive a message with the results in your Telegram chat.

## Environment Variables
You need to create a .env file in the root of the project with the following values:

~~~env
BOT_TOKEN=your-telegram-bot-token
CHAT_ID=your-chat-id
~~~

## Notes
- The framework is designed to be flexible and extensible. You can add new page objects or helper functions as needed.
- The framework is currently configured for testing the https://www.qa-practice.com/ website, but you can modify the URLs and locators to suit your application.
