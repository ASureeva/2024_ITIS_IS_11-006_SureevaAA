import re


unic_words = []
dictionary = {}


def intersection(list1, list2):
    temp = set(list2)
    list3 = [value for value in list1 if value in temp]
    return list3


def disintersection(list2):
    list1 = list(range(0, 101))
    temp = set(list2)
    list3 = [value for value in list1 if value not in temp]
    return list3


for i in range(101):
    file = open(f'../2/tokens/{i}.txt', 'r',  encoding="utf-8")
    words = file.read()
    words = re.split(r'[\s\n]', words)
    while '' in words:
        words.remove('')
    unic_words.append(set(words))
    # print(len(words), len(unic_words[i]))
    for word in list(unic_words[i]):
        if word != " ":
            if word in dictionary:
                dictionary[word].append(i)
            else:
                dictionary[word] = [i]
    file.close()

file = open('dictionary.txt', 'w',  encoding="utf-8")
file.write('')
file.close()

for key in dict(sorted(dictionary.items())):
    file = open('dictionary.txt', 'a',  encoding="utf-8")
    file.write(f"{key}: {dictionary[key]}\n")
file.close()

# str = 'колодезный | альпийский & ! материал | успешно'


def main_(str):
    str = str.split(' ')
    answer = str

    for i, element in enumerate(answer):
        if element not in ['|', '&', '!']:
            answer[i] = dictionary[answer[i]]

    while '!' in answer:
        index = answer.index('!') + 1
        answer[index] = disintersection(answer[index])
        answer.remove('!')

    while '&' in answer:
        index = answer.index('&') + 1
        answer[index] = intersection(answer[index - 2], answer[index])
        answer.remove('&')
        answer.pop(index-2)

    while '|' in answer:
        index = answer.index('|') + 1
        answer[index] = list(set(answer[index - 2] + answer[index]))
        answer.remove('|')
        answer.pop(index-2)

    return str


if __name__ == '__main__':
    strings = ['колодезный & альпийский | материал', 'колодезный | альпийский | материал',
               'колодезный & альпийский & материал', 'колодезный & ! альпийский | ! материал',
               'колодезный | ! альпийский | ! материал']
    for string in strings:
        print(main_(string))
