"""a class to send an email"""

import smtplib
from email.mime.text import MIMEText


class Email:
	def __init__(self, username, password, email, url, port):
		self._user = username
		self._pwd = password
		self._email = email
		self._url = url
		self._port = port

		self._subject = None
		self._body = None

	def connect(self):
		self._smtp = smtplib.SMTP(self._url, self._port)
		self._smtp.ehlo()
		self._smtp.login(self._user, self._pwd)

	def connect_tls(self):
		self._smtp = smtplib.SMTP(self._url, self._port)
		self._smtp.ehlo()
		self._smtp.starttls()
		self._smtp.login(self._user, self._pwd)

	def setMessage(self, subject, body):
		self._subject = subject
		self._body = body

	def sendMail(self, email):
		if self._subject == None:
			return -1
		if self._body == None:
			return -1

		msg = MIMEText(self._body)
		msg["Subject"] = self._subject
		msg["From"] = self._email
		msg["To"] = email

		self._smtp.send_message(msg)

	def quit(self):
		self._smtp.quit()



