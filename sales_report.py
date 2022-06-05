import collections
import current_stock
import beat_it_by_10
import competitors
import analysis

"""These dictionaries measure how many units were sold before and after the
beat it by 10% discount was brought in. We then measure what the difference is in
profits for In financial year 1 (fy1) and financial year 2 (fy2). In fy2 the discount was included
but it was not included in fy1. We will assume for this example other variables that may impact sales 
are otherwise accounted for. The purpose is to determine the validity of Bunning's discount to see if they
sell enough stock to make up for the lower prices"""

"""this function will multiple the units sold in a financial year by the price of the products 
duirng that financial year"""
def profits(units_sold: dict,prices: dict):
    profits_for_category = {
    k: v * units_sold[k]
    for k, v in prices.items()
    if k in units_sold
    }
    profits_for_category_rounded = dict()
    for key in profits_for_category:
        profits_for_category_rounded[key] = round(profits_for_category[key], 2)
    return profits_for_category_rounded


#Financial year 1, units sold.
power_tools_units_sold_fy1 = {'drill':436, 'chainsaw':2378,'sander':215}
outdoor_furniture_units_sold_fy1 = {'chair':475, 'table':135,'hammock':984}
timber_units_sold_fy1 = {'pine':325, 'oak':734,'balsa':745}

fy1_units_sold_nested = {
'power_tools_units_sold_fy1' : {'drill':436, 'chainsaw':2378,'sander':215},
'outdoor_furniture_units_sold_fy1' : {'chair':475, 'table':135,'hammock':984},
'timber_units_sold_fy1' : {'pine':325, 'oak':734,'balsa':745},
}

#Financial year 2 number of units sold units sold.
power_tools_units_sold_fy2 = {'drill':763, 'chainsaw':2398,'sander':285}
outdoor_furniture_units_sold_fy2 = {'chair':575, 'table':165,'hammock':1001}
timber_units_sold_fy2 = {'pine':525, 'oak':736,'balsa':845}

#The prices of stock sold in fy1 are already listed in current_stock.py as dictionaries.

#prices of stocked items in fy2 with the discount applied if a competitor has a lower price on a stocked item are calculated
power_tools_fy2_price = beat_it_by_10.discounted_prices(current_stock.power_tools,competitors.comp_power_tools)
outdoor_furniture_fy2_price = beat_it_by_10.discounted_prices(current_stock.outdoor_furniture,competitors.comp_outdoor_furniture)
timber_fy2_price = beat_it_by_10.discounted_prices(current_stock.timber,competitors.comp_timber)

#profits made in fy 1
power_tools_profits_fy1 = profits(power_tools_units_sold_fy1,current_stock.power_tools)
outdoor_furniture_profits_fy1 = profits(outdoor_furniture_units_sold_fy1,current_stock.outdoor_furniture)
timber_profits_fy1 = profits(timber_units_sold_fy1,current_stock.timber)

#profits made on sales in fy2
power_tools_profits_fy2 = profits(power_tools_units_sold_fy2,power_tools_fy2_price)
outdoor_furniture_profits_fy2 = profits(outdoor_furniture_units_sold_fy2,outdoor_furniture_fy2_price)
timber_profits_fy2 = profits(timber_units_sold_fy2,timber_fy2_price)

#profits of fy2 - profits of fy1 to examine the growth or reduction in sales
power_tool_sales = analysis.profit_loss_by_year_category_total(power_tools_profits_fy1, power_tools_profits_fy2)
outdoor_furniture_sales = analysis.profit_loss_by_year_category_total(outdoor_furniture_profits_fy1, outdoor_furniture_profits_fy2)
timber_sales = analysis.profit_loss_by_year_category_total(timber_profits_fy1, timber_profits_fy2)







