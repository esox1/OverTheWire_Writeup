# Bandit

### **Bandit Level 0 → Level 1**

**Level Goal**
>The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.


In Bandit0 we are given the passwd to bandit0 which is bandit0
![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit0.png)



### **Bandit Level 1 → Level 2**

**Level Goal**
>The password for the next level is stored in a file called - located in the home directory

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit1.png)


### **Bandit Level 2 → Level 3**

**Level Goal**
>The password for the next level is stored in a file called spaces in this filename located in the home directory

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit2.png)


### **Bandit Level 3 → Level 4**

**Level Goal**
>The password for the next level is stored in a hidden file in the inhere directory.

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit3.png)

``` "ls -a" to see ".hidden files/folders"
cat inhere/.hidden
```

### **Bandit Level 4 → Level 5**

**Level Goal**
>The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

` cd ./inhere/ `

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit4.png)

We find a bunch of file0, file1, etc..with giberrish, except one

The **find** with **exec** flag to execute **file** with result subsitute with **{}** and **+** to tell "find" that it is the end of cmd

` find . -exec file {} + | grep ASCII `

Another way is to use **"file"** to see type

` file ./* `


### **Bandit Level 5 → Level 6**

**Level Goal**
>The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
>human-readable
>1033 bytes in size
>not executable

In this level we get a bunch of folders with a bunch of different files and given conditions:
**human-readable, 1033 bytes in size, not executable**

We can use diskusage**(du)** to read current directory and with **-b** (bytes) flag, we get the block(bytes)size and the **-a** flag writes counts to all files and not just direcotry, again piped with **grep** to find our 1033 size


` **cd /inhere/** `
` **du -ba | grep 1033**`

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit5.png)


Another way is to use the find tool. **find** can be used to determine the **size**, 1033 bytes, and not executable aloing with tagging the **file** cmd and piping output to **grep** to search for ASCII

` find . -size 1033c -readable ! executable -exec file {} + | grep ASCII`


### **Bandit Level 6 → Level 7**

**Level Goal**
>The password for the next level is stored somewhere on the server and has all of the following properties:
>owned by user bandit7
>owned by group bandit6
>33 bytes in size

This one has the file with passwd located somewhere on the server
conditions: file is owned by user bandit7, file is in group bandit6, file's size is 33 bytes

We can use the **find** cmd and specify the **user** and **group** flags

`find / -type f -group bandit6 -user bandit7 -size 33c`

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit6.png)


### **Bandit Level 7 → Level 8**

**Level Goal**
>The password for the next level is stored in the file data.txt next to the word millionth

This one we can jsut use **grep** to find the word **millionth** in data.txt

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit7.png)



### **Bandit Level 8 → Level 9**

**Level Goal**
>The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

Here we can benefit from the **sort** & **uniq** commands.

` sort data.txt | uniq -u `

**The sort will sort lines in lexicographically order(it reorders them alpabatically as the matching ones are together) and uniq cmd omits repeated lines and -u flag tell to report uniqe lines**

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit8.png)


### **Bandit Level 9 → Level 10**

**Level Goal**
>The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters.

We can either try and use the **grep** with its **a** flag which processes a binary file as if it were text file. We can also use the **strings** command. Here's what I did

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit9.png)

The **a** flag in **grep** process a binary file as if it were a text
if we check file data.txt we get "data" by using -a flag grep process it as if it were a text file.

Or using the "strings" which prints the printable characters sequences that are at least 4 chars long. Its useful for determing the contents of non-text files

` strings data.txt | grep == `


### **Bandit Level 10 → Level 11**

**Level Goal**
>The password for the next level is stored in the file data.txt, which contains base64 encoded data

base64 is basically a binary datain a sequence of printable chars in plaintext encoded in an ASCII string format
we use base64 command with -d flag to decode it to plain text

` base64 -d data.txt `

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit10.png)


### **Bandit Level 11 → Level 12**

**Level Goal**
>The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

>Accoring to Ro13 on wikipedia, A its rotation 13 alpha is N and Z Ro13 is M, so is a is n and z is m using the tr to comparesets

**tr 'a-zA-Z' 'n-za-mN-ZA-M'**
using a-z as SET1 and n-za-mN-Za as set 2
1) a=n --> n-z
2) z=m --> n-za-m
3) A=N --> n-za-mN
4) Z=M --> n-za-mN-ZA-M  (completed)

ex: echo "LOVEEGYPT" | tr 'a-zA-Z' 'n-za-mN-ZA-M' = YBIRRTLCG**

` cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M' `

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit11.png)


**Bandit Level 12 → Level 13**

**Level Goal**
>The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

we start by **ls** the directory. We find **data.txt** then `cat the data.txt`. We find the content of data.txt is all in hexadecimal. We can use the command **xxd** with **r** flag to revert hex to binary then we can redirect it into a file.

`xxd -r > ./data`

But I get a permmission denied. I need to create a directory in /tmp and and redo the last command in that new directory

`mkdir /tmp/es/`
`cat ~/data.txt | xxd -r > ./data`

I see the type of data using `file data` and I see that it is a **gzip** compressed file. Lets uncompress it. But first,
I rename it to **data** & I add **.gz** extension to it, then extract it using **gunzip** command
and I repeat the same steps from there on..

![alt text](https://github.com/esox1/OverTheWire_Writeup/blob/master/bandit-scrshots/bandit12a.png)


I start using **file** and **mv** to move to the next file until I hit the password file.

//add bandit12b.png


### **Bandit Level 13 → Level 14**

**Level Goal**
>The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

So we are given the ssh private key to level 14. We connect to bandit14@localhost using the given privatekey in bandit13
With **ssh** and it **i** flag we can connect to level 14

``ssh -i ./ssh.key_private bandit14@localhost``

//add bandit13


Bandit Level 14 → Level 15

**Level Goal**
>The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
where the passwd for level 14 was saved in /etc/bandit_pass/bandit14

cat /above/directory to get bandit14 passwd.

To get the passwd to level15
condition: the passwd can be retrieved by sumbitting the passwd of the current level to port 30000 on localhost

I had to look this one up
so you can listen to a running service using **nc** or **telnet** commands
`nc localhost 30000`
which didnt work for me but telnet did

`telnet localhost 30000`

//add bandit14.png
then it awaits for you to enter bandit14 password to give you a surprise

Bandit Level 15 → Level 16

Level Goal

The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

This level the credentials can be retrieved by submitting the password of the current level to a port 30001 on localhost using ssl encryption

`telent localhost 30001`


then entering the passwd to current level
I get an ERROR 140737354049184:ssl routines ssl3_get_record:wrong version number

Here's what I learned after googling online about ssl. if we wanted to test a webiste by sending a custom hearder, but say websites uses **https** if we used
telnet www.example 80
GET /index.html
that would be a valid HTTP GET and you would see the servers response headers and response data. but with a ssl webiste that wont work. We use **openssl s_client**

`openssl s_client -connect localhost:30001`
and it's unsccessful. >I get servers response headers and response data then its waiting to enter the passwd of the current level (bandit15)  but I get

"HEARTBEATING
 read R BLOCK
 read:errno=0"

//add bandit15a.png
//add bandit15b.png

 according to otw
 using the **-quiet** flag wich implies -ign_eof we get our passwd for bandit16

//add bandit15c.png



Bandit Level 16 → Level 17

Level Goal

The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

We get a range of ports that we need to scan to see which ones the server is listening to and test which ones are ssl

A very helpful network thats widely used in scanning open ports on systems is **nmap**

`nmap -p31000-32000 localhost`

We see that 31046/tcp open
 31518/tcp open
 31691/tcp open
 31790/tcp open
 31960/tcp open

//add bandit16a.png

We can use echo test | nc -v localhost 31046
 "test"
 31518 = ERROR
 31691 = test
 31790 = ERROR
 31960 = test

 so only 31518 and 31790 are ssl


//add bandit16b.png


Using `openssl s_client -connect localhost:31790`

then entering the paswd to current level we get the private key to the next level

create a directory in /tmp/any/name/ and save  the private key  displayed in file, name it whatever
mkdir /tmp/any/name/

`vim /tmp/es/private.key` & paste the private key in private.key

Now change the permission of the file to be only accessible by you otherwise it will be ignored in the next step

`chmod 700 ./private.key`

then we are going to login to bandit17 using the private key

`ssh -i ./private.key bandit17@localhost`

once we in bandit17 we can find the passwd for this level in

>/etc/bandit_passwd/bandit17



