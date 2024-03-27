#!/usr/bin/env bash
#Using puppets to make changes to our configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,

contents => "
	
	#ssh puppets configuration
	
	Host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
