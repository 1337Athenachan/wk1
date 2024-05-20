#!/bin/bash

#Create the array variable and store something inside it
ARRAY_1=(one two three four)

#Printing different position in the array
echo ${ARRAY_1[@]}
echo ${ARRAY_1[3]}
echo ${ARRAY_1[1]}

#Border and space
echo
echo "********************"
echo
#Using a for loop to iterate through the list then printing word count
for item in ${ARRAY_1[@]}; do echo -n $item | wc -c; done 
#-n is a flag for echo to ignore newline characters
