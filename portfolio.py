# -*- coding: utf-8 -*-

"""
Debes realizar la siguiente tarea y enviar link de repositorio de github con la respuesta.
Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates.
Assume each Stock has a "Price" method that receives a date and returns its price.

Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.
"""
from datetime import datetime

from util.stock_init import stock_init

class portfolio():
	def __init__(self):
		self.stock_qty = {
		'Risky Norris':100,
		'Moderate Pitt':100,
		'Conservative Clooney':100,
		'Very Conservative Streep':100
		}

		self.stocks = {key:stock_init(name=key, qty=self.stock_qty[key]) for key in self.stock_qty.keys()}

	def Profit(self, date_from, date_to):
		value_from = 0
		value_to = 0
		for stock in self.stocks.keys():
			value_from += self.stocks[stock].Price(date_from) * self.stocks[stock].Quantity()
			value_to += self.stocks[stock].Price(date_to) * self.stocks[stock].Quantity()

		profit = value_to - value_from

		print("\nProfit of the portfolio between {} and {} was ${}".format(date_from, date_to, int(profit)))
		print("\tValue of portfolio at {}: ${}".format(date_from, int(value_from)))
		print("\tReturn over investment in period: {}%".format(int(profit/value_from*1000)/10))

		days_diff = datetime.strptime(date_to, "%Y-%m-%d") - datetime.strptime(date_from, "%Y-%m-%d")
		days_diff = days_diff.days
		print("\n\tAnnualized returns: {}%".format(int(((value_to/value_from)**(365/days_diff) - 1)*1000)/10))


if __name__ == '__main__':
	p = portfolio()
	p.Profit("2021-05-01","2022-05-01")