import socket
import threading

def tcp_connect(server_ip, server_port, room_name, operation_code):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((server_ip, server_port))

    # 例: チャットルーム「MyRoom」に参加
    room_name_encoded = room_name.encode('utf-8')
    header = bytes([len(room_name_encoded)]) + bytes([operation_code]) + b'\x00' + bytes([0])
    sock.sendall(header + room_name_encoded)

    # サーバからのレスポンス（トークンなど）を受け取る
    response = sock.recv(1024)
    print(f"Received: {response.decode('utf-8')}")
    sock.close()

    return response.decode('utf-8')

def udp_send_message(server_ip, server_port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode('utf-8'), (server_ip, server_port))

def main():
    server_ip = '127.0.0.1'
    server_port = 9002
    room_name = "MyRoom"
    token = tcp_connect(server_ip, server_port, room_name, 1)  # 1: チャットルーム作成, 2: 参加
    # UDPでメッセージ送信など

if __name__ == "__main__":
    main()
