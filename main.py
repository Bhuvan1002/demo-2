import qrcode 
import os  
def genrate_qr():
    url = input("enter your url :")
    img = qrcode.make(url) 
    folder_name = "qrcodes"
    if not os.path.exists(folder_name): 
        os.makedirs(folder_name) 

    file=os.path.join(folder_name,"qrcode.png") 
    img.save(file) 
    print(f"qr code generated and saved as : {folder_name}")

if __name__ == "__main__":
    genrate_qr()