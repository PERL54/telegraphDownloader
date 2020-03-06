from bs4 import BeautifulSoup as bs
import wget
import requests
import pyperclip 
import os

url = pyperclip.paste()
images = []
path = []

print(url)
print('---------')

def download():
	kavoS = 0
	page = requests.get(url)

	print(page.status_code)

	soup = bs(page.text, "html.parser")
	t = soup.findAll('title')
	t = str(t)
	t = t[8:-9]
	print(t)

	images = soup.findAll('img')

	for i in range(0,len(images)):
		img = images[i]
		img = str(img)
		img = img[10:-3]
		path.append(img)
		print(path[i])

	print("----------")
	print(str(len(path)) + ' images found!')
	
	os.mkdir(t)
	os.chdir(t)
	for i in range(0,len(path)):
		wget.download("https://telegra.ph" + str(path[i]), str(i) + ".png")
		print(' ')
		kavoS = kavoS + os.path.getsize(str(i) + '.png')
		print(str(i) + '.png was succesfully downloaded! ' + str(i+1) + '/' + str(len(path)) + '  Curent size - ' + str(round(kavoS/1024/1024, 1)) + 'M')
		
	print('-----------')
	print(str(round(kavoS/1024/1024, 1)) + ' M total ' + t)

if 'telegra.ph' in url:
	print("All done! It's a telegraph link")
	download()
else:
	print("Error #1 - non telegra.ph link!")
	input()