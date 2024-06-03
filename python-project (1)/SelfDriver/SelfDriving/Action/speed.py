class Speed:
    def __init__(self, initial_speed: int = 0):
        self._speed = initial_speed
        self._deceleration = False

    def decrease(self, amount: int):
        """Decreases the speed by the specified amount."""
        if self._deceleration:
            self._apply_deceleration(amount)
        else:
            new_speed = max(self._speed - amount, 0)
            if new_speed != self._speed:
                self._speed = new_speed
                print(f"Speed decreased to {self._speed}")

    def _apply_deceleration(self, amount: int):
        """Applies deceleration to the speed."""
        new_speed = max(self._speed - amount, 0)
        if new_speed != self._speed:
            self._speed = new_speed
            print(f"Deceleration applied. Speed is now {self._speed}")

    def start_deceleration(self):
        """Starts the deceleration process."""
        self._deceleration = True
        print("Deceleration started.")

    def stop_deceleration(self):
        """Stops the deceleration process."""
        self._deceleration = False
        print("Deceleration stopped.")

    def hold_down_to_stop(self, amount: int):
        """Decreases the speed continuously until it reaches zero."""
        max_iterations = 1000  # Limit the maximum number of iterations
        iterations = 0
        while not self.is_stopped() and iterations < max_iterations:
            self.decrease(amount)
            iterations += 1
        if iterations >= max_iterations:
            print("Maximum iterations reached. Unable to stop.")

    def increase(self, amount: int):
        """Increases the speed by the specified amount."""
        new_speed = min(self._speed + amount, 100)
        if new_speed != self._speed:
            self._speed = new_speed
            print(f"Speed increased to {self._speed}")

    def is_stopped(self) -> bool:
        """Checks if the speed has reached zero."""
        return self._speed == 0

    def get_speed(self) -> int:
        """Returns the current speed."""
        return self._speed
