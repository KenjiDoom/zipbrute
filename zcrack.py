import zipfile 
import argparse
import os


def keywords(args=None):
	print("""
 _______ _ __ __ _  ___| | __
|_  / __| '__/ _` |/ __| |/ /
 / / (__| | | (_| | (__|   <
/___\___|_|  \__,_|\___|_|\_\\
""")
	parser = argparse.ArgumentParser(description='Brutforcing Zip files')
	parser.add_argument('wordlist', metavar='-w', type=str, help='Password list file, must be txt file.')
	parser.add_argument('zip', metavar='-z', type=str, help='Zip file location')
	return parser.parse_args(args)


def main():
	args = keywords()
	if os.path.exists(args.wordlist):
		if os.path.exists(args.zip):
			print('Also working')
	else:
		print('Nada')


if __name__ == '__main__':
	main()
