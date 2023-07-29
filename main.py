
with  open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()



for i in range(len(names)):
    name = (names[i]).strip()
    x = letter.replace("[name]", name)

    with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
        file.write(x)

    print(x)

