 

### Linux Shell Scripting CookBook

#### Chapter 1

###### 1.The $ character represents regular users and # represents the administrative user root

###### 2.A shell script typically begins with a shebang #!/bin/bash

###### 3.echo; echo -e "1\t2\t3"

###### 4.printf "%-5s %-10s %-4s\n" No Name Mark  -means left

###### 5.Colors for text are represented by color codes, including, reset = 0, black = 30, red = 31, green = 32, yellow = 33, blue = 34, magenta = 35, cyan = 36, and white = 37.

###### echo -e "\e[1;31m This is red text \e[0m"

###### echo -e "\e[1;42m Green Background \e[0m"

###### install man-pages

###### 6.env/printenv

###### cat /proc/$PID/environ

###### pgrep clash

###### cat /proc/12501/environ | tr '\0' '\n'

###### 7.a=1

###### echo $a; echo ${a}

###### 8.HOME,PWD,USER,UID,SHELL

###### 9.var=1234

###### *echo ${#var}*

###### 10.echo $SHELL; echo $0

###### 11.if

```shell
exam1:
If [ $UID -ne 0 ]; then
 echo Non root user. Please run as root.
else
 echo Root user
fi
exam2:
if test $UID -ne 0:1
 then
 echo Non root user. Please run as root
 else
 echo Root User
fi
```

###### 12.path

###### prepend() { [ -d "$2" ] && eval $1=\"$2':'\$$1\" && export $1; }

###### prepend() { [ -d "$2" ] && eval $1=\"$2':'\$$1\" && export $1; }

###### 13.let,[],(()),expr,bc

###### install bc

###### result=`expr 3 + 4`

```shell
#!/bin/bash
Desc: Number conversion
no=100
echo "obase=2;$no" | bc
1100100
no=1100100
echo "obase=10;ibase=2;$no" | bc
100
```

###### 14.echo "111" 2>&1 allOutput.txt

###### echo "111" &> allOutput.txt

###### 15.array_var=(test1 test2 test3 test4)

```shell
echo ${#array_var}
```

###### 16.date

![image-20220710171213600](/home/licona/.config/Typora/typora-user-images/image-20220710171213600.png)

```shell
#!/bin/bash
 function DEBUG()
 {
 [ "$_DEBUG" == "on" ] && $@ || :
 }
 for i in {1..10}
 do
 DEBUG echo "I is $i"
 done
```

