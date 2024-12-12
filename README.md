# leds-play

Fun with LEDs & Raspberry

## Idée

- Mettre des LEDs derrière les carreaux de cette paroi vitrée dans mon appart pour en faire un écran de 6x7 px.

<img src="https://github.com/user-attachments/assets/44430fdd-a368-4abf-a0f8-48c74fae11d4" width="400">

- Pouvoir déployer des programmes par SSH, HTTP ou autre
- Pouvoir contrôler le programme avec un contrôleur Bluetooth
- Idées de programmes:
  - Snake
  - Tetris
  - Message défilant
  - Réaction à la musique (ASIO?)
  - Crazy Taxi
  - Doodle Jump
  - Flappy Bird
  - Un détecteur de mouvement qui allume les LEDs

## Matériel

- Raspberry Pi
- LEDs addressables: 2 x [bandes NeoPixel de 5m](https://www.bastelgarage.ch/rouleau-de-bande-led-neopixel-ws2812b-de-5m-30led-m?search=421328)
- Fil: [Câble 3x0.25mm²](https://www.bastelgarage.ch/cable-3x0-25mm-awg24-gris-liyy?search=420539)
- Alimentation:
  - [Adaptateur secteur 5V 2A](https://www.bastelgarage.ch/adaptateur-secteur-ac-dc-5v-dc-2000ma-prise-5-5mm-2-1mm?search=422326)
  - [Connecteur Barrel Jack](https://www.bastelgarage.ch/prise-dc-femelle-barrel-jack-5-5mm-2-1mm-avec-bornes-a-vis?search=420128)
  - [Condensateurs](https://www.bastelgarage.ch/condensateur-electrolytique-1000-f-25-v?search=420416)
- Contrôleur Bluetooth: [Zero 2](https://www.8bitdo.com/zero2/)

## Connexion SSH

```sh
ssh pi@192.168.1.116
# mot de passe
cd leds-play
```

## Développement

```
python -m venv venv
```

```
pip install -r requirements.txt
```

## Dépendances

- [Adafruit CircuitPython NeoPixel](https://docs.circuitpython.org/projects/neopixel/en/latest/)
- [InquirerPy](https://inquirerpy.readthedocs.io/en/latest/index.html)