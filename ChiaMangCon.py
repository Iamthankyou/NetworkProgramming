import ipaddress as ip

if __name__ == '__main__':
    IP_ADDR = '192.168.0.0/26'
    network = ip.ip_network(IP_ADDR)
    print('So mang con: {}'.format(network.num_addresses)) #Subnetting
    print('Network address: {}'.format(network.network_address))
    print('Netmask {}'.format(network.netmask))
    dia_chi_dau,dia_chi_cuoi = list(network.hosts())[0],list(network.hosts())[-1]
    print('Dia chi dau: ', dia_chi_dau)
    print('Dia chi cuoi: ', dia_chi_cuoi)
    print('Dia chi quang ba: ', network.broadcast_address)