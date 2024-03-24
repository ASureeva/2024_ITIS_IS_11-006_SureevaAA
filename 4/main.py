import re
import pandas as pd
import math


dictionary = {
    'in_file': {},
    'tf': {},
    'idf': {},
    'tf-idf': {},
}
words_len = {

}
# number of documents in the collection
n_of_document_in_coll = 101


for i in range(101):
    file = open(f'../2/tokens/{i}.txt', 'r',  encoding="utf-8")
    words = file.read()
    words = re.split(r'[\s\n]', words)
    while '' in words:
        words.remove('')
    word_count = 0
    words_len[i] = len(words)
    for word in words:
        if word:
            if word in dictionary['in_file']:
                if i not in dictionary['in_file'][word]:
                    dictionary['tf'][word][i] = 1
                    dictionary['in_file'][word].append(i)
                else:
                    dictionary['tf'][word][i] += 1
            else:
                dictionary['in_file'][word] = [i]
                dictionary['tf'][word] = [0 for j in range(101)]
                dictionary['tf'][word][i] += 1
    file.close()


sorted_dict_in_file = dict(sorted(dictionary['in_file'].items()))
sorted_dict_tf = dict(sorted(dictionary['tf'].items()))


def get_tf():
    data = {}
    for i in range(101):
        data[f'Document № {i}'] = [round(key[1][i] / words_len[i], 5) for key in sorted_dict_tf.items()]
    df = pd.DataFrame(data)
    df.insert(0, "Word", [key[0] for key in sorted_dict_tf.items()], True)
    df.to_excel('./tf.xlsx')


def get_idf():
    data = {"Word": [key[0] for key in sorted_dict_tf.items()],
            "Idf": [round(math.log(n_of_document_in_coll / len(key[0])), 5) for key in sorted_dict_in_file.items()]}
    df = pd.DataFrame(data)
    df.to_excel('./idf.xlsx')


def get_tf_idf():
    data = {}
    for i in range(101):
        data[f'Document № {i}'] = [round((key[1][i] / words_len[i]) * math.log(n_of_document_in_coll / len(key[0])), 5) for key in sorted_dict_tf.items()]
    df = pd.DataFrame(data)
    df.insert(0, "Word", [key[0] for key in sorted_dict_tf.items()], True)
    df.to_excel('./tf_idf.xlsx')


for key in dict(sorted(dictionary['in_file'].items())):
    file = open('dictionary.txt', 'a',  encoding="utf-8")
    file.write(f"{key}: {dictionary['in_file'][key]}\n")
file.close()


if __name__ == '__main__':
    get_tf()
    get_idf()
    get_tf_idf()
