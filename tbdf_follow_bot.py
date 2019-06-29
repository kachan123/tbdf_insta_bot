import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class tbdBot():
	def __init__(self, username, password):
		self.browser = webdriver.Chrome('/usr/local/bin/chromedriver')  # Optional argument, if not specified will search path.
		self.username = username
		self.password = password
		
	def signIn(self):
		self.browser.get('https://www.instagram.com/accounts/login/')

		#the only two input classes are the username and pass
		email_input = self.browser.find_elements_by_css_selector('form input')[0]
		password_input = self.browser.find_elements_by_css_selector('form input')[1]

		#filling out form 
		email_input.send_keys(self.username)
		password_input.send_keys(self.password)
		password_input.send_keys(Keys.ENTER)

		time.sleep(2)
		
	def followWithUsername
	# def unfollowWithUsername
	# def getUserFollowers
	# def closeBrowser
	# def __exit__

bot=tbdBot('tbdfwomen', 'TBDFpass2018!')
bot.signIn()