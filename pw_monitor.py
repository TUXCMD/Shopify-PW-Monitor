import time
import random
import requests
import threading
from datetime import datetime
from bs4 import BeautifulSoup
from dhooks import *


urls = ['https://eflash-us.doverstreetmarket.com','https://shop.travisscott.com','https://bdgastore.com','https://shop-usa.palaceskateboards.com','https://dropsau.com/','https://eflash-jp.doverstreetmarket.com/','https://wearebraindead.com','https://eflash-sg.doverstreetmarket.com','https://shop-jp.palaceskateboards.com/']

webhook_url = ''

error_url = ''#Input Your Webhook URL

delay = '5' # number 1-10

headers = {

	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


def message_post(pw_status,monitor_store_url):
    hook = Webhook(webhook_url)
    embed = Embed(description='**'+str(pw_status)+'**',color=0x36393F,timestamp='now')
    embed.set_title(title=str(monitor_store_url),url=monitor_store_url)
    embed.set_footer(text='@zyx898',icon_url='https://pbs.twimg.com/profile_images/1118878674642714624/lNXTIWNT_400x400.jpg')
    hook.send(embed=embed)
    print('[SUCCESS] --> Successfully sent success webhook!')


def error_post(message,monitor_store_url):
    hook = Webhook(error_url)
    embed = Embed(description='**'+str(message)+'**',color=0x36393F,timestamp='now')
    embed.set_title(title=str(monitor_store_url),url=monitor_store_url)
    embed.set_footer(text='@zyx898',icon_url='https://pbs.twimg.com/profile_images/1118878674642714624/lNXTIWNT_400x400.jpg')
    hook.send(embed=embed)
    print('[SUCCESS] --> Successfully sent success webhook!')


def main(url):
    last_status = ''

    while True:
        try:
            page_source = requests.get(url,headers=headers)

            page_text = BeautifulSoup(page_source.text,"lxml")

            if 'Opening Soon' in page_text.title.text:

                pw_status = "Password Page Up :lock:"

                if pw_status != last_status:

                    message_post(pw_status,url)

                    last_status = pw_status

            else:

                pw_status = "Password Page Down :unlock:"

                if pw_status != last_status:

                    message_post(pw_status,url)

                    last_status = pw_status

            now = datetime.now()

            print(str(now) + ' Monitoring-------------------[ '+str(url)+'   '+last_status+' ]')

            time.sleep(int(delay))
        except:
            print('Error Requesting to This site   ',url)
            time.sleep(5)

if __name__ == "__main__":
    for i in urls:
        threading.Thread(name=str(i),target=main,args=(i,)).start()
