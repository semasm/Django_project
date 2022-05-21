import requests
from bs4 import BeautifulSoup
import string

class my_parser():
    def __init__(self, url_str):
        self.url_str = url_str


    def GetContent(self):
        url_data = requests.get(self.url_str)

        soup = BeautifulSoup(url_data.text, 'html.parser')

        res = set(s for s in soup.get_text().split() if len(s.strip(' ,.!?()')) == 6)

        url_data1 = url_data.text
        for s in res:
            url_data1 = url_data1.replace(' '+ s + ' '  , ' ' + s + '&#8482; ')

#        print(url_data)



#        a = 'embedding appropriate junk to the PDF format itself'
#        a = a.replace('format', 'format'+'&#8482;')
#        return a

        return url_data1



if __name__ == '__main__':
    soup = BeautifulSoup('<a href="http:&#x2F;&#x2F;shattered.io&#x2F;static&#x2F;pdf_format.png" rel="nofollow">http:&#x2F;&#x2F;shattered.io&#x2F;static&#x2F;pdf_format.png</a>', 'html.parser')
    print(soup.get_text())

    res = [s for s in soup.get_text().split() if len(s.strip(' ,.!?')) == 6]
    print(res)