# -*- coding: utf-8 -*-
import os, sys, requests
import pandas as pd

from datetime import date, time, datetime, timedelta

"""
API Documentation: https://fintual.cl/api-docs/index.html
"""

class fintual_manager():
	def __init__(self):
		self.api_url = 'https://fintual.cl/api'

		# Authentication
		### Not used in this simplified version

		# Assets info
		### Not used in this simplified version

		# Money info
		### Not used in this simplified version

		# Banco Central manager
		### Not used in this simplified version

	def get_asset_prices(self, asset_id, date=None, from_date=None, to_date=None):
		"""
		If want to get asset price in individual date, pass date
		If want to get asset price in time, pass date range
		"""
		url = '/real_assets/{}/days'.format(asset_id)
		r = self.request_to_json(url, 
									params=None,
									data={
									'date':date,
									'from_date':from_date,
									'to_date':to_date
									}
									)
		
		if len(r['data']) <= 0:
			return pd.DataFrame()

		agg_df = pd.DataFrame()
		last_price = 0
		for _day in r['data']:
			df = pd.DataFrame({	
							'asset_id':asset_id,
							'date':_day['attributes']['date'],
							'price':_day['attributes']['price'] if 'price' in _day['attributes'] else last_price,
							},
							index=[0]
			)
			last_price = _day['attributes']['price'] if 'price' in _day['attributes'] else last_price
			agg_df = pd.concat([agg_df, df], sort=False)
			agg_df['date'] = pd.to_datetime(agg_df['date'], format='%Y-%m-%d')

		return agg_df

	def print_status(self, resp):
		status = resp.status_code
		print("=============================")
		if status==200:
			print("OK. Successful request.")
		elif status==401:
			print("Unauthorized. Authorization is required or has been failed.")
		elif status==400:
			print("Bad request.")
		elif status==403:
			print("Forbidden. Action is forbidden for API key.")
		elif status==429:
			print("ERROR: Too Many Requests. Your connection has been rate limited.")
		elif status==500:
			print("ERROR: Internal server error")
		elif status==503:
			print("Service Unavailable. Service is down for maintenance.")
		elif status==504:
			print("Gateway Timeout. Request timeout expired.")
		else:
			print("REMINDER: Develop code to print messages and more info about error codes...")
			print(("Error code: {}".format(status)))

		print("=============================")

	def request_to_json(self, url, params, data, print_status=False):
		req_url = self.api_url + url
		response = requests.get(req_url, params=params, data=data)
		json = response.json()

		if print_status:
			if len(json) == 0:
				print("=============================")
				print("Empty response")
				print("=============================")
				return None
			self.print_status(response)

		return json

if __name__ == '__main__':
	fm = fintual_manager()
	fm.get_asset_prices(asset_id=186,date="2022-04-25")
