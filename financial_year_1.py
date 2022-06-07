import analysis


#The prices of stock sold no discount applied
power_tools = {'drill':40, 'chainsaw':50,'sander':30}
outdoor_furniture = {'chair':50, 'table':40,'hammock':30}
timber = {'pine':50, 'oak':40,'balsa':30}

#Units sold.
power_tools_units_sold = {'drill':436, 'chainsaw':2378,'sander':215}
outdoor_furniture_units_sold = {'chair':475, 'table':135,'hammock':984}
timber_units_sold = {'pine':325, 'oak':734,'balsa':745}

#profits made in fy 1
power_tools_profits = analysis.profits(power_tools_units_sold,power_tools)
outdoor_furniture_profits = analysis.profits(outdoor_furniture_units_sold,outdoor_furniture)
timber_profits = analysis.profits(timber_units_sold,timber)