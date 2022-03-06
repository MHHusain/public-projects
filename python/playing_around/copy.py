file = open(r"C:\Users\NS\Desktop\images.jpg", "rb")
# file.seek(7000)
file2 = open("./hello.jpg", "ab")
part = file.read(400)
while part and file.tell() % 2 == 0:

    part = file.read(400)
    file2.write(part)

file.close()
file2.close()
