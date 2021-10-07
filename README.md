# zipbrute
Zcrack is a python script desgined for bruteforcing zip files.

### Manual
$ python zcrack.py --help
```
_______ _ __ __ _  ___| | __
|_  / __| '__/ _` |/ __| |/ /
 / / (__| | | (_| | (__|   <
/___\___|_|  \__,_|\___|_|\_\

usage: zcrack.py [-h] [-w wordlist] [-z zip]

Brutforcing Zip files

optional arguments:
  -h, --help   show this help message and exit
  -w wordlist  Password list file, must be txt file.
  -z zip       Zip file location
```

Running the program is as simple as,
```
python zcrack.py -w rockyou.txt -z 614ef84133c5d458fcb365ff.zip
```

### To-Do
- [] - Check for diffrent kinds of encryption
- [] - Display the amount of attempts have been made
