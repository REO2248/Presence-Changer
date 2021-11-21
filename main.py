"""
MIT License

Copyright (c) 2021 FirestormFan / SRPN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pypresence
import time
import traceback
import json
import sys
from flask import Flask, render_template, request
from threading import Thread

app = Flask('',template_folder="./")
start = None
end = None

def reset_start():
    global start
    if Time == False:
        start = None
    else:
        start = time.time()


def reload():
    global config
    global ClientID
    global State
    global Details
    global Time
    global Large_Image
    global Large_Text
    global Small_Image
    global Small_Text
    global Buttons
    global IsbuttonsTrue
    global Button
    global Port

    config = json.load(open("config.json", "r", encoding="utf-8"))
    ClientID = config["main"]["ClientID"]
    State = config["main"]["State"]
    Details = config["main"]["Details"]
    Time = config["main"]["time"]
    Large_Image = config["main"]["Large_Image"]
    Large_Text = config["main"]["Large_Text"]
    Small_Image = config["main"]["Small_Image"]
    Small_Text = config["main"]["Small_Text"]
    Buttons = config["button"]
    IsbuttonsTrue = Buttons["button"]
    Port = config["web"]["port"]

    Button = [
        {
            "label": Buttons["button1_label"],
            "url": Buttons["button1_url"]
        },
        {
            "label": Buttons["button2_label"],
            "url": Buttons["button2_url"]
        }
    ]
    if Buttons["button2_label"] == "" or Buttons["button2_url"] == "":
        Button.pop()

reload()
reset_start()

def run():
    app.run(host="0.0.0.0", port=Port)



RPC = pypresence.Presence(ClientID)

try:
    RPC.connect()
    print("Discordを検出しました。")
except pypresence.exceptions.InvalidPipe:
    x = input("Discordが検出されませんでした。 再検出を開始する場合は y と入力してください。")
    if x == "y":
        for i in range(10):
            if not i == 9:
                try:
                    print(f"再検出中...({i+1})")
                    RPC.connect()
                    break
                except pypresence.exceptions.InvalidPipe:    
                    time.sleep(4)
            if i == 9:
                print("再検出に失敗しました。")
                input("終了します。")
                exit()
    else:
        exit()

def update():
    reload()
    if IsbuttonsTrue:
        RPC.update(
            state=State,
            details=Details,
            start=start,
            large_image=Large_Image,
            large_text=Large_Text,
            small_image=Small_Image,
            small_text=Small_Text,
            buttons=Button,
        )
    else:
        RPC.update(
            state=State,
            details=Details,
            start=start,
            large_image=Large_Image,
            large_text=Large_Text,
            small_image=Small_Image,
            small_text=Small_Text,
        )
    print("updated")

server = Thread(target=run)
server.setDaemon(True)
server.start()

CLIENT_ID=ClientID

def main():
    print("Rich Presenceへ接続完了！ RichなDiscordが今、始まる！")
    try:
        while True:
            update()
            time.sleep(15)
    except KeyboardInterrupt:
        print("停止させています...")
        RPC.close()
        print("Rich Presenceから切断しました!")
        sys.exit()
    except Exception as e:
        print(traceback.format_exc())
        input("エラーが発生しました。繰り返し発生する場合は諦めてください。")
        time.sleep(3)
        RPC.close()
        sys.exit()
        exit()

@app.route('/')
def rootpage():
    return render_template("index.html",clientid=CLIENT_ID)

@app.route('/reset', methods=['GET', 'POST'])
def web_resettimer():
    reset_start()
    update()
    return "timer reseted"

@app.route("/update/main/<parameter>", methods=['GET', 'POST'])
def web_update(parameter):
    print(parameter in config["main"])
    if parameter in config["main"]:
        config["main"][parameter] = request.form["value"]
        with open("config.json", mode="wt",encoding="utf-8") as file:
            json.dump(config,file,ensure_ascii=False,indent=4)
        update()
        return ""
    return ""

@app.route("/update/buttons/button/<boool>", methods=['GET', 'POST'])
def web_button_button_update(boool):
    
    if boool == "True":
        config["button"]["button"] = True
    elif boool == "False":
        config["button"]["button"] = False
    else:
        print("どっちでもない")
    with open("config.json", mode="wt",encoding="utf-8") as file:
        json.dump(config,file,ensure_ascii=False,indent=4)
    update()
    return ""

@app.route("/update/buttons/<parameter>", methods=['GET', 'POST'])
def web_buttons_update(parameter):
    print(parameter in config["button"])
    if parameter in config["button"]:
        config["button"][parameter] = request.form["value"]
        with open("config.json", mode="wt",encoding="utf-8") as file:
            json.dump(config,file,ensure_ascii=False,indent=4)
        update()
        return ""
    return ""

main()