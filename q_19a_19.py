import string
string = input("Enter a string: ")
translator = str.maketrans('', '', string.punctuation)
string_without_punctuation = string.translate(translator)
print("String without punctuation:", string_without_punctuation)
