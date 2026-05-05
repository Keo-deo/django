import subprocess
import webbrowser
import serial
import os # Biblioteca para comandos do sistema

# chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

porta_arduino = 'COM5' 

try:
    conexao = serial.Serial(porta_arduino, 9600, timeout=1)
    print(f"Conectado na ao arduino pela porta {porta_arduino}.")

    while True:
        if conexao.in_waiting > 0:
            linha = conexao.readline().decode('utf-8').strip()
            
            if linha == "Youtube":
                print("youtube")
                webbrowser.open("https://www.youtube.com/")
            if linha == "Git Hub":
                print("git hub")
                webbrowser.open("https://github.com/")
            if linha == "Programacao":
                print("Programcao")
                webbrowser.open("https://gemini.google.com/app/4d18c528ad02cd75")
            if linha == "arduino":
                print("Arduino")
                webbrowser.open("https://gemini.google.com/app/fffbf1845717b475")
            if linha == "Whatsapp":
                print("WhatsApp")
                webbrowser.open("https://web.whatsapp.com/")
            if linha == "Django":
                print("servidor django iniciado")
                os.system(r'start cmd /k "cd C:\Users\Murilo\django\projeto && python manage.py runserver 0.0.0.0:8000"')
            if linha == "Spotify":
                print("Spotify")
                webbrowser.open("https://open.spotify.com/")
            if linha == "VScode":
                caminho_vsc = r"C:\Users\Murilo\Microsoft VS Code\Code.exe"
                if os.path.exists(caminho_vsc):
                    print("Visual Studio Code")
                    subprocess.Popen([caminho_vsc])
            if linha == "Mongo":
                caminho_MDB = r"C:\Users\Murilo\AppData\Local\MongoDBCompass\MongoDBCompass.exe"
                if os.path.exists(caminho_MDB):
                    print("MongoDB Compass")
                    subprocess.Popen([caminho_MDB])
except Exception as e:
    print(f"Erro de conexão: {e}")
    print("Dica: Feche o Monitor Serial da IDE do Arduino!")