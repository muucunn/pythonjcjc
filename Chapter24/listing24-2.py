from asyncore import dispatcher
import socket, asyncore

class ChatServer(dispatcher):   

    def handle_accept(self):    
    #handle_accept是dispatcher里的一个方法，这个方法不一样?
        conn, addr = self.accept()   #调用accept方法
        print ('Connection attempt from', addr[0])#修改：增加（）

s = ChatServer()
s.create_socket(socket.AF_INET, socket.SOCK_STREAM) 
#AF_INET决定了要用ipv4地址（32位的）
#流式Socket（SOCK_STREAM）是一种面向连接的Socket，针对于面向连接的TCP服务应用
s.bind(('', 5005))     #这里看似有两个参数，但打了两个括号，其实是一个参数
s.listen(5)         #是不是表示最大连接线路是5?
asyncore.loop()