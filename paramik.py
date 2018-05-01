import paramiko
from datetime import datetime

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


file = open('connections', 'r')

for line in file:
	time = str(datetime.now())
	print('Time: ', time)
	info = {}
	info['host'] = line.split(' ') [0]
	info['username'] = line.split(' ') [1]
	info['port'] = line.split(' ') [2]
	info['password'] = line.split(' ') [3]

def get_transport():
	print('_SSH connect_')

	host = 'connecting to IP: ' + info['host']
	print(host)

	user = 'connecting to User: ' + info['username']
	print(user)

	port = 'connecting to Port: ' + info['port']
	print(port)

	password = 'connecting with password: ' + info['password']
	print(password+'\n')

	client.connect(hostname=info['host'], username=info['username'], password=info['password'], port=info['port'])	

	ftp = client.open_sftp()
	#созданный на контейнере файл echo.py
	ftp.get('echo.py', 'localPath')
	ftp.close()

try:
	get_transport()
	stdin, stdout, stderr = client.exec_command('ls -l')
	print(stdout.read())

except Exception:
	print("UnknownTransport")

client.close()