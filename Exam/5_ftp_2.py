from ftplib import FTP

if __name__ == '__main__':
    ftp_ip = "ftp.byethost15.com"
    ftp_usr = "b15_28062580"
    ftp_pwd = "Nuw%8#&,fMpqzp9"

    f = FTP(ftp_ip)

    try:
        f.login(user=ftp_usr, passwd=ftp_pwd)
        print(f.getwelcome())
        f.cwd('htdocs')

        print('All file name and folder in ', f.pwd())
        for i in f.nlst():
            print(i)

        while True:
            folder_name = input('Please typing folder name: ')
            f.mkd(folder_name)
            print(f.retrlines('LIST'))

    except FTP.all_error as e:
        print(e)