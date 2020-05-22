ipv4Hex = ''
ipv6Hextet1 = '2002'
ipv6Hextet2 = ''
ipv6Hextet3 = ''

#take input
print('Enter IPv4 address:')
ipv4 = input()

#split input to octets
ipv4 = ipv4.split('.',4)

#convert IPv4 address to hex string
for octet in ipv4:
	if len(hex(int(octet))[2:])>1:
		ipv4Hex += hex(int(octet))[2:]
	else:
		ipv4Hex += '0'
		ipv4Hex += hex(int(octet))[2:]

#split into hextets
for i in range(4):
	ipv6Hextet2 += (ipv4Hex[i])
for i in range(4,8):
	ipv6Hextet3 += (ipv4Hex[i])

#Convert to dec and back to remove leading zeros
ipv6Hextet2 = hex(int(ipv6Hextet2,16))[2:]
ipv6Hextet3 = hex(int(ipv6Hextet3,16))[2:]

#form and print 6to4 address
print(ipv6Hextet1+':'+ipv6Hextet2+':'+ipv6Hextet3+'::/128')