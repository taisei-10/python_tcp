import socket
import sys
import json

def send_tcp(target_ip:str, target_port:int, send_datas: dict):
    
    # TCPソケットの作成
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TCPサーバに接続
    tcp_client.connect((target_ip,target_port))
    print("connect!")

    # TCPサーバにデータを送信
    delimiter="/"
    for send_data in send_datas.values():
        print(send_data)
        tcp_client.send(send_data+delimiter.encode())

    # TCPサーバからのレスポンスを受信
    buffer_size = 1024
    res_byte = tcp_client.recv(buffer_size)
    res_str = res_byte.decode()
    print("Received a response:{}".format(res_str))

    tcp_client.close()


def collect_json ():

    # jsonのkeyの数を尋ねる
    print("How many types of data to be entered?:")
    num_data_types = input()

    key_name = []
    # keyの名称を尋ねる
    for i in range(int(num_data_types)):
        print("No.%d data type name:"%(i+1))
        key_name.append(input())

    # 入力したいjsonデータの件数を尋ねる
    print("How many json data do you want to input?:")
    num_json = input()

    json_datas={}
    # 具体的なjsonデータを入力
    for i in range(int(num_json)):
        json_data={}
        print("\nNo.%d data\n"%(i+1))
        for j in range(int(num_data_types)):
            print("%s:"%key_name[j])
            value=input()
            json_data[key_name[j]]=value
        json_datas[i]=json.dumps(json_data)

    # bytes型に変換
    json_bytes={}
    for i in range(int(num_json)):
        json_str=json_datas[i]
        json_bytes[i]=json_str.encode()
    return json_bytes


target_ip = "127.0.0.1"
target_port = 8080

# jsonデータ収集
json_bytes = collect_json()


# TCP通信開始
send_tcp(target_ip, target_port, json_bytes)


