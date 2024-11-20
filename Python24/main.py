#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# pull invited names in to object
# open starting lettter. find Name and rplace 

import os
print(os.getcwd())

search_string = "[name]"

# Open the starting letter file and read its content
with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter_content = file.read()  # Read the entire content into a string

# Open the invited names file and read the names
with open("Input/Names/invited_names.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        replacement_name = line.strip()  # Remove any leading/trailing whitespace
        new_file_path = f'Output/ReadyToSend/{replacement_name}.txt'  # Ensure the file has a .txt extension

        # Replace the placeholder with the actual name
        new_letter = starting_letter_content.replace(search_string, replacement_name)

        # Write the new letter to a new file
        with open(new_file_path, "w") as new_file:
            new_file.write(new_letter)
        
    




        
