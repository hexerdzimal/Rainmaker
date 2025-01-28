# Rainmaker

Welcome to the **Rainmaker**, a small Python tool designed to demonstrate how easily password combinations can be generated and evaluated. This tool shows how simple information, such as names, places, and dates, can be used to create massive amounts of potential password combinations that can be cracked easily using modern hashing techniques, building a
rainbowtable and a target specific dictionary at the same time.

Rainbow tables were once a widely used method to quickly reverse hash values into plaintext passwords using precomputed tables.
Although modern security techniques like salting have rendered rainbow tables less effective, the underlying issue remains: weak or predictable passwords.
Attackers often leverage OSINT (Open Source Intelligence) to gather personal information, such as pet names, birth dates, or the names of spouses,
making passwords based on such information easy to guess. Nowadays, attackers rely on alternative methods like dictionary attacks, credential stuffing,
or social engineering to obtain passwords. The key takeaway is that if a password can be guessed using OSINT, attackers don’t need advanced techniques.
The solution lies not only in technical safeguards, such as salting, but also in the use of strong, random passwords that do not rely on personal information. 

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
```bash
python rainmaker.py
```
### Enter your data:

The program will prompt you to enter names and associated dates. You can enter one name per line, followed by its associated dates (e.g., John: 15.01.1990, 03.07.1992).

### Choose an output format:

After generating combinations and calculating hashes, the program will ask you to select an output format. Choose from:
- 1: Tabular (plain text)
- 2: JSON
- 3: CSV

### View the results:

Once the program finishes, the results will be saved to a file (e.g., rainbow_table.txt, rainbow_table.json, or rainbow_table.csv) based on your choice.

## Example

Lets say you are to investigate a female (not blaming females, could do the same on any male) target and you found out following things via OSINT:

- Her husband is called Peter. Peter was born April 15th 1963 and they married May 20th 1998
- They have a son called Paul, born June 20th 2000 and a daugther Mary, born Dec 22nd 2004
- Your target and Peter first met in Italy Oct 25th 1982
- They have a cat, called Doggo for whatever sick reason and the cat joined the household at Aug 5th, 2015

To generate (not ALL but) 196384 possible password combinations the tool needed 4.83 seconds.
You can find the results in the json file in the repository.


![grafik](https://github.com/user-attachments/assets/a3ea3d5f-056d-4f25-bc72-e212af5b9702)



## Why is this important?

This program is a demonstration of how easy it is to generate password combinations based on simple personal data, such as names and dates. In real-world scenarios, many people choose passwords that are based on such information. Understanding how attackers can use tools like this to crack weak passwords is essential in securing sensitive information.
License

This program is licensed under the GNU General Public License version 3. See the LICENSE file for more details.

Feel free to contribute or use this tool for educational purposes. 
