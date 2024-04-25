from ftplib import FTP

ftp = FTP('192.168.[班番号].1')
ftp.login('user', 'password')
print(ftp.retrlines('LIST'))
file = open('hogehoge.csv', 'rb')
ftp.cwd('/target_dir/')
ftp.storbinary('STOR hogehoge_rcv.csv', file)
file.close()
ftp.quit()
