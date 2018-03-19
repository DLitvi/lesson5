import requests

def get_html(url):
	try:
	    result = requests.get(url)
	    result.raise_for_status()
	    return result.text
	except requests.exceptions.RequestException as e:
		print(e)
		return False

html = get_html ('https://yandex.ru/search/?text=python&lr=10747')

