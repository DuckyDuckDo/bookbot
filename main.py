from stats import get_num_words, get_character_map, sort_character_map
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    PATH = sys.argv[1]
    word_count = get_num_words(PATH)
    char_map = sort_character_map(get_character_map(PATH))
    print(char_map)

    def generate_report(word_count, char_map, PATH):
        title_line = "=" * 12 + " " + "BOOKBOT" + " " + "=" * 12 + "\n" + f"Analyzing book found at {PATH}..."
        print(title_line)
        word_count_line = "-" * 11 + " " + "Word Count" + " " + "-" * 11 + "\n" + f"Found {word_count} total words"
        print(word_count_line)
        char_count_line = "-" * 10 + " " + "Character Count" + " " + "-" * 11
        print(char_count_line)

        for char in char_map:
            if char[0].isalpha():
                print(f"{char[0]}: {char[1]}")

        end_line = "=" * 12 + " " + "END" + " " + "=" * 12
        print(end_line)

    generate_report(word_count, char_map, PATH)

if __name__ == "__main__":
    main()