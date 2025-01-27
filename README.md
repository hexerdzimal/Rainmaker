# Rainmaker

Welcome to the **Rainmaker**, a small Python tool designed to demonstrate how easily password combinations can be generated and evaluated. This tool shows how simple information, such as names, places, and dates, can be used to create massive amounts of potential password combinations that can be cracked easily using modern hashing techniques.

## Features

- **Input names and associated dates**: Allowing users to enter multiple dates per name, which the program combines into different patterns.
- **Combination generation**: Generates a large number of password combinations using various date patterns and separators.
- **Hash calculation**: Calculates SHA-256 hashes for all generated combinations.
- **Output formats**: Saves the results in multiple formats such as:
  - **Tabular**: Plain text with combinations and hashes aligned.
  - **JSON**: Easy-to-parse format for integration or further analysis.
  - **CSV**: Ideal for import into spreadsheet programs.
- **Progress bar**: Displays progress while generating and hashing combinations.
  
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hexerdzimal/Rainmaker.git
   ```

2. Navigate to the project folder:

    ```bash
    cd Rainmaker
    ```

3. Install the required Python dependencies (if any):

    You can create a virtual environment and install the dependencies by running:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

## Usage

### Run the program:

After navigating to the project folder, simply run the script:

python rainmaker.py

### Enter your data:

The program will prompt you to enter names and associated dates. You can enter one name per line, followed by its associated dates (e.g., John: 15.01.1990, 03.07.1992).

### Choose an output format:

After generating combinations and calculating hashes, the program will ask you to select an output format. Choose from:
- 1: Tabular (plain text)
- 2: JSON
- 3: CSV

### View the results:

Once the program finishes, the results will be saved to a file (e.g., rainbow_table.txt, rainbow_table.json, or rainbow_table.csv) based on your choice.

### Example

If you enter the following:

John: 15.01.1990, 03.07.1992
Anna: 22.03.1985

The program will generate combinations like:

    15-01-1990-John
    John-15-01-1990
    1990-01-15-Anna
    Anna-1990-15-01

Then, it will calculate the SHA-256 hashes for these combinations and save them to the specified output file.
Why is this important?

This program is a demonstration of how easy it is to generate password combinations based on simple personal data, such as names and dates. In real-world scenarios, many people choose passwords that are based on such information. Understanding how attackers can use tools like this to crack weak passwords is essential in securing sensitive information.
License

This program is licensed under the GNU General Public License version 3. See the LICENSE file for more details.

Feel free to contribute or use this tool for educational purposes. 
