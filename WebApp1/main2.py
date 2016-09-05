# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import ffn
import bt
import ffn

from matplotlib.figure import Figure
from matplotlib.backends.backend_webagg_core import (
    FigureManagerWebAgg, new_figure_manager_given_figure)
import json

input_filename="input.csv"

"""
return a png figure
"""
def plot1():
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)

	xs = range(100)
	ys = [random.randint(1, 50) for x in xs]

	axis.plot(xs, ys)
	canvas = FigureCanvas(fig)
	output = StringIO.StringIO()
	canvas.print_png(output)
	response = make_response(output.getvalue())
	response.mimetype = 'image/png'
	return response

"""
save a png figure
"""
def plot2():
	fig = Figure()
	# download price data from Yahoo! Finance. By default,
	# the Adj. Close will be used.
	prices = ffn.get('aapl,msft', start='2010-01-01')
	# let's compare the relative performance of each stock
	# we will rebase here to get a common starting point for both securities
	ax = prices.rebase().plot(figsize=(10,5))
	# save the figure
	fig = ax.get_figure()
	fig.savefig('asdf.png')
	# Debug
	print "save the a png picture finished!"



@app.route("/"+figue_name)
def display(figue_name):
	return plot2()

@app.route("/")
def index():


if __name__ == "__main__":
	df=pd.read_csv(input_filename)