with open('books/frankenstein.txt', 'r') as file:
    text = file.read()


def character_dict(text):
    characters = {}
    text = text.lower().replace(' ', '').replace('\n', '')
    for char in text:
        if char not in characters:
            characters[char] = 0
        characters[char] += 1
    return characters


def sort_characters(characters_dict):
    characters = list(characters_dict.items())
    characters.sort(key=lambda x: x[1], reverse=True)
    return characters


characters_ordered = sort_characters(character_dict(text))

print('--- Begin report of books/frankenstein.txt ---')
print(f"{len(text.split())} words found in the document")

for char, count in characters_ordered:
    print(f"The '{char}' character was found {count} times")

print('--- End report ---')
