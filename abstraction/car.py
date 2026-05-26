import time

class Car:
    """
    Represents a car. The internal mechanics are abstracted away from the driver.
    The methods starting with an underscore (_) are internal implementation details
    that the driver does not need to know about.
    """
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self._is_running = False
        self._speed = 0
        self._fuel_level = 100.0

    # --- Internal (hidden) methods ---
    def _check_fuel(self):
        """Internal method to check if there is fuel."""
        print("   - (Internal) Checking fuel...")
        if self._fuel_level > 0:
            return True
        else:
            print("   - (Internal) Out of fuel!")
            return False

    def _ignite_spark_plug(self):
        """Internal method simulating spark plug ignition."""
        print("   - (Internal) Spark plug fires.")
        time.sleep(0.5)

    def _inject_fuel(self):
        """Internal method simulating fuel injection."""
        print("   - (Internal) Injecting fuel into engine.")
        self._fuel_level -= 2.5 # Consume some fuel to start
        time.sleep(0.5)

    # --- Public (exposed) interface for the driver ---
    def start(self):
        """
        Starts the car. This is part of the public interface.
        It calls several complex, hidden methods.
        """
        print("\nTurning the key to start the car...")
        if not self._is_running and self._check_fuel():
            self._inject_fuel()
            self._ignite_spark_plug()
            self._is_running = True
            print(f"The {self.make} {self.model}'s engine is now running!")
        elif self._is_running:
            print("The car is already running.")
        else:
            print("Cannot start the car.")

    def accelerate(self):
        """Makes the car go faster."""
        if self._is_running and self._fuel_level > 0:
            self._fuel_level -= 5
            self._speed += 10
            print(f"\nAccelerating... Current speed: {self._speed} mph.")
            if self._fuel_level <= 0:
                print("Warning: Ran out of fuel!")
                self._is_running = False
                self._speed = 0
        else:
            print("\nCannot accelerate. The engine is not running.")
            
    def brake(self):
        """Slows the car down."""
        if self._speed > 0:
            self._speed -= 15
            if self._speed < 0:
                self._speed = 0
            print(f"\nBraking... Current speed: {self._speed} mph.")
        else:
            print("\nThe car is already stopped.")

    def get_status(self):
        """Reports the current status of the car."""
        status = "running" if self._is_running else "off"
        print(f"\n--- Car Status ---")
        print(f"  Speed: {self._speed} mph")
        print(f"  Engine: {status}")
        print(f"  Fuel: {self._fuel_level:.2f}%")
        print(f"--------------------")


# --- Using the Abstraction ---
# The driver only needs to know these simple commands.
if __name__ == "__main__":
    my_car = Car("Tesla", "Model S") # Oops, let's pretend it's a gas car for the example :)
    
    # The driver interacts with the simple, abstract interface.
    my_car.get_status()
    my_car.start()
    my_car.get_status()
    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()
    my_car.accelerate()
    my_car.get_status()
    my_car.brake()
    my_car.brake()
    my_car.brake()
    my_car.get_status()