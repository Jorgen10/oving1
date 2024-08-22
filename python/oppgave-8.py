seconds = float(input("Skriv inn antall sekunder objektet har falt: "))
acceleration = 9.81
originalSpeed = 0
currentSpeed = originalSpeed + acceleration*seconds
distance = 0.5*currentSpeed*seconds

print(f"Farten er {currentSpeed} m/s, og objektet har falt {distance} m.")