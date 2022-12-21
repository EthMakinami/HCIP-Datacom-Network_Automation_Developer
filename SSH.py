import paramiko
import time

device = paramiko.SSHClient()
device.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
device.connect(hostname='1.1.1.1',username='makinami',password='ayanami2022')

cli = device.invoke_shell()
cli.send('display version\n')
time.sleep(2)

lines = cli.recv(999999).decode()
print(lines)
