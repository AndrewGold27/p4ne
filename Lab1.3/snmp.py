from pysnmp.hlapi import * # Импортировать только High-level API

result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
                  lexicographicMode=False)


# result2 = nextCmd (..., lexicographicMode=False) # Не идти в глубину

#snmp_object1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной

#snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной

for x in result:
    v=x[3]
    print (v)
for y in v:
    for z in y:
        print (z)


for x in result2:
   v=x[3]
   print (v)
for y in v:
   for z in y:
        print (z)