import numpy
import math
import pandas as pd


dictionary = []


with open(f'../4/dictionary.txt', encoding="utf-8") as file:
    for line in file:
        line_ = line.split(' ')
        dictionary.append(line_[0][:-1])


def get_vector(words):
    vector = [0 for _ in range(len(dictionary))]
    for word in words:
        vector[dictionary.index(word)] = 1
    return vector


def get_cosine_similarity(vec):
    result = {}
    for i in range(len(tf_idf[0])-2):
        l = numpy.dot(vec, tf_idf[:, i+2])
        k = (math.sqrt(sum(map(lambda x: x**2, vec)))*math.sqrt(numpy.sum(tf_idf[:, i+2]**2)))
        cosine_similarity = l/k
        if cosine_similarity:
            result[i] = round(cosine_similarity, 5)
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


queries = ['царь', 'великий', 'объединить',
           'царь великий',
           'царь великий объединить']

vectors = []
answer = {}
tf_idf = pd.read_excel('../4/tf_idf.xlsx')
tf_idf = tf_idf.to_numpy()

for index, query in enumerate(queries):
    vectors.append(get_vector(query.split(' ')))
    answer[query] = get_cosine_similarity(vectors[index])

print(answer)
file = open('answer.txt', 'w', encoding="utf-8")
for key, value in answer.items():
    file.write(f"{key}\n{value}\n")
