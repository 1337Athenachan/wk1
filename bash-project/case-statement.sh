#!/bin/bash

#Similar to a for loop
case ${1,,} in
	bill | admin)
		echo "Hello Boss!"
		;;
	help)
		echo "Enter Usernam..."
		;;
	*)
		echo "Hello Worker!"
		;;
esac
