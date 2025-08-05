
def duplicate_count(text):
    letters = {}
    for char in text:
        letters[char] = letters.get(char, 0) + 1
        if letters[char] > 0:
            letters[count] = letters.get(count, 0) + 1


        if letters[count] == 0:
            return 'no characters repeats more than once'
        elif letters[count] > 0:
            return f"{letters[char]} and {letters[char]}"
#result = duplicate_count("abcde")
#result = duplicate_count("aabbcde" )
print(result)