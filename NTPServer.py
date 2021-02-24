import ntplib
from time import ctime

if __name__ == '__main__':
    client = ntplib.NTPClient()
    r = client.request('pool.ntp.org')
    # Time on server:
    print('Time show in server: ', ctime(r.tx_time))
    # Reference time ref_id_to_text:
    print('Ref cloke {}'.format(ntplib.ref_id_to_text(r.ref_id)))