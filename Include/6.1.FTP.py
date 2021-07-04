import ftplib
import os
from ftplib import FTP

if __name__ == '__main__':
    f = FTP('ftp.ibiblio.org')
    print("Thong bao tu server: %s "%f.getwelcome())
    f1 = 'HEADER.html'
    f2 = 'HEADER.html'
    try:
        f.login()
        print("Thu muc hien thoi: %s"%f.pwd())
        #hien thi cac file va thu muc
        #fd = f.nlst("/")
        # fd.sort()
        # print("tong so file va thu muc:%s" %len(fd))
        # for i in fd:
        #     print(i)
        # chuyen vao thu muc
        # f.cwd('/pub/')
        # fd = f.nlst("")
        # fd.sort()
        # print("tong so file va thu muc:%s" % len(fd))
        # for i in fd:
        #     print(i)

        # files = []
        # f.dir(files.append())
        # print(files)
        f.sendcmd('TYPE I')
        s = f.size('HEADER.html')
        print(s)

        with open(f2, 'w') as fp:
            r = f.retrlines('RETR' + f1, fp.write)
            if not r.startswith('226 Transfer complete'):
                print("loi")
                if os.path.isfile(f2):
                    os.remove(f2)

    except ftplib.all_errors as e:
        print("error:",e)
        if os.path.isfile(f2):
            os.remove(f2)
    f.quit()
