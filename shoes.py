#Shoe module for shoe budgeting app

class shoes:
	def __init__ (self, name, price):
		self.name = name
		self.price = float(price)
	
	def budget_check(self, budget):
		if not isinstance(budget, (int, float)):
			print("Invalid entry, please enter a number: ")
			exit()
	
	def change(self, budget):
		return (budget - self.price)
		
	def buy(self, budget):
		self.budget_check(budget)
		
		if budget >= self.price:
			print(f"You can afford some {self.name}")
				
			if budget == self.price:
				print("You have exactly enough money for these shoes")			
			else:
				print(f"You can buy these shoes and still have $ {self.change(budget)} left over")
			exit("Thanks for using the budgeting app. Made by King Alfred.")

