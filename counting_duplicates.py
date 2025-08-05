from itertools import count


def duplicate_count(text):



    for item in text:
        letters = {'char': '', 'count': 0}

        if letters['count'] == 0:
            letters['char'] += item
            letters['count'] += 1
            return 'no characters repeats more than once'
        elif letters['count'] > 0:
            return f"{letters['char']} and {letters['char']}"
result = duplicate_count("abcde")
print(result)