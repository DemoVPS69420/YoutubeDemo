import discord
import requests

# Get your Discord bot token from https://discord.com/developers/applications
TOKEN = "MTEwNjQ4NzgwNTk4NDY0OTMyNg.G5FYX4.rZZF4F8yCA0RwlG0Vofs7jrJie_2qf5OiMn8aw"

# Create a Discord client
client = discord.Client()

# Get the latest video from a YouTube channel.
def get_latest_video(channel_id):
  url = f"https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={channel_id}"
  response = requests.get(url)
  data = response.json()
  latest_video = data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]["items"][0]["snippet"]
  return latest_video

# Send a notification to Discord.
def send_notification(channel_id, title, url):
  message = f"New video from {title}: {url}"
  client.get_channel(channel_id).send(message)

# Create a loop that checks for new videos every minute.
async def main():
  while True:
    # Get the latest video from each channel.
    channels = [
      # Your YouTube channel ID
    ]
    for channel_id in channels:
      latest_video = await get_latest_video(channel_id)
      if latest_video:
        # Send a notification to Discord.
        await send_notification(channel_id, latest_video["title"], latest_video["thumbnails"]["default"]["url"])
    await asyncio.sleep(60) # 60 seconds

# Run the bot.
client.on("ready", lambda: main())
client.run(TOKEN)
