# -*- coding: utf-8 -*-
from util.fintual_manager import fintual_manager

class stock_init():
	def __init__(self, name, qty):
		self.name = name
		self.qty = qty

	def Price(self, date):
		asset_id = {
		'Risky Norris':186,
		'Moderate Pitt':187,
		'Conservative Clooney':188,
		'Very Conservative Streep':15077
		}

		price = fintual_manager().get_asset_prices(asset_id[self.name], date=date
													)['price'].iloc[0]

		return price

	def Quantity(self):
		return self.qty

if __name__ == '__main__':
	# Test
	s_i = stock_init("Risky Norris", 100)
	print(s_i.Price("02-05-2022"))