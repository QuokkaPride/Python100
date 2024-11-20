import pandas
dictionary= {}

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary
def nato():
    word = input("Enter your word you want to natoized:").upper()
    try:
        for (index, row) in alphabet_data_frame.iterrows():
            dictionary[row.letter] = row.code
        response = [dictionary[char] for char in word]
        print(response)

    except KeyError:
        print("enter only alphabetic characters")
        nato()

nato()