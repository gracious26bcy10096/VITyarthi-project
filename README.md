# VITyarthi Project: Currency Converter CLI

A lightweight, command-line interface (CLI) tool written in Python that allows users to seamlessly convert amounts between 30 different global currencies using fixed exchange rates.

## Prerequisites

* **Python & IDLE:** Ensure Python 3.6+ is installed on your system.

  * You can download it from the official website: [python.org/downloads](https://www.python.org/downloads/?utm_source=gemini).

  * **CRITICAL FOR CMD:** When installing Python, make sure to check the box at the bottom of the installer that says **"Add Python to PATH"**. This is required to run the program from your Command Prompt.

  * The standard installation also includes Python IDLE, which you can use if you ever want to view or edit the script's source code.

* **Git:** Required to download the project repository to your local machine.

### Installing Git

* **Windows:** Download the official installer from [git-scm.com/download/win](https://git-scm.com/download/win?utm_source=gemini) and follow the setup wizard, or open Command Prompt and run `winget install --id Git.Git -e --source winget`.

* **macOS:** Download the installer from [git-scm.com/download/mac](https://git-scm.com/download/mac?utm_source=gemini), or open Terminal and install via Homebrew by running `brew install git`.

* **Linux (Ubuntu/Debian):** Open Terminal and execute `sudo apt update` followed by `sudo apt install git`.

## Setup and Installation

1. Open your Command Prompt (Windows) or Terminal (macOS/Linux).

2. Clone the repository to your local machine:

   ```
   git clone https://github.com/gracious26bcy10096/VITyarthi-project.git
   
   ```

3. Navigate into the cloned project directory:

   ```
   cd VITyarthi-project
   
   ```

## Execution

1. Verify you are in the project folder containing the Python script.

2. Launch the application by executing the following command in your Command Prompt/Terminal:

   ```
   python "currency converter.py"
   
   ```

*(Note: Depending on your system configuration, you may need to use `python3 "currency converter.py"` if `python` defaults to an older version.)*

## Usage Instructions

1. Upon running the script, type `1` at the main menu and press **Enter** to start a new conversion.

2. Review the printed table of 30 available currency codes (e.g., USD, EUR, INR).

3. Enter the 3-letter code of the currency you currently have and press **Enter**.

4. Enter the 3-letter code of the target currency you want and press **Enter**.

5. Input the integer amount you wish to convert and press **Enter**.

6. The terminal will calculate and display the final converted amount, rounded to two decimal places.

7. Type `2` at the main menu and press **Enter** to safely exit the program.
