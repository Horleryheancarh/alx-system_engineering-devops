# Installs a Nginx server with add header

exec {'update':
  provider => shell,
  command  => 'sudo apt update -y',
  before   => Exec['Install Nginx'],
}

exec {'Install Nginx':
  provider => shell,
  command  => 'sudo apt install nginx -y',
  before   => Exec['Add header'],
}

exec {'Add header':
  provider    => shell,
  environment => ['HOST=${hostname}'],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
  before      => Exec['Restart Nginx'],
}

exec {'Restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
