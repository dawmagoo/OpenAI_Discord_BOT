import openai
import discord

openai.api_key = "OPEN_AI_KEY"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
  # ignoruj wiadomości od samego bota
  if message.author == client.user:
    return

  # sprawdź, czy wiadomość zaczyna się od /chat
  if message.content.startswith("/chat"):
    # wyciągnij tekst po /chat
    prompt = message.content[len("/chat"):].strip()

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=1024,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    # wyślij odpowiedź od OpenAI do czatu Discord
    await message.channel.send(response["choices"][0]["text"])

client.run("DISCORD_KEY")
