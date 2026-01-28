import socket
class LogListener:
    def __init__(self,host='0.0.0.0',port=5140):
        self.host=host
        self.port=port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start_listening(self,callback_function):
        print(f"[*] MicroSIEM dinleniyor:{self.host}:{self.port} (UDP)")
        self.sock.bind((self.host,self.port))
        while True:
            data, addr = self.sock.recvfrom(4096)
            log_message = data.decode("utf-8")
            source_ip = addr[0]
            callback_function(source_ip, log_message)