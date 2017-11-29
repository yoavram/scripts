#!	/Users/yoavram/miniconda3/bin/python
import poplib
from email.parser import Parser
import keyring

USERNAME = 'yoavram'
MAIL_SYSTEM = 'gmail'
MAIL_SERVER = 'pop.gmail.com'

# run 'keyring set MAIL_SYSTEM USERNAME' to set the password once
password = keyring.get_password(MAIL_SYSTEM, USERNAME)
pop_conn = poplib.POP3_SSL(MAIL_SERVER)
pop_conn.user(USERNAME)
res = pop_conn.pass_(password)
assert res == b'+OK Welcome.', res
parser = Parser()

num = len(pop_conn.list()[1])
if not num:
	print("No new messages")
else:
	#print("{} new messages".format(num))
	messages = (pop_conn.top(i, 0) for i in range(1, num + 1))
	messages = ((m.decode('utf8') for m in msg[1]) for msg in messages)
	messages = ("\n".join(msg) for msg in messages)
	messages = [parser.parsestr(msg) for msg in messages]
	for msg in messages:
	    print('{}: {}'.format(msg['from'], msg['subject']))
pop_conn.quit()