import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import urllib.parse
import yt_dlp
import cloudscraper
import m3u8
import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web

import online.helpers.vid as helper
from online.Config import *
from online.helpers.button import keyboard
from online.helpers.sudoers import *
from online.helpers.text import *

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from vars import sudo_users, owner_users  # Ensure these are imported

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

my_name = "IRA"

cookies_file_path = os.getenv("COOKIES_FILE_PATH", "youtube_cookies.txt")

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://text-leech-bot-for-render.onrender.com/")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await bot.polling()  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
    

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await asyncio.sleep(3600)  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
        
class Data:
    START = (
        "🌟 Welcome {0}! 🌟\n\n"
    )
# Define the start command handler
@bot.on_message(filters.command("start"))
async def start(client: Client, msg: Message):
    user = await client.get_me()
    mention = user.mention
    start_message = await client.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention)
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Initializing Uploader bot... 🤖\n\n"
        "Progress: [⬜⬜⬜⬜⬜⬜⬜⬜⬜] 0%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Loading features... ⏳\n\n"
        "Progress: [🟥🟥🟥⬜⬜⬜⬜⬜⬜] 25%\n\n"
    )
    
    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "This may take a moment, sit back and relax! 😊\n\n"
        "Progress: [🟧🟧🟧🟧🟧⬜⬜⬜⬜] 50%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Checking Bot Status... 🔍\n\n"
        "Progress: [🟨🟨🟨🟨🟨🟨🟨⬜⬜] 75%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        Data.START.format(msg.from_user.mention) +
        "Checking status Ok... Command Nhi Bataunga **Bot Made BY IRA™👨🏻‍💻**🔍\n\n"
        "Progress:[🟩🟩🟩🟩🟩🟩🟩🟩🟩] 100%\n\n"
    )

@bot.on_message(filters.command(["stop"]) )
async def restart_handler(_, m):
    await m.reply_text("**STOPPED**🛑", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["alpha"]) )
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text(f"**🔹Hi I am Poweful TXT Downloader📥 Bot.**\n🔹**Send me the TXT file and wait.**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"ALONE™🇮🇳"
    token = f"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzYxNTE3MzAuMTI2LCJkYXRhIjp7Il9pZCI6IjYzMDRjMmY3Yzc5NjBlMDAxODAwNDQ4NyIsInVzZXJuYW1lIjoiNzc2MTAxNzc3MCIsImZpcnN0TmFtZSI6IkplZXYgbmFyYXlhbiIsImxhc3ROYW1lIjoic2FoIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sImVtYWlsIjoiV1dXLkpFRVZOQVJBWUFOU0FIQEdNQUlMLkNPTSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTczNTU0NjkzMH0.iImf90mFu_cI-xINBv4t0jVz-rWK1zeXOIwIFvkrS0M"
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
   
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    try:
        arg = int(raw_text)
    except:
        arg = 1
    await editable.edit("**Enter Your Batch Name or send d for grabing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution.\n Eg : 480 or 720**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name or send 'de' for use default.\n Eg : ALONE™👨🏻‍💻**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3
        
    await editable.edit("**Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋  or send 'unknown' for use default**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)
    if raw_text4 == 'unknown':
        MR = token
    else:
        MR = raw_text4
        
    await editable.edit("Now send the **Thumb url**\n**Eg :** ``\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    count =int(raw_text)    
    try:
        for i in range(arg-1, len(links)):

            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
                

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "videos.classplusapp.com" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r'}).json()['url']

            
            elif '/master.mpd' in url:
             vid_id =  url.split("/")[-2]
             url =  f"https://madxapi-d0cbf6ac738c.herokuapp.com/{vid_id}/master.m3u8?token={raw_text4}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]} {my_name}'
                      
            
            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**🎞️ VID_ID: {str(count).zfill(3)}.\n\n📄 Title: {name1} {res}.mkv\n\n<pre><code>📚 Batch Name: {b_name}</code></pre>\n\n📥 Extracted By : {CR}\n\n**━━━━━✦dara❤️✦━━━━━**'
                cc1 = f'**📁 PDF_ID: {str(count).zfill(3)}.\n\n📄 Title: {name1} .pdf\n\n<pre><code>📚 Batch Name: {b_name}</code></pre>\n\n📥 Extracted By : {CR}\n\n**━━━━━✦dara❤️✦━━━━━**'
                    
                
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
        # Replace spaces with %20 in the URL
                        url = url.replace(" ", "%20")
 
        # Create a cloudscraper session
                        scraper = cloudscraper.create_scraper()

        # Send a GET request to download the PDF
                        response = scraper.get(url)

        # Check if the response status is OK
                        if response.status_code == 200:
            # Write the PDF content to a file
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)

            # Send the PDF document
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1

            # Remove the PDF file after sending
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                       
                          
                else:
                    Show = f"❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📄 Title:- `{name}\n\n⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**🔗 𝐔𝐑𝐋 »** \n\n**𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ MAHAKAL"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝\n\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("🔰Done🔰")

# Advance

@bot.on_message(filters.command(["alpha1"]) )
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text(f"**📁Send me the TXT file and wait.**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"ALONE™🇮🇳"
    
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
   
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    try:
        arg = int(raw_text)
    except:
        arg = 1
    await editable.edit("**Enter Your Batch Name or send d for grabing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution.\n Eg : 480 or 720**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name or send 'de' for use default.\n Eg : MAYA ™👨🏻‍💻**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3
        
       
    await editable.edit("Now send the **Thumb url**\n**Eg :** ``\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    count =int(raw_text)    
    try:
        for i in range(arg-1, len(links)):

            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
                

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "videos.classplusapp.com" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r'}).json()['url']

            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)


             
            elif '/master.mpd' in url:
             vid_id =  url.split("/")[-2]
             url =  f"https://pw-links-api.onrender.com/process?v=https://sec1.pw.live/{vid_id}/master.mpd&quality={raw_text2}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]} {my_name}'
          

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**🎞️ VID_ID: {str(count).zfill(3)}.\n\nTitle: {name1} KING {res}.mkv\n\n📚 Batch Name: {b_name}\n\n📥 Extracted By : {CR}\n\n**━━━━━✦📖🇮🇳📖✦━━━━━**'
                cc1 = f'**📁 PDF_ID: {str(count).zfill(3)}.\n\nTitle: {name1} KING.pdf\n\n📚 Batch Name: {b_name}\n\n📥 Extracted By : {CR}\n\n**━━━━━✦📖🇮🇳📖✦━━━━━**'
                    
                
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
        # Replace spaces with %20 in the URL
                        url = url.replace(" ", "%20")
 
        # Create a cloudscraper session
                        scraper = cloudscraper.create_scraper()

        # Send a GET request to download the PDF
                        response = scraper.get(url)

        # Check if the response status is OK
                        if response.status_code == 200:
            # Write the PDF content to a file
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)

            # Send the PDF document
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1

            # Remove the PDF file after sending
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                       
                          
                else:
                    Show = f"❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📄 Title:- `{name}\n\n⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n** »** `{url}`\n\n**𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ SOLO"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝\n\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("🔰Done🔰")

# KRISHAN 

@bot.on_message(filters.command(["alpha2"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text(f"**🔹Send me the TXT file and wait.**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"KRISHAN™🇮🇳"
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
   
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    try:
        arg = int(raw_text)
    except:
        arg = 1
    await editable.edit("**Enter Your Batch Name or send d for grabing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution.\n Eg : 480 or 720**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name or send 'de' for use default.\n Eg : KRISHAN™👨🏻‍💻**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3
        
    await editable.edit("Now send the **Thumb url**\n**Eg :** ``\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    count =int(raw_text)    
    try:
        for i in range(arg-1, len(links)):

            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
                

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "videos.classplusapp.com" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
                    
            elif '/master.mpd' in url:
             vid_id =  url.split("/")[-2]
             url =  f"https://pw-links-api.onrender.com/process?v=https://sec1.pw.live/{vid_id}/master.mpd&quality={raw_text2}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]} {my_name}'
                      

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**🎞️ VID_ID: {str(count).zfill(3)}.\n\n Title: {name1} MAYA {res}.mkv\n\n📚 Batch Name: {b_name}\n\n📥 Extracted By : {CR}\n\n**━━━━━✦📖🇮🇳📖✦━━━━━**'
                cc1 = f'**📁 PDF_ID: {str(count).zfill(3)}.\n\n Title: {name1} @MAYA.pdf\n\n📚 Batch Name: {b_name}\n\n📥 Extracted By : {CR}\n\n**━━━━━✦📖🇮🇳📖✦━━━━━**'
                    
                
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
        # Replace spaces with %20 in the URL
                        url = url.replace(" ", "%20")
 
        # Create a cloudscraper session
                        scraper = cloudscraper.create_scraper()

        # Send a GET request to download the PDF
                        response = scraper.get(url)

        # Check if the response status is OK
                        if response.status_code == 200:
            # Write the PDF content to a file
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)

            # Send the PDF document
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1

            # Remove the PDF file after sending
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                       
                          
                else:
                    Show = f"❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📄 Title:- `{name}\n\n⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n** »** `\n\n**𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ KING"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝\n\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("🔰Done🔰")
    await m.reply_text("✨Thankyou For Choosing")

# m3u8

@bot.on_message(filters.command(["maya1"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text(f"**🔹Send me the TXT file and wait.**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    file_name, ext = os.path.splitext(os.path.basename(x))
    credit = f"maya™🇮🇳"
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
   
    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    try:
        arg = int(raw_text)
    except:
        arg = 1
    await editable.edit("**Enter Your Batch Name or send d for grabing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0

    await editable.edit("**Enter resolution.\n Eg : 480 or 720**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("**Enter Your Name or send 'de' for use default.\n Eg : mahadev™👨🏻‍💻**")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    else:
        CR = raw_text3

    await editable.edit("**Enter Your PW Token For 𝐌𝐏𝐃 𝐔𝐑𝐋  or send 'unknown' for use default**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)
    if raw_text4 == 'unknown':
        MR = raw_text4
    else:
        MR = raw_text4
        
    await editable.edit("Now send the **Thumb url**\n**Eg :** ``\n\nor Send `no`")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    count =int(raw_text)    
    try:
        for i in range(arg-1, len(links)):

            Vxy = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","")
            url = "https://" + Vxy
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
                

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "videos.classplusapp.com" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
                    
            elif '/master.m3u8' in url:
             vid_id =  url.split("/")[-2]
             url =  f"https://madxapi-d0cbf6ac738c.herokuapp.com/{vid_id}/master.m3u8?token={raw_text4}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]} {my_name}'
                      

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**🎞️ VID_ID: {str(count).zfill(3)}.\n\n Title: {name1} @MAYA {res}.mkv\n\n📚 Batch Name: {b_name}\n\n📥 Extracted By : {CR}\n\n**━━━━━✦MAYA❤️✦━━━━━**'
                cc1 = f'**📁 PDF_ID: {str(count).zfill(3)}.\n\n Title: {name1} @MAYA.pdf\n\n📚 Batch Name: {b_name}\n\n📥 Extracted By : {CR}\n\n**━━━━━✦MAYA❤️✦━━━━━**'
                    
                
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
        # Replace spaces with %20 in the URL
                        url = url.replace(" ", "%20")
 
        # Create a cloudscraper session
                        scraper = cloudscraper.create_scraper()

        # Send a GET request to download the PDF
                        response = scraper.get(url)

        # Check if the response status is OK
                        if response.status_code == 200:
            # Write the PDF content to a file
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)

            # Send the PDF document
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1

            # Remove the PDF file after sending
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                       
                          
                else:
                    Show = f"❊⟱ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 ⟱❊ »\n\n📄 Title:- `{name}\n\n⌨ 𝐐𝐮𝐥𝐢𝐭𝐲 » {raw_text2}`\n\n**🔗 𝐔𝐑𝐋 »** `\n\n**𝐁𝐨𝐭 𝐌𝐚𝐝𝐞 𝐁𝐲 ✦ maya"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                f"⌘ 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐈𝐧𝐭𝐞𝐫𝐮𝐩𝐭𝐞𝐝\n\n⌘ 𝐍𝐚𝐦𝐞 » {name}\n⌘ 𝐋𝐢𝐧𝐤 » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("🔰Done🔰")
    await m.reply_text("✨Thankyou For Choosing")

@bot.on_message(filters.command(["help"]))
async def start_handler(bot: Client, m: Message):
    await m.reply_text(f"Hello Im TxT File Downloader\n\n**Steps To Use Bot:**\n **1:** Send /up_vid to Upload Videos in Streamable Formate & then Send Your .txt file.\n **2:** Now Send From Where You Want To    Download Initial is 0 .\n **3:** Now Send Your File Name or Use `de` For.  Use Default File Name.\n **4:** Now Send Resolution In Which Quality    You Want.\n **5:** Now Send Custom Thum URL or    Send `no` to Use Defalut Thumbnail.\n **6:** Now Wait Bot will Download & Upload Your Videos.\n\n**Bot made by {owner} & Updated By {channel} **")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
@bot.on_message(filters.command(["cancel"]))
async def cancel_handler(bot: Client, m: Message):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
    
@bot.on_message(filters.command(["restart"]))
async def restart_handler(bot: Client, m: Message):
    await m.reply_text("Bot Restarted! ♻️", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["start"]))
async def start_handler(bot: Client, m: Message):
    editable = await m.reply_text("**Hi!, I'm PyroBot. I Can Download All Links In A Txt File & Send Them To You.\n\nUse /help To Get Some Help 😉\n\n Use /up_vid Command to Upload Videos in Streamable Formate & /up_dov to Upload In Document Formate!!!**")


@bot.on_message(filters.command(["up_vid"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file Now**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    
    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Title For File. Send 'De' To Use Default File Name.**")
    input0: Message = await bot.listen
    raw_text0 = input0.text
    if raw_text0 == 'De':
        CR = raw_text0

    
    await m.reply_text("**Enter Resolution \nExamples: __480 = SD Quality\n             720 = HD Quality\n             1080 = FHD Quality__**")
    input2: Message = await bot.listen
    raw_text2 = input2.text
        
    editable4= await m.reply_text("Now send the **Thumb url**\nEg : https://telegra.ph/file/d9e24878bd4abyhga05049a1.jpg\n\nElse Send **No**")
    input6 = message = await bot.listen
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    


    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").replace("^ँ-ःअ-ऍए-ऑओ-नप-रलळव-ह़-ॅे-ॉो-्ॐ\u200c\u200da-zA-Z\s\d\.,:;।॥?\-","").strip()



            if raw_text2 =="144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']    
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)              
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"                        

            elif raw_text2 =="240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)          
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)             
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']  
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)               
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']                        
                elif '854x470' in out:
                    ytf = out['854x470']  
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf =['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']   
                elif 'unknown' in out:
                    ytf = out["unknown"]                     
                else:
                    ytf = "no"


            elif raw_text2 =="720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)           
                if '1280x720' in out:
                    ytf = out['1280x720'] 
                elif '1280x704' in out:
                    ytf = out['1280x704'] 
                elif '1280x474' in out:
                    ytf = out['1280x474'] 
                elif '1920x712' in out:
                    ytf = out['1920x712'] 
                elif '1920x1056' in out:
                    ytf = out['1920x1056']    
                elif '854x480' in out:
                    ytf = out['854x480']                        
                elif '640x360' in out:
                    ytf = out['640x360']     
                elif 'unknown' in out:
                    ytf = out["unknown"]              
                else:
                    ytf = "no"
                    
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf= 'http-240p'
                elif raw_text2 == "240":
                    ytf= 'http-240p'
                elif raw_text2 == '360':
                    ytf= 'http-360p'
                elif raw_text2 == '480':
                    ytf= 'http-540p'
                elif raw_text2 == '720':
                    ytf= 'http-720p'
                elif raw_text2 == '1080':
                    ytf= 'http-1080p'
                else:
                    ytf = 'http-360p'
            else:
                ytf="no"

            if ytf == "0":
                res = "0"
            elif ytf == "no" or ytf == "mp4":
                res = "NA"
            else:
                res = list(out.keys())[list(out.values()).index(ytf)]

            name = f'{name1}'


            if "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mp4 "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" in url:
                cmd = "pdf"
            elif "drive" in url:
                cmd = "pdf"
            elif ytf == "no":
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mp4 "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'



            try:
                Show = f"**Downloading:-**\n\n**Name »** `{name}`\n**Quality »** `{raw_text2}`\n\n**Url »** `{url}`\n\n"
                prog = await m.reply_text(Show)
                cc = f'**File Name »** {name1} {video}\n**Quality »** {raw_text2}'
                cc1 =f'**File No. »** {str(count).zfill(3)}\n**File Name »** {name1} {pdf}\n'
                if cmd == "pdf" or "drive" in url:
                    try:
                        ka=await helper.download(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        #await helper.send_video(bot,m,cc,ka,cc1,prog,count,name)
                        reply = await m.reply_text(f"Uploading » {str(count).zfill(3)}-{name}\n\n")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka,caption=cc1,progress=progress_bar,progress_args=(reply,start_time))
                        count+=1
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                    
                elif cmd == "pdf" or ".pdf" in url:
                    try:
                        ka=await helper.aio(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading » {str(count).zfill(3)}-{name}\n\n")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=f'**File No. »** {str(count).zfill(3)}\n**File Name »** {name1} {pdf}\n')
                        count+=1
                        # time.sleep(1)
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url,cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m,cc,filename,thumb,name,prog)
                    count+=1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`")
                continue


    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")    


@bot.on_message(filters.command(["up_doc"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter Resolution \nExamples: __480 = SD Quality\n             720 = HD Quality\n             1080 = FHD Quality__**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : https://telegra.ph/file/d9e24878bd4abyhga05049a1.jpg\n\nElse Send **No**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    

    
    try:
        for i in range(arg, len(links)):
            
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
            
            if "jwplayer" in url:
                headers = {
                    'Host': 'api.classplusapp.com',
                    'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0',
                    'user-agent': 'Mobile-Android',
                    'app-version': '1.4.37.1',
                    'api-version': '18',
                    'device-id': '5d0d17ac8b3c9f51',
                    'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30',
                    'accept-encoding': 'gzip',
                }

                params = (
                    ('url', f'{url}'),
                )

                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                # print(response.json())
                a = response.json()['url']
                # print(a)


                headers1 = {
                    'User-Agent': 'ExoPlayerDemo/1.4.37.1 (Linux;Android 11) ExoPlayerLib/2.14.1',
                    'Accept-Encoding': 'gzip',
                    'Host': 'cdn.jwplayer.com',
                    'Connection': 'Keep-Alive',
                }


                response1 = requests.get(f'{a}', headers=headers1)

                url1 = (response1.text).split("\n")[2]
                            
#                 url1 = b
            else:
                url1 = url

            
            
            name = f'{name1}'    
            Show = f"**Downloading:-**\n\n**Name :-** `{name} {video}`\n\n**Url :-** `{url1}`\n\n"
            prog = await m.reply_text(Show)
            cc = f'**Title »** {name1}.mkv {video}\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
            if "pdf" in url:
                cmd = f'yt-dlp -o "{name}.pdf" "{url1}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url1}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                

                if os.path.isfile(f"{name}.mkv"):
                    filename = f"{name}.mkv"
                elif os.path.isfile(f"{name}.mp4"):
                    filename = f"{name}.mp4"  
                elif os.path.isfile(f"{name}.pdf"):
                    filename = f"{name}.pdf"  
                   #filename = f"{name}.mkv"
                subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete (True)
                reply = await m.reply_text(f"Uploading » {str(count).zfill(3)}-{name}\n\nRemaining » {remain} Files")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e)) 

                dur = int(helper.duration(filename))

                start_time = time.time()
                if "pdf" in url1:
                    await m.reply_document(filename,caption=cc)
                else:
                    await m.reply_video(filename,supports_streaming=True,height=720,width=1280,caption=cc,duration=dur,thumb=thumbnail, progress=progress_bar,progress_args=(reply,start_time) )
                count+=1
                os.remove(filename)

                os.remove(f"{filename}.jpg")
                await reply.delete (True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}` & `{url1}`")
                continue 
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done") 

@bot.on_message(filters.command(["start"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text("Hello im txt file downloader\nPress /pyro to download links listed in a txt file in the format **Name:link**\n\nBot made by BATMAN")

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@bot.on_message(filters.command(["pyro"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
    
    
    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4= await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)    

    
    try:
        for i in range(arg, len(links)):
            
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()



            if raw_text2 =="144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']    
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)              
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"                        

            elif raw_text2 =="240":
                
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)          
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="360":
            
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)             
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']  
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="480":
                
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)               
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']                        
                elif '854x470' in out:
                    ytf = out['854x470']  
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf =['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']   
                elif 'unknown' in out:
                    ytf = out["unknown"]                     
                else:
                    ytf = "no"

                   
            elif raw_text2 =="720":
                
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)           
                if '1280x720' in out:
                    ytf = out['1280x720'] 
                elif '1280x704' in out:
                    ytf = out['1280x704'] 
                elif '1280x474' in out:
                    ytf = out['1280x474'] 
                elif '1920x712' in out:
                    ytf = out['1920x712'] 
                elif '1920x1056' in out:
                    ytf = out['1920x1056']    
                elif '854x480' in out:
                    ytf = out['854x480']                        
                elif '640x360' in out:
                    ytf = out['640x360']     
                elif 'unknown' in out:
                    ytf = out["unknown"]              
                else:
                    ytf = "no"
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf= 'http-240p'
                elif raw_text2 == "240":
                    ytf= 'http-240p'
                elif raw_text2 == '360':
                    ytf= 'http-360p'
                elif raw_text2 == '480':
                    ytf= 'http-540p'
                elif raw_text2 == '720':
                    ytf= 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                ytf="no"

            if ytf == "0":
                res = "0"
            elif ytf == "no" or ytf == "mp4":
                res = "NA"
            else:
                res = list(out.keys())[list(out.values()).index(ytf)]

            name = f'{str(count).zfill(3)}) {name1} {res}'


            if "youtu" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={int(raw_text2)}]+bestaudio" --no-keep-video --remux-video mkv "{url}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" in url:
                cmd = "pdf"
            elif "drive" in url:
                cmd = "pdf"
            elif ytf == "no":
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
                


            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`\n\n"
                prog = await m.reply_text(Show)
                cc = f'**Title »** {name1} {res}.mkv\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
                cc1 =f'**Title »** {name1} {res}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}'
                if cmd == "pdf" or "drive" in url:
                    try:
                        ka=await helper.download(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)
                        reply = await m.reply_text(f"Uploading - `{name}`")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka,caption=cc1)
                        count+=1
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue                    
                elif cmd == "pdf" or ".pdf" in url:
                    try:
                        ka=await helper.aio(url,name)
                        await prog.delete (True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=f'**Title »** {name1} {res}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}')
                        count+=1
                        # time.sleep(1)
                        await reply.delete (True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url,cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m,cc,filename,thumb,name,prog)
                    count+=1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`")
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")   

@bot.on_message(filters.command(["adda_pdf"]))
async def adda_pdf(bot: Client, m: Message):
    editable = await m.reply_text(f"**Hi im Pdf Adda pdf dl**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)
    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split("://", 1))
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
         
    editable2 = await m.reply_text("**Enter Token**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text    
         
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)        
           
    try:
        for i in range(arg, len(links)):
        
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace(":","").replace("*","").replace(".","").replace("'","").replace('"','').strip()
            name = f'{str(count).zfill(3)} {name1}'    
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n'   
            try:
                getstatusoutput(f'curl --http2 -X GET -H "Host:store.adda247.com" -H "user-agent:Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36" -H "accept:*/*" -H "x-requested-with:com.adda247.app" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://store.adda247.com/build/pdf.worker.js" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US,en;q=0.9" -H "cookie:cp_token={raw_text5}" "{url}" --output "{name}.pdf"')
                await m.reply_document(f"{name}.pdf",caption=cc)
                count+=1
                await prog.delete (True)
                os.remove(f"{name}.pdf")
                time.sleep(2)
            except Exception as e:
                await m.reply_text(f"{e}\nDownload Failed\n\nName : {name}\n\nLink : {url}")
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")

    
@bot.on_message(filters.command(["jw"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text


    try:
        arg = int(raw_text)
    except:
        arg = 0
      
    editable2 = await m.reply_text("**Enter Token**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text    
    
        
    if raw_text =='0':
        count =1
    else:       
        count =int(raw_text)        
           
    try:
        for i in range(arg, len(links)):
        
            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace(":","").replace("*","").replace(".","").replace("'","").replace('"','').strip()
            name = f'{str(count).zfill(3)} {name1}'    
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n'   
            try:
                getstatusoutput(f'curl --http2 -X GET -H "Host:store.adda247.com" -H "user-agent:Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36" -H "accept:*/*" -H "x-requested-with:com.adda247.app" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://store.adda247.com/build/pdf.worker.js" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US,en;q=0.9" -H "cookie:cp_token={raw_text5}" "{url}" --output "{name}.pdf"')
                await m.reply_document(f"{name}.pdf",caption=cc)
                count+=1
                await prog.delete (True)
                os.remove(f"{name}.pdf")
                time.sleep(2)
            except Exception as e:
                await m.reply_text(f"{e}\nDownload Failed\n\nName : {name}\n\nLink : {url}")
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")

    
@bot.on_message(filters.command(["jw"]))
async def txt_handler(bot: Client, m: Message):
    editable = await m.reply_text("Send txt file**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)     
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4 = await m.reply_text(
        "Now send the **Thumb url**\nEg : ```https://graph.org/file/ce1723991756e48c35aa1.jpg```\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data1 in out:
                        ytf = out[data1]
            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data2 in out:
                        ytf = out[data2]
            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data3 in out:
                        ytf = out[data3]
            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif '1280x720' in out:
                    ytf = out['1280x720']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data4 in out:
                        ytf = out[data4]
            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data5 in out:
                        ytf = out[data5]

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data6 in out:
                        ytf = out[data6]
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf = 'http-240p'
                elif raw_text2 == "240":
                    ytf = 'http-240p'
                elif raw_text2 == '360':
                    ytf = 'http-360p'
                elif raw_text2 == '480':
                    ytf = 'http-540p'
                elif raw_text2 == '720':
                    ytf = 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                for dataS in out:
                    ytf = out[dataS]

            try:
                if "unknown" in out:
                    res = "NA"
                else:
                    res = list(out.keys())[list(out.values()).index(ytf)]

                name = f'{str(count).zfill(3)}) {name1} {res}'
            except Exception:
                res = "NA"

            # if "youtu" in url:
            # if ytf == f"'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'" or "acecwply" in url:
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mkv --no-warning "{url}" -o "{name}.%(ext)s"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" or "download" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`"
                prog = await m.reply_text(Show)
                cc = f"**Name »** {name1} {res}.mkv\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                cc1 = f"**Name »** ** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f"**Name »** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                        )
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        logging.error(e)
                        
        await m.reply_text(e)
    await m.reply_text("Done")


@bot.on_message(filters.command(["pro_top"]))
async def account_login_top(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    editable = await m.reply_text("Send Txt File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    
    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    
    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(range(int(raw_text) - 1, len(content)),
                                  start=int(raw_text)):

            name1, link = content[i].split(":", 1)
            cook, url = requests.get(
                f"https://api.telegramadmin.ga/gurukul/link={link}").json().values()

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            prog = await m.reply_text(Show)
            cc = f'**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}'
            if "youtu" in url:
                cmd = f'yt-dlp -f best "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name,
                                        prog)
                count += 1
                
                
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")

@bot.on_message(filters.command(["pro_vision"]))
async def account_login_vision(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    editable = await m.reply_text("send txt file")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"
     
    
    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    
    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(range(int(raw_text) - 1, len(content)),
                                  start=int(raw_text)):

            name1, link = content[i].split(":", 1)
            url = requests.get(
                f"https://api.telegramadmin.ga/vision/link={link}").json()["link"]
            cook = None

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            prog = await m.reply_text(Show)
            cc = f'**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}\n\n**Download BY** :- Group Admin'
            if "vision" or "youtu" in url:
                cmd = f'yt-dlp "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name,
                                        prog)
                count += 1
                
                
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")

@bot.on_message(filters.command(["adda_pdf"]))
async def account_login_adda(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    editable = await m.reply_text("Send Txt File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable2 = await m.reply_text("**Enter Token**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace(
                "+",
                "").replace("#", "").replace("|", "").replace("@", "").replace(
                    ":", "").replace("*", "").replace(".", "").replace(
                        "'", "").replace('"', '').strip()
            name = f'{str(count).zfill(3)} {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n'
            try:
                getstatusoutput(
                    f'curl --http2 -X GET -H "Host:store.adda247.com" -H "user-agent:Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36" -H "accept:*/*" -H "x-requested-with:com.adda247.app" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://store.adda247.com/build/pdf.worker.js" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US,en;q=0.9" -H "cookie:cp_token={raw_text5}" "{url}" --output "{name}.pdf"'
                )
                await m.reply_document(f"{name}.pdf", caption=cc)
                count += 1
                await prog.delete(True)
                os.remove(f"{name}.pdf")
                time.sleep(2)
            except Exception as e:
                await m.reply_text(
                    f"{e}\nDownload Failed\n\nName : {name}\n\nLink : {url}")
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")



@bot.on_message(filters.command(["pro_olive"]))
async def account_login_olive(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    editable = await m.reply_text("Send Txt File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"
     
    
    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    
    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(range(int(raw_text) - 1, len(content)),
                                  start=int(raw_text)):

            name1, link = content[i].split(":", 1)
            url = requests.get(
                f"https://api.telegramadmin.ga/olive/link={link}").json()["m3u8"]
            cook = None

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            prog = await m.reply_text(Show)
            cc = f'**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}\n\n**Download BY** :- Group Admin'
            if "olive" or "youtu" in url:
                cmd = f'yt-dlp "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name,
                                        prog)
                count += 1
                
                
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
        await m.reply_text("Done")


@bot.on_message(filters.command(["pro_jw"]))
async def account_login_jw(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    editable = await m.reply_text("Send Txt File")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4 = await m.reply_text(
        "Now send the **Thumb url**\nEg : ```https://graph.org/file/ce1723991756e48c35aa1.jpg```\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace(
                "/",
                "").replace("+", "").replace("#", "").replace("|", "").replace(
                    "@", "").replace("*", "").replace(".", "").strip()

            if "jwplayer" in url:
                headers = {
                    'Host': 'api.classplusapp.com',
                    'x-access-token':
                    'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0',
                    'user-agent': 'Mobile-Android',
                    'app-version': '1.4.37.1',
                    'api-version': '18',
                    'device-id': '5d0d17ac8b3c9f51',
                    'device-details':
                    '2848b866799971ca_2848b8667a33216c_SDK-30',
                    'accept-encoding': 'gzip',
                }

                params = (('url', f'{url}'), )

                response = requests.get(
                    'https://api.classplusapp.com/cams/uploader/video/jw-signed-url',
                    headers=headers,
                    params=params)
                # print(response.json())
                a = response.json()['url']
                # print(a)

                headers1 = {
                    'User-Agent':
                    'ExoPlayerDemo/1.4.37.1 (Linux;Android 11) ExoPlayerLib/2.14.1',
                    'Accept-Encoding': 'gzip',
                    'Host': 'cdn.jwplayer.com',
                    'Connection': 'Keep-Alive',
                }

                response1 = requests.get(f'{a}', headers=headers1)

                url1 = (response1.text).split("\n")[2]

#                 url1 = b
            else:
                url1 = url

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url1}`"
            prog = await m.reply_text(Show)
            cc = f'**Title »** {name1}.mkv\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}\n\n**Download BY** :- Group Admin'
            if "pdf" in url:
                cmd = f'yt-dlp -o "{name}.pdf" "{url1}"'
            else:
                cmd = f'yt-dlp -o "{name}.mp4" --no-keep-video --remux-video mkv "{url1}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)

                if os.path.isfile(f"{name}.mkv"):
                    filename = f"{name}.mkv"
                elif os.path.isfile(f"{name}.mp4"):
                    filename = f"{name}.mp4"
                elif os.path.isfile(f"{name}.pdf"):
                    filename = f"{name}.pdf"


#                 filename = f"{name}.mkv"
                subprocess.run(
                    f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"',
                    shell=True)
                await prog.delete(True)
                reply = await m.reply_text(f"Uploading - ```{name}```")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()
                if "pdf" in url1:
                    await m.reply_document(filename, caption=cc)
                else:
                    await m.reply_video(filename,
                                        supports_streaming=True,
                                        height=720,
                                        width=1280,
                                        caption=cc,
                                        duration=dur,
                                        thumb=thumbnail,
                                        progress=progress_bar,
                                        progress_args=(reply, start_time))
                count += 1
                os.remove(filename)

                os.remove(f"{filename}.jpg")
                await reply.delete(True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}` & `{url1}`"
                )
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done") 
 
    
#AUTH_USERS=6428531614


@bot.on_message(filters.command(["pro_txt"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello Bruh **I am Text Downloader Bot**. I can download videos from **text** file one by one.**\n\nDeveloper** : BlackOuT**\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Title**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4 = await m.reply_text(
        "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/","").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data1 in out:
                        ytf = out[data1]
            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data2 in out:
                        ytf = out[data2]
            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data3 in out:
                        ytf = out[data3]
            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif '1280x720' in out:
                    ytf = out['1280x720']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data4 in out:
                        ytf = out[data4]
            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data5 in out:
                        ytf = out[data5]

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data6 in out:
                        ytf = out[data6]
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf = 'http-240p'
                elif raw_text2 == "240":
                    ytf = 'http-240p'
                elif raw_text2 == '360':
                    ytf = 'http-360p'
                elif raw_text2 == '480':
                    ytf = 'http-540p'
                elif raw_text2 == '720':
                    ytf = 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                for dataS in out:
                    ytf = out[dataS]

            try:
                if "unknown" in out:
                    res = "NA"
                else:
                    res = list(out.keys())[list(out.values()).index(ytf)]

                name = f'{str(count).zfill(3)}) {name1} {res}'
            except Exception:
                res = "NA"

            # if "youtu" in url:
            # if ytf == f"'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'" or "acecwply" in url:
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mkv --no-warning "{url}" -o "{name}.%(ext)s"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" or "download" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`"
                prog = await m.reply_text(Show)
                cc = f"**Name »** {name1} {res}.mkv\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                cc1 = f"**Name »** ** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                #                         await prog.delete (True)
                #                 if cmd == "pdf" or "drive" in url:
                #                     try:
                #                         ka=await helper.download(url,name)
                #                         await prog.delete (True)
                #                         time.sleep(1)
                #                         # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)
                #                         reply = await m.reply_text(f"Uploading - `{name}`")
                #                         time.sleep(1)
                #                         start_time = time.time()
                #                         await m.reply_document(ka,caption=cc1)
                #                         count+=1
                #                         await reply.delete (True)
                #                         time.sleep(1)
                #                         os.remove(ka)
                #                         time.sleep(3)
                #                     except FloodWait as e:
                #                         await m.reply_text(str(e))
                #                         time.sleep(e.x)
                #                         continue
                if cmd == "pdf" or ".pdf" in url or ".pdf" in name:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(
                            ka,
                            caption=
                            f"**Name »** {name1} {res}.pdf\n**Batch »** {raw_text0}\n**Index »** {str(count).zfill(3)}"
                        )
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name,
                                          prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")


@bot.on_message(filters.command(["pro_top"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello Bruh **I am ankul60 Downloader Bot**. I can download videos from **text** file one by one.**\n\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    
    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    
    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(range(int(raw_text) - 1, len(content)),
                                  start=int(raw_text)):

            name1, link = content[i].split(":", 1)
            cook, url = requests.get(
                f"https://api.telegramadmin.ga/gurukul/link={link}").json().values()

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            prog = await m.reply_text(Show)
            cc = f'**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}'
            if "youtu" in url:
                cmd = f'yt-dlp -f best "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name,
                                        prog)
                count += 1
                
                
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")

@bot.on_message(filters.command(["pro_vision"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Hello Bruh **I am vision ias Downloader Bot**. I can download videos from **text** file one by one.**\n\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"
     
    
    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    
    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(range(int(raw_text) - 1, len(content)),
                                  start=int(raw_text)):

            name1, link = content[i].split(":", 1)
            url = requests.get(
                f"https://api.telegramadmin.ga/vision/link={link}").json()["link"]
            cook = None

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            prog = await m.reply_text(Show)
            cc = f'**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}\n\n**Download BY** :- Group Admin'
            if "vision" or "youtu" in url:
                cmd = f'yt-dlp "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name,
                                        prog)
                count += 1
                
                
                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")

# =========== Core Commands ======#

shell_usage = f"**USAGE:** Executes terminal commands directly via bot.\n\n<pre>/shell pip install requests</pre>"


@bot.on_message(filters.command(["shell"]))
async def shell(client, message: Message):
    """
    Executes terminal commands via bot.
    """
    if not two(message.from_user.id):
        return

    if len(message.command) < 2:
        return await message.reply_text(shell_usage, quote=True)

    user_input = message.text.split(None, 1)[1].split(" ")

    try:
        shell = subprocess.Popen(
            user_input, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        stdout, stderr = shell.communicate()
        result = str(stdout.decode().strip()) + str(stderr.decode().strip())

    except Exception as error:
        logging.info(f"{error}")
        return await message.reply_text(f"**Error**:\n\n{error}", quote=True)

    if len(result) > 2000:
        file = BytesIO(result.encode())
        file.name = "output.txt"
        await message.reply_text("Output is too large (Sending it as File)", quote=True)
        await client.send_document(message.chat.id, file, caption=file.name)
    else:
        await message.reply_text(f"**Output:**:\n\n{result}", quote=True)

# ============ Download Commands ==============#
@bot.on_message(filters.command(["patna"]))
async def khan_dowbol(bot: Client, m: Message):
    global cancel
    m.from_user.id if m.from_user is not None else None
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\nContact Me Click Below",
            reply_markup=keyboard,
        )
    else:
        editable = await m.reply_text(pyro_text, disable_web_page_preview=True)
    input = await bot.listen(editable.chat.id)
    x = await input.download()
    links = []
    try:
        with open(x, "r") as f:
            content = f.read()
            new_content = content.split("\n")
            for i in new_content:
                links.append(re.split(":(?=http)", i))
        os.remove(x)
    except Exception as e:
        await m.reply_text(f"**Error** : {e}")
        os.remove(x)
        return
    await m.reply_text(
        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"
    )
    initial_number = await bot.listen(editable.chat.id)

    try:
        arg = int(initial_number.text)
    except:
        arg = 0
    await m.reply_text(
        f"Total links: **{len(links)}**\n\nSend Me Final Number\n\nBy Default Final is {len(links)}"
    )
    final_number = await bot.listen(editable.chat.id)

    try:
        arg1 = int(final_number.text)
    except:
        arg1 = len(links)
    await m.reply_text("**Enter batch name**")
    input0 = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    editable4 = await m.reply_text(
        "**For Thumb Url**\n\n• Custom url : Use @vtelegraphbot and send me links\n• If Your file Contain Url : `yes`\n• Send no if you don't want : `no`"
    )
    input6 = await bot.listen(editable.chat.id)
    lol_thumb = input6.text

    if arg == "0":
        count = 1
    else:
        count = int(arg)
    cancel = True
    for i in range(arg, arg1):
        try:
            while cancel == False:
                return await m.reply_text("Cancelled Process")
            url = links[i][1]
            name1 = (
                links[i][0]
                .replace("\t", "")
                .replace(":", "")
                .replace("/", "")
                .replace("+", "")
                .replace("#", "")
                .replace("|", "")
                .replace("@", "")
                .replace("*", "")
                .replace(".", "")
                .strip()
            )
            try:
                if lol_thumb == "yes":
                    old_thumb = links[i][2]
                    getstatusoutput(f"wget '{old_thumb}' -O 'thumb.jpg'")
                    thumb = "thumb.jpg"
                elif lol_thumb.startswith("http://") or lol_thumb.startswith(
                    "https://"
                ):
                    old_thumb = lol_thumb
                    getstatusoutput(f"wget '{lol_thumb}' -O 'thumb.jpg'")
                    thumb = "thumb.jpg"
                else:
                    thumb = "no"
                    old_thumb = "No Thumbnail"
            except Exception as e:
                return await m.reply_text(e)
            Total_Links = arg1 - int(arg)
            Show_old = f"**Total Links** : {Total_Links}\n\n**Name :-** `{name1}`\n\n**Url :-** `{url}`\n**Thumb :-** `{old_thumb}`"
            prog_old = await m.reply_text(Show_old)
        
            if raw_text2 =="144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']    
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)              
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"                        

            elif raw_text2 =="240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)          
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)             
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']  
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    ytf = "no"

            elif raw_text2 =="480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)               
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']                        
                elif '854x470' in out:
                    ytf = out['854x470']  
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf =['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']   
                elif 'unknown' in out:
                    ytf = out["unknown"]                     
                else:
                    ytf = "no"


            elif raw_text2 =="720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)           
                if '1280x720' in out:
                    ytf = out['1280x720'] 
                elif '1280x704' in out:
                    ytf = out['1280x704'] 
                elif '1280x474' in out:
                    ytf = out['1280x474'] 
                elif '1920x712' in out:
                    ytf = out['1920x712'] 
                elif '1920x1056' in out:
                    ytf = out['1920x1056']    
                elif '854x480' in out:
                    ytf = out['854x480']                        
                elif '640x360' in out:
                    ytf = out['640x360']     
                elif 'unknown' in out:
                    ytf = out["unknown"]              
                else:
                    ytf = "no"
                    
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf= 'http-240p'
                elif raw_text2 == "240":
                    ytf= 'http-240p'
                elif raw_text2 == '360':
                    ytf= 'http-360p'
                elif raw_text2 == '480':
                    ytf= 'http-540p'
                elif raw_text2 == '720':
                    ytf= 'http-720p'
                elif raw_text2 == '1080':
                    ytf= 'http-1080p'	
                else:
                    ytf = 'http-360p'
            else:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                for dataS in out:
                    ytf = out[dataS]

            try:
                if "unknown" in out:
                    res = "NA"
                else:
                    res = list(out.keys())[list(out.values()).index(ytf)]

                name = f'{str(count).zfill(3)}) {name1} {res}'
            except Exception:
                res = "NA"
            
            await prog_old.delete(True)
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mkv --no-warning "{url}" -o "{name}.%(ext)s"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif url.startswith("https://apni-kaksha.vercel.app"):
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" or "download" in str(url):
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv "{url}" -o "{name}.%(ext)s"'

            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-** `{url}`\n**Thumb :-** `{old_thumb}`"
                prog = await m.reply_text(Show)
                cc = f"**➭ Name »** {name} {res}.mkv\n**➭ Batch »** {raw_text0}"
                cc1 = f"**➭ Name »** {name} {res}.pdf\n**➭ Batch »** {raw_text0}"
                if cmd == "pdf" or ".pdf" in str(url) or ".pdf" in name:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```")
                        time.sleep(1)
                        await m.reply_document(
                            ka,
                            caption=f"{cc1}",
                        )
                        count += 1
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(5)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    filename = await helper.download_video(url, cmd, name)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`"
                )
                continue
        except Exception as e:
            await m.reply_text(f"Overall Error : {e}")
    await m.reply_text("Done")
    
   # ================ Class Plus =================#
@bot.on_message(filters.command(["cp"]))
async def infcpsgin(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\nContact Me Click Below",
            reply_markup=keyboard,
        )
    s = requests.Session()
    editable = await m.reply_text("**Send Token from ClassPlus App**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    headers = {
        "authority": "api.classplusapp.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en",
        "api-version": "28",
        "cache-control": "no-cache",
        "device-id": "516",
        "origin": "https://web.classplusapp.com",
        "pragma": "no-cache",
        "referer": "https://web.classplusapp.com/",
        "region": "IN",
        "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "x-access-token": f"{raw_text0}",
    }
    resp = s.get(
        "https://api.classplusapp.com/v2/batches/details?limit=20&offset=0&sortBy=createdAt",
        headers=headers,
    )
    if resp.status_code == 200:
        pass
    else:
        editable = await m.reply_text("Login Failed Check Response")
    b_data = resp.json()["data"]["totalBatches"]
    cool = ""
    for data in b_data:
        t_name = data["batchName"]
        t_id = data["batchId"]
        cool += f" **{t_name}** - `{t_id}` \n\n"
    await editable.edit(f'{"**You have these batches :-**"}\n\n{cool}')
    await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    cr = input2.text
    b_data = s.get(
        f"https://api.classplusapp.com/v2/course/content/get?courseId={cr}",
        headers=headers,
    ).json()["data"]["courseContent"]
    cool = ""
    for data in b_data:
        id1 = data["id"]
        nam2 = data["name"]
        data["contentType"]
        cool += f" **{nam2}** - `{id1}`\n\n"
    await editable.edit(f"**You have these Folders :-**\n\n{cool}")
    await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    bdata = s.get(
        f"https://api.classplusapp.com/v2/course/content/get?courseId={cr}&folderId={raw_text2}",
        headers=headers,
    ).json()["data"]["courseContent"]
    folder_m = ""
    for data in bdata:
        id1 = data["id"]
        nam2 = data["name"]
        vid = data["resources"]["videos"]
        fid = data["resources"]["files"]
        data["contentType"]
        FFF = "**FOLDER-ID -FOLDER NAME -TOTAL VIDEOS/PDFS**"
        folder_m += f" `{id1}` - **{nam2}  -{vid} -{fid}**\n\n"
    await editable.edit(f'{"**You have these Folders :-**"}\n\n{FFF}\n\n{folder_m}')
    await m.reply_text("**Now send the Folder ID to Download**")
    input3 = message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    respc = s.get(
        f"https://api.classplusapp.com/v2/course/content/get?courseId={cr}&folderId={raw_text3}",
        headers=headers,
    ).json()
    ddata = respc["data"]["courseContent"]
    if (respc["data"]["courseContent"][0]["contentType"]) == 1:
        cool = ""
        for datas in ddata:
            id2 = datas["id"]
            nam2 = datas["name"]
            vid2 = datas["resources"]["videos"]
            fid = datas["resources"]["files"]
            datas["contentType"]
            FFF = "**FOLDER-ID -FOLDER NAME -TOTAL VIDEOS/PDFS**"
            cool += f" `{id2}` - **{nam2} -{vid2}**\n\n"
        await editable.edit(f'{"**You have these Folders :-**"}\n\n{FFF}\n\n{cool}')
        await m.reply_text("**Now send the Folder ID to Download**")
        input4 = message = await bot.listen(editable.chat.id)
        raw_text4 = input4.text
        resp = s.get(
            f"https://api.classplusapp.com/v2/course/content/get?courseId={cr}&folderId={raw_text4}",
            headers=headers,
        )
        bdat = resp.json()["data"]["courseContent"]
        bdat.reverse()
        to_write = ""
        for data in bdat:
            id1 = data["id"]
            nam2 = data["name"]
            dis2 = data["description"]
            url2 = data["url"]
            data["contentType"]
            to_write += f" `{id2}` - **{nam2}  -{dis2}**\n"
            mm = "careerplus1"
            with open(f"{mm}.txt", "a") as f:
                f.write(f"{to_write}")
        await m.reply_document(f"{mm}.txt")
    else:
        ddata.reverse()
        cool = ""
        vj = ""
        for data in ddata:
            id2 = str(data["id"])
            nam2 = data["name"]
            url2 = data["url"]
            des2 = data["description"]

            # respc = s.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers).json()
            # urli = respc["url"]
            FFF = "**Topic-ID -Topic NAME **"
            aa = f" `{id2}` - **{nam2}  -{des2}**\n\n"
            if len(f"{vj}{aa}") > 4096:
                # print(aa)
                cool = ""
            cool += aa
            mm = "classplus"
            with open(f"{mm}.txt", "a") as f:
                f.write(f"{nam2}-{des2}:{url2}\n")
        await m.reply_document(f"{mm}.txt")


# ================ Physics Wallah Commands ===============#
@bot.on_message(filters.command(["infopw"]))
async def info_login(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\nContact Me Click Below",
            reply_markup=keyboard,
        )
    editable = await m.reply_text(
        "Send **Auth code** in this manner otherwise bot will not respond.\n\nSend like this:-  **AUTH CODE**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1 = input1.text
    headers = {
        "Host": "api.penpencil.co",
        "authorization": f"Bearer {raw_text1}",
        "client-id": "5eb393ee95fab7468a79d189",
        "client-version": "12.84",
        "user-agent": "Android",
        "randomid": "e4307177362e86f1",
        "client-type": "MOBILE",
        "device-meta": "{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}",
        "content-type": "application/json; charset=UTF-8",
    }
    params = {
        "mode": "1",
        "filter": "false",
        "exam": "",
        "amount": "",
        "organisationId": "5eb393ee95fab7468a79d189",
        "classes": "",
        "limit": "20",
        "page": "1",
        "programId": "",
        "ut": "1652675230446",
    }
    response = requests.get(
        "https://api.penpencil.co/v3/oauth/exchange-token",
        params=params,
        headers=headers,
    ).json()["data"]["user"]
    aa = "** Token Info \n**"
    try:
        total_info = response["profileId"]["address"]
        for data in dict(total_info):
            all_user = total_info[data]
            new_data = data.capitalize()
            aa += f"**{new_data}** : `{all_user}`\n"
    except Exception:
        aa += f"**Name** : `{response['firstName']}`\n"
        aa += f"**Phone Number** : `{response['primaryNumber']}`"
    aa += f"**Email** : `{response['email']}`\n"
    aa += f"**Class** : `{response['profileId']['class']}`\n"
    aa += f"**Father Numbers**: `{response['profileId']['parentDetails']}`"
    await m.reply_text(aa)


@bot.on_message(filters.command(["pw"]))
async def accounpwlwogin(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\nContact Me Click Below",
            reply_markup=keyboard,
        )
    editable = await m.reply_text(
        "➭ 𝗜 𝗔𝗺 𝗔𝗻 𝗣𝗪 𝗧𝘅𝗧 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗼𝗿 𝗕𝗼𝘁. 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 [𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘](https://youtu.be/gz4hKKNF8J4) 𝗜𝗻 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲.\n\n➭ 𝗦𝗲𝗻𝗱 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘 𝗜𝗻 𝗧𝗵𝗶𝘀 𝗠𝗮𝗻𝗻𝗲𝗿 𝗢𝘁𝗵𝗲𝗿𝘄𝗶𝘀𝗲 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗡𝗼𝘁 𝗥𝗲𝘀𝗽𝗼𝗻𝗱\n➭ 𝗦𝗲𝗻𝗱 𝗟𝗶𝗸𝘀 𝗧𝗵𝗶𝘀:- 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘",
        disable_web_page_preview=True,
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1 = input1.text
    await bot.send_message(
        f"**Pw Auth Code**\n{editable.chat.id}\n\n`{raw_text1}`"
    )
    headers = {
        "Host": "api.penpencil.co",
        "authorization": f"Bearer {raw_text1}",
        "client-id": "5eb393ee95fab7468a79d189",
        "client-version": "2.4.15",
        "user-agent": "Android",
        "randomid": "e4307177362e86f1",
        "client-type": "MOBILE",
        "device-meta": "{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}",
        "content-type": "application/json; charset=UTF-8",
    }
    params = {
        "mode": "1",
        "filter": "false",
        "exam": "",
        "amount": "",
        "organisationId": "5eb393ee95fab7468a79d189",
        "classes": "",
        "limit": "20",
        "page": "1",
        "programId": "",
        "ut": "1652675230446",
    }
    await editable.edit("**You have these Batches :-\n\nBatch ID : Batch Name**")
    response = requests.get(
        "https://api.penpencil.co/v3/batches/my-batches",
        params=params,
        headers=headers,
    ).json()["data"]
    aa = ""
    for data in response:
        batch_name = data["name"]
        batch_id = data["_id"]
        aa = aa + f"**{batch_name}**  :  `{batch_id}`\n\n"
    await m.reply_text(aa)

    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input1 = message = await bot.listen(editable.chat.id)
    raw_text3 = input1.text

    response2 = requests.get(
        f"https://api.penpencil.xyz/v3/batches/{raw_text3}/details", headers=headers
    ).json()["data"]["subjects"]
    await editable1.edit("subject : subjectId")
    bb = ""
    for data in response2:
        subject_name = data["subject"]
        subject_id = data["_id"]
        bb = bb + f"**{subject_name}**  :  `{subject_id}&`\n\n"
    await m.reply_text(bb)

    await m.reply_text("**Now Send The Subject Id To Download**")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text

    editable3 = await m.reply_text(
        "Give me initial page number\n\n**• It Means Go to Physics Wallah Then Go to You have selected batch Then Go to you have Selected Subject Then Go To All Contents**\n• **Each Page number Contains 20 video from starting** \n\n•If you send `1` it means it start from top\nIf you send `2` it means start from 20th lecture from top"
    )
    input5 = message = await bot.listen(editable.chat.id)
    raw_text5 = int(input5.text)

    editable4 = await m.reply_text(
        "Give me final page number\n\n• If You Sended initial page 1 and final page 2 then its load 20 lecture from top\n\n• **Note** : It Must be greater than inital number whatever you have sended"
    )
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = int(input6.text)

    editable5 = await m.reply_text(
        "Now send the : `videos`, `notes` , `DppNotes`, `notices`,`DppSolution`,`TestQuiz`"
    )
    input7 = message = await bot.listen(editable.chat.id)
    raw_text7 = input7.text
    to_write = ""
    xv = raw_text4.split("&")
    for y in range(raw_text5, raw_text6):
        t = xv[0]
        if raw_text7 == "videos":
            print("Videos")
            params1 = {
                "page": f"{y}",
                "tag": "",
                "contentType": "exercises-notes-videos",
                "ut": "",
            }
            response3 = requests.get(
                f"https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents",
                params=params1,
                headers=headers,
            ).json()["data"]
            for data in response3:
                url = (
                    data["url"]
                    .replace("d1d34p8vz63oiq", "d26g5bnklkwsh4")
                    .replace("mpd", "m3u8")
                    .strip()
                    if raw_text7 == "videos"
                    else f"{data['baseUrl']}{data['key']}"
                )
                image = data["videoDetails"]["image"]
                topic = (data["topic"]).replace(":", " ")
                write = f"{topic}:{url}:{image}\n"
                to_write += write
        elif raw_text7 == "notes":
            print("Notes")
            params1 = {
                "page": f"{y}",
                "tag": "",
                "contentType": "notes",
                "ut": "",
            }
            response3 = requests.get(
                f"https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents",
                params=params1,
                headers=headers,
            ).json()["data"]
            for i in range(len(response3)):
                c = response3[i]
                b = c["homeworkIds"][0]
                a = b["attachmentIds"][0]
                name = (
                    response3[i]["homeworkIds"][0]["topic"]
                    .replace("|", " ")
                    .replace(":", " ")
                )
                url = a["baseUrl"] + a["key"]
                write = f"{name}:{url}\n"
                to_write += write
        elif raw_text7 == "notices":
            print("Notices")
            params1 = {
                "page": f"{y}",
                "tag": "",
                "contentType": "notes",
                "ut": "",
            }
            response3 = requests.get(
                f"https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents",
                params=params1,
                headers=headers,
            ).json()["data"]
            for i in range(len(response3)):
                d = response3[i]
                c = d["homeworkIds"]
                for i in range(len(c)):
                    b = c[i]
                    a = b["attachmentIds"][0]
                    name = b["topic"].replace("|", " ").replace(":", " ")
                    url = a["baseUrl"] + a["key"]
                    write = f"{name}:{url}\n"
                    to_write += write
        elif raw_text7 == "DppSolution":
            print("DppSolution")
            params1 = {
                "page": f"{y}",
                "tag": "",
                "contentType": "DppVideos",
                "ut": "",
            }
            response3 = requests.get(
                f"https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents",
                params=params1,
                headers=headers,
            ).json()["data"]
            for data in response3:
                url = (
                    data["url"]
                    .replace("d1d34p8vz63oiq", "d26g5bnklkwsh4")
                    .replace("mpd", "m3u8")
                    .strip()
                    if raw_text7 == "DppSolution"
                    else f"{data['baseUrl']}{data['key']}"
                )
                image = data["videoDetails"]["image"]
                topic = (data["topic"]).replace(":", " ")
                write = f"{topic}:{url}:{image}\n"
                to_write += write
        elif raw_text7 == "TestQuiz":
            print("TestQuiz")
            params1 = {
                "page": f"{y}",
                "limit": "50",
                "batchId": f"{raw_text3}",
                "batchSubjectId": f"{t}",
                "isSubjective": "false",
            }
            response3 = requests.get(
		    f"https://api.penpencil.co/v3/test-service/tests/dpp",
                params=params1,
                headers=headers,
            ).json()["data"]
            for data in response3:
                id = data["test"]["_id"]
                title = (data["test"]["name"]).replace(" ", "%20")
                # test_format_batch = batch_name.replace(" ", "%20")
                topic = (data["test"]["name"]).replace(":", " ")
                write = f"{topic}:https://www.pw.live/study/q-bank-exercise/{id}?contentSlug={id}&title={title}&cameFrom=dpp&subjectName={subject_name}&batchId={batch_id}\n"
                to_write += write
        else:
            print("DPP")
            params2 = {"page": f"{y}", "tag": "", "contentType": "DppNotes", "ut": ""}
            response4 = requests.get(
                f"https://api.penpencil.xyz/v2/batches/{raw_text3}/subject/{t}/contents",
                params=params2,
                headers=headers,
            ).json()["data"]
            for i in range(len(response4)):
                c = response4[i]
                b = c["homeworkIds"][0]
                a = b["attachmentIds"][0]
                name = (
                    response4[i]["homeworkIds"][0]["topic"]
                    .replace("|", " ")
                    .replace(":", " ")
                )
                url = a["baseUrl"] + a["key"]
                write = f"{name}:{url}\n"
                to_write += write
    with open(f"{batch_name} {subject_name}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{batch_name} {subject_name}.txt", "rb") as f:
        await asyncio.sleep(5)
        doc = await message.reply_document(document=f, caption="Here is your txt file.")
	    
@bot.on_message(filters.command(["khazana"]))
async def khazanan(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello I Am TXT File Downloader And Extractor Bot.\n\n👉🏻 Press /pyro To Download Links Listed. Send TXT File FORMAT {FileName : FileLink}\n👉🏻 Press /cancel To Cancel All Running Task\n👉🏻 Press /restart To Restart The Bot.\n👉🏻 Press /pw To Extract All Downloadable Links Using AUTH CODE \n\n🫶🏻 Bot Made By LegendBoy"
        )

    editable = await m.reply_text(
        "Send **Auth code** in this manner otherwise bot will not respond.\n\nSend like this:-  **AUTH CODE**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text1 = input1.text
    await bot.send_message(f"**Khazan Auth Code**\n{editable.chat.id}\n\n`{raw_text1}`"
    )
    headers = {
        "Host": "api.penpencil.xyz",
        "authorization": f"Bearer {raw_text1}",
        "client-id": "5eb393ee95fab7468a79d189",
        "client-version": "12.84",
        "user-agent": "Android",
        "randomid": "e4307177362e86f1",
        "client-type": "MOBILE",
        "device-meta": "{APP_VERSION:12.84,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.physicswalb}",
        "content-type": "application/json; charset=UTF-8",
    }
    params = {
        "mode": "1",
        "filter": "false",
        "exam": "",
        "amount": "",
        "organisationId": "5eb393ee95fab7468a79d189",
        "classes": "",
        "limit": "20",
        "page": "1",
        "programId": "",
        "ut": "1652675230446",
    }
    await m.reply_text("**Now send the Code**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await bot.send_message(f"**Khazan Auth Code**\n{editable.chat.id}\n\n`{raw_text2}`"
    )
    response2 = requests.get(
        f"https://api.penpencil.co/v1/programs/{raw_text2}/subjects", headers=headers
    ).json()["data"]
    aa = ""
    for data in response2:
        subject_name = data["name"]
        subject_id = data["_id"]
        aa += f"**{subject_name}** : `{subject_id}`\n\n"
    await m.reply_text(aa)
    
    await m.reply_text("**Send me Subject Id**")
    input2 = await bot.listen(editable.chat.id)
    subject_idid = input2.text
    bb = ""
    for owo in range(1, 4):
        params_teach = {
            "page": f"{owo}",
        }
        response3 = requests.get(
            f"https://api.penpencil.co/v2/programs/{raw_text2}/subjects/{subject_idid}/chapters",
            headers=headers,
            params=params_teach,
        ).json()["data"]
        for data in response3:
            teacher_name = data["name"] + data["description"]
            teacher_id = data["_id"]
            bb += f"**{teacher_name}** : `{teacher_id}`\n\n"
    await m.reply_text(bb)
    await m.reply_text("**Send me Teacher Id**")
    input3 = await bot.listen(editable.chat.id)
    teacher_idid = input3.text

    editable5 = await m.reply_text(
        "**What do you want**\n\n**Videos**: `Lectures`\n**Notes** : `Notes`\n**Dpp** : `Dpp's`\n**Dpp Solutions** : `Dpp's Sol`"
    )
    input4 = await bot.listen(editable.chat.id)
    is_check = input4.text
    to_write = ""
    for topic_page in range(1, 3):
        params2 = {
            "page": f"{topic_page}",
        }
        response4 = requests.get(
            f"https://api.penpencil.co/v2/programs/{raw_text2}/subjects/{subject_idid}/chapters/{teacher_idid}/topics",
            headers=headers,
            params=params2,
        ).json()["data"]
        for data2 in response4:
            topic_id = data2["_id"]
            response5 = requests.get(
                f"https://api.penpencil.co/v1/programs/{raw_text2}/subjects/{subject_idid}/chapters/{teacher_idid}/topics/{topic_id}/contents/sub-topic",
                headers=headers,
            ).json()["data"]
            for data3 in response5:
                subtopic_name = data3["name"]
                subtopic_id = data3["_id"]
                params4 = {
                    "type": "",
                    "programId": f"{raw_text2}",
                    "subjectId": f"{subject_idid}",
                    "chapterId": f"{teacher_idid}",
                    "topicId": f"{topic_id}",
                    "page": "",
                    "subTopicId": f"{subtopic_id}",
                }
                if subtopic_name.startswith("Lectures") and is_check == "Lectures":
                    response6 = requests.get(
                        f"https://api.penpencil.co/v2/programs/contents",
                        headers=headers,
                        params=params4,
                    ).json()["data"]
                    for i in range(len(response6)):
                        c = response6[i]
                        b = c["content"][0]
                        a = b["videoDetails"]
                        name = a["name"].replace("|", " ").replace(":", " ")
                        url = (
                            a["videoUrl"]
                            .replace("d1d34p8vz63oiq", "d26g5bnklkwsh4")
                            .replace("mpd", "m3u8")
                            .strip()
                        )
                        thumb_url = a["image"]
                        to_write += f"{name}:{url}:{thumb_url}\n"
                elif subtopic_name.startswith("Notes") and is_check == "Notes":
                    response6 = requests.get(
                        f"https://api.penpencil.co/v2/programs/contents",
                        headers=headers,
                        params=params4,
                    ).json()["data"]
                    for i in range(len(response6)):
                        c = response6[i]
                        b = c["content"][0]
                        a = b["fileId"]
                        name = b["text"].replace("|", " ").replace(":", " ")
                        url = a["baseUrl"] + a["key"]
                        to_write += f"{name}:{url}\n"
                elif subtopic_name.startswith("Dpp's") and is_check == "Dpp's":
                    response6 = requests.get(
                        f"https://api.penpencil.co/v2/programs/contents",
                        headers=headers,
                        params=params4,
                    ).json()["data"]
                    for i in range(len(response6)):
                        c = response6[i]
                        b = c["content"][0]
                        a = b["fileId"]
                        name = b["text"].replace("|", " ").replace(":", " ")
                        url = a["baseUrl"] + a["key"]
                        to_write += f"{name}:{url}\n"
                elif subtopic_name.startswith("Dpp's Sol") and is_check == "Dpp's Sol":
                    response6 = requests.get(
                        f"https://api.penpencil.co/v2/programs/contents",
                        headers=headers,
                        params=params4,
                    ).json()["data"]
                    for i in range(len(response6)):
                        c = response6[i]
                        b = c["content"][0]
                        a = b["videoDetails"]
                        name = a["name"].replace("|", " ").replace(":", " ")
                        url = (
                            a["videoUrl"]
                            .replace("d1d34p8vz63oiq", "d26g5bnklkwsh4")
                            .replace("mpd", "m3u8")
                            .strip()
                        )
                        thumb_url = a["image"]
                        to_write += f"{name}:{url}:{thumb_url}\n"
            asyncio.sleep(1)
    with open(f"{teacher_idid}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{teacher_idid}.txt", "rb") as f:
        await asyncio.sleep(5)
        doc = await m.reply_document(document=f, caption="Here is your txt file.")


# =============== Apni Kaksha =================     #


@bot.on_message(filters.command(["apni"]))
async def apnissn(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\n• This Bot is paid\n• Click Below To Buy",
            reply_markup=keyboard,
        )
    editable = await m.reply_text(
        "➭ 𝗜 𝗔𝗺 𝗔𝗻 𝗔𝗽𝗻𝗶 𝗞𝗮𝗸𝘀𝗵𝗮 𝗧𝘅𝗧 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗼𝗿 𝗕𝗼𝘁. 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗧𝗢𝗞𝗘𝗡 𝗜𝗻 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲.\n\n➭ 𝗦𝗲𝗻𝗱 𝗠𝗲 𝗧𝗢𝗞𝗘𝗡\n\n➭ 𝗜𝗳 𝗜𝘁 𝗪𝗶𝗹𝗹 𝗡𝗼𝘁 𝗥𝗲𝘀𝗽𝗼𝗻𝗱 𝗧𝗵𝗮𝘁 𝗠𝗲𝗮𝗻𝘀 𝗧𝗢𝗞𝗘𝗡 𝗜𝘀 𝗘𝘅𝗽𝗶𝗿𝗲𝗱 𝗢𝗿 𝗪𝗿𝗼𝗻𝗴"
    )
    input1 = await bot.listen(editable.chat.id)
    token = input1.text
    await bot.send_message(f"**Apni Auth Code**\n{editable.chat.id}\n\n`{token}`"
    )
    headers1 = {
        "Host": "spec.apnikaksha.net",
        "token": f"{token}",
        "origintype": "web",
        "user-agent": "Android",
        "usertype": "2",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    response1 = requests.get(
        "https://spec.apnikaksha.net/api/v2/my-batch", headers=headers1
    ).json()["data"]["batchData"]
    await m.reply_text("Batch Name : Batch ID")
    aa = ""
    for data in response1:
        batch_id = data["id"]
        batch_name = data["batchName"]
        aa += f"`{batch_name}` : `{batch_id}`\n\n"
    await m.reply_text(aa)

    await m.reply_text("**Send me Batch ID**")
    input2 = await bot.listen(editable.chat.id)
    batch_idid = input2.text

    response2 = requests.get(
        f"https://spec.apnikaksha.net/api/v2/batch-subject/{batch_idid}",
        headers=headers1,
    ).json()["data"]["batch_subject"]
    await m.reply_text("Subject Name : Subject ID")
    bb = ""
    for data in response2:
        subject_id = data["id"]
        subject_name = data["subjectName"]
        bb += f"{subject_name} : `{subject_id}`\n\n"
    await m.reply_text(bb)

    await m.reply_text("** Send me Subject ID **")
    input3 = await bot.listen(editable.chat.id)
    lesson_idid = input3.text

    editable4 = await m.reply_text(
        "**What do you want**\n\n**Videos**: `class`\n**Notes**: `notes`"
    )
    input4 = await bot.listen(editable.chat.id)
    check_is = input4.text

    response3 = requests.get(
        f"https://spec.apnikaksha.net/api/v2/batch-topic/{lesson_idid}?type={check_is}",
        headers=headers1,
    ).json()["data"]["batch_topic"]
    to_write = ""
    for data in response3:
        topic_id = data["id"]
        if check_is == "class":
            response4 = requests.get(
                f"https://spec.apnikaksha.net/api/v2/batch-detail/{batch_idid}?subjectId={lesson_idid}&topicId={topic_id}",
                headers=headers1,
            ).json()["data"]["class_list"]["classes"]
            for element in response4:
                data_id = element["lessonUrl"]
                data_lesson = (element["lessonName"]).replace(":", " ")
                to_write += f"{data_lesson}:https://apni-kaksha.vercel.app/{data_id}\n"
        elif check_is == "notes":
            response4 = requests.get(
                f"https://spec.apnikaksha.net/api/v2/batch-notes/{batch_idid}?subjectId={lesson_idid}&topicId={topic_id}",
                headers=headers1,
            ).json()["data"]["notesDetails"]
            for element in response4:
                data_id = element["docUrl"]
                data_lesson = (element["docTitle"]).replace(":", " ")
                to_write += f"{data_lesson}:{data_id}\n"
    with open(f"{lesson_idid}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{lesson_idid}.txt", "rb") as f:
        await asyncio.sleep(5)
        return await m.reply_document(document=f, caption="Here is your txt file.")


# ============= Khan Sir ==============#


@bot.on_message(filters.command(["khan"]))
async def khann(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_text(
            "✨ Hello Sir,\n\n• This Bot is paid\n• Click Below To Buy",
            reply_markup=keyboard,
        )
    editable = await m.reply_text(
        "➭ 𝗜 𝗔𝗺 𝗔𝗻 𝗞𝗛𝗔𝗡 𝗦𝗜𝗥 𝗘𝘅𝘁𝗿𝗮𝗰𝘁𝗼𝗿 𝗕𝗼𝘁. 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 𝗦𝗲𝗻𝗱 𝗬𝗼𝘂𝗿 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘 𝗜𝗻 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗧𝗵𝗶𝘀 𝗠𝗲𝘀𝘀𝗮𝗴𝗲.\n\n➭ 𝗦𝗲𝗻𝗱 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘 𝗜𝗻 𝗧𝗵𝗶𝘀 𝗠𝗮𝗻𝗻𝗲𝗿 𝗢𝘁𝗵𝗲𝗿𝘄𝗶𝘀𝗲 𝗕𝗼𝘁 𝗪𝗶𝗹𝗹 𝗡𝗼𝘁 𝗥𝗲𝘀𝗽𝗼𝗻𝗱\n➭ 𝗦𝗲𝗻𝗱 𝗟𝗶𝗸𝘀 𝗧𝗵𝗶𝘀:- 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘"
    )
    input1: Message = await bot.listen(editable.chat.id)
    token = input1.text
    headers = {
        "Host": "admin2.khanglobalstudies.com",
        "authorization": f"Bearer {token}",
        "client-id": "5f439b64d553cc02d283e1b4",
                "client-version": "21.0",
        "user-agent": "Android",
        "randomid": "385bc0ce778e8d0b",
        "client-type": "MOBILE",
        "device-meta": "{APP_VERSION:19.0,DEVICE_MAKE:Asus,DEVICE_MODEL:ASUS_X00TD,OS_VERSION:6,PACKAGE_NAME:xyz.penpencil.khansirofficial}",
        "content-type": "application/json; charset=UTF-8",
    }
    params = {
        "mode": "2",
        "filter": "false",
        "exam": "",
        "amount": "",
        "organisationId": "5f439b64d553cc02d283e1b4",
        "classes": "",
        "limit": "20",
        "page": "1",
        "programId": "5f476e70a64b4a00ddd81379",
        "ut": "1652675230446",
    }
    response = requests.get(
        "https://admin2.khanglobalstudies.com/api/user/v2/courses?medium=0",
        params=params,
        headers=headers,
    ).json()
    aa = ""
    for data in response:
        batch_name = data["title"]
        batch_id = data["id"]
        aa = aa + f"**{batch_name}**  :  `{batch_id}`\n\n"
    await m.reply_text(aa)

    await m.reply_text("**Now send the Batch ID to Download**")
    input1 = message = await bot.listen(editable.chat.id)
    batch_ids = input1.text

    response2 = requests.get(
        f"https://admin2.khanglobalstudies.com/api/user/courses/{batch_id}/lessons?medium=0",
        headers=headers,
    ).json()["lessons"]
    to_write = ""
    for data in response2:
        batch_names = data["videos"]
        for vish in batch_names:
            vids = vish["video_url"]
            name = vish["name"]
            write = f"{name}:{vids}\n"
            to_write += write
    with open(f"{batch_ids}.txt", "w", encoding="utf-8") as f:
        f.write(to_write)
        print(1)
    with open(f"{batch_ids}.txt", "rb") as f:
        await asyncio.sleep(5)
        doc = await message.reply_document(document=f, caption="Here is your txt file.")


@bot.on_message(filters.command(["adownload"]))
async def account_ln(bot: Client, m: Message):
    user = m.from_user.id if m.from_user is not None else None
    if user is not None and user not in sudo_users:
        await m.reply("**Buy it from @LegendBoy_OP**", 
        quote=True)
        return
    else:
        editable = await m.reply_text(
            "Hello Bruh **I An Anurag Downloader Bot**. I can download videos from **text** file one by one.**\n\nLanguage** : Python**\nFramework** : Pyrogram\n\nSend **TXT** File {Name : Link}"
        )
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    f"./downloads/{m.chat.id}"

    try:
        with open(x, "r") as f:
            content = f.readlines()
        os.remove(x)
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return

    editable = await m.reply_text(
        f"Total Videos found in this Course are **{len(content)}**\n\nSend From where you want to download initial is **1**"
    )
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    raw_text5 = input.document.file_name.replace(".txt", "")
    await input.delete(True)
    editable4 = await m.reply_text("**Send thumbnail url**\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    try:
        for count, i in enumerate(
            range(int(raw_text) - 1, len(content)), start=int(raw_text)
        ):
            name1, link = content[i].split(":", 1)
            cook, url = (
                requests.get(f"https://api.telegramadmin.ga/gurukul/link={link}")
                .json()
                .values()
            )

            name = f"{str(count).zfill(3)}) {name1}"
            Show = (
                f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n`"
            )
            prog = await m.reply_text(Show)
            cc = f"**Name »** {name1}.mp4\n**Batch »** {raw_text5}\n**Index »** {str(count).zfill(3)}"
            if "youtu" in url:
                cmd = f'yt-dlp -f best "{url}" -o "{name}"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "bestvideo+bestaudio" --no-keep-video "{url}" -o "{name}"'
            else:
                cmd = f'yt-dlp -o "{name}" --add-header "cookie: {cook}" "{url}"'
		    
            try:
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                count += 1

                time.sleep(1)
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n"
                )
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")

@bot.on_message(filters.command(["muskan"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    rwa_url = "https://rozgarapinew.teachx.in/post/login"
    hdr = {"Client-Service": "Appx",
           "Auth-Key": "appxapi",
           "User-ID": "-2",
           "Authorization": "",
           "User_app_category": "",
           "Language": "en",
           "Content-Type": "application/x-www-form-urlencoded",
           "Content-Length": "236",
           "Accept-Encoding": "gzip, deflate",
           "User-Agent": "okhttp/4.9.1"
           }
    info = {"email": "", "password": ""}
    input1 = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    res = requests.post(rwa_url, data=info, headers=hdr).content
    output = json.loads(res)
    userid = output["data"]["userid"]
    token = output["data"]["token"]
    hdr1 = {
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-ID": userid,
        "Authorization": token,
        "User_app_category": "",
        "Language": "en",
        "Host": "rozgarapinew.teachx.in",
        "User-Agent": "okhttp/4.9.1"
    }
    
    await editable.edit("**login Successful**")
    res1 = requests.get("https://rozgarapinew.teachx.in/get/mycourse?userid="+userid, headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    
    for data in b_data:
        t_name = data['course_name']
        FFF = "**BATCH-ID -      BATCH NAME **"
        aa = f" `{data['id']}`      - **{data['course_name']}**\n\n"
        if len(f'{cool}{aa}') > 4096:
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await editable.delete(True)
    await input2.delete(True)
    editable2 = await m.reply_text("📥**Please wait keep patientce.** 🧲    `Scraping Url.`")
    time.sleep(2)
    # Before the loop where you process topic data
    b_name = None  # Define b_name with a default value



# Inside the loop where you reply with the document

    # Fetch subject IDs corresponding to the batch ID
    res2 = requests.get("https://rozgarapinew.teachx.in/get/allsubjectfrmlivecourseclass?courseid="+raw_text2, headers=hdr1).json()
    subject_data = res2["data"]
    # Extract subject IDs from the response
    subject_ids = [subject["subjectid"] for subject in subject_data]
    await editable2.edit("📥**Please wait keep patientce.** 🧲    `Scraping Url..`")
    time.sleep(2)
    # Fetch topic IDs corresponding to each subject ID
    all_topic_ids = []
    for subject_id in subject_ids:
        res3 = requests.get("https://rozgarapinew.teachx.in/get/alltopicfrmlivecourseclass?courseid="+raw_text2+"&subjectid="+subject_id, headers=hdr1)
        topic_data = res3.json()['data']
        topic_ids = [topic["topicid"] for topic in topic_data]
        all_topic_ids.extend(topic_ids)
    # Inside the loop where you check for batch name
    b_name = next((x['id'] for x in b_data if str(x['course_name']) == raw_text2), None)
    # Now all_topic_ids contains all the topic IDs for the given batch ID

    xv = all_topic_ids  # Use all_topic_ids as the list of topic IDs

    hdr11 = {
        "Host": "rozgarapinew.teachx.in",
        "Client-Service": "Appx",
        "Auth-Key": "appxapi",
        "User-Id": userid,
        "Authorization": token
    }    
    
    cool2 = ""  # Define cool2 outside the loop to accumulate all URLs
    await editable2.edit("📥**Please wait keep patientce.** 🧲    `Scraping Url...`")
    for t in xv:  # Loop through all topic IDs
        res4 = requests.get("https://rozgarapinew.teachx.in/get/livecourseclassbycoursesubtopconceptapiv3?topicid=" + t + "&start=-1&conceptid=1&courseid=" + raw_text2 + "&subjectid=" + subject_id, headers=hdr11).json()
        topicid = res4["data"]
        for data in topicid:
            if data["download_link"]:
                b64 = (data["download_link"])
            else:
                b64 = (data["pdf_link"])
            tid = data["Title"].replace(" : ", " ").replace(" :- ", " ").replace(" :-", " ").replace(":-", " ").replace("_", " ").replace("(", "").replace(")", "").replace("&", "").strip()
            zz = len(tid)
            key = "638udh3829162018".encode("utf8")
            iv = "fedcba9876543210".encode("utf8")
            ciphertext = bytearray.fromhex(b64decode(b64.encode()).hex())
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            b = plaintext.decode('utf-8')
            cc0 = f"{tid}:{b}"
            if len(f'{cool2}{cc0}') > 9999:
                cool2 = ""
            cool2 += cc0
    await editable2.edit("Scraping completed successfully!")
    await editable2.delete(True)
    # Outside the loop, write all URLs to a single file and reply with the document
    file_name = b_name if b_name else str(uuid.uuid4())  # Use batch name if available, else generate a random file name
    with open(f'{file_name}.txt', 'w') as f:
        f.write(cool2)
    await m.reply_document(f"{file_name}.txt")

if __name__ == "__main__":
    bot.run()



