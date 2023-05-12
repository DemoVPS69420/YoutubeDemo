const Discord = require('discord.js');

const client = new Discord.Client();

// Get the latest video from a YouTube channel.
async function getLatestVideo(channelId) {
  const url = `https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id=${channelId}`;
  const response = await fetch(url);
  const data = await response.json();
  const latestVideo = data.items[0].contentDetails.relatedPlaylists.uploads.items[0].snippet;
  return latestVideo;
}

// Send a notification to Discord.
async function sendNotification(channelId, title, url) {
  const message = `New video from ${title}: ${url}`;
  await client.channels.get(channelId).send(message);
}

// Create a loop that checks for new videos every minute.
async function main() {
  while (true) {
    // Get the latest video from each channel.
    const channels = [
      // Your YouTube channel ID
    ];
    for (const channelId of channels) {
      const latestVideo = await getLatestVideo(channelId);
      if (latestVideo) {
        // Send a notification to Discord.
        await sendNotification(channelId, latestVideo.title, latestVideo.thumbnails.default.url);
      }
    }
    await new Promise(resolve => setTimeout(resolve, 60000)); // 60 seconds
  }
}

// Run the bot.
client.on('ready', () => {
  console.log('Bot is ready!');
  main();
});

client.login('MTEwNjQ4NzgwNTk4NDY0OTMyNg.G5FYX4.rZZF4F8yCA0RwlG0Vofs7jrJie_2qf5OiMn8aw');
