# leds-play

Fun with LEDs, Raspberry &amp; Arduino

## Idée

- Mettre des LEDs derrière les carreaux de cette paroi vitrée dans mon appart:

<img src="https://github.com/user-attachments/assets/44430fdd-a368-4abf-a0f8-48c74fae11d4" width="400">

- Pouvoir déployer des programmes par FTP ou autre
- Pouvoir contrôler le programme avec un contrôleur Bluetooth

## Matériel

- Raspberry Pi
- LEDs addressables, exemples
  - [NeoPixel RGB 5050](https://www.adafruit.com/product/3094)
  - [LEDs WS2812B](https://www.amazon.fr/WS2812B-couleur-int%C3%A9gr%C3%A9-Symphonie-programmable/dp/B0B8D53RMS?dib=eyJ2IjoiMSJ9._Z_-WLQ1l7umCgRe701iq-5g3P8AZtPlisJOa6mQSpwttwznzy4S3GsKmTxgM7OO1sV5x3EcIHTLLdonusTmNcZSB-z2GTKiUT7QtVMEyI-bMUBcpZPLTWgdAYWCIw-LDe07_Znqr3cM1oj7H5VzLm__ijYwJsAjA-Yn9F_VD7wrX2P4Jtc3TOugckuUmhfAPRkhCZ1K5CGII-h8zZtBYskXbGZE4b9jjDaarGLrjwBemb1vAoMQWWHqlDyzlmtGbc3hTBt01adXf26K2X4v8RtdoBwkrSNtJzfDdcYRGbI.J7-X4YRyEk4x0iFxJdbn5Sf3T4De_t3I03NNI3HHdk0&dib_tag=se&keywords=led%2Bws2812b&qid=1732466870&sr=8-29&th=1)
- Fil
  - Le mieux serait d'avoir de la bande qui contient 3 fils pour connecter les 3 points sur les leds (signal, +, -) 
  - Flat Flexible Cable. [Ce genre de truc](https://fr.farnell.com/pro-power/pp001486/c-ble-cavalier-ffc-0-5mm-20-conduct/dp/2776611) mais il y a bcp trop de conducteurs.
  - Flat Ribbon Cable. [Ce genre de truc](https://www.galaxus.ch/fr/s1/product/rs-pro-cable-en-nappe-rs-pro-64-voies-28-awg-pas-de-127-cable-prise-electronique-19209271?utm_campaign=organicshopping&utm_source=google&utm_medium=organic&utm_content=3013528&supplier=3013528) mais ça risque d'être trop gros non ?
  - [Mais wtf c'est vrm plus de 1000 balles pour 30 m de câble ?](https://www.distrelec.ch/en/ribbon-cable-34x-08mm-unscreened-30m-3m-3319-34/p/30110005?trackQuery=Ribbon%20Cable%203x&pos=3&origPos=3&origPageSize=50&track=true&sid=9e94e76945791b7664f9a640b764447b2234c631&itemList=search)
  - Câbles gainés. [Exemple](https://www.digitec.ch/fr/s1/product/rs-pro-cable-electrique-rs-pro-3g075-mm-gaine-caoutcho-25-m-cable-dalimentation-19221828?utm_campaign=organicshopping&utm_source=google&utm_medium=organic&utm_content=3013528&supplier=3013528) Il fait 0.78 cm de diamètre donc un peu gros.
  - [Celui-là](https://www.conrad.ch/fr/p/econ-connect-28awg4gr-cable-en-nappe-pas-1-27-mm-4-x-0-08-mm-gris-30-50-m-1656453.html) dit 4 conducteurs mais j'en compte 8, bizarre.
  - [Bon ça ça à l'air nickel non ?](https://www.distrelec.ch/fr/cable-en-nappe-pvc-3x-25mm-non-blinde-30m-rnd-rnd-475-00804/p/30139982?trackQuery=cat-DNAV_PL_091302&pos=11&origPos=1&origPageSize=50&track=true&filterapplied=filter_P%25C3%25B4les%3D3&sid=c5f79fc5168fd2bd72c0a0d504ea358c5187ecec&itemList=category)
  - ou alors juste du [fil de cuivre émaillé](https://www.conrad.ch/fr/p/fil-de-cuivre-emaille-block-cul-100-0-15-o-exterieur-sans-vernis-isolant-0-15-mm-609-m-0-10-kg-605053.html) et du scotch non ? Bon ça va être super relou à faire par contre.
- Contrôleur Bluetooth
  - Un truc déjà tout fait ? Exemple [Zero 2](https://www.8bitdo.com/zero2/)
  - Un module prêt à l'emploi ? [Bluefruit EZ-Key](https://www.adafruit.com/product/1535)
  - DIY total
    - Un microcontrôleur [Arduino Nano 33 BLE](https://store.arduino.cc/products/arduino-nano-33-ble)
    - Une [batterie LiPo](https://www.conrad.ch/fr/p/reely-pack-de-batterie-lipo-3-7-v-1000-mah-nombre-de-cellules-1-30-c-bec-2582341.html)
    - Un module de charge genre [TP4056](https://www.bastelgarage.ch/module-de-chargement-batterie-tp4056-lithium-lipo-usb-c-5v-1a)
    - Des boutons
    - Imprimer une boîte en plastique
