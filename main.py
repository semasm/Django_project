# Подключаем библиотку для получения соежимого страниц сайта
import requests
from bs4 import BeautifulSoup

class my_parser():
    def __init__(self, url_str):
        self.url_str = url_str


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    a = my_parser('https://news.ycombinator.com/item?id=13713480')
    print(a.url_str)

    r = requests.get(a.url_str)

    soup = BeautifulSoup(r.text, 'html.parser')
    with open('temp.txt', 'w', encoding='utf-8') as f:
        print(soup.get_text(), file=f)

    with open('temp.txt', 'r', encoding='utf-8') as f:
        res = f.readlines()

    print(res[1:5])
    print()


    for i in range(len(res)):
        a = ' '.join([w if len(w) != 6 else w+'11' for w in res[i].split()])+'\n'
        res[i] = a

    print(res[1:5])

#    print(res)

    #print(soup.get_text())
    #print(''.join(res))


#    with open('test.html', 'w') as output_file:
#        output_file.write(r.text.encode('cp1251'))

#    print(soup)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
