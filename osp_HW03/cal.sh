#!/bin/bash
read < num1.txt num1
read < num2.txt num2

if [ $# -gt 0 ]; then
	op=$1
else
	echo "...none operator parameter..."
	PS3="select menu : "
	select op in add sub div mult
	do
		if [ -z $op ]; then
			echo "Invalid Operation"
		else
			break
		fi
	done
fi

case $op in
	add) let result=$num1+$num2 ;;
	sub) let result=$num1-$num2 ;;
	div) let result=$num1/$num2 ;;
	mult) let result=$num1*$num2 ;;
	*) echo "Invalid Operation" ; exit ;;
esac

echo
echo "num1 : $num1"
echo "num2 : $num2"
echo "op : $op"
echo "result : $result"
