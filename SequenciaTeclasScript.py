import pyautogui
import time

def move_character(sequencia, delay_tecla, delay_iniciar):
    print(f"Iniciando em {delay_iniciar} segundos.")
    time.sleep(delay_iniciar)
    
    for key in sequencia:
        if key.lower() in ['w', 'a', 's', 'd']:
            pyautogui.keyDown(key.lower())
            time.sleep(delay_tecla)
            pyautogui.keyUp(key.lower())
            time.sleep(0.1)

if __name__ == "__main__":
    sequencia = input("Digite a sequência de teclas (WASD) que deseja mover: ").strip()
    
    delay_tecla = float(input("Digite a duração de cada pressionamento de tecla em segundos: ").strip())
    
    delay_iniciar = float(input("Digite o tempo de atraso antes de iniciar em segundos: ").strip())

    move_character(sequencia, delay_tecla, delay_iniciar)
    print("Sequência de movimentos completada!")