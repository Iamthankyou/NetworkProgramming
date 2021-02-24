import dns.resolver

if __name__ == '__main__':
    hostname = 'www.gmail.com'
    kieubanghi = 'CNAME' # 'A','CNAME','MX'

    #Query
    q = dns.resolver.resolve(hostname,kieubanghi)
    if kieubanghi == 'A':
        print('Ip Address: %s'%[x.to_text()] for x in q)
    if kieubanghi == 'CNAME':
        print('Alias: %s' % [x.to_text()] for x in q)
    if kieubanghi == 'MX':
        for i in q:
            print('Mail server:',i.exchange.to_text())
