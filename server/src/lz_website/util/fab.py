# from fabric import Connection
# from invoke import Responder
# c = Connection(host='192.168.32.222', port=22, user='root', connect_kwargs={"password": "123456"})
# sudopass = Responder(
#     pattern=r'\[sudo\]password:',
#     response='123456\n'
# )
#
# a = c.run("pwd", pty=True, watchers=[sudopass])
# b = c.put('1.txt', remote='/home/root')
# # print(b)

# import paramiko
# from scp import SCPClient
# ssh = paramiko.SSHClient()
#
# # 这行代码的作用是允许连接不在know_hosts文件中的主机。
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect("192.168.32.222", 22, "root", "123456")
#
# scp = SCPClient(ssh.get_transport(),socket_timeout=5.0)
#
# scp.put('1.txt', '/home/root')

# print("(a,(b,None,N),(c,d))" in "(a,b,(c,d))")
# stack = [1,2,3,4]
# print(stack.pop())
#
for i in [] or [None]:
    print(i)





