# Install a package: Flask
class pypackage{
  package { 'flask':
    ensure  => '2.1.0',
    provider => 'pip3'
  }
}
