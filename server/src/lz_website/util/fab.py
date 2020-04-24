

# from fabric import Connection
# from invoke import Responder
# c = Connection(host='192.168.32.222', port=22, user='root', connect_kwargs={"password": "123456"})
# sudopass = Responder(
#     pattern=r'\[sudo\]password:',
#     response='123456\n'
# )
#
# a = c.run("scp", pty=True, watchers=[sudopass])
# print(b)
# scp -o ProxyCommand='ssh -q root@192.168.20.201 -W %h:%p' lz.txt root@192.168.32.222:~/
# def m(a,b,c,d):
#     print('hello:%s,%s,%s,%s'%( a,b,c,d))
# import paramiko
# from scp import SCPClient
# ssh = paramiko.SSHClient()
#
# # 这行代码的作用是允许连接不在know_hosts文件中的主机。
# host = {"proxy": 'ssh -q root@192.168.20.201 -W 192.168.32.222>/dev/null'}
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# proxy = paramiko.ProxyCommand(host["proxy"])
# ssh.connect("192.168.32.222", 22, "root", "123456", sock=proxy)
#
# scp = SCPClient(ssh.get_transport(), socket_timeout=5.0, progress4=m)
#
# scp.put('qwe.txt', '/home/root')

# import socks
# import paramiko
#
# sock=socks.socksocket()
# sock.set_proxy(
#     proxy_type=socks.SOCKS5,
#     addr="192.168.20.201",
#     port=22,
#     username="root",
#     password="123456"
# )
# sock.connect(('192.168.32.222', 22))
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('ignored without host key verification', username='root', sock=sock)
# print((ssh.exec_command('ls')[1]).read().decode())
# ssh.close()

#
# print("(a,(b,None,N),(c,d))" in "(a,b,(c,d))")
# stack = [1,2,3,4]
# print(stack.pop())

# scp -o ProxyCommand='ssh -q 用户名@A.A.A.A -W %h:%p' helloWord-1.0-SNAPSHOT.jar 用户名@B.B.B.B:/home/worker/

# from fabric import Connection
# from invoke import Responder
# class SCPClient:
#     # def __init__(self, host, port , local_file_path, remote_file_path):
#     #     self.host = host
#     #     self.port = port
#     #     self.local_path = local_file_path
#     #     self.remote_path = remote_file_path
#
#     def springboard(self, ip='192.168.20.201', port=22, username='root', password='123456'):
#         self.springboard_conn = Connection(host=ip, port=port, user=username, connect_kwargs={"password": password})
#         sudopass = Responder(
#             pattern=r'\[sudo\]password:',
#             response='123456\n'
#         )
#         self.springboard_conn.run('scp rabbitmq.sh  root@192.168.32.222:~/', pty=True, watchers=[sudopass])
#
# if __name__ == '__main__':
#     a = SCPClient()
#     a.springboard()

import paramiko
from sshtunnel import SSHTunnelForwarder
import logging
from scp import SCPClient
with SSHTunnelForwarder(
    ('192.168.20.201', 22),
    ssh_username="root",
    ssh_password='123456',
    remote_bind_address=('192.168.32.222', 22),
    local_bind_address=('0.0.0.0', 18882),
) as tunnel:
    print(tunnel.local_bind_port,tunnel.local_bind_address)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('127.0.0.1', 18882, username='root', password='123456')
    scp = SCPClient(client.get_transport(), socket_timeout=5.0)
    scp.put('qwe.txt', '/home/root')
    # do some operations with client session
    client.close()

print('FINISH!')

