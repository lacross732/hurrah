import socket
import threading

def handle_client(client_socket, addr):
    """Handle incoming client connections"""
    request = client_socket.recv(4096).decode()
    print(f"Request from {addr}:\n{request}\n")
    
    # For now, just send back a simple response
    response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Proxy Working!</h1>"
    client_socket.send(response)
    client_socket.close()

def start_proxy(host='localhost', port=8888):
    """Start the proxy server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    
    print(f"Proxy running on {host}:{port}")
    
    try:
        while True:
            client_socket, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
    except KeyboardInterrupt:
        print("Proxy stopped")
        server.close()

if __name__ == "__main__":
    start_proxy()
