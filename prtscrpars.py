import random
import requests
from bs4 import BeautifulSoup
import time
import os

os.system('cls')

HEADERS = { 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 YaBrowser/20.3.1.197 Yowser/2.5 Safari/537.36',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

fail, done, number = 0, 0, 0
print('                  Scraper for Lightshot\n                  Powered by ShiZZZeRRR')
print('Введите путь до конечной папки (не забывайте слэш в конце).')
path = input('scraper > ')
os.system('cls')
print('                  Scraper for Lightshot\n                  Powered by ShiZZZeRRR')
print('Введите нужное количество картинок.')
count = int(input('scraper > '))

while done < count:

	number += 1

	page = ''

	for randomizer in range(6):
		page += random.choice(list('123456789qwertyuiopasdfghjklzxcvbnm') ) 

	url = 'https://prnt.sc/' + page

	r = requests.get(url, headers=HEADERS)

	soup = BeautifulSoup(r.text,'html.parser')

	pngurl = soup.find('img',class_='no-click screenshot-image').get('src')

	if pngurl != '//st.prntscr.com/2020/03/13/0139/img/0_173a7b_211be8ff.png':
		img = requests.get(pngurl, headers=HEADERS)
		img_file = open(path+page+'.png', 'wb')
		img_file.write(img.content)
		img_file.close()
		done += 1 
	else:
		fail += 1
	os.system('cls')
	print('         Scraper for Lightshot\n         Powered by ShiZZZeRRR')
	print( '     Происходит загрузка картинок...')
	print(f'{done} загружено | {fail} ошибкок | {number} попыток')
	
os.system('cls')
print('            Scraper for Lightshot\n            Powered by ShiZZZeRRR')
print(f'Программа завершена. Было скачано {done} картинок.')