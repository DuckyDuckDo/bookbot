def get_num_words(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"{len(words)} words found in the document")

def get_character_map(path):
    with open(path) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        character_frequency = {}
        for character in file_contents:
            character_frequency[character] = character_frequency.get(character, 0) + 1
        print(character_frequency)