#!	/Users/yoavram/miniconda3/bin/python
import poplib
from email import parser
import keyring

USERNAME = 'yoavram'
MAIL_SYSTEM = 'gmail'
MAIL_SERVER = 'pop.gmail.com'

# run 'keyring set MAIL_SYSTEM USERNAME' to set the password once
password = keyring.get_password(MAIL_SYSTEM, USERNAME)
pop_conn = poplib.POP3_SSL(MAIL_SERVER)
pop_conn.user(USERNAME)
pop_conn.pass_(password)
#Get messages from server:
num = len(pop_conn.list()[1])
if not num:
	print("No new messages")
else:
	#print("{} new messages".format(num))
	messages = (pop_conn.retr(i) for i in range(1, num + 1))
	# Concat message pieces:
	messages = ((m.decode('utf8') for m in mssg[1]) for mssg in messages)
	messages = ("\n".join(mssg) for mssg in messages)
	#Parse message intom an email object:
	messages = [parser.Parser().parsestr(mssg) for mssg in messages]
	for message in messages:
	    print('{}: {}'.format(message['from'], message['subject']))
pop_conn.quit()