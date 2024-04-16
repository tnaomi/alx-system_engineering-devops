# 0x14-mysql

## Author

Tadala N. Kapengule

## Description

### Objectives

- What is the main role of a database
- What is a _database replica_
- What is the purpose of a _database replica_
- Why database backups need to be stored in different physical locations
- What operation should you regularly perform to make sure that your _database backup strategy_ actually works

### Requirements


- Allowed editors: ``vi``, ``vim``, ``emacs``
- All your files will be interpreted on ``Ubuntu 16.04 LTS``
- All your files should end with a new line
- A ``README.md`` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass ``Shellcheck`` (version ``0.3.7-5~ubuntu16.04.1`` via ``apt-get``) without any error
- The first line of all your Bash scripts should be exactly ``#!/usr/bin/env bash``
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

### 0. Install MySQL

First things first, let’s get MySQL installed on both your ``web-01`` and ``web-02`` servers.

- MySQL distribution must be ``5.7.x``
- Make sure that task #3 of your SSH psudo mysqlsudoroject is completed for ``web-01`` and ``web-02``. The checker will connect to your servers to check MySQL status
- Please make sure you have your ``README.md`` pushed to GitHub.

### 1. Let us in!

In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

- Create a MySQL user named ``holberton_user`` on both ``web-01`` and ``web-02`` with the ``host`` name set to ``localhost`` and the ``password`` ``projectcorrection280hbtn``. This will allow us to access the replication status on both servers.
- Make sure that ``holberton_user`` has permission to check the primary/replica status of your databases.
- In addition to that, make sure that task #3 of your SSH project is completed for ``web-01`` and ``web-02``. You will likely need to add the public key to ``web-02`` as you only added it to ``web-01`` for this project. The checker will connect to your servers to check MySQL status

### 2. If only you could see what I've seen with your eyes 