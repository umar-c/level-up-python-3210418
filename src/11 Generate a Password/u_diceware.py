import secrets

def generate_passphrase(num_words, wordlist_file = 'diceware.wordlist.asc'):
    with open(wordlist_file, 'rt', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    # Choose 'num' random numbers to form the password
    words = [secrets.choice(word_list) for _ in range(num_words)]

    return ' '.join(words)

# commands used in solution video for reference
if __name__ == '__main__':
    print(generate_passphrase(7))
    print(generate_passphrase(10))