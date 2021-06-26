
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
		pass
	else:
		print("Error: Command Not found")

commandEx(["tbrws", "-h"])