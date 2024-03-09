import requests
import re
from urllib.parse import urlparse, urljoin, unquote
from bs4 import BeautifulSoup, UnicodeDammit
import os


currency_links = []


def delete_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f'Ошибка при удалении файла {file_path}. {e}')


def get_links(url, index, l, h_url):
    try:
        r = requests.get(url, timeout=2.5)
    except requests.exceptions.Timeout:
        print("Timeout occurred")
        return [0]
    except:
        print('oops')
        return [0]


    try:
        if r.headers['content-type'][:9] == 'text/html':
            r.encoding = r.apparent_encoding
    except:
        print('oops', r.headers)
        return [0]

        # print(r.text)
    soup = BeautifulSoup(r.text, features="html.parser")

    links = []
    for a in soup.find_all('a'):
        link = a.get("href")
        link = urljoin(url, link)
        parsed_href = urlparse(link)

        link = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        links.append(link)

    # links = re.findall(fr'{h_url}/.[^"]+(?:"|</|s)', r.text)
    # links[:] = [f'{URL}{link[len(h_url):]}' for link in links]
    # links.extend(re.findall(r'https://.[^"]+(?:"|</|s)', r.text))
    #
    # links[:] = [link for link in links if links not in currency_links and link not in l]

    text = soup.get_text(separator=' ')

    text_for_check = re.sub(r'[а-яА-ЯёЁ-]', '', text)
    text_of_page = re.sub(r'([^а-яА-ЯёЁ-])', ' ', text)
    text_in_pages = re.sub(r'\s\s+', '\n', text_of_page)

    ru = len(text_for_check) / len(text_in_pages)

    words = re.split(r'-+\s+|\s+-+|\s+|\t|\n', text_of_page)

    while ' ' in words:
        words.remove(' ')

    while '-' in words:
        words.remove('-')

    word_length = len(words)
    # print(word_length, url, words)

    if word_length > 999 and r.url not in currency_links and url not in currency_links and ru <= 1:
        file = open('index.txt', 'a', encoding="utf-8")
        file.write(f"{index} {unquote(url)} {word_length}\n")
        file.close()
        print(index)
        currency_links.extend([r.url, url])
        page = open(f'pages/{index}.txt', 'w', encoding="utf-8")
        page.write(text_in_pages)
        page.close()
        index += 1
        return index, links

    currency_links.extend([r.url, url])

    return [0]


delete_files_in_folder('pages/')

URL_default = 'https://minecraft.fandom.com/ru'
# URL = 'https://ru.wikipedia.org/wiki'https://habr.com/ru/feed/


def create_home_url(URL):
    home_url = []
    for url in URL:
        home_url.append(url[url.rfind('/'):])
    return home_url


links_to_site = []
link_other = []
site_index = 0


file = open('index.txt', 'w', encoding="utf-8")
file.write(f"index link words\n")
file.close()


if __name__ == '__main__':
    URL = []
    counter = True
    print('укажите ссылку:')
    while counter:
        input_url = input()
        if input_url:
            URL.append(input_url)
        else:
            counter = False

    if not URL:
        URL = URL_default

    home_urls = create_home_url(URL)

    for i in range(len(URL)):
        answer = get_links(url=URL[i], index=site_index, l=links_to_site, h_url=home_urls[i])
        site_index = answer[0]
        if site_index != 0:
            links_to_site.extend(answer[1])
            while site_index < 101:
                link = links_to_site.pop(0)
                answer = get_links(url=f'{link}', index=site_index, l=links_to_site, h_url=home_urls[i])
                index = answer[0]
                if index != 0:
                    site_index = index
                    links_to_site.extend(answer[1])
