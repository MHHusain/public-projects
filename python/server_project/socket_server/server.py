import os
import socket
import threading

from jinja_render import my_render


class Main:
    def __init__(self, ip_address, port, listen_count):
        self.sock_obj = socket.socket()
        self.sock_obj.bind((ip_address, port))
        self.sock_obj.listen(listen_count)
        print("start")
        self.con_obj, self.client_ip_address = self.sock_obj.accept()
        print("stop")
        self.request_header = self.con_obj.recv(8000).decode("utf-8")
        if self.request_header:
            self.url = self.request_header.split()[1]
        else:
            self.url = None
        self.url_exists = os.path.exists("." + self.url) and os.path.isfile("." + self.url)

    def start(self):
        while True:
            print('______________start of while loop____________')

            print("________________________________request header________________________________")
            print(self.request_header)
            print("________________________________end of request header__________________________")

            self.con_obj, self.client_ip_address = self.sock_obj.accept()
            Main.set_request_header(self)

            if not self.request_header:
                print("blank request or hand shake (syn) ____________url variable not defined_________")
            Main.set_url(self)

            thread1 = threading.Thread(target=Main.main_function_url, args=(self,))
            # thread2 = threading.Thread(target=Main.start_viewing, args=(self,))
            thread1.start()
            # thread2.start()

            print("______________end of while loop______________")

    def set_request_header(self):
        # temp = []
        # self.recv = self.con_obj.recv(1024)
        # while self.recv:
        #     temp.append(self.recv)
        #     self.recv = self.con_obj.recv(1024)

        # self.request_header = b"".join(temp).decode("utf-8")
        self.request_header = self.con_obj.recv(8000).decode("utf-8")

        print("end of set request header")

    def set_url(self):
        if self.request_header:
            self.url = self.request_header.split()[1]
        else:
            self.url = None

    def main_function_url(self):
        if self.url:
            if self.url_exists and not (os.path.splitext(self.url)[1] == ".html"):
                print("before printing url")
                print(self.url)
                print("after printing url")

                file = open(os.path.abspath(self.url[1:]), "rb")
                # reading_file = file.read(1000)
                try:
                    # while reading_file:
                    #     print(self.con_obj)
                    #     self.con_obj.send(reading_file)
                    #     reading_file = file.read(3000)
                    self.con_obj.sendfile(file)
                    file.close()
                    # self.con_obj.close()

                except ConnectionResetError as e:
                    print(f"connection closed_______{e}")
                    file.close()
            else:
                Main.start_viewing(self)

    def with_argument(self, custom_url):
        def outer(decorated_func):
            def inner(*args, **kwargs):
                print("befor printing url 2")
                print(self.url)
                print("after pringting url 2")

                if self.url in custom_url:
                    returned_html = decorated_func(*args, **kwargs).encode("utf-8")
                    while True:
                        self.con_obj.send(returned_html)
                else:

                    print("_____________________one of the views have ran")

            return inner

        return outer

    def start_viewing(self):
        # ____________________________________________________________________________________________________

        # ____________________________________________________________________________________________________

        @Main.with_argument(self, custom_url=("/muntatharvideo.html", "/sa"))
        def video():
            return my_render("html/video.html")

        @Main.with_argument(self, custom_url=("/index.html", "/"))
        def index():
            return my_render("html/index.html")

        index()
        video()


app = Main("localhost", 80, 2)
app.start()
