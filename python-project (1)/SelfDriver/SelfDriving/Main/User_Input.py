class AutomatedCarUI:
    def __init__(self, sleep_time=1):
        self.sleep_time = sleep_time
        self.ux_print("Hello! Welcome to the Automated Car System. AIU for short")

    def ux_print(self, message):
        print(message)

    def get_destination(self):
        destination = self.get_string("Where are you going?: ")
        return destination

    def get_string(self, prompt):
        return input(prompt)
