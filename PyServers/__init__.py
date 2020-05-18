from socketserver import ThreadingUDPServer, DatagramRequestHandler
from socketserver import ThreadingTCPServer, BaseRequestHandler, StreamRequestHandler
from threading import Thread
from types import FunctionType

__name__ = 'PortableServers'
__version__ = '1.0.0'
__author__ = 'Ren'
__description__ = 'Portable servers for everyone! :P'
__url__ = 'https://steamcommunity.com/id/SamXDR/'

__all__ = [
	'SocketServerUDP',
	'SocketServerTCP',
	'StreamSocketServerTCP',
]


class SocketServerUDP(ThreadingUDPServer):
	class __Request(DatagramRequestHandler):
		def setup(self):
			super().setup()
			self.selfmain.setup(self)
		def handle(self):
			super().handle()
			self.selfmain.handle(self)
		def finish(self):
			super().finish()
			self.selfmain.finish(self)
	def __init__(self, addr, **kwargs):
		self.thread = Thread(target=self.serve_forever, daemon=True)
		self.__Request.selfmain = self
		self.setup = FunctionType(self.setup.__code__, self.setup.__globals__)
		self.handle = FunctionType(self.handle.__code__, self.handle.__globals__)
		self.finish = FunctionType(self.finish.__code__, self.finish.__globals__)
		super().__init__(addr, self.__Request, True)
	def start(self):
		self.thread.start()
	def stop(self):
		self.thread.stop()
	def IsAlive(self):
		self.thread.is_alive()
	def __GetDaemon(self) -> bool:
		return self.thread.daemon
	def __SetDaemon(self, daemonic:bool):
		if isinstance(daemonic, bool) != True:
			return
		self.thread.daemon = daemonic
	def __DelDaemon(self):
		return
	daemon = property(__GetDaemon, __SetDaemon, __DelDaemon)
	def setup(self):
		pass
	def handle(self):
		pass
	def finish(self):
		pass

class SocketServerTCP(ThreadingTCPServer):
	class __Request(BaseRequestHandler):
		def setup(self):
			super().setup()
			self.selfmain.setup(self)
		def handle(self):
			super().handle()
			self.selfmain.handle(self)
		def finish(self):
			super().finish()
			self.selfmain.finish(self)
	def __init__(self, addr, **kwargs):
		self.thread = Thread(target=self.serve_forever, daemon=True)
		self.__Request.selfmain = self
		self.setup = FunctionType(self.setup.__code__, self.setup.__globals__)
		self.handle = FunctionType(self.handle.__code__, self.handle.__globals__)
		self.finish = FunctionType(self.finish.__code__, self.finish.__globals__)
		super().__init__(addr, self.__Request, True)
	def start(self):
		self.thread.start()
	def stop(self):
		self.thread.stop()
	def IsAlive(self):
		self.thread.is_alive()
	def __GetDaemon(self) -> bool:
		return self.thread.daemon
	def __SetDaemon(self, daemonic:bool):
		if isinstance(daemonic, bool) != True:
			return
		self.thread.daemon = daemonic
	def __DelDaemon(self):
		return
	daemon = property(__GetDaemon, __SetDaemon, __DelDaemon)
	def setup(self):
		pass
	def handle(self):
		pass
	def finish(self):
		pass

class StreamSocketServerTCP(ThreadingTCPServer):
	class __Request(StreamRequestHandler):
		def setup(self):
			super().setup()
			self.selfmain.setup(self)
		def handle(self):
			super().handle()
			self.selfmain.handle(self)
		def finish(self):
			super().finish()
			self.selfmain.finish(self)
	def __init__(self, addr, **kwargs):
		self.thread = Thread(target=self.serve_forever, daemon=True)
		self.__Request.selfmain = self
		self.setup = FunctionType(self.setup.__code__, self.setup.__globals__)
		self.handle = FunctionType(self.handle.__code__, self.handle.__globals__)
		self.finish = FunctionType(self.finish.__code__, self.finish.__globals__)
		super().__init__(addr, self.__Request, True)
	def start(self):
		self.thread.start()
	def stop(self):
		self.thread.stop()
	def IsAlive(self):
		self.thread.is_alive()
	def __GetDaemon(self) -> bool:
		return self.thread.daemon
	def __SetDaemon(self, daemonic:bool):
		if isinstance(daemonic, bool) != True:
			return
		self.thread.daemon = daemonic
	def __DelDaemon(self):
		return
	daemon = property(__GetDaemon, __SetDaemon, __DelDaemon)
	def setup(self):
		pass
	def handle(self):
		pass
	def finish(self):
		pass
