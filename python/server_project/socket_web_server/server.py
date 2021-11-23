import socket
import os
import urllib.parse
socket_obj = socket.socket()
socket_obj.bind((socket.gethostbyname(socket.gethostname()), 80))
socket_obj.listen(2)

while True:
    print("start while")
    connection_socket, ip_port = socket_obj.accept()
    print("created connection")
    print(connection_socket)
    print(ip_port)

    request_header = connection_socket.recv(8000)
    print(f"length of request is : {len(request_header)}")
    decoded_header = request_header.decode("utf-8")
    print("start blank request")
    print(decoded_header)
    print("end blank request")
    if decoded_header:
        url = decoded_header.split()[1]
        print(url)
        print("decoded url")
        url = urllib.parse.unquote(url)
        print(url)
        if os.path.exists(f".{url}") and os.path.isfile(f".{url}"):
            video = open(f".{url}", 'rb')
            reading_file = video.read(8000)

            try:
                while reading_file:
                    # connection_socket.settimeout(None)  # the same as --> connection_socket.setblocking(True)
                    # connection_socket.sendfile(video)
                    if url.endswith(".mp4"):
                        connection_socket.send(b"HTTP/1.x 200\r\ncontent-type: video/mp4\r\n\r\n")
                        connection_socket.send(reading_file)
                        reading_file = video.read(8000)

                    elif url.endswith(".css"):
                        connection_socket.send(b"HTTP/1.x 200\r\ncontent-type: text/css;charset=UTF-8\r\n\r\n")
                        connection_socket.send(reading_file)
                        reading_file = video.read(8000)

                    elif url.endswith(".js"):
                        connection_socket.send(b"HTTP/1.x 200\r\ncontent-type: application/javascript\r\n\r\n")
                        connection_socket.send(reading_file)
                        reading_file = video.read(8000)

                video.close()
                print("done sending video")
            except ConnectionResetError as e:
                print(f"connection closed {e}")
                connection_socket.close()
            except ConnectionAbortedError as i:
                print(f"connection closed {i}")
                connection_socket.close()

        else:

            index = open("template/index.html", "r")
            reading = index.read()
            connection_socket.send(b"HTTP/1.x 200\r\ncontent-type: text/html;charset=UTF-8\r\n\r\n")
            connection_socket.send(reading.encode("utf-8"))
            index.close()

        # if url.endswith(".css"):
        #     index_css = open("static/css/index_style.css", 'r')
        #     reading_css = index_css.read()
        #     connection_socket.send(reading_css.encode("utf-8"))
        #     index_css.close()
        # elif url.endswith(".mp4"):
        #     video = open("videos/Greek Music - Greek Gods & Goddesses.mp4", 'rb')
        #     reading_mp4 = video.read(8000)
        #     try:
        #         while reading_mp4:
        #             connection_socket.settimeout(None)  # the same as --> connection_socket.setblocking(True)
        #         # connection_socket.sendfile(video)
        #             connection_socket.send(reading_mp4)
        #             reading_mp4 = video.read(8000)
        #         video.close()
        #         print("done sending video")
        #     except ConnectionResetError as e:
        #         print(f"connection closed {e}")
        #         connection_socket.close()
        # else:
        #     # connection_socket.send(b"HTTP/1.1 201\r\ncontent-type: text/html; charset=utf-8\r\n\r\n")
        #     index = open("template/index.html", "r")
        #     reading = index.read()
        #     connection_socket.send(reading.encode("utf-8"))
        #     index.close()

        connection_socket.close()
    print("end while")
