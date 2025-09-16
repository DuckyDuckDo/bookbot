def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

def get_character_map(path):
    with open(path) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        character_frequency = {}
        for character in file_contents:
            character_frequency[character] = character_frequency.get(character, 0) + 1
        return character_frequency

def sort_character_map(character_map):
    char_map = sorted(character_map.items(), key = lambda item: item[1], reverse = True)
    return char_map