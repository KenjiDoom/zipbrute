from zipfile import ZipFile
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
	parser.add_argument('-w', metavar='wordlist', type=str, help='Password list file, must be txt file.')
	parser.add_argument('-z', metavar='zip', type=str, help='Zip file location')
	return parser.parse_args(args)


def main(args=keywords()):
	if os.path.exists(args.w) and os.path.exists(args.z) == True:
		zip_file = zipfile.ZipFile(args.z)
		with open(args.w, 'rb') as password:
			for password in password:
				for word in password.split():
					try:
						zip_file.extractall(pwd=word)
						zip_file.printdir()
						print('[+] Password: ' + word.decode())
						return True
					except:
						continue
	else:
		print('[-] Files do not exists')


if __name__ == '__main__':
	main()
