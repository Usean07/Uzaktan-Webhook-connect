from discord_webhook import DiscordEmbed, DiscordWebhook

WeebhokSoru = input("WebHook url: ")
titleSoru = input("Title Girin: ")
authorSoru = input("Author Yazıyı Girin: ")
footerSoru = input("Footer yazısı: ")
timeSoru = input("TimeStamp Olsunmu (y or n): ")


content = "Merhaba Dünya"

webhook = DiscordWebhook(url=WeebhokSoru)

embed = DiscordEmbed(title=titleSoru, color=242424)
embed.set_author(name=authorSoru)
embed.set_footer(title=footerSoru)
if timeSoru == "y":
    embed.set_timestamp()

webhook.add_embed(embed)
response = webhook.execute()