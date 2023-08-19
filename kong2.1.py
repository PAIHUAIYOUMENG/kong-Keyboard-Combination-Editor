import ctypes
import threading
import webbrowser
import pystray
from PIL import Image
import sys
import os
import subprocess
import itertools
import json

from pynput import keyboard

import keyboard as key1

import datetime


with open('./keys_key.json', 'r') as file:# 读取 JSON 数据
      super_key=json.load(file)
class super_keys:
    def __init__(self, super_k=super_key['name']):
        # self.keys_pressed = key_set()
        self.hot_key_pressed = False
        self.hot_key_pressed2 = False
        self.keys = []
        self.super_key = super_k

        self.ss = super_k.replace('Key.', '')
        key1.block_key(self.ss)

        self.hot_keys = super_key

        self.previous_key = None
        self.previous_time = None
        self.previous_key2 = None
        self.previous_time2 = None

        self.key_lock=False
        self.hot_num = 0

    def hot_key(self, key):

        try:
            n = key.name
        except:
            n = key.char
        if str(n) in self.hot_keys:
            # print(n)
            self.hot_num = len(self.hot_keys[n].split("+"))
            print(self.hot_keys[n])
            # hk=self.hot_keys[n].split("+")
            key1.press_and_release(self.hot_keys[n])

    def on_press(self, key):
        print(self.keys)
        if key != self.previous_key or datetime.datetime.now() != self.previous_time:
          if self.hot_num==0:
            self.previous_time = datetime.datetime.now()
            self.previous_key = key
            # if str(key) not in self.keys:
            if str(key) != self.super_key and self.super_key not in self.keys:
                # print('pass')
                try:
                    for k, v in itertools.islice(self.hot_keys.items(), 1, None):
                        key1.unblock_key(k)
                        print('解锁')
                        self.key_lock=False
                except:
                    pass
            else:
                self.hot_key_pressed = not self.hot_key_pressed

                # print('上锁完毕')
                # print(f'按下 {key}')
                if str(key) in self.keys:
                    pass
                else:
                    self.keys.append(str(key))
                if str(key) != self.super_key:
                    self.hot_key_pressed2 = True
                    self.hot_key_pressed = True
                elif not self.key_lock:
                    for k, v in itertools.islice(self.hot_keys.items(), 1, None):
                        key1.block_key(k)
                    self.key_lock=True
                    print('上锁')
                    self.hot_key_pressed2 = False
                self.hot_key(key)

    def on_release(self, key):

        if key != self.previous_key2 or datetime.datetime.now() != self.previous_time2:
            self.previous_time2 = datetime.datetime.now()
            self.previous_key2 = key
            if str(key) == self.super_key:
                if not self.hot_key_pressed and not self.hot_key_pressed2:
                    key1.press(self.ss)  #######
                    key1.release(self.ss)

            if str(key) == self.super_key and self.super_key in self.keys and self.key_lock:
                try:
                    for k, v in itertools.islice(self.hot_keys.items(), 1, None):
                        key1.unblock_key(k)
                    self.key_lock= False
                    print('解锁完成pass')
                except:
                    pass
            if str(key) not in self.keys:
                if self.hot_num==0:
                    self.hot_num += 1
            elif self.hot_num == 0:
                self.hot_num += 1
                # self.keys_pressed.remove(key)
                while str(key) in self.keys:
                    self.keys.remove(str(key))
                try:
                    kn = key.name
                    kn = kn.replace('l_l', 'l')
                    kn = kn.replace('l_r', 'l')
                    kn = kn.replace('t_l', 'l')
                    kn = kn.replace('t_r', 'l')
                    key1.release(kn)
                except:
                    print(key)
                    kn = key.char
                    kn = kn.replace('l_l', 'l')
                    kn = kn.replace('l_r', 'l')
                    kn = kn.replace('t_l', 'l')
                    kn = kn.replace('t_r', 'l')
                    key1.release(kn)
            self.hot_num -= 1
            print(f'释放 {key}')

            # if key == keyboard.Key.esc:
            #     return False

    def detect_keys(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()



class TrayIcon:
    def __init__(self):
        self.zongduan=False

        self.image = Image.open("icon.png")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.menu = [
            # pystray.MenuItem("重新加载", lambda: self.reload_program()),
            pystray.MenuItem("关注我：获取更新", lambda: self.open_webpage()),
            pystray.MenuItem("打开文件位置", lambda: self.open_file_location()),
            pystray.MenuItem("退出", lambda: self.exit_program())

        ]
        self.tray_icon = pystray.Icon("name", self.image, "空", self.menu)
        self.tray_icon.menu = self.menu
        self.tray_icon.onClick = self.on_click



    def open_webpage(url):
        webbrowser.open('https://space.bilibili.com/34831394')
    def create_tray_icon(self):

        self.tray_icon.run()


    def on_click(self, icon, item):
        print("Tray icon clicked.")

    def reload_program(self):
        python = sys.executable
        script = os.path.abspath(__file__)
        subprocess.Popen([python, script])
        self.zongduan=True
        self.exit_program()

    def open_file_location(self):
        # path = os.path.abspath(__file__)
        script_path = os.path.abspath(sys.argv[0])
        directory = os.path.dirname(script_path)
        print(directory)
        if sys.platform.startswith('win'):
            os.startfile(directory)
        elif sys.platform.startswith('darwin'):
            subprocess.Popen(['open', directory])
        else:
            subprocess.Popen(['xdg-open', directory])

    def exit_program(self):
        if self.zongduan:
            self.zongduan=False
            self.tray_icon.stop()
            sys.exit()
        else:
            self.tray_icon.stop()
            ctypes.windll.kernel32.ExitProcess(0)



def run_key_detection():
    key_detector = super_keys()
    key_detector.detect_keys()

# 启动程序
if __name__ == "__main__":
    tray_icon = TrayIcon()
    key_thread = threading.Thread(target=run_key_detection)
    key_thread.start()
    tray_icon.create_tray_icon()