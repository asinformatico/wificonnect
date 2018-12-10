print " __          __ _____  ______  _____         _____                                  _      "
print " \ \        / /|_   _||  ____||_   _|       / ____|                                | |     "
print "  \ \  /\  / /   | |  | |__     | | ______ | |      ___   _ __   _ __    ___   ___ | |_    "
print "   \ \/  \/ /    | |  |  __|    | ||______|| |     / _ \ | '_ \ | '_ \  / _ \ / __|| __|   "
print "    \  /\  /    _| |_ | |      _| |_       | |____| (_) || | | || | | ||  __/| (__ | |_    "
print "     \/  \/    |_____||_|     |_____|       \_____|\___/ |_| |_||_| |_| \___| \___| \__|   "
print "==========================================================================================="
print " By Jesús Pacheco - Follow me on Twitter: @as_informatico \n"
                                                                                       
import os

os.system('nmcli d | grep "wifi" > tarjetawifi')
f = open('tarjetawifi', 'r')
tarjetawifi = tarjetawifi.split(' ')
tarjetawifi = tarjetawifi[0]

os.system('ifconfig ' + tarjetawifi + ' up')

print "Redes Wifi detectadas:"
os.system('iwlist ' + tarjetawifi + ' scan | grep "ESSID:"')

wifiseleccionada = raw_input("Escriba el nombre de la red a la que quiere conectarse:")
clavewifi = raw_input("Introduzca la clave de la red WiFi:")

os.system('nmcli d wifi connect "' + wifiseleccionada + '" password "' + clavewifi + '" iface ' + tarjetawifi)
os.system('nmcli c up "' + wifiseleccionada + '"')
print "Se ha conectado a la red " + wifiseeccionada + " correctamente."

                                                                                       
