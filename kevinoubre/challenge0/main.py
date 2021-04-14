from ftplib import FTP


IP = "138.47.102.120"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/7/"
MODE=7
USE_PASSIVE = True # set to False if the connection times out
REMOTE = False

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

data = []
justperms = []
print("FILES:")
# display the folder contents
for f in files:
    print(f)
    data.append(f)
    justperms.append(f[:10])