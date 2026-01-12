def hide_cursor():
  print("\033[?25l", end="")

def show_cursor():
  print("\033[?25h", end="")

def clear_screen():
  print("\033[2J\033[H", end="")

def format_time(time_format, current_time):
    if time_format=="24h":
     current_time==current_time.strftime("%H:%M:%S")
     return current_time.strftime("%H:%M:%S")
    elif time_format=="12h":
     current_time==current_time.strftime("%H:%M:%S")
     return current_time.strftime("%I:%M:%S %p")


def display_menu(time_string, time_format, is_paused):
    hide_cursor()
    pause_or_not= "in pause" if is_paused else ""
  
    print("\033[2;0H")
    print("Clock menu")
    print("\033[2K", end="")
    print(f"{time_string}({time_format}){pause_or_not}")
    print("1. Change time/tap a")
    print("2. Set an alarm/tap b")
    print("3. Reset time/tap c")
    print("4. change format/tap d")
    print("5. Pause/tap e")
    print("6. Ctrl+C to quit")