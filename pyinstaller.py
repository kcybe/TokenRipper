# Compiler Editor #
import os

bat = "pyinstaller.exe --onefile -n "
settings = 'Settings: \n\n'

while True:

    #   Output Name    #
    output_name = input('Output Name (No Spaces): ')
    bat += output_name
    settings += f'Output Name: {output_name}'
    os.system('cls')

    #   Icon    #
    icon = input('Custom Icon? [y/n] ')
    os.system('cls')
    if icon == 'y':
        print('Put the icon that you want to use in the Icons folder.')
        print('Note: Write the file name with .ico at the end')
        icon_name = input('\nIcon File Name: ')
        bat += f' --icon=icons/{icon_name} --clean'
        settings += f'\nIcon File: {icon_name}'
        os.system('cls')
    else:
        pass

    #   Settings Chosen    #
    print(settings)
    confirm = input('1. Accept \n2. Change Settings \n> ')
    if confirm == '1':
        os.system('cls')
        break
    else:
        os.system('cls')
        continue

with open('pyinstaller.bat', 'w') as f:
    bat += ' ripper.py'
    f.write(bat)

print('pyinstaller.bat has been made. Open it to compile ripper.py')
input('[ENTER] to exit')