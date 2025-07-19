# Comlock-UI
UI for my comlock from space 1999, still work in progress

## Requirements
- Raspberry Pi Zero 2W
- Small [TFT SCREEN](https://www.amazon.it/-/en/AZDelivery-Display-Compatible-Raspberry-Including/dp/B078J5TS2G/ref=sr_1_7?crid=HC41MH2WFD84&dib=eyJ2IjoiMSJ9.y5XXH9LvkwbqgnAzjvaPxfJafcztFWrMQDXqJj7KCrq4oFssqPPzMOc-hCpdN-kQnZ6ZqnzZLE0eGPpOlAx_8N7kORtoYwAXmbGRINB21lOXHqdt8ibVF8YSRX6cW8tk2aidRZDyFK_bWKRNDhS-VVows4cHHlsLmVzlp1r4h76RXLmvlV2AH-EgiteCa2AwXbFpBujhKcclTulcMh1Omdwc6ApXgFBqEtO1TS9VVe0-JmDl51uwWZCaiC1QG66caGT0xn36q-FF4Bh_vLcmgM_oA0EgPoffAagQl6WbNFM.zznof4WCUuudlayUwq2b-kLUbE1i_EgJIwc45XThFwI&dib_tag=se&keywords=tft%2Bdisplay&qid=1752943426&sprefix=tft%2Bdispla%2Caps%2C123&sr=8-7&th=1)
- Micro SD


## Preparation
On an sd card flash Raspberry Pi OS (32-bit, legacy), the bullsey one, not the bookworm. 
Make sure in the settings to enable ssh so that you can connect to it with your computer.(setting up your Wi-Fi in the settings is a great idea).  
Once booted up ssh into it or connect it to an exteral monitor and login with your credentials(creating a user account before flashing should speed the process up).

## IMPORTANT!
Before running the following, please run `sudo apt update && sudo apt upgrade -y`


## Instalation
Run `sudo raspi-config` and under System Options --> Boot/Auto login, enable the Desktop auto login.
After this, in the  Interface Options menu enable SPI. Good, now you can apply the changes and reboot your pi. 



Once the Pi has rebooted ssh back into it and copy the following code `cd /usr && sudo git clone https://github.com/TheMrNull/Comlock-UI.git`

When it has copied, cd into the directory with the command `cd /usr/Comlock-UI` and make sure that the installation script is runnable with `sudo chmod +x install.sh`.   

To start the installation, run `sudo ./install.sh`

The script will install all the required drivers for the display(for problems with the display please refer to [fbcp-ili9341](https://github.com/juj/fbcp-ili9341.git)).  
The script should install all the dependencies and configure it in order to work and start automatically, if not make sure to have these lines in your `/boot/config.txt`

> hdmi_force_hotplug=1  
hdmi_group=2  
hdmi_mode=87  
hdmi_cvt=160 128 60 1 0 0 0  
dtoverlay=vc4-fkms-v3d
>
And that this line `dtoverlay=vc4-kms-v3d`is commented out like this `#dtoverlay=vc4-kms-v3d`.  

After installing the drivers for the screen, the script will install the custom GUI from this repo.  
After the script it's done, we need to make some last changes by hand.  


To make the GUI start after boot we need to create a service.  
Run `sudo nano /etc/systemd/system/comlock.service` and <ins>paste in the following, be careful to put your pi username insite the `User` field.  </ins>
>[Unit]  
Description=Comlock UI Service  
After=graphical.target  
[Service]  
User= your-pi-username  
Environment=DISPLAY=:0  
WorkingDirectory=/usr/Comlock-UI  
ExecStart=/usr/bin/python3 gui.py  
Restart=on-failure  
StandardOutput=journal
StandardError=journal  
[Install]  
WantedBy=graphical.target
>

To save and exit the changes press ^x, than conferm with y and hit enter (note you can also use vim or any other text editor if you prefer it).  

Then run this `sudo systemctl daemon-reload  &&
sudo systemctl enable comlock.service &&
sudo systemctl start comlock.service`

At this point your Pi should be good to go, run `sudo reboot now` and after turning back on everything should work as expected.

For now  the UI is very simple, you can connect a mouse to test it or a keyboard. It will be updated and completed when I'll have time.  

Keybinds:
- c = call
- h = home

