from bs4 import BeautifulSoup
from import_html import get_html


html = get_html('https://yandex.ru/search/?text=python&clid=1955453&win=324&lr=10747')

if html:
	bs = BeautifulSoup(html, 'html.parser')

	data = []

	for item in bs.find_all('li', class_="serp-item"):
		block_title = item.find('a', class_='organic__url')
		href = item.find('a', class_='path__item')
		data.append({
			'title':block_title.text,
			'link':href.get('href')
			})

	print(data)

else:
	print('Что-то пошло не так!')