import requests
import time
import os
from bs4 import BeautifulSoup

def get_title(html):

    soup = BeautifulSoup(html, 'html.parser')
    return soup.title.string

def get_html(url):
    r = requests.get(url)
    return r.text

def write_log(url, title):
    c_time = time.localtime()
    temp_str = 'Target URL: {}\nTitle:\t{}\nTime:\t{}'.format(url, title, c_time)
    with open('lab5.txt', 'w') as f:
        f.write(temp_str)
    f.close()

def main():
    url = 'http://www.startribune.com/trump-to-hold-white-house-news-conference-on-thursday/413970593/'
    html = get_html(url)
    title = get_title(html)
    write_log(url, title)
    print('Title for <{}>'.format(url))
    print(title)

if __name__=='__main__':
    try:
        main()
    except:
        pass
