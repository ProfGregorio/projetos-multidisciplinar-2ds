import pyttsx3
from deep_translator import GoogleTranslator



def traduzir_ingles_para_portugues(texto_ingles):
    traducao = GoogleTranslator(source='en', target='pt').translate(texto_ingles)
    return traducao


def cantar_musica(traducao):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) 
    engine.setProperty('volume', 1)  
    engine.say(traducao)  
    engine.runAndWait()


def cantar_musica_em_portugues(letra_ingles):
    print("Traduzindo a letra para o português...")
    qual_musica =input('''
    ESCOLHA A MUSICA QUE VC QUER OUVIR:
    1 - Can't Help Falling In Love - Elvis Presley
    2 - 505 - Arctic Monkey 
    3 - I Will survive - Gloria Gaynor
    4 - Civil War - Guns N' Roses
    5 - I'm Still Standing - Elton John
    6 - We are the champions

    ''')
    musica = open(f"musica{qual_musica}.txt", "r")
    musica_completa = ' '.join(musica.readlines())

    letra_traduzida = traduzir_ingles_para_portugues(musica_completa)
    print("Letra traduzida:")
    print(letra_traduzida)
    print("\nCANTANDO A MÚSICA...")
    cantar_musica(letra_traduzida)



letra_ingles = """

"""


cantar_musica_em_portugues(letra_ingles)
