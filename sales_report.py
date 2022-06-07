import financial_year_1
import financial_year_2
import analysis


"""These variables measure what the difference is in profits for financial year 1 (fy1) and financial year 2 (fy2). 
The 10% discount was applied in fy2 but not in fy1. We will assume for this example other variables that 
may impact sales are otherwise accounted for. The purpose is to determine the profitability of Bunning's discount to see 
if they sold enough stock to make up for the lower prices"""


"""The profits from fy1 are subtracted from the profits in fy2 to determine if the sales went up or down after the beat
it by 10 discount was applied"""

power_tool_sales_growth = analysis.profit_loss_by_year_category_total(financial_year_1.power_tools_profits, financial_year_2.power_tools_profits)
outdoor_furniture_sales_growth = analysis.profit_loss_by_year_category_total(financial_year_1.outdoor_furniture_profits, financial_year_2.outdoor_furniture_profits)
timber_sales_growth = analysis.profit_loss_by_year_category_total(financial_year_1.timber_profits, financial_year_2.timber_profits)







