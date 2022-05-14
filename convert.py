from moviepy.editor import *
from os  import *
from time import *

# obs: O arquivo só será convertido caso esta localizado no mesmo local onde está este script em python
print("************************** Meu conversor *****************************")

while True:
    print("\033[33m")

    name_achrives = input('     Insert the name >> ')
    print("\033[m")

    video = VideoFileClip(f'{name_achrives}.mp4')
    print('     Convertendo...')
    audio = video.audio
    print("\033[32m")
    audio.write_audiofile(f'{name_achrives}.mp3')
    print("\033[m")
    audio.close()
    video.close()

    print('     Conversão feita!')

    abrir = str(input('Deseja Abrir? (Y/N) >> '))

    if  (abrir=="N" or abrir == "n"):
        print("\n")
        pass

    elif (abrir=='y' or abrir=='Y'):
        print('\033[33m Abrindo...\033[m')
        print(f'File {name_achrives} rodando...')
        sleep(2)
        startfile(f'{name_achrives}.mp3')

    option = input('Deseja continuar? N/Y >> ')
    if(option =="n" or option == 'N'):break

    elif (option =="y" or option == 'Y'): 
        print("\n")
        pass


print("************************** Fim do Programa *****************************")
sleep(1)