from asyncore import dispatcher
import asyncore

class ChatServer(dispatcher): pass   ＃继承dispatcher类

s = ChatServer()
asyncore.loop()   ＃调用asyncore里的loop函数