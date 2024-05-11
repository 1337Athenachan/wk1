#!/bin/bash

#Requires shoe-module.py to function correctly

from shoes import shoes

low = shoes("Biden c'mon man sneakers", 200)
medium = shoes("Trump's golden sneakers", 450)
high = shoes("Kanye classics", 9000)

try:
	shoe_budget = float(input("What is your shoe budget?: "))
except ValueError:
	exit("Please enter a number")

for shoes in [high, medium, low]:
	shoes.buy(shoe_budget)
