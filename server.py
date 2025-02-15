import socket
import sys

def w_json_to_file(filepath: str, recv_data: str):
     with open(filepath,"w") as o:
          w_datas = recv_data.split("/")
          for w_data in w_datas:
               print(w_data,file=o)

def listen_TCP(ip_address: str, port: int, limit_num_client: int):
    
    # ソケット作成　socket.AF_INET=IPv4, socket.SOCK_STREAM=TCP
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # IPアドレスとポートを紐づける
    tcp_server.bind((ip_address, port))

    # 接続待ち
    tcp_server.listen()

    try:
        while True:
            # 接続待ちする
            conn, address = tcp_server.accept()
            print("[*] Connected!! [ Source : {}]".format(address))

            # msgの受信を行う
            buf_size = 1024
            recv_data = conn.recv(buf_size)
            recv_data_str = recv_data.decode()
            print("[*] Received Data : {}".format(recv_data_str))

            # 受信データをfileへ吐き出し
            file_path="recv_data.txt"
            w_json_to_file(file_path,recv_data_str)

            # 受信確認の返信
            send_data = "receved msg :{}".format(recv_data_str)
            send_data_byte = send_data.encode()
            conn.send(send_data_byte)
            conn.close()

    except KeyboardInterrupt:
            tcp_server.close()
            print("Closed a TCP Server")

host = "localhost"
limit_num_client = 5
port = 8080
print("hostname:"+host)
IP_address = socket.gethostbyname(host)

print(host,IP_address)

listen_TCP(IP_address,port,limit_num_client)