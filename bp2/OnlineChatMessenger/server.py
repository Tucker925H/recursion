import socket

# AF_INETを使用し、UDPソケットを作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# サーバーのIPアドレスとポート番号を指定
server_address = '0.0.0.0'
server_port = 9001
print('starting up on port {}'.format(server_port))

clients = set()

# ソケットをアドレスにバインド
sock.bind((server_address, server_port))

while True:
  print('\nwaiting to receive message')
  data, address = sock.recvfrom(4096)

  print('received {} bytes from {}'.format(len(data), address))
  print(data)

  if data:
        print(f"Received message from {address}")
        clients.add(address)
        # 全クライアントにメッセージをブロードキャスト
        for client in clients:
            print(f"Sending message to {client}")
            if client != address:  # 送信元には送らない
                print(f"Sending message to {client}")
                sock.sendto(data, client)
