# Fixing "phpp" to "php" in wp-settings.php file

exec{'fix-wordpress extention error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin'
}