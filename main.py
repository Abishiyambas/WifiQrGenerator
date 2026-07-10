import qrcode

#Wifi name
print("Enter your wifi name:")
wifi_name = input()
print(f"your wifi name is {wifi_name}")

#Wifi password
print("Enter your wifi password:")
wifi_password =input()

# Wi-Fi security
print("What is your security?")
print("Choose one of them:")
print("1. WPA/WPA2")
print("2. WEP")
print("3. No Password (Open)")

user_security = input()

while user_security != "1" and user_security != "2" and user_security != "3":
    print("Invalid input. Please choose 1, 2 or 3.")
    user_security = input()

if user_security == "1":
    security = "WPA"
    print("Your security is WPA/WPA2")

elif user_security == "2":
    security = "WEP"
    print("Your security is WEP")

elif user_security == "3":
    security = "nopass"
    print("Your security has no password")

wifi_data = f"WIFI:T:{security};S:{wifi_name};P:{wifi_password};;"

qr = qrcode.QRCode(

    box_size= 5,
    border= 5,
    version= 5,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
   
)

qr.add_data(wifi_data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr.png")







