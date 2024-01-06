def generate_words(alphabet, regex, num_words):
    def match_pattern(pattern, text):
        if not pattern:
            return True
        if not text:
            return False

        char, *rest = pattern

        if char == text[0]:
            return match_pattern(rest, text[1:])
        elif char == '*':
            return (
                    match_pattern(rest, text) or
                    match_pattern(pattern, text[1:])
            )
        else:
            return False

    words = []
    for i in range(1, num_words + 1):
        word = alphabet[0] * i
        if match_pattern(regex, word):
            words.append(word)

    return words


def is_word_in_language(word, language):
    return word in language


if __name__ == "__main__":
    alphabet = input("Enter the alphabet S (e.g., a,b, separated by commas): ").split(',')
    regex = input("Enter the regular expression: ")
    num_words = int(input("How many words of the L language do you want to see? "))

    words_in_language = generate_words(alphabet, regex, num_words)

    print("\nThe regular expression can be generated from the S alphabet. Your words are listed:")
    print(f"L = {{{', '.join(words_in_language)}}}")

    bonus_word = input("BONUS: Enter a word to check if it belongs to the L language: ")

    if is_word_in_language(bonus_word, words_in_language):
        print(f"This word '{bonus_word}' belongs to the L language.")
    else:
        print(f"This word '{bonus_word}' does not belong to the L language.")
