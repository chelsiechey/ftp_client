import ftplib
from ftplib import FTP
from os.path import exists

host = 'localhost'

with FTP(host) as ftp:
    if exists('secrets.py'):
        from secrets import password, user
    else:
        print('Please enter your username')
        user = input()
        print('Please enter your password')
        password = input()

    ftp_response = ftp.login(user=user, passwd=password)
    print(ftp_response)

    # Upload test_upload_file.txt to the FTP server as upload.txt
    with open('test_upload_file.txt', 'rb') as f:
        ftp_response = ftp.storbinary('STOR ' + 'upload.txt', f)
        print(ftp_response)

    # Retrieve upload.txt from the FTP server and write it to test.txt
    with open('test.txt', 'wb') as f:
        ftp_response = ftp.retrbinary('RETR ' + 'upload.txt', f.write, 1024)
        print(ftp_response)

    # Delete a file
    ftp_response = ftp.delete('upload.txt')
    print(ftp_response)

    ftp.quit()
