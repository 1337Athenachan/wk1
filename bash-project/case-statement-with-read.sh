#!/bin/bash

echo "What is your name?: "
read NAME
case $NAME in
	bill) 
		echo "Hello Boss!"
		;;
	*)
		echo "Wrong person..."
		;;

esac
