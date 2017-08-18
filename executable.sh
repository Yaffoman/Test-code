#!/bin/bash

read -p "Username:" user
read -p "Password:" pass
echo $user 
echo $pass

sudo sh -c "echo 'network={\n\tssid=\"UCSD-PROTECTED\"\n\tkey_mgmt=WPA-EAP\n\teap=PEAP\n\tidentity=\"YOUR_USERNAME\"\n\tpassword=\"YOUR_PASSWORD\"\n\tphase2=\"auth=MSCHAPv2\"\n}' >> /etc/wpa_supplicant/wpa_supplicant.conf"
sudo sed -i -e "s/YOUR_USERNAME/$user/g" /etc/wpa_supplicant/wpa_supplicant.conf
sudo sed -i -e "s/YOUR_PASSWORD/$pass/g" /etc/wpa_supplicant/wpa_supplicant.conf
sudo reboot

