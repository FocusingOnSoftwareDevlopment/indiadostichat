import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('103.86.176.185', username='root', password='Imdbest1997@')

commands = [
    "netstat -tulpn",
    "systemctl status apache2",
    "systemctl status nginx",
    "curl -I https://www.indiadostichat.com/"
]

for cmd in commands:
    print(f"=== Command: {cmd} ===")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode('utf-8', errors='ignore')
    print(output.encode('ascii', errors='backslashreplace').decode('ascii'))
    print(stderr.read().decode('utf-8', errors='ignore'))

ssh.close()
