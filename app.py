import tkinter as tk
from discord_webhook import DiscordEmbed, DiscordWebhook

form = tk.Tk()
form.title('Discord Embed Generator')
form.geometry('600x350')


## Token Message ##

TokenTitle = tk.Label(text='Webhook Token:', fg='black')
TokenTitle.pack()
TokenTitle.place(x=20, y=60)

tokenEntry = tk.Entry(fg='black', bg='gray', width=40)
tokenEntry.pack()
tokenEntry.place(x=127, y=60)

## Title Message ##

titleMessage = tk.Label(text='Title Yazısı:', fg='black')
titleMessage.pack()
titleMessage.place(x=20, y=100)

titleEntry = tk.Entry(fg='black', bg='gray', width=40)
titleEntry.pack()
titleEntry.place(x=127, y=100)


## Author Message ##


authorMessage = tk.Label(text='Author Yazısı:', fg='black')
authorMessage.pack()
authorMessage.place(x=20, y=140)

authorEntry = tk.Entry(fg='black', bg='gray', width=40)
authorEntry.pack()
authorEntry.place(x=127, y=140)


## Color ##


colorMessage = tk.Label(text='Color Id:', fg='black')
colorMessage.pack()
colorMessage.place(x=20, y=180)

colorEntry = tk.Entry(fg='black', bg='gray', width=40)
colorEntry.pack()
colorEntry.place(x=127, y=180)


## Set Footer ##


footerMessage = tk.Label(text='Color Id:', fg='black')
footerMessage.pack()
footerMessage.place(x=20, y=180)

footerEntry = tk.Entry(fg='black', bg='gray', width=40)
footerEntry.pack()
footerEntry.place(x=127, y=180)


## Radio Timestamp ##

a = tk.StringVar()

timeTitle = tk.Label(text='Time Stamp:', fg='black')
timeTitle.pack()
timeTitle.place(x=20, y=220)

Time1 = tk.Radiobutton(text="Var", fg='black', value=1,
                       variable=a, activebackground='gray')
Time1.pack()
Time1.place(x=125, y=220)

Time2 = tk.Radiobutton(text="Yok", fg='black', value=2,
                       variable=a, activebackground='gray')
Time2.pack()
Time2.place(x=187, y=220)


## Button ##


def veriStart():

    webhook = DiscordWebhook(url=tokenEntry.get())

    embed = DiscordEmbed(title=titleEntry.get())
    if colorEntry.get() == "red":
        embed.set_color(color=242424)

    embed.set_author(name=authorEntry.get())
    embed.set_footer(text=footerEntry.get())
    if a.get() == '1':
        embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()

    pass


buton = tk.Button(form, text='Mesajı Gönder', fg='black',
                  bg='gray', height=1, width=19, command=veriStart)
buton.pack(side=tk.BOTTOM, pady=17)


##########################################################################################


form.mainloop()
