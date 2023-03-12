import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Christoffer Ivar"
email["to"] = "christoffer.ivar@outlook.com"
email["subject"] = "Jag testar att skicka mejl via Python"

email.set_content(html.substitute({"name": "Rebecca"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("christoffer.iwar@gmail.com", "obedfjwsgwdbtuoo")
	smtp.send_message(email)
	print("Allt är skickat")