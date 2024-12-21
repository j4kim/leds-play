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
  - Flappy Bird
  - Un détecteur de mouvement qui allume les LEDs
  - Pong

## Matériel

- Raspberry Pi
- LEDs addressables: 2 x [bandes NeoPixel de 5m](https://www.bastelgarage.ch/rouleau-de-bande-led-neopixel-ws2812b-de-5m-30led-m?search=421328)
- Fil: [Câble 3x0.25mm²](https://www.bastelgarage.ch/cable-3x0-25mm-awg24-gris-liyy?search=420539)
- Alimentation:
  - [Adaptateur secteur 5V 2A](https://www.bastelgarage.ch/adaptateur-secteur-ac-dc-5v-dc-2000ma-prise-5-5mm-2-1mm?search=422326)
  - [Connecteur Barrel Jack](https://www.bastelgarage.ch/prise-dc-femelle-barrel-jack-5-5mm-2-1mm-avec-bornes-a-vis?search=420128)
  - [Condensateurs](https://www.bastelgarage.ch/condensateur-electrolytique-1000-f-25-v?search=420416)
- Contrôleurs Bluetooth: 2 x [Zero 2](https://www.8bitdo.com/zero2/)

## Développement

Créer un venv:

```sh
python -m venv venv
```

L'activer:

```sh
source venv/bin/activate
```

Créer le fichier de config:

```sh
cp config.py.example config.py
```

Deux drivers à choix dans `config.py`: "pygame" et "neopixel". 

### Driver pygame

À utiliser pour le prototypage

```sh
pip install -r drivers/pygame/requirements.txt
```

<video src="https://github.com/user-attachments/assets/5225aeb9-31cc-484a-9133-a43038fde24b"></video>

### Driver neopixel

Utilisable seulement sur le Raspberry.

```sh
pip install -r drivers/neopixel/requirements.txt
```

<img src="https://github.com/user-attachments/assets/3d76d101-3ce0-4852-8f79-8da803eaa03b" width="400" title="Prgramme 'random' sur le driver neopixel"/>

Pour manipuler les LEDs, on doit être admin, donc lancer python en sudo. Mais on ne peut pas faire ça lorsqu'un est dans un venv. Donc on doit cibler l'exécutable de python dans le venv:

```sh
sudo venv/bin/python main.py
```

## Dépendances

- [InquirerPy](https://inquirerpy.readthedocs.io/en/latest/index.html)
- (driver neopixel) [Adafruit CircuitPython NeoPixel](https://docs.circuitpython.org/projects/neopixel/en/latest/)
- (driver pygame) [pygame](https://www.pygame.org/docs/)

## Connexion SSH au Raspberry

```sh
ssh pi@192.168.1.116
# mot de passe
cd leds-play
sh run.sh
```
