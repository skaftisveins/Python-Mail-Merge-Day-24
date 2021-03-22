PLACEHOLDER = "[name]"

# Open invited_names.txt for reading
with open("input/names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

    # Open starting_letter.txt for reading
    with open("input/letters/starting_letter.txt", "r") as body_file:

        # Read the entire contents of the body
        contents = body_file.read()

        # Iterate over names
        for name in names:
            stripped_name = name.strip()
            new_letter = contents.replace(PLACEHOLDER, stripped_name)

            # write the letters to individual files
            with open(f"output/readytosend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)

# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    # Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
