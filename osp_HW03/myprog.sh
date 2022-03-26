#!/bin/bash
echo "...create temp directory..."
mkdir temp
echo "...copy files to temp directory..."
cp cal.sh temp/cal.sh
cp num1.txt temp/num1.txt
cp num2.txt temp/num2.txt

PS3="select menu : "
select op in add sub div mult
do
	if [ -z $op ]; then
		echo "Invalid Operation"
	else
		echo "...$op selected..."
		break
	fi
done

echo "...run calculater..."
temp/cal.sh $op
