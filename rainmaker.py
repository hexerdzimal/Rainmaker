    #Rainmaker. A small tool to demonstrate how easy PW combinations can be evaluated
    #Copyright (C) 2025  Matthias Ferstl (mail@matthias-ferstl.de)

    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <https://www.gnu.org/licenses/>


import hashlib
from time import time
from itertools import product


# Function to display a greeting message
def greeting():
    print("""
           
            ██████╗  █████╗ ██╗███╗   ██╗███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗ 
            ██╔══██╗██╔══██╗██║████╗  ██║████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
            ██████╔╝███████║██║██╔██╗ ██║██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝
            ██╔══██╗██╔══██║██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
            ██║  ██║██║  ██║██║██║ ╚████║██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║
            ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

            """)
    print("""
                    *******************************************************
                    *                                                     *
                    *            Welcome to the Rain(bow Table )Maker!    *
                    *            A tool to demonstrate password           *
                    *            combinations from names and dates.       *
                    *                                                     *
                    *******************************************************
            """)
    print("""
    This program generates hash values from names and flexible date combinations.
    It is designed to show how easily massive password combinations can be created
    by using simple information like names, places, and dates — often found through 
    OSINT on social media profiles.
          
    You can use it in security training. Use it to understand and show how easy it
    is to crack weak passwords, especially when people use predictable information
    like important dates or names for their passwords.
    ---------------------------------------------------------------
    """)


# Function to input names and their associated dates
def input_names_and_dates():
    """
    Prompts the user to input names and associated dates in the format:
    Name1: Date1, Date2
    Name2: Date3, Date4
    Returns a dictionary with names as keys and lists of dates as values.
    """
    print("\nPlease enter names (persons, places...etc) and their associated dates \n(e.g., Anna: 10.04.1963, 15.07.1985 or Sorbonne University: 16.08.2001):\n")
    print("Enter one name per line. Leave an empty line to finish.")
    
    data = {}
    while True:
        line = input("Entry: ").strip()
        if not line:
            break  # End input on empty line
        try:
            name, dates = line.split(":")
            data[name.strip()] = [date.strip() for date in dates.split(",")]
        except ValueError:
            print("Invalid format. Use: Name: Date1, Date2")
    
    return data


# Function to split a date into its components
def split_date(date):
    """
    Splits a date in the format DD.MM.YYYY into day, month, and year.
    Returns None for invalid dates.
    """
    try:
        day, month, year = date.split(".")
        return day, month, year
    except ValueError:
        print(f"Error: Invalid date format '{date}'. Expected format: DD.MM.YYYY")
        return None, None, None


# Function to generate combinations of names, date components, and separators
def generate_combinations(name_date_dict):
    """
    Generates combinations of names, date components, and variations using various patterns.
    Includes separators, leetspeak substitutions, and capitalization variations.
    """
    separators = ["", "-", ".", "_", "@", "#", "!", "*"]  # Different separators for flexibility
    combinations = []

    leet_map = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "$"}
    def apply_leetspeak(name):
        """
        Applies leetspeak substitutions to a name.
        Returns a list of variations with substitutions.
        """
        variations = [name]
        for char, substitute in leet_map.items():
            if char in name.lower():
                variations.append(name.lower().replace(char, substitute))
        return variations

    def capitalize_variations(name):
        """
        Generates capitalization variations for a given name.
        """
        return [name.lower(), name.upper(), name.capitalize()]

    for name, dates in name_date_dict.items():
        # Generate leetspeak and capitalization variations for the name
        name_variations = apply_leetspeak(name)
        name_variations += [variant for variation in name_variations for variant in capitalize_variations(variation)]

        for date in dates:
            day, month, year = split_date(date)
            if not day or not month or not year:
                continue  # Skip invalid dates

            # Generate combinations with all date components and name variations
            for sep1, sep2, sep3 in product(separators, repeat=3):
                for name_variant in name_variations:
                    combinations.append(f"{day}{sep1}{month}{sep2}{year}{sep3}{name_variant}")  # e.g., 15-07-2023-Anna
                    combinations.append(f"{day}{sep1}{year}{sep2}{month}{sep3}{name_variant}")  # e.g., 15-2023-07-Anna
                    combinations.append(f"{month}{sep1}{day}{sep2}{year}{sep3}{name_variant}")  # e.g., 07-15-2023-Anna
                    combinations.append(f"{month}{sep1}{year}{sep2}{day}{sep3}{name_variant}")  # e.g., 07-2023-15-Anna
                    combinations.append(f"{year}{sep1}{day}{sep2}{month}{sep3}{name_variant}")  # e.g., 2023-15-07-Anna
                    combinations.append(f"{year}{sep1}{month}{sep2}{day}{sep3}{name_variant}")  # e.g., 2023-07-15-Anna
                    combinations.append(f"{name_variant}{sep1}{day}{sep2}{month}{sep3}{year}")  # e.g., Anna-15-07-2023
                    combinations.append(f"{name_variant}{sep1}{month}{sep2}{year}{sep3}{day}")  # e.g., Anna-07-2023-15
                    combinations.append(f"{name_variant}{sep1}{year}{sep2}{day}{sep3}{month}")  # e.g., Anna-2023-15-07

            # Generate combinations with partial date components
            for sep1, sep2 in product(separators, repeat=2):
                for name_variant in name_variations:
                    combinations.append(f"{day}{sep1}{month}{sep2}{name_variant}")  # e.g., 15-07-Anna
                    combinations.append(f"{day}{sep1}{year}{sep2}{name_variant}")  # e.g., 15-2023-Anna
                    combinations.append(f"{month}{sep1}{day}{sep2}{name_variant}")  # e.g., 07-15-Anna
                    combinations.append(f"{month}{sep1}{year}{sep2}{name_variant}")  # e.g., 07-2023-Anna
                    combinations.append(f"{year}{sep1}{day}{sep2}{name_variant}")  # e.g., 2023-15-Anna
                    combinations.append(f"{year}{sep1}{month}{sep2}{name_variant}")  # e.g., 2023-07-Anna
                    combinations.append(f"{name_variant}{sep1}{day}{sep2}{month}")  # e.g., Anna-15-07
                    combinations.append(f"{name_variant}{sep1}{month}{sep2}{year}")  # e.g., Anna-07-2023
                    combinations.append(f"{name_variant}{sep1}{year}")  # e.g., Anna-2023
                    combinations.append(f"{year}{sep1}{name_variant}")  # e.g., 2023-Anna

            # Generate combinations with single date components
            for sep1 in separators:
                for name_variant in name_variations:
                    combinations.append(f"{day}{sep1}{name_variant}")  # e.g., 15-Anna
                    combinations.append(f"{month}{sep1}{name_variant}")  # e.g., 07-Anna
                    combinations.append(f"{year}{sep1}{name_variant}")  # e.g., 2023-Anna
                    combinations.append(f"{name_variant}{sep1}{day}")  # e.g., Anna-15
                    combinations.append(f"{name_variant}{sep1}{month}")  # e.g., Anna-07
                    combinations.append(f"{name_variant}{sep1}{year}")  # e.g., Anna-2023   

    # Remove duplicates (to be sure ) by converting to a set and back to a list
    return list(set(combinations))


# Function to calculate the SHA-256 hash of a plaintext string
def calculate_hash(plaintext):
    """
    Calculates the SHA-256 hash for a given plaintext.
    """
    h = hashlib.sha256()
    h.update(plaintext.encode("utf-8"))  # Convert plaintext to bytes and hash it
    return h.hexdigest()


# Function to display a progress bar in the console
def display_progress(progress, total):
    """
    Displays a progress bar in the console.
    """
    percent = int((progress / total) * 100)  # Calculate percentage completed
    bar = f"[{'#' * (percent // 5)}{' ' * (20 - percent // 5)}]"  # Create a 20-character progress bar
    print(f"\r{bar} {percent}% complete", end="")


# Function to save combinations and their hashes to a file
def save_to_file(combinations, hashes, filename="rainbow_table"):
    """
    Saves the generated combinations and their hash values to a file.
    User can select the output format: Tabular, JSON, or CSV.
    """
    print("\nChoose output format:")
    print("1: Tabular (plain text)")
    print("2: JSON")
    print("3: CSV")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        filename += ".txt"
        with open(filename, "w") as f:
            # Write header
            f.write(f"{'Combination':<40} | {'Hash':<64}\n")
            f.write("-" * 105 + "\n")
            for plaintext, hash_value in zip(combinations, hashes):
                f.write(f"{plaintext:<40} | {hash_value:<64}\n")
    elif choice == "2":
        filename += ".json"
        import json
        data = [{"combination": plaintext, "hash": hash_value} for plaintext, hash_value in zip(combinations, hashes)]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    elif choice == "3":
        filename += ".csv"
        with open(filename, "w") as f:
            f.write("Combination,Hash\n")
            for plaintext, hash_value in zip(combinations, hashes):
                f.write(f"{plaintext},{hash_value}\n")
    else:
        print("Invalid choice. Saving as default tabular format.")
        filename += ".txt"
        with open(filename, "w") as f:
            # Write header
            f.write(f"{'Combination':<40} | {'Hash':<64}\n")
            f.write("-" * 105 + "\n")
            for plaintext, hash_value in zip(combinations, hashes):
                f.write(f"{plaintext:<40} | {hash_value:<64}\n")

    print(f"Results have been saved to '{filename}'.")

# Main function to execute the program
def main():
    greeting()  # Show greeting message

    # User input for names and dates
    name_date_dict = input_names_and_dates()

    # Generate combinations
    print("\nGenerating combinations...")
    combinations = generate_combinations(name_date_dict)

    if not combinations:
        print("No combinations created. Exiting the program.")
        return

    print(f"\n{len(combinations)} combinations were generated.")

    # Calculate hashes with progress bar
    print("\nCalculating hashes...")
    start_time = time()  # Record start time
    hashes = []
    total = len(combinations)
    for i, combination in enumerate(combinations, start=1):
        hashes.append(calculate_hash(combination))
        display_progress(i, total)  # Update progress bar

    elapsed_time = time() - start_time  # Calculate elapsed time

    # Display summary
    print(f"\n\n{len(combinations)} combinations and {len(hashes)} hashes were created in {elapsed_time:.2f} seconds.")

    # Display the first 10 results for preview
    print("\nResults (first 10 entries):")
    for plaintext, hash_value in list(zip(combinations, hashes))[:10]:
        print(f"{plaintext} -> {hash_value}")

    # Save results to a file
    save_to_file(combinations, hashes)


# Entry point of the program
if __name__ == "__main__":
    main()
