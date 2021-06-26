
def commandEx(command):
	try:
		commandParser(command)
	except:
		print(f"Error: Improper Command: \"{command}\"")
def commandParser(command):
	cmd = command
	if cmd[1][0:8] == "https://" or cmd[1][0:7] == "http://":
		pass
	elif "-s" in cmd:
		ind = cmd.index("-s")
		possibilitys = []
		for i in range(len(cmd)):
			if i != ind and i != 0:
				possibilitys.append(i)
		possibleQuerry = cmd[possibilitys[0]]
		print(possibleQuerry)
	elif cmd[1] == "-h":
		instructions = [
			"ASK FOR HELP",
			" tbrws -h",
			"SEARCH A QUERRY",
			" tbrws -s <search querry>",
			"BROWSE A SITE",
			" tbrws <sitename>"
		]
		for i in instructions:
			print(f" {i}")
	else:
		print("Error: Command Not found")
