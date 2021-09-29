from cmd import Cmd
import sys
import getpass
import paramiko

class Term(Cmd):
    prompt = 'cmd>'

    def default(self, args):
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(ip, port=port , username=username , password=passwd)
            _, stdout, stderr = client.exec_command(args)
            output = stdout.readlines() + stderr.readlines()

            if output:
                for line in output:
                    print(line.strip())

            
        except Exception as e:
            print(f'[-] {e}')


    def do_exit(self, args):
        return True

term = Term()

if len(sys.argv) == 3:
    username = sys.argv[1]
    ip = sys.argv[2]
    passwd = getpass.getpass()
    port = 22

elif len(sys.argv) ==4:
    username = sys.argv[1]
    ip = sys.argv[2]
    port = sys.argv[3]
    passwd = getpass.getpass()

else:
    print('usage :  python3 ssh.py user localhost')
    print(len(sys.argv))

term.cmdloop()
