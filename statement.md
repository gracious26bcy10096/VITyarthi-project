## Problem Statement
Individuals and professionals often need a quick, accessible method to calculate currency exchange rates without relying on complex financial software or web browsers. There is a need for a lightweight, reliable, and straightforward tool that provides instant currency conversion estimates directly from the command line, bypassing the friction of heavy graphical user interfaces or internet-dependent applications. 

## Scope of the Project
This project revolves around a Python script named "currency converter.py". The application is a terminal-based program designed to calculate conversions between 30 specific fiat currencies using a predefined, static set of exchange rates. The scope includes reading user input for currency codes and amounts, performing the mathematical conversion, and outputting the result. It operates in a continuous loop until the user explicitly chooses to exit. The scope strictly excludes real-time API integrations, live market data updates, and graphical user interfaces.

## Target Users
* **Travelers and Expatriates:** Individuals needing quick, offline estimates of currency values while budgeting or managing expenses.
* **Command-Line Users:** Developers and tech-savvy users who prefer using terminal-based utilities for rapid, localized calculations.
* **Students and Educators:** Beginners in computer science who can use this script as a straightforward example of input handling, list indexing, and basic program looping. 

## High-Level Features
* **Extensive Currency Library:** Supports conversions across 30 international currencies, including major ones like USD, EUR, GBP, INR, and JPY.
* **Interactive Terminal Menu:** Features a continuous prompt allowing users to choose between making a new entry or exiting the program gracefully.
* **Reference Table Display:** Automatically outputs a formatted grid of all available currency codes before prompting the user, ensuring they know the valid inputs.
* **Input Validation & Error Handling:** Automatically converts user inputs to uppercase to prevent case-sensitivity issues and verifies that both the source and target currencies exist in the system, providing specific error messages if they do not.
* **Precision Calculation:** Executes a two-step conversion process (base division followed by target multiplication) and automatically rounds the final output to two decimal places for standard financial formatting.