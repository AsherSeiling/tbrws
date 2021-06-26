import os
import sys

import modules.interpreter as inpt

# Main Function
def main():
	inpt.commandParser(sys.argv)


# Call that starts the program
if __name__ == '__main__':
	main()