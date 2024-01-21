"""Automated birthday party email sending"""
for name in open("Input/Names/invited_names.txt", "r"):
    name = name.strip()
    with open("Input/Letters/starting_letter.txt", "r") as letter:
        template = letter.read()
        template = template.replace("[name]", name)
        template = template.replace("Angela", "Chris!")
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as new_letter:
            new_letter.write(template)
