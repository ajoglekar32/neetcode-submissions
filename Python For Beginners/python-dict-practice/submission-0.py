from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    string_mappings = {}
    for char in word:
        if(char in string_mappings):
            string_mappings[char] += 1
        else:
            string_mappings[char] = 1
    return string_mappings


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
