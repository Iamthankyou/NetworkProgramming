import dns.resolver

if __name__ == '__main__':
    hostname = 'www.gmail.com'
    kieubannghi = 'CNAME' # 'A' / 'CNAME' / 'MX'

    # truy van
    q = dns.resolver.resolve(hostname, kieubannghi)
    if kieubannghi == 'A':
        print("dia chi ip: %s" %[x.to_text() for x in q ])
    if kieubannghi == 'CNAME':
        print("Alias %s:"%[x.to_text() for x in q])
    if kieubannghi == 'MX':
        for i in q:
            print("Mail server: ",i.exchange.to_text())