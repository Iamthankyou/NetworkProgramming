from ftplib import FTP

if __name__ == '__main__':
    f = FTP('ftp.ibiblio.org')
    print('Nofication from server: {}'.format(f.getwelcome()))
    try:
        f.login()
        print('Folder now:{}'.format(f.pwd()))
        # fd = f.nlst("/")
        # print('Sum all files directory: {}'.format(len(fd)))
        #
        # f.cwd('/pub/')
        #
        # for i in fd:
        #     print(i)

        # files= []
        # f.dir(files.append)
        # print(files)

        print(f.retrlines('LIST'))

        file_name = "HEADER.html"
        file_stream = open(file_name, "wb")
        f.retrbinary('RETR {}'.format(file_name),file_stream.write, 1024)
        file_stream.close()

    except FTP.all_errors as e:
        print('Error {}'.format(e))
    f.quit()