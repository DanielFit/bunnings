import beat_it_by_10
import analysis
import financial_year_1

""""To improve sales Bunning's has recorded some of their top competitors prices below, if they match an
item Bunning's currently stocks. In this financial year Bunning's will run its discount 'If a cheaper price
is found on a stocked item we'll beat it by 10%'"""

#competitors prices in financial year 2
comp_power_tools = {'drill':45, 'chainsaw':34,'sander':28}
comp_outdoor_furniture = {'chair':42, 'table':45,'hammock':17}
comp_timber = {'pine':67, 'oak':31,'balsa':36}


""""Recorded below is Bunning's stocked items separated into three category's (power tools, outdoor
furniture and timber) prices of the items and number units sold in financial year 2. In this example
we won't be recording the competitors sales or profits made"""

#prices of Bunning's stock with the 10% discount applied if a competitor has a lower price on a stocked item
power_tools_price = beat_it_by_10.discounted_prices(financial_year_1.power_tools,comp_power_tools)
outdoor_furniture_price = beat_it_by_10.discounted_prices(financial_year_1.outdoor_furniture,comp_outdoor_furniture)
timber_price = beat_it_by_10.discounted_prices(financial_year_1.timber,comp_timber)

#Bunning's units sold.
power_tools_units_sold = {'drill':763, 'chainsaw':2398,'sander':285}
outdoor_furniture_units_sold = {'chair':575, 'table':165,'hammock':1001}
timber_units_sold = {'pine':525, 'oak':736,'balsa':845}

#Bunning's profits made on sales in fy2
power_tools_profits = analysis.profits(power_tools_units_sold,power_tools_price)
outdoor_furniture_profits = analysis.profits(outdoor_furniture_units_sold,outdoor_furniture_price)
timber_profits = analysis.profits(timber_units_sold,timber_price)