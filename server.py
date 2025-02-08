import socket
import sys

def listen_TCP(ip_address: str, port: int, limit_num_client: int):
    
    # ソケット作成　socket.AF_INET=IPv4, socket.SOCK_STREAM=TCP
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # IPアドレスとポートを紐づける
    tcp_server.bind((ip_address, port))

    # 接続待ち
    tcp_server.listen()

    # 接続する
    conn, address = tcp_server.accept()
    print("[*] Connected!! [ Source : {}]".format(address))

    # msgの受信を行う
    buf_size = 1024
    recv_data = conn.recv(buf_size)
    recv_data_str = recv_data.decode()
    print("[*] Received Data : {}".format(recv_data_str))

    # 受信確認の返信
    send_data = "receved msg :{}".format(recv_data_str)
    send_data_byte = send_data.encode()
    conn.send(send_data_byte)

host = "localhost"
limit_num_client = 5
port = 8080
print("hostname:"+host)
IP_address = socket.gethostbyname(host)

print(host,IP_address)

listen_TCP(IP_address,port,limit_num_client)