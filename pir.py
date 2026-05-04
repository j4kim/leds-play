import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("Initialisation du capteur PIR... attendre 30s")
time.sleep(30)  # Le HC-SR501 a besoin de 30s pour se calibrer
print("Prêt !")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Mouvement détecté !")
        else:
            print("Pas de mouvement")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Arrêt du programme")
    GPIO.cleanup()
