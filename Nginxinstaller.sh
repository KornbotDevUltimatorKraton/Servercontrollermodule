echo "ufw fire wall setting and port"
sudo ufw enable
sudo ufw status 
sudo ufw allow 80
sudo ufw allow 8000
sudo ufw allow ssh 
#echo "Install nginx"
#sudo apt-get install nginx -y 
sudo systemctl start nginx 
sudo systemctl enable nginx 
sudo systemctl status nginx 
sudo ufw status
