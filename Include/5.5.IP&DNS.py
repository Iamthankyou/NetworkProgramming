import ntplib
from time import ctime

if __name__ == '__main__':
    client = ntplib.NTPClient()
    r = client.request('pool.ntp.org')

    # thoi gian may chu : tx time
    print("thoi gian may chu: {}".format(ctime(r.tx_time)))
    #tham chieu thoi gian ref_id_to_text  stratum
    print("ref clock {}",ntplib.ref_id_to_text(r.ref_id,r.stratum))
    print("offset: {}".format(r.offset))
    print("delay: {}".format(r.root_delay))