sudo nano /etc/ssh/sshd_config

add lines
	ServerAliveInterval 3600
	ServerAliveCountMax 24
to send keepalive messages to the server once an hour for max of 24h