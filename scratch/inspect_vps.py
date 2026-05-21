import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('103.86.176.185', username='root', password='Imdbest1997@')

commands = [
    "ls -la /var/www",
    "ls -la /etc/nginx/sites-enabled",
    "cat /etc/nginx/sites-enabled/*",
    "pm2 list"
]

for cmd in commands:
    print(f"=== Command: {cmd} ===")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode('utf-8', errors='ignore'))
    print(stderr.read().decode('utf-8', errors='ignore'))

ssh.close()
