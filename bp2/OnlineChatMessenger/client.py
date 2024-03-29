import socket
import time
import threading

def receive_messages(sock):
    while True:
        data, _ = sock.recvfrom(4096)
        print("\nReceived:", data.decode('utf-8'))
        print("Message: ", end='', flush=True)  # ユーザーのメッセージ入力プロンプトを再表示

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = input("Type in the server's address to connect to: ")
server_port = 9001

port = input("Type in the port to bind to: ")
port = int(port)

while True:
  username = input("Type in your username: ")
  if len(username) < 255:
    break

address = ''
message = b'Message to send to the client.'

initial_message = bytes([len(username)]) + username.encode('utf-8')

# 空の文字列も0.0.0.0として使用できます。
sock.bind((address,port))

try:
  print('sending {!r}'.format(message))
  # サーバへのデータ送信
  sent = sock.sendto(initial_message, (server_address, server_port))
  print('Send {} bytes'.format(sent))

  # メッセージ受信用のスレッドを開始
  receiver_thread = threading.Thread(target=receive_messages, args=(sock,))
  receiver_thread.daemon = True  # メインプログラムが終了した時にスレッドも終了させる
  receiver_thread.start()

  while True:
    sock.settimeout(10)  # タイムアウトを設定
    message = input("Type in your message: ")
    if message == "exit":
      break
    message = bytes([len(message)]) + message.encode('utf-8')
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, (server_address, server_port))
    print('Send {} bytes'.format(sent))

    # 応答を受信
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
  print('closing socket')
  sock.close()
