def calc_words_count(data_path):
    with open(data_path, 'r') as data:
        words_count = len(data.read().split())
        print(words_count)

calc_words_count('homework-2/text_file.txt')