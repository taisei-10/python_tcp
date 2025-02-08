import socket
import sys

def send_tcp(target_ip:str, target_port:int, send_data: bytes):
    
    # TCPソケットの作成
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TCPサーバに接続
    tcp_client.connect((target_ip,target_port))
    print("connect!")

    # TCPサーバにデータを送信
    tcp_client.send(send_data_byte)

    # TCPサーバからのレスポンスを受信
    buffer_size = 1024
    res_byte = tcp_client.recv(buffer_size)
    res_str = res_byte.decode()
    print("Received a response:{}".format(res_str))

    tcp_client.close()


target_ip = "127.0.0.1"
target_port = 8080

print("Please send msg input:\n")
send_data = input()
send_data_byte =send_data.encode()

# TCP通信開始
send_tcp(target_ip, target_port, send_data_byte)


