#Count the number of vowels in a string.
def count_vowels(string):
    vowel = "aeiouAEIOU"
    temp = set()
    
    for char in string:
        if char in vowel:
           temp.add(char.lower()) 
    return len(temp)
string = input("Enter the String: ")
print(count_vowels(string))
