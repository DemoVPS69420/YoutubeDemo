import discord
import youtube_dl

# Get the Discord bot token from your Discord developer dashboard.
TOKEN = "MTEwNjQ4NzgwNTk4NDY0OTMyNg.G5FYX4.rZZF4F8yCA0RwlG0Vofs7jrJie_2qf5OiMn8aw"

# Get the YouTube channel ID of the channel you want to monitor.
CHANNEL_ID = "UCott96qGP5ADmsB_yNQMvDA"

# Get the Discord channel ID of the channel you want to send notifications to.
NOTIFY_CHANNEL_ID = "878680807823253544"

# Create a Discord client.
client = discord.Client()

# Create a YouTubeDL object.
ydl = youtube_dl.YoutubeDL()

# Set the on_new_video_uploaded event handler.
def on_new_video_uploaded(video_id):
    # Get the video information.
    video_info = ydl.extract_info("https://www.youtube.com/watch?v={}".format(video_id))

    # Get the video title.
    title = video_info["title"]

    # Get the video thumbnail URL.
    thumbnail_url = video_info["thumbnail"]

    # Send a message to the Discord channel.
    client.send_message(NOTIFY_CHANNEL_ID, "New video uploaded by {}: {} ({})".format(video_info["author"], title, thumbnail_url))

# Start the bot.
client.run(TOKEN)
