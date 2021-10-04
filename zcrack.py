from zipfile import ZipFile
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
	wordlist = args.wordlist
	zip_file = args.zip
	if os.path.exists(wordlist):
		if os.path.exists(zip_file) == True:
			print("[+] Cracking....")
			wordlist = open(args.wordlist, 'r')
			for password in wordlist:
				password = password.strip()
				with ZipFile(zip_file) as zipp:
					zipp.extractall(pwd=bytes(password, 'utf-8'))
	else:
		print('No passwords found...')

if __name__ == '__main__':
	main()
