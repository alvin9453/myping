import os
import sys
import socket
import getopt

def addr_version(addr):
	try:
		socket.inet_aton(addr)
		return 4

	except socket.error:
		try:
			socket.inet_pton(socket.AF_INET6, addr)
			return 6
		except socket.error:
			return 


def get_addr(dest_addr , version):
	v6_exist = False
	unknow_host = False
	try :
		addr_info = socket.getaddrinfo( dest_addr,80, 0, 0, socket.IPPROTO_TCP)
		if version == 4:  # If option is '-4' , find IPv4 addr and return
			for i in range(0,len(addr_info)):  
				if addr_version( addr_info[i][4][0] ) == 4:
					dest_addr = addr_info[i][4][0]
					return unknow_host,dest_addr
		
		# No options in user input
		for i in range(0,len(addr_info)):   # if there is IPv6 addr -> use it
			if addr_version( addr_info[i][4][0] ) == 6 :
				v6_exist = True
				dest_addr = addr_info[i][4][0]
				break
		if not v6_exist :  # if no IPv6 addr -> use the first IPv4 addr
			dest_addr = addr_info[0][4][0]
	except :
		unknow_host = True
		pass
	
	return unknow_host,dest_addr

def main():
	choose_version = None
	remote_addr = sys.argv[1]
	options, remainder = getopt.getopt(sys.argv[1:], '4:' , '')

	for opt, arg in options:
		if opt == '-4':
			choose_version = 4
		remote_addr = arg

	is_unknow_host , dest_addr = get_addr( remote_addr , choose_version)

	if is_unknow_host:
		cmd = "ping " + dest_addr
	elif addr_version(dest_addr) == 4 or choose_version == 4:
		cmd = "ping " + dest_addr
	elif addr_version(dest_addr) == 6:
		cmd = "ping6 " + dest_addr
	#else:
		#print ("There must be something wrong so you are here.")
	
	os.system(cmd)
	
		
if __name__ == '__main__':
	main()
