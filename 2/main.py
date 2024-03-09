import pymorphy2
import re
import os


morph = pymorphy2.MorphAnalyzer()
words = []


def normalizer(word):
    return morph.parse(word)[0].normal_form


def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


delete_files_in_folder('tokens/')

file = open('stop_words.txt', 'r', encoding="utf-8")
stop_words = file.read()
stop_words = re.split(r'[\s\n]', stop_words)


if __name__ == '__main__':
    for i in range(0, 101):
        file = open(f'../1/pages/{i}.txt', 'r', encoding="utf-8")
        text = file.read()
        file.close()

        currency_words = ['']
        currency_index = 0
        for j in text:
            if re.fullmatch(r'\n', j):
                currency_index += 2
                currency_words.append('1')
                currency_words.append('')
            elif re.fullmatch(r'\s', j):
                currency_index += 2
                currency_words.append('2')
                currency_words.append('')
            elif j == '-':
                if re.fullmatch(r'\s', text[text.index(j) - 1]):
                    pass
                elif re.fullmatch(r'\s', text[text.index(j) + 1]):
                    currency_index += 1
                    currency_words.append('')
            else:
                currency_words[currency_index] += j

        # currency_words = re.split(r'-+\s+|\s+-+|\s+|\t|\n', text)

        page = open(f'tokens/{i}.txt', 'a', encoding="utf-8")

        for word in currency_words:
            if word:
                word = normalizer(word).lower()
                if word not in stop_words and word not in ['1', '2']:
                    page.write(f'{word}')
                if word == '1':
                    page.write('\n')
                if word == '2':
                    page.write(' ')

        page.close()
