def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for i in string:
        if i not in vowels:
            result = result + i
    return result
# if i is not vowel then add it to result
print(remove_vowels("Hello, World!"))
  