#!/usr/bin/env bash
#Using puppets to make changes to our configuration file

file { '/etc/ssh/ssh_config':
	ensure => present,

	content => "
		#SSH Puppets Configuration
	
		Host*
			IdentityFile ~/.ssh/school
			PasswordAuthentication no
	",
}
