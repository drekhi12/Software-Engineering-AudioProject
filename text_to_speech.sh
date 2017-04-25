echo -n "Enter some text " 
read text
echo $text
espeak -s 125 -v en+m3 -p 25 ${text}
 