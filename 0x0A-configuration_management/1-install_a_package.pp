# Install a package

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => '/usr/bin',
  environment => 'HOME=/root',
}
