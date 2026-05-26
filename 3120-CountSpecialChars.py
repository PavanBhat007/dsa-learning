"""
3120. Count the Number of Special Characters I [Easy]

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word.
"""

#-------------------------------------------------------------------------------------------------------------------------

def count_special_chars(string):
    visited = set() # set to store unique visited chars
    special_chars = [] # to store already processed special chars and avoid repetition
    special = 0 # return value

    for char in string:
        if (char.lower() in special_chars) or (char.upper() in special_chars):
            continue # skip already processed chars
        
        if char.islower() and char.upper() in visited:
            special_chars.append(char)
            special += 1
            visited.remove(char.upper())
        elif char.isupper() and char.lower() in visited:
            special_chars.append(char)
            special += 1
            visited.remove(char.lower())
        else:
            visited.add(char)

    return special


if __name__ == "__main__":
    str_len = int(input("STRING LENGTH: "))
    string = input("STRING: ")

    special_char_count = count_special_chars(string)
    print(f"SPECIAL CHAR COUNT: {special_char_count}")