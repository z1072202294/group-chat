from socket import *
from select import select
from json import loads
from time import localtime, strftime



# 初始化  创建套接字
host = '192.168.1.29'
port = 3300
bufsize = 1024
address = (host, port)
tcp_server = socket(AF_INET, SOCK_STREAM)
# 绑定端口 并监听
tcp_server.bind(address)
tcp_server.listen(10)
# 设置套接字的阻塞或非阻塞模式：如果flag为false，则套接字设置为非阻塞，否则设置为阻塞模式。
tcp_server.setblocking(False)
inputs = [tcp_server]
print('Wait for client connection...')
# 第一个参数就是服务器端的socket,
# 第二个是我们在运行过程中存储的客户端的socket,
# 第三个存储错误信息。
# 重点是在返回值, 第一个返回的是可读的list,
# 第二个存储的是可写的list,
# 第三个存储的是错误信息的list
while True:
    rlist, wlist, xlist = select(inputs, [], [])
    # 1、select函数阻塞进程，直到inputs中的套接字被触发（在此例中，套接字接收到客户端发来的握手信号，
    # 从而变得可读，满足select函数的“可读”条件），
    # rlist返回被触发的套接字（服务器套接字）；
    # 4、select再次阻塞进程，
    # 同时监听服务器套接字和获得的客户端套接字；
    for s in rlist:
        if s is tcp_server:  # 2、如果是服务器套接字被触发（监听到有客户端连接服务器）
            tcp_client, addr = s.accept()
            print('有连接...', addr)
            tcp_server.setblocking(False)
            inputs.append(tcp_client)  # 3. inputs加入客户端套接字
        else:
            data = s.recv(bufsize)
            if not data:  # 5、当客户端发送数据时，客户端套接字被触发，
                # rlist返回客户端套接字，然后进行下一步处理。
                inputs.remove(s)
                s.close()
                continue
            res = loads(data.decode('utf-8'))
            time = strftime('%Y-%m-%d %H:%M:%S', localtime())
            data = '[{}]{}:{}'.format(time, res['name'], res['msg'])
            for i in inputs:
                if i is not tcp_server:
                    i.send(data.encode('utf-8'))

