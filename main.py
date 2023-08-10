PLACEHOLDER = "[Recipient's Name]"

with open('names_list.txt', mode='w') as file:
    name = input('what is your name?\n')
    n = file.write(name)
with open('names_list.txt') as file:
    names = file.readlines()


with open('birthday.txt') as letter_file:
    letter = letter_file.read()
    for new_name in names:
        stripped_name = new_name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f'./Birthday/{stripped_name}.txt', mode='w') as card:
            card.write(new_letter)
