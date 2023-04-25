# Install Nginx


exec {'install':
	provider => shell,
	command => 'sudo apt -y update ; sudo apt -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/Horleryheancarh permanent;/" /etc/nginx/sites-available/default ; service nginx start',
}
