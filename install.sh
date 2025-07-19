#!/bin/bash
cd ~
sudo apt-get install unclutter -y
unclutter -idle 0
sudo apt install cmake -y
sudo apt-get install libraspberrypi-dev -y
cd ~
cd /usr
sudo mkdir screen && cd screen
sudo git clone https://github.com/juj/fbcp-ili9341.git #installing the drivers for the screen
cd fbcp-ili9341
mkdir build
cd build
cmake -DST7735R=ON -DGPIO_TFT_DATA_CONTROL=24 -DGPIO_TFT_RESET_PIN=25 -DGPIO_TFT_BACKLIGHT=1 -DSTATISTICS=0 -DDISPLAY_SWAP_BGR=ON -DSPI_BUS_CLOCK_DIVISOR=8 ..
make -j

echo "hdmi_force_hotplug=1" | sudo tee -a /boot/config.txt > /dev/null
echo "hdmi_group=2" | sudo tee -a /boot/config.txt > /dev/null
echo "hdmi_mode=87" | sudo tee -a /boot/config.txt > /dev/null
echo "hdmi_cvt=160 128 60 1 0 0 0" | sudo tee -a /boot/config.txt > /dev/null
sudo sed -i 's/^dtoverlay=vc4-kms-v3d/#&/' /boot/config.txt
echo "dtoverlay=vc4-fkms-v3d" | sudo tee -a /boot/config.txt > /dev/null
sudo sed -i '/^exit 0/i sudo /usr/Comlock-UI/screen/fbcp-ili9341/build/fbcp-ili9341 &' /etc/rc.local
#Installing GUI

cd ~
cd /usr
cd Comlock-UI 
sudo apt-get install python3-tk -y
#python3 -m venv guivenv
#source guivenv/bin/activate
sudo apt install -y python3-dev libjpeg-dev zlib1g-dev libpng-dev libtiff-dev libfreetype6-dev
pip3 install -r requirements.txt
echo The script is complete. Please proceed with the final steps on the GitHub repo
echo @TheMrNull