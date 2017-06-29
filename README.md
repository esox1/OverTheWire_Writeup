# Bandit

### **Bandit Level 0 → Level 1**
Bandit0 we are given the passwd which is bandit0

//add bandit0.png

Level Goal

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

//add bandit1.png

### **Bandit Level 1 → Level 2**

Level Goal

The password for the next level is stored in a file called - located in the home directory

//add bandit2.png

### **Bandit Level 2 → Level 3**

Level Goal

The password for the next level is stored in a file called spaces in this filename located in the home directory

//add bandit3.png

``` "ls -a" to see ".hidden files/folders" 
cat inhere/.hidden 
```


### **Bandit Level 4 → Level 5**

Level Goal

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

` cd ./inhere/
`
"theres a bunch of file0, file1, etc..with giberrish .except one"
` find . -exec file {} + | grep ASCII `

**find with exec command file with result subsitute with {} and + to tell find it is the end of cmd**

Another way is to use **"file"** to see type

` file ./* `

//add bandit4


**Bandit Level 5 → Level 6**

Level Goal

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable

In this level we get a bunch of folders with a bunch of different files and given conditions:
human-readable, 1033 bytes in size, not executable
` **cd /inhere/** `
` **du -ba | grep 1033**`

**we read all subdir and get the block(bytes)size and piped with grep to find our 1033 size**

//add bandit5.png

Another way is to use the find tool

` find . -size 1033c -readable ! executable -exec file {} + | grep ASCII`

using find to determine the size 1033 bytes and not executable and tagging file cmd and piping grep with ASCII
//add bandit5.png

**Bandit Level 6 → Level 7**

Level Goal

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

This one has the file with passwd located somewhere on the server
conditions: file is owned by user bandit7, file is in group bandit6, file's size is 33 bytes

We can use the find cmd and specify the user and group flags
find / -type f -group bandit6 -user bandit7 -size 33c

//add bandit6.png

**Bandit Level 7 → Level 8**

Level Goal

The password for the next level is stored in the file data.txt next to the word millionth

For this one we can use grep to find the word millionth in data.txt

//add bandit7.png

**Bandit Level 8 → Level 9**

Level Goal

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

sort data.txt | uniq -u
the sort will sort lines in lexicographically order(it reorders them alpabatically as the matching ones are together) and uniq cmd omits repeated lines and -u flag tell to report uniqe lines

//add bandit8.png


**Bandit Level 9 → Level 10**

Level Goal

The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters.

//add bandit9.png

The -a flag in grep process a binary file as if it were a text
if we check file data.txt we get "data" by using -a flag grep process it as if it were a text file.

Another way is to use command "strings" whicih prints the printable characters sequences that are at least 4 chars long. Its useful for determing the contents of non-text files

strings data.txt | grep ==

**Bandit Level 10 → Level 11**

Level Goal

The password for the next level is stored in the file data.txt, which contains base64 encoded data

//add bandit10.png

base64 is basically a binary datain a sequence of printable chars in plaintext encoded in an ASCII string format

**we use base64 command with -d flag to decode it to plain text**
` base64 -d data.txt`

**Bandit Level 11 → Level 12**

Level Goal

The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

//add bandit11.png

Accoring to Ro13 on wikipedia, A its rotation 13 alpha is N and Z Ro13 is M, so is a is n and z is m using the tr to compare sets

tr 'a-zA-Z' 'n-za-mN-ZA-M'
using a-z as SET1 and n-za-mN-Za as set 2
1) a=n --> n-z
2) z=m --> n-za-m
3) A=N --> n-za-mN
4) Z=M --> n-za-mN-ZA-M  (completed)

cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'

ex: echo "LOVEEGYPT" | tr 'a-zA-Z' 'n-za-mN-ZA-M' = YBIRRTLCG


**Bandit Level 12 → Level 13**

Level Goal

The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

we start by ls the directory and cat the data.txt. We find the content of data.txt is all in hex
We can use the xxd with -r flag to revert hex to binary and redirecting it into a file, we call it data

xxd -r > ./data
but we get a permmission denied. We need to create a directory in /tmp and and redo the last command in that
mkdir /tmp/es/
cat ~/data.txt | xxd -r > ./data

//add bandit12a.png

we find the type of data using "file data" and we see its gzip compressed
we rename it with a .gz extension then extract it using gunzip command
and I repeat the same steps from there on..

