from bs4 import BeautifulSoup
import requests, os, xlsxwriter


def scrap(url, file):
	page=requests.get(url)
	c = page.text
	soup = BeautifulSoup(c, 'lxml')
	workbook = xlsxwriter.Workbook(file + '/worksheet.xlsx')
	worksheet1 = workbook.add_worksheet('Sheet 1')
	worksheet1.write(0, 0, "Image Links")
	worksheet1.write(0, 1, "External Links")
	i = 1
	for tag in soup.find_all('img'):
		image = tag.get("src") + ''
		print(image)
		worksheet1.write(i, 0, image)
		i = i + 1

	i = 1
	for l in soup.find_all('link'):
		link = l.get('href')
		worksheet1.write(i, 1, link)
		i = i + 1

	workbook.close()

	return True




