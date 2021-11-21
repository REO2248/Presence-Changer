# Presence Changer 
[qwerty同志](https://github.com/qwertyquerty/)の[pypresence](https://github.com/qwertyquerty/pypresence)を使用したDiscordのPresence(ステータス)を変更するプログラムです。

[Firestormfan同志](https://github.com/Firestormfan/)の[
Presence-Changer](https://github.com/Firestormfan/Presence-Changer)を改変したDiscordのPresence(ステータス)を変更するプログラムです。

[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

# 変更内容
flaskを使ってwebブラウザーから設定できるようにしたよ。

# 最初に
Presence Changerには[Developer Portal](https://discord.com/developers/applications)のApplicationが必要です。
事前に作成しておくことをお勧めします。

# 使い方
1. install.batを起動する
2. config.jsonで設定する
3. run.batを起動する
4. 楽しむ

# Config
ClientID以外は起動後[localhostのポート8081](http://localhost:8081)で設定できます。

## main
| 設定名 | 内容 |
:---|:---
| ClientID | Developer PortalのClientID |
| State | 今行っていることを表示する場所(残り人数等) |
| Details | Stateの位置違い |
| Time | 残り時間を表示するか trueかfalseで指定 |
| Large_Image | プレイしているゲームの画像(後述) |
| Large_Text | Large_Imageにカーソルを合わせたときに表示される文 |
| Small_Image | Large_Imageの右下に表示される画像 |
| Small_Text | Large_Textと同じ |
## button
| 設定名 | 内容 |
:---|:---
| button | ボタンをオンにするかどうか trueかfalseで指定 |
| button1_label | 一つ目のボタンに表示される文字 |
| button1_url | 一つ目のボタンを押した時に飛ぶリンク |
| button2_label | button1_labelと同じ 何も入力しないとボタン2がなくなる |
| button2_url | button1_urlと同じ |

# Image
Rich PresenceタブのArt Assetsに行き、Add Image(s)から登録できます。
![dev](https://cdn.discordapp.com/attachments/836119816900313100/909561230795087902/unknown.png)

# Tips
State, Detailsは空にできません。  
button2_label または button2_url を "" にすると、ボタン2を消すことができます。

# わからないことがある、エラーがでた
自己解決してください

# 最後に
Presence Changerを不正に使用して生じた損害に関しては、誰も責任を負いません。
