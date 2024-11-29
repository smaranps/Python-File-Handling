import requests

inp = input("Enter anything: ")
fileName= input("What is the name of your file (QR CODE image file name): ")

QR = requests.get(f"https://api.qrserver.com/v1/create-qr-code/?data={inp}&size=512x512")
QRJS = QR.content
file = open(f"{fileName}.jpg","wb")
file.write(QRJS)
file.close()
print(QRJS)