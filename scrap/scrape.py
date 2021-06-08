import requests
from bs4 import BeautifulSoup
import pprint

# res = requests.get('https://news.ycombinator.com/news')
# res2 = requests.get('https://news.ycombinator.com/news?p=')
# soup = BeautifulSoup(res.text, 'html.parser')

# SCRAPY framework for saving data in Databases
# BS$ library

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        tittle = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'tittle': tittle, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)

def lot_of_pages():
    limite = 1    
    noticias = []
    for link in range(9):      
        if limite < 10:
            pages = requests.get(f'https://news.ycombinator.com/news?p={limite}')
            sopa = BeautifulSoup(pages.text, 'html.parser')
            limite = limite + 1
            links = sopa.select('.storylink')
            subtext = sopa.select('.subtext')
            num_pag = (f'Page number: {limite - 1}')
            SuperLista = create_custom_hn(links, subtext)            
            noticias.append((num_pag, SuperLista))
    return noticias, 'All done'

pprint.pprint(lot_of_pages())
# lot_of_pages()
# print(soup.find_all('a'))
# print(soup.find(id='score_27412122'))
# print(soup.select('.score'))
# links = soup.select('.storylink')
# subtext = soup.select('.subtext')

# print(votes[0])

# print(votes[0].get('id'))









# create_custom_hn(links, subtext)

