from datetime import datetime, timedelta
import time
import threading

class Clock:
    def __init__(self):
        # On initialise les variables d'état ici
        self.current_time = datetime.now()
        self.set_time_alarm = None
        self.time_format = "24h"

    def start_running(self):
        """Lance le thread de l'horloge."""
        thread = threading.Thread(target=self._running_hour, daemon=True)
        thread.start()

    def _running_hour(self):
        """Méthode interne pour incrémenter le temps."""
        while True:
            self.current_time += timedelta(seconds=1)
            time.sleep(1)

    def define_time(self, hours, minutes, seconds):
        self.current_time = self.current_time.replace(
            hour=hours, minute=minutes, second=seconds
        )

    def set_alarm(self, h, m, s):
        self.set_time_alarm = self.current_time.replace(
            hour=h, minute=m, second=s
        )
        return self.set_time_alarm.time().strftime("%H:%M:%S")

    def reset_time(self):
        self.current_time = datetime.now()

    def change_format(self):
        if self.time_format == "24h":
            self.time_format = "12h"
        else:
            self.time_format = "24h"

    def get_formatted_time(self):
        if self.time_format == "12h":
            return self.current_time.strftime("%I:%M:%S %p")
        return self.current_time.strftime("%H:%M:%S")