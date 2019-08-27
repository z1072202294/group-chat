from socket import *
from json import dumps
from threading import Thread
from tkinter import *


class My_thread(Thread):
    def __init__(self, tcp_client, bfu_size=1024):
        Thread.__init__(self)
        self.daemon = True
        self.tcp_client = tcp_client
        self.bfu_size = bfu_size

    def run(self):
        # 接受数据
        while True:
            data = tcp_client.recv(self.bfu_size)
            if not data:
                tcp_client.close()
                # root.destroy()
            else:
                output.insert(END, data.decode('utf-8'))


def send_msg():
    msg = input.get('1.0', END)
    tcp_client.send(
        dumps({'name': name,
               'msg': msg}).encode('utf-8'))


    input.delete('1.0', END)


# def log_out():
#     # msg = '退出群聊'
#     # tcp_client.send(
#     #     dumps({'name': name,
#     #            'msg': msg}).encode('utf-8'))
#     # # input.delete('1.0', END)
#     root.destroy()



host = '192.168.1.29'
port = 3300
address = (host, port)
name = '王'  # 可更改
tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect(address)
root = Tk()
root.geometry('600x430+500+200')
root.resizable(0, 0)
root.title('多人聊天(%s)' % name)
frame1 = Frame(root, height=200, width=300)
frame2 = Frame(root, height=200, width=300)
frame1.pack(expand=1, fill='both')
frame2.pack(expand=1, fill='both')
input = Text(frame2, height=6)
output = Text(frame1)
input.pack(expand=1, fill='both')
output.pack(expand=1, fill='both')
but_frame = Frame(frame2, height=20, bg='#FFFFFF')
but_frame.pack(expand=1, fill='both')
button = Button(but_frame, text='发送', bg='blue',
                fg='#FFFFFF', width=8, command=send_msg)
button.pack(side='right')
# button1 = Button(but_frame, text='退出', bg='blue',
#                  fg='#FFFFFF', width=8, command=log_out)
# button1.pack(side='left')
m = My_thread(tcp_client)
m.start()

root.mainloop()
