import paramiko

with open('servers.txt', 'r') as servers:
    for server in servers:
        try:
            username = "root"
            password = "123456798"
            port = 22
            server = server.strip()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(server, port, username, password, banner_timeout=200)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('which app')
            output = ssh_stdout.read().decode('utf-8').strip()
            if output:
                print(f"app is installed at {output} in {server}")
            else:
                print(f"app is not installed in {server}")

            ssh.close()
        except Exception as error:
    # handle the exception
            print(f"An exception occurred: {error} in {server}")
     