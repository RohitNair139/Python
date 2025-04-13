def calculate_love_score(name1: str, name2: str) -> str:
    """
    Calculates a love score by counting the occurrences of the letters in "TRUE" and "LOVE"
    within the concatenated names. The final love score is produced by concatenating the
    count of letters in "TRUE" (first part) and the count of letters in "LOVE" (second part).

    Args:
        name1 (str): The first name.
        name2 (str): The second name.

    Returns:
        str: The love score as a string (e.g., "42").
    """
    # Combine and convert both names to uppercase
    combined_names = (name1 + name2).upper()
    
    # Count the letters for "TRUE"
    true_count = sum(combined_names.count(letter) for letter in "TRUE")
    
    # Count the letters for "LOVE"
    love_count = sum(combined_names.count(letter) for letter in "LOVE")
    
    # Combine the counts into a two-part score string
    love_score = f"{true_count}{love_count}"
    return love_score


def main():
    # Get input names from the user
    name1 = input("Enter your name: ")
    name2 = input("Enter the other person's name: ")
    
    # Calculate love score
    score = calculate_love_score(name1, name2)
    
    # Display the result
    print(f"Your love score is: {score}")


if __name__ == "__main__":
    main()
