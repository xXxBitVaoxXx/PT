import paramiko
import json
from time import strftime, localtime

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
with open('connections_ssh.json', 'r') as f:
	file = json.load(f)

def get_transport():

	host_ = file['host']

	try:
		transport = (str(input('change transport: SSH | SQLite\n'))).lower()
	except Exception:
		print("UnknownTransport")

	if transport == 'ssh':
		info = file['transport']['SSH']
		login_ = info['login']
		password_ = info['password']
		port_ = info['port']
	
		# [01-05-2018 / 21:23:10] SSH connect: {'login': 'root', 'password': 'pwd', 'port': 22022} 
		print('[{} / {}] SSH connect: {}'.format(strftime('%d-%m-%Y', localtime()), strftime('%H:%M:%S', localtime()), info))

		client.connect(hostname = host_, username = login_, password = password_, port = port_)
	
		ftp = client.open_sftp()
		#созданный на контейнере файл echo.py
		ftp.get('echo.py', 'localPath')
		ftp.close()



#try:
get_transport()
stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.read())
client.close()
#except Exception as e:
#	print(str(e))
#	print("UnknownTransport")

