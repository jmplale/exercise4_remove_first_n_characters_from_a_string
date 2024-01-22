# make a def function:
def remove_chars(string, n):
    if n < 0:
        return "Invalid!"
    
    return string[n:]

word = "pynative"

# print an introduction outcome
print(f"The word is {word}")

# print the first example
print(remove_chars(word, 4))

# print the second example
print(remove_chars(word, 2))