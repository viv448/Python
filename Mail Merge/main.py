#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open("Input/Names/invited_names.txt", "r") as f:
    names = f.readlines()


with open("Input/Letters/starting_letter.txt") as data:
    letter_start = data.read()
    for name in names:
        name_use = name.strip()
        x = letter_start.replace("[name]", name_use)
        with open(f"Output/ReadyToSend/letter_for_{name_use}.txt", mode="w") as letter_completed:
            letter_completed.write(x)

