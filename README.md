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

## This is wrong!

Do you think it’s wrong to publish a tool like this, knowing it could enable bad people to do bad things?

When I first started learning about IT security, I quickly realized how little I actually knew. Who could have explained these things to me? Nobody. Reading about them or watching videos online or on television is like a drop of water in the desert—nice to have, but nowhere near enough.

I started experimenting with things just to understand them, and I was often shocked at how easy it is to exploit vulnerabilities and how naive people can be.

As a former martial arts trainee (Wing Tsun), I know that the best fight is the one you can avoid. And you can avoid most fights when you know how to stand your ground and protect yourself. A good martial arts trainer, especially in far-eastern traditions, teaches students not to harm others but to use their knowledge to do good, like protecting themselves and others.

If someone wants to harm others, they will find a way—regardless of who their trainer is or even if they have no trainer at all.

Now, let’s apply this principle to IT security.
If someone is truly determined to crack your passwords, they will find a way. And this tool? It’s not that powerful. There are tools out there that outperform it by far.

But you and I can use this tool to demonstrate how dangerous it is to rely on passwords that (or parts of it) can be easily discovered via OSINT (Open Source Intelligence). We can show people that tools like this can generate over 100,000 combinations of names and dates in under five seconds. We can open people’s eyes. We can help them protect themselves by revealing the “dark side.”

I’m not a fan of the phrase, “Weapons don’t kill people; people kill people,” but I have to admit, there’s truth in it. Long before guns were invented, people were stabbing each other with swords. Long before swords, they were smashing heads with stones. People will always find ways to harm each other.

But there are also those who choose to use their skills and knowledge to help others—those who show people how the “bad guys” operate so they can defend themselves.
So maybe you want to join me and show people what bad people do. Maybe you want to join me in teaching IT security. If you want to contribute, text me!

I hope you will use this tool wisely.
Thanks for reading

– Mat



