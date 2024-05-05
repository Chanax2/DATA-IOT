from machine import Pin, PWM
import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'CEO'
password = 'aaaeeerr'
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://192.168.224.136:3000/house"

led = [PWM(Pin(13, mode=Pin.OUT)), PWM(Pin(14, mode=Pin.OUT)), PWM(Pin(15, mode=Pin.OUT))]

while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

maison = {
"Gryffindor": [255,0,0],
"Hufflepuff": [200,200,0],
"Ravenclaw": [0,0,255],
"Slytherin":[0,255,0],
"":[255,255,255]}

def Color(c):
    for i in range(3):
        led[i].duty_u16(c[i]*256)


while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        Color(maison[r.json()["house"]])
        r.close() # ferme la demande
        utime.sleep(1)  
    except Exception as e:
        print(e)
    