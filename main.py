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
import json

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

if Buttons["button2_label"] or Buttons["button2_url"] is None:
    Button.pop()

if Time == False:
    start = None
else:
    start = time.time()

RPC = pypresence.Presence(ClientID)
RPC.connect()
print("接続完了!")

if IsbuttonsTrue:
    while True:
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
        time.sleep(15)
else:
    while True:
        RPC.update(
            state=State,
            details=Details,
            start=start,
            large_image=Large_Image,
            large_text=Large_Text,
            small_image=Small_Image,
            small_text=Small_Text,
        )
        time.sleep(15)