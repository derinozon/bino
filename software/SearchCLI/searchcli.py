import sys, os

#Manage dependencies

try:
	from selenium import webdriver
except ImportError as e:
	print(e)
	inp = input("Proceed to install (y/n)? ")
	if (inp == 'y'):
		os.system("pip3 install selenium")
		from selenium import webdriver
	else :
		sys.exit()

try:
	import bs4 as bs
except ImportError as e:
	print(e)
	inp = input("Proceed to install (y/n)? ")
	if (inp == 'y'):
		os.system("pip install beautifulsoup4")
		import bs4 as bs
	else :
		sys.exit()


term = {
	"RESET": "\033[0m",
	"BLACK": "\033[30m",
	"RED": "\033[31m",
	"GREEN": "\033[32m",
	"YELLOW":  "\033[33m",
	"BLUE":    "\033[34m",
	"MAGENTA": "\033[35m",
	"CYAN":    "\033[36m",
	"WHITE":   "\033[37m",
	"BOLDBLACK":   "\033[1m\033[30m",
	"BOLDRED":     "\033[1m\033[31m",
	"BOLDGREEN":   "\033[1m\033[32m",
	"BOLDYELLOW":  "\033[1m\033[33m",
	"BOLDBLUE":    "\033[1m\033[34m",
	"BOLDMAGENTA": "\033[1m\033[35m",
	"BOLDCYAN":    "\033[1m\033[36m",
	"BOLDWHITE":   "\033[1m\033[37m"
}

_driver = None

def _assert (obj) :
	if (obj == None) :
		print(term["BOLDRED"] + "ANSWER NOT FOUND" + term["RESET"])
		_driver.quit()
		return -1
	else : 
		return 0

def str2web (txt) :
	word = txt.replace('+', '%2B')
	words = word.split(" ")
	web = ""
	for word in words :
		web += (word + "+")
	return web[:-1]

def askgoogle (question) :
	web_question = str2web(question)
	print(term["BLUE"] + "searching >>> " + web_question + term["RESET"])

	_driver.get("https://www.google.com/search?q=" + web_question)

	src = _driver.page_source
	
	soup = bs.BeautifulSoup(src, "html.parser")

	final = soup.find('div', class_='kCrYT')
	if _assert(final) == -1 : return
	
	print(term["BOLDGREEN"] + "ANSWER" + term["RESET"])
	print(final.text)

def askstack (question) :
	web_question = str2web(question)
	print(term["BLUE"] + "searching >>> " + web_question + term["RESET"])

	_driver.get("https://stackoverflow.com/search?q=" + web_question)
	_driver.find_element_by_class_name("question-hyperlink").click()

	src = _driver.page_source

	soup = bs.BeautifulSoup(src, "html.parser")

	a = soup.find('div', class_='answer accepted-answer')
	if (a == None) :
		a = soup.find('div', class_='answer accepted-answer highlighted-post')
	
	if (_assert(a) == -1) : return

	final = a.find('div', class_='s-prose js-post-body')
	
	if (_assert(final) == -1) : return
	
	print(term["BOLDGREEN"] + "ANSWER" + term["RESET"])
	print(final.text)

	_driver.quit()

def main () :
	START_PHANTOM()

	argc = len(sys.argv)-1
	question = ""
	if (argc < 2) :
		question = input(term["CYAN"] + "question >>> " + term["RESET"])
	else :
		question = sys.argv[2]
	
	if (argc == 0) :
		askgoogle(question)
	if (argc > 0) :
		if (sys.argv[1] == 'google') :
			askgoogle(question)
		if (sys.argv[1] == 'stack') :
			askstack(question)
	
def START_PHANTOM () :
	global _driver

	_driver = webdriver.PhantomJS()

if __name__ == "__main__":
	main()