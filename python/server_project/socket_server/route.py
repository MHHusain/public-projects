import socket
import render
import threading
import os
import sys

sock_obj = socket.socket()
sock_obj.bind(("", 80))
sock_obj.listen(2)


def start():
    while True:
        print('______________start of while loop____________')

        con_obj, client_ip_address = sock_obj.accept()



        recv_msg_header = con_obj.recv(8830).decode("utf-8")
        if recv_msg_header:
            url = recv_msg_header.split()[1]
            print("i am if in main_function_url")
        else:
            url = None
            print("i am else in main_function_url")

        
        def main_function_url():
            if url:
                is_file__exists = os.path.exists("." + url) and os.path.isfile("." + url)
                if is_file__exists and not (os.path.splitext(url)[1] == ".html"):
                    print("before printing url")
                    print(url)
                    print("after printing url")
                    # header(con_obj, status_cod=404)

                    file = open(os.path.abspath(url[1:]), "rb")
                            
                    try:
                        con_obj.sendfile(file)
                        file.close()
                        con_obj.close()
                        
                    except ConnectionResetError as e:
                        print(f"connection closed_______{e}")
                        file.close()
                        
            else:
                print("blank request or hand shake (syn) ____________url variable not defined_________")
                sys.exit()
                


        thread1 = threading.Thread(target=main_function_url)
        # thread2 = threading.Thread(target=function, args=(con_obj))
        print(client_ip_address)
        print("before thread1")
        thread1.start()
     
        print("______________end of while loop______________")

if __name__ == "__main__":

    start()
