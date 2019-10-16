import cli

print "\n\n **Executing show version** \n\n"
cli_command = "show version"
cli.executep(cli_command)

print "\n\n **Executing show inventory** \n\n"
cli_command = "show inventory"
cli.executep(cli_command)
device_type = cli.executep(cli_command)

print "\n\n **Download Image** \n\n"
cli_command = "copy tftp://169.254.0.1/cat9k_iosxe.16.09.03.SPA.bin flash:"
cli.executep(cli_command)


print "\n\n **Copy Base Config** \n\n"
cli_command = "copy tftp://169.254.0.1/base_config flash:"
cli.executep(cli_command)

int "\n\n **Copy Base Config** \n\n"
cli_command = "copy flash:base_config running-config"
cli.executep(cli_command)



#print "\n\n **Configure BootVAR** \n\n"
#cli_command = "boot system flash:cat9k_iosxe.16.09.03.SPA.bin"
#cli.configurep(cli_command)


print "\n\n **Save Config and Reload** \n\n"
cli_command = "wr me"
cli.executep(cli_command)

cli_command = "reload"
cli.executep(cli_command)

print "\n\n **ZTP Complete** \n\n"




