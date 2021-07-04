from ftplib import FTP

if __name__ == '__main__':
    ftp_ip = "ftp.byethost15.com"
    ftp_usr = "b15_28062580"
    ftp_pwd = "Nuw%8#&,fMpqzp9"

    f = FTP(ftp_ip)

    try:
        f.login(user=ftp_usr, passwd=ftp_pwd)
        print('Notification from server: ', f.getwelcome())
        print('Current location: ', f.pwd())
        f.cwd('htdocs')
        print('Current location: ', f.pwd())
        print('List show',f.retrlines('LIST'))
        file = input('Please typing name file: ')

        flag = False
        for i in f.nlst():
            if file == i:
                flag = True
                break
        if flag == True:
            print('Founded file on server')
            print(f.pwd(file))

        else:
            print('File not found on server')

        htmlfile = f.open('index.html','r')
        readfile = htmlfile.read()
        print(readfile)

    except FTP.all_error as e:
        print(e)

