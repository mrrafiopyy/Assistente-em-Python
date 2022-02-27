# Importando módulos
import speech_recognition as sr
import sounddevice as sd
import wavio as wv
import pyttsx3
import webbrowser
import random
import os
import pyautogui
import time


def inscreva_se():
    # Presses the tab key once
    pyautogui.press("tab")
    pyautogui.press('tab')
    pyautogui.press('enter')


# Função de fala do assistente.
def iafala(fala):
    engine = pyttsx3.init()
    engine.say(fala)
    engine.runAndWait()


# Função de gravar audio para reconhecimento.
def grava():
    freq = 48000  # Altere a frequência se achar necessário
    duration = 5  # Altere a duração de cada gravação
    recording = sd.rec(int(duration * freq),
                       samplerate=freq, channels=2)
    print('Fale agora!')
    sd.wait()
    wv.write("minhavoz.wav", recording, freq, sampwidth=2)
    print('Ok! Processando')


# Importando arquivos de voz
filename = "minhavoz.wav"

# Lista de curiosidades (Opcional)
curiosidades = [
    "Existem mais formas de vida vivendo na sua pele do que humanos habitando a Terra. Esta, certamente, é uma das curiosidades do mundo mais impactantes.",
    "Em média, cada pessoa perde 4kg de pele morta em um ano",
    "Charles Osborne teve uma crise de soluços que durou, nada mais nada menos que, 69 anos. Começou em 1922, quando pesava um cerdo para sacrificá-lo e só parou quando ele já tinha 97 anos.",
    "Todas as pessoas que têm olhos azuis têm um mesmo ancestral em comum.",
    "O cérebro é um órgão extraordinário. Isso porque comanda todo o organismo humano. Além disso, é o único que não pode sentir dor.",
    "Geralmente, 30% do sangue bombeado pelo coração vai direto para o cérebro.",
    "A decomposição do corpo humano começa apenas 4 minutos depois da morte.",
    "Respirar pela boca o tempo todo pode causar cáries e modificar o formato da mandíbula.Uma das curiosidades do mundo mais chocantes, hein?",
    "Quando você fala para si mesmo, por exemplo, enquanto lê, essa ‘voz’ interior é acompanhada de movimentos muito sutis da laringe.",
    "Beijar um bebê na orelha pode deixá-lo surdo.",
    "As três famílias mais ricas do mundo têm mais dinheiro que a riqueza dos 48 países mais pobres do mundo.",
    "A cerveja não era considerada uma bebida alcoólica na Rússia até o ano de 2011. Afinal, até então era classificada como um refresco.",
    "Os homens são 6 vezes mais propensos a serem atingidos por um raio do que as mulheres.",
    "É mais provável que uma pessoa morra com um coco caindo sobre a sua cabeça do que por um ataque de tubarão.",
    "Estados Unidos, Birmânia e Libéria são os únicos países no mundo que não usam o sistema métrico como padrão de medição.",
    "Cerca de 2.500 pessoas canhotas morrem a cada ano. Porque inúmeros acidentes são causados por equipamentos e ferramentas criadas para destros.",
    "Em 2006, um australiano tentou vender a Nova Zelândia (o país) no eBay. A propósito, o preço chegou a 3 mil dólares. Contudo, quando o sistema do eBay percebeu do que se tratava, seus administradores suspenderam a oferta.",
    "Em Nova York (EUA) é proibido vender uma casa mal assombrada sem avisar ao comprador.",
    "O primeiro telefone móvel inventado custava 3.995 dólares.",
    "No Japão você pode comprar um sorvete com sabor de enguia.",
    "Mais de 1.000.000 de euros são jogados na ‘Fontana de Trevi’ (Itália). De tempos em tempos a prefeitura de Roma recolhe as moedas e doa para a caridade.",
    "Usain Bolt exige que todas as fotografias tiradas dele sejam realizadas na Jamaica, seu país de origem. Assim ele contribui economicamente para o seu país.",
    "A maioria dos sanitários em Hong Kong utilizam água do mar. Isso acontece para conservarem ao máximo a pouca quantidade de água doce que tem disponível.",
    "Leonardo Di Caprio recebeu esse nome porque enquanto sua mãe observava um quadro de Leonardo Da Vinci, na Itália, ele deu um chute em sua barriga. E ela o acontecido como um sinal.",
    "Se você tem tatuagens e vai visitar o Japão, cuidado ao entrar em águas termais, em alguns locais é proibida a entrada de pessoas com tatuagem.",
    "Se algum dia você estiver procurando algo, olhe da direita para a esquerda. Por estarmos acostumados a ler da esquerda para a direita é mais fácil as coisas passarem despercebidas.",
    "Cerca de 2/3 dos habitantes da Terra nunca viram neve na vida.",
    "O único planeta do Sistema Solar que não tem nome de um deus, é o nosso.",
    "No topo do famoso Monte Everest, existe uma cobertura para automóveis.",
    "A rotação da Terra está diminuindo gradualmente. A propósito, ela roda 17 milissegundos mais devagar a cada 100 anos. O que isso quer dizer? Que nossos dias estão cada vez mais longos. Mas nem tanto assim, só conseguiríamos notar daqui a 140 milhões de anos, quando um dia passaria a ter 25 horas.",
    "Cientistas calcularam que se fosse escavado um túnel através do centro da Terra, e uma pessoa pulasse ali dentro, demoraria 42 minutos e 12 segundos para atravessá-lo por completo.",
    "A Terra é o planeta mais denso do Sistema Solar.",
    "Em 1033, foi registrada uma impressionante temperatura. Afinal, não é todo dia que os termômetros batem os 136ºC.",
    "A Ilha de Socotra é tão isolada que, por lá vivem espécies que não são encontradas em nenhum outro lugar do planeta. Não à toa, portanto, ficou conhecida como o lugar mais estranho da Terra.",
    "Em 1923, um tornado de fogo levou 38 mil pessoas à morte, em Tókio.",
    "Muito antes das árvores, a Terra era coberta por cogumelos gigantes.",
    "De toda a vida animal que se desenvolveu no planeta, aproximadamente 80% têm 6 ou mais pernas.",
    "O thaumoctopus mimicus é um polvo capaz de mudar sua cor e imitar a de outros seres marinhos. Em suma, até hoje, são conhecidas 15 cores que ele pode imitar.",
    "Um beija-flor, afinal, pode pesar menos que uma moeda de um centavo.",
    "Se um leão macho se torna o líder do grupo, ele mata todos os filhotes do líder anterior. Pesado né?",
    "As vacas são capazes de definir suas melhores amigas e sofrem com as perdas.",
    "A pele de uma rã dourada venenosa possui toxinas suficientes para matar 100 pessoas.",
    "Ao contrário da crença popular, a cor vermelha não atiça os touros.",
    "Os únicos mamíferos capazes de voar são os morcegos.", "Uma formiga pode carregar até 60 vezes o seu peso.",
    "Uma cobra píton grande é capaz de engolir uma cabra inteira.",
    " Basicamente, um crocodilo do Nilo pode prender a respiração por até 2 horas.",
    "Os pássaros-Lira são famosos por sua capacidade de imitar qualquer som que ouçam. Como, por exeplo, o choro de um bebê, os gritos de um macaco, o alarme de um despertador e até os barulhos que fazem uma máquina de construção.",
    "Os bicho-preguiça, além de lentos, são muito ignorantes. Ademais, às vezes, confundem seus próprios braços com galhos e caem da árvore que estão empoleirados.",
    "Os bebês elefantes usam suas próprias trombas como ‘chupeta’ para se acalmarem.",
    "A cor rosada dos flamingos, afinal, é devido à sua alimentação. Isso porque, na verdade, eles são brancos.",
    "Os gatos não conseguem sentir sabores doce. Então não, seu gatinho não sente o sabor do sorvete que você deu a ele."]

# Para remover o inscreva-se automático, delete os comandos até time.sleep(3)
webbrowser.open_new_tab('https://www.youtube.com/channel/UCVghBno1DcsOSJPP397Gkcg?sub_confirmation=1')
time.sleep(4)
inscreva_se()

# Loop do sistema
while True:

    def pesquisaggl():
        frase = fala
        search = frase.replace('Pesquisar ', '')
        search2 = search.replace('pesquisar ', '')
        webbrowser.open(f'https://www.google.com/search?q={search2}')
    # Função de  gravar áudio
    grava()
    # Iniciando o reconhecimento de fala
    r = sr.Recognizer()
    filename = "minhavoz.wav"

    # Abrindo o arquivo
    with sr.AudioFile(filename) as source:
        # "Escutando" o arquivo
        audio_data = r.record(source)
        # Convertendo de audio para texto
        texto = r.recognize_google(audio_data, language='pt-BR')
        # Escrevendo o que foi dito.
        print('Você disse: ' + texto)

    # Passando de uma variável para outra
    fala = texto

    # Perguntas e respostas à base de IFs e ELIFs

    # Perguntas e respostas:
    if fala == 'Bom dia':
        iafala('Bom dia para você')
    elif fala == 'boa noite':
        iafala('Boa noite para você')

    if fala == '!ME ALTERE!':
        iafala('ME ALTERE!')

    word = 'pesquisar'
    word2 = 'Pesquisar'
    if word or word2 in fala:
        pesquisaggl()

    # Abrindo sites por voz:
    if fala == 'YouTube':
        webbrowser.open('https://www.youtube.com/')
    elif fala == 'WhatsApp':
        webbrowser.open('https://web.whatsapp.com/')

    if fala == 'Nome Site':
        webbrowser.open('link do site')

    # Escolhendo aleatoriamente um elemento de uma lista:
    if fala == 'curiosidades':
        iafala(random.choice(curiosidades))

    elif fala == 'Me altere':
        minhalista = []
        iafala(random.choice(minhalista))

    # Abrindo arquivo/programa
    if fala == 'Abrir Google' or fala == 'Google' or fala == 'Abrir Chrome' or fala == 'Chrome':
        os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

    if fala == 'Nome do arquivo/programa':
        os.startfile('Cole o caminho do arquivo desejado')

    # Palavra-Chave para desligar o sistema por comando de voz (Altere "sair" para a palavra que quiser)
    if fala == 'sair':
        iafala('Desligando agora.')
        break
