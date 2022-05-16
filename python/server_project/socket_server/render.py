import sys
import os
import view_html


def with_argument(custom_url):
    def outer(decorated_func):
        def inner(*args, **kwargs):
            print("start of inner")
            print(url)
            is_file__exists = os.path.exists("." + url) and os.path.isfile("." + url)
            if (url in custom_url) and not is_file__exists:
                returned_html = decorated_func(*args, **kwargs)
                con_obj.send(returned_html.encode("utf-8"))
                con_obj.close()
                sys.exit()

            print("end of inner")
        return inner

    return outer




    view_html.start_viewing()
