import ftplib
from ftplib import FTP
from secrets import password

host = 'localhost'
user = 'chelsieconrad'

with FTP(host) as ftp:
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

    # Attempt to retrieve the deleted file
    try:
        with open('test.txt', 'wb') as f:
            ftp.retrbinary('RETR ' + 'upload.txt', f.write, 1024)
    except ftplib.all_errors as e:
        if e.args[0][:3]:
            print(e)
            print('File not found')
        else:
            print(e)

    ftp.quit()
