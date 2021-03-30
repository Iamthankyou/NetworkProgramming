import ipaddress as ip

if __name__ == '__main__':
    IP_ADDR = '192.168.0.0/26'

    network_ = ip.ip_network(IP_ADDR)
    print('So mang con {}'.format(network_.num_addresses))
    print('Network address : {}'.format(network_.network_address))
    print('Net mask: {}'.format(network_.netmask))
    dcdau, dccuoi = list(network_.hosts())[0], list(network_.hosts())[-1]
    print('mag co dai tu {0} den {1} '.format(dcdau,dccuoi))
    print('dia chi quang ba {}'.format(network_.broadcast_address))
