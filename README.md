# group-chat
群聊
socket写的群聊
版本号:1.0版
声明: 界面 传输 接受 功能
功能: 实现多人在线聊天
用tkinter搭建一个界面,用json传输数据

服务端: from socket import *
初始化 创建tcp套接字 
绑定端口 并监听 bind listen
接受到客户端发送过来的数据通过json loads发序列化出来
反序列化后 在发送给客户端


客户端: from socket import *
初始化 创建tcp套接字
连接服务器connect
向服务器发送数据 通过json dumps序列化后在传输

创建客户端窗口 tkinter
功能 : 发送
先获取到输入的数据 然后通过json 发送给服务器

创建客户端线程:
实例化tcp对象
接受数据服务器发送过来的数据



