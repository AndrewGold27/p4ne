from ipaddress import IPv4Network
import random

def f(d):
    return d.key_value()

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        iprandom=random.randint(0x0B000000,0xDF000000)
        maskrandom=random.randint(8,24)
        IPv4Network.__init__(self,(iprandom,maskrandom),strict=False)
    def key_value(self):
          return int(self.network_address._ip) + int(self.netmask._ip)*2**32


list_of_networks=[]
for i in range (0,50):
    list_of_networks.append(IPv4RandomNetwork())
#for x in sorted(list_of_networks, key=f):
for x in sorted(list_of_networks, key=IPv4RandomNetwork.key_value):
    print(x)


#int(IPv4Network.network_address._ip) — получить адрес подсети в виде числа
#int(IPv4Network.netmask._ip) — получить маску подсети в виде числа


#sorted(последовательность, key=функция) — возвращает отсортированную последовательность

