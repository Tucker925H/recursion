import socket
import threading
import json

# クライアント情報とチャットルームを管理する辞書
clients = {}
chatrooms = {}

def handle_tcp_client(conn, addr):
    while True:
        header = conn.recv(32)
        if not header:
            break  # クライアントが接続を閉じた場合

        # ヘッダーから情報を解析
        room_name_size = header[0]
        operation = header[1]
        state = header[2]
        operation_payload_size = int.from_bytes(header[3:32].strip(b'\x00'), 'big')

        room_name = conn.recv(room_name_size).decode('utf-8')
        operation_payload = conn.recv(operation_payload_size).decode('utf-8')

        if operation == 1:  # 新しいチャットルームを作成
            token = "unique_token_{}".format(len(chatrooms) + 1)
            chatrooms[room_name] = {'host': addr, 'token': token}
            conn.send(token.encode('utf-8'))  # クライアントにトークンを送信
        elif operation == 2:  # チャットルームに参加
            if room_name in chatrooms:
                token = chatrooms[room_name]['token']
                conn.send(token.encode('utf-8'))  # 参加成功した場合はトークンを送信
            else:
                conn.send(b'Error: Room not found')

def start_tcp_server():
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.bind(('0.0.0.0', 9002))
    sock_tcp.listen()

    while True:
        conn, addr = sock_tcp.accept()
        thread = threading.Thread(target=handle_tcp_client, args=(conn, addr))
        thread.start()

def handle_udp_client():
    sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_udp.bind(('0.0.0.0', 9001))

    while True:
        data, addr = sock_udp.recvfrom(4096)
        # UDPで受け取ったデータの処理。トークン検証など。

if __name__ == "__main__":
    tcp_thread = threading.Thread(target=start_tcp_server)
    tcp_thread.start()

    handle_udp_client()
