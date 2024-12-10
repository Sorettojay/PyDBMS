"""
Tokenizer.py
"""

def Tokenize(text):
    tokens = text.split() #Using split to parse text into tokens first
    temp = [] #Temp list that will be renamed to tokens

    #For loop to go through each tokenized word from the split text to check for special characters
    for word in tokens:
        #Accounting for special characters not attached to a word and "I"
        if len(word) == 1:
            temp.append(word)
        #Either special characters are found, or word is not a command and must be joined
        elif word.isupper() is False and len(word) > 1:
            unjoined_word = [] #List to hold unjoined words
            for char in word:
                #Character is a number or a special character
                if char.isalpha() is False:
                    #Character is a number
                    if char.isnumeric() is True:
                        unjoined_word.append(char)
                    #Character is a special character
                    else:
                        temp.append("".join(unjoined_word) + char) #Joining and appending word to temp list
                        unjoined_word = [] #resetting unjoined_word list so we don't get duplicate values
                #Character is a letter
                else:
                    if len(word) == word.index(char) + 1: #Final character in the word sequence
                        temp.append("".join(unjoined_word) + char)  # Joining and appending word to temp list
                        unjoined_word = []  # resetting unjoined_word list so we don't get duplicate values
                    else:
                        unjoined_word.append(char)
        #Word is a command and nothing else needs to be done
        else:
            temp.append(word)

    tokens = temp
    return tokens