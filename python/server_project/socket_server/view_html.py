# import render as r
from jinja_render import my_render
import os
import server


ld = os.listdir
e1, e = (ld("images/elf__300"), ld("images/elf"))
compleated_elf_list = []
def pair(first, second):
    index = 0
    while index < len(e):
        compleated_elf_list.append([first[index], second[index]])
        index+=1
    return compleated_elf_list



class View(server.Main):
    def main_function_url(self):
        print("i am main in view")
        server.Main.main_function_url(self)
        View.start_viewing(self)

    def start_viewing(self):
        @View.with_argument(self, custom_url=("/muntatharvideo.html", "/sa"))
        def video():
            return my_render("html/video.html")

        @View.with_argument(self, custom_url=("/index.html", "/"))
        def index():
            return my_render("html/index.html")
        index()
        video()
app = View("", 80, 4)

app.start()