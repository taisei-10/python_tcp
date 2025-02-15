import json

# key="date"
# value="awaji"
# dict={key:value}

# print(dict)
# json_str=json.dumps(dict)
# print(json_str)

# json_bytes=json_str.encode()

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