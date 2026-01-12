import time
import keyboard
from clock import Clock

def menu():
    # On crée une instance de l'horloge
    my_clock = Clock()
    my_clock.start_running()

    while True:
        print("\033[?25l", end="") # Cache le curseur
        
        # Affichage
        print("\033[2;0H")
        print("Clock menu")
        print("\033[K", end="")
        print(f"{my_clock.get_formatted_time()} ({my_clock.time_format})")
        print("\033[4;0H")
        print("1. Change time/tap a")
        print("\033[5;0H")
        print("2. Set an alarm/tap b")
        print("\033[6;0H")
        print("3. Reset time/tap c")
        print("\033[7;0H")
        print("4. change format/tap d")
        
        time.sleep(0.01)
        print("\033[J", end="")

        # Vérification Alarme
        if my_clock.set_time_alarm and \
           my_clock.current_time.strftime("%H:%M:%S") == my_clock.set_time_alarm.strftime("%H:%M:%S"):
            print("\033[H\033[J", end="")
            print("your alarm is ringing!")
            my_clock.set_time_alarm = None  
            time.sleep(5)
            continue
        
        # Interactions clavier
        elif keyboard.is_pressed("a"):
            print("\033[?25h", end="")
            try:
                H = int(input("choose an hour: "))
                M = int(input("choose minutes: "))
                S = int(input("choose seconds: "))
                my_clock.define_time(H, M, S)
            except ValueError:
                print("Enter numbers only!")
                time.sleep(2)

        elif keyboard.is_pressed("b"):
            print("\033[?25h", end="")
            try:
                h_al = int(input("choose an hour: "))
                m_al = int(input("choose minutes: "))
                s_al = int(input("choose seconds: "))
                alarm_str = my_clock.set_alarm(h_al, m_al, s_al)
                print(f"alarm set at: {alarm_str}")
                time.sleep(1)
            except ValueError:
                print("Enter numbers only!")
                time.sleep(2)

        elif keyboard.is_pressed("c"):
            my_clock.reset_time()
            time.sleep(0.3)

        elif keyboard.is_pressed("d"):
            my_clock.change_format()
            time.sleep(0.3)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        # On affiche un message gracieux au lieu d'une erreur technique
        print("\n\033[?25h") # Réaffiche le curseur
        print("Clock stopped!")