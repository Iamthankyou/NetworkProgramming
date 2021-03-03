from ftplib import FTP

if __name__ == '__main__':
    ftp_ip = "ftp.byethost15.com"
    ftp_usr = "b15_28062580"
    ftp_pwd = "Nuw%8#&,fMpqzp9"

    f = FTP(ftp_ip)

    try:
        f.login(user=ftp_usr,passwd=ftp_pwd)
        print('Nofication from server: {}'.format(f.getwelcome()))
        print(f.pwd())
        f.cwd('htdocs')
        #Show all files
        print('Before upload:')
        print(f.retrlines('LIST'))

        #Upload file
        # read file to send to byte
        file_stream = open("index.html", "rb")

        # send the file
        f.storbinary("{CMD} {FileName}".format(CMD="STOR", FileName="index.html"), file_stream)
        file_stream.close()
        print('Apter upload')
        print(f.retrlines('LIST'))

    except FTP.all_errors as e:
        print('Error {}'.format(e))

    f.quit()