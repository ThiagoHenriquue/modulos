import os

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - Versao do sistema operacional
os.system('ver')

# 4 - Configuracoes da maquina
os.system('systeminfo')

# 5 - Limpar a tela do terminal 
os.system('cls')

# Desligar o Computador e cancelar o pc
# os.system('shutdown /s')
# os.system('shutdown /s /t 0')
# os.system('shutdown /a')

"""
def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_half_an_hour():
    os.system('shutdown /s /t 1800')

def cancel_shutdonw():
    os.system('shutdown /a')

turn_off_half_an_hour()
cancel_shutdonw()"""