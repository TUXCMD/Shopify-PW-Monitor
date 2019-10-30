import time
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordEmbed, DiscordWebhook
from datetime import datetime


monitor_store_url = 'https://shop.balkobot.com'


webhook_url = ''#Input Your Webhook URL

delay = '2' # number 1-10

headers = {

	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}


def message_post(pw_status,monitor_store_url):

		webhook = DiscordWebhook(url=webhook_url,content='')
		
		embed = DiscordEmbed(title=pw_status, color=0x00fea9,url=monitor_store_url)
		
		embed.add_embed_field(name=monitor_store_url,value='**'+str(pw_status)+'**')
				
		embed.set_footer(text='@zyx898',icon_url='https://pbs.twimg.com/profile_images/1118878674642714624/lNXTIWNT_400x400.jpg')
		
		embed.set_timestamp()
		
		webhook.add_embed(embed)
		
		webhook.execute()
		
		print('[SUCCESS] --> Successfully sent success webhook!')


def main():

	last_status = ''

	while True:

		page_source = requests.get(monitor_store_url,headers=headers)

		page_text = BeautifulSoup(page_source.text,"html.parser")

		if 'Opening Soon' in page_text.title.text:

			pw_status = "Password Page Up"

			if pw_status != last_status:

				message_post(pw_status,monitor_store_url)

				last_status = pw_status

		else:

			pw_status = "Password Page Down"

			if pw_status != last_status:

				message_post(pw_status,monitor_store_url)

				last_status = pw_status

		now = datetime.now()

		print(str(now) + 'Monitoring-------------------[ '+last_status+' ]')

		time.sleep(int(delay))
main()
