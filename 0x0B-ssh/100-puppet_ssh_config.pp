#!/usr/bin/env bash
#Using puppets to make changes to our configuration file

file { 'etc/ssh/ssh_config':
	ensure => present,

content =>"
	
	#ssh puppets configuration
	
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",
}
