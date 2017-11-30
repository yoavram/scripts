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
	print("{} new messages".format(num))
	try:
		n = int(input("How many? (0)"))
	except ValueError:
		n = 0
	for i in range(num - n + 1, num + 1):
		msg = pop_conn.top(i, 0)
		msg = (m.decode('utf8') for m in msg[1])
		msg = "\n".join(msg)
		msg = parser.parsestr(msg)
		print('{}\t{}\t{}\n'.format(i, msg['from'], msg['subject']))		
pop_conn.quit()