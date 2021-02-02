
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    guest_name = names_file.readlines()
    print(guest_name)


with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()
    for name in guest_name:
        stipped_name = name.strip()
        inv_letter = template.replace(PLACEHOLDER, stipped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stipped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(inv_letter)

