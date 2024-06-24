# Install a package: Flask
package { 'Werkzeug':
  ensure   => '2.2.0',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
