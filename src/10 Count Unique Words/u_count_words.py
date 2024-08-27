from collections import Counter
import re

def count_words(file):
    if file is None or "".__eq__(file.strip()):
        print("No input file has been provided! Exiting...")
        return
    
    with open(file, 'rt') as f:
        word_file = f.read()

    word_list = re.findall(r"[a-z0-9'-]+", word_file.lower())
    print(f'\nTotal Words: {len(word_list)}')

    word_counter = Counter(word_list)
    
    # print('\nWord\t\t  Count')
    # for word, count in word_counter.items():
    #     print(f"{word:20s}\t{count:5d}")

    print('\nTop 20 most occuring owrds:\n')
    for word, count in word_counter.most_common(20):
        print(f"{word:6s}\t{count:5d}")

# commands used in solution video for reference
if __name__ == '__main__':
    count_words('shakespeare.txt')