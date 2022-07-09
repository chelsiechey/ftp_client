from ftplib import FTP
from secrets import password

host = 'localhost'
user = 'chelsieconrad'

with FTP(host) as ftp:

    ftp.login(user=user, passwd=password)

    # Confirm connection
    print(ftp.getwelcome())

    # Upload test_upload_file.txt to the FTP server as upload.txt
    with open('test_upload_file.txt', 'rb') as f:
        ftp.storbinary('STOR ' + 'upload.txt', f)

    # Retrieve upload.txt from the FTP server and write it to test.txt
    with open('test.txt', 'wb') as f:
        ftp.retrbinary('RETR ' + 'upload.txt', f.write, 1024)

    ftp.quit()