# 0x0A-configuration_management

## Author

Tadala N Kapengule

## Tasks

### 0. Create a file

Using Puppet, create a file in `/tmp`.

Requirements:

- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

```bash
puppet-lint 0-create_a_file.pp
""

puppet apply 0-create_a_file.pp
"
Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
Notice: Finished catalog run in 0.03 seconds
"
```

__File__
`0-create_a_file.pp`

### 1. Install a package

Using Puppet, install `flask` from `pip3`.

Requirements:

- Install `flask`
- Version must be `2.1.0`

```bash
puppet apply 1-install_a_package.pp

"
Notice: Compiled catalog for 9665f0a47391 in environment production in 0.14 seconds
Notice: /Stage[main]/Main/Package[Flask]/ensure: created
Notice: Applied catalog in 0.20 seconds
"
```

__File__
`1-install_a_package.pp`

### 2. Execute a command

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

- Must use the `exec` Puppet resource
- Must use `pkill`

Example:

Terminal #0 - starting my process

```bash
cat killmenow
"
#!/bin/bash
while [[ true ]]
do
    sleep 2
done
"

./killmenow
```

Terminal #1 - executing my manifest

```bash
puppet apply 2-execute_a_command.pp

"Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds"
```

Terminal #0 - process has been terminated

```bash
./killmenow

" Terminated "
```

__File__
`2-execute_a_command.pp`
