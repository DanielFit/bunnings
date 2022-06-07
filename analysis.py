import collections
import beat_it_by_10
import current_stock
import competitors
from collections import defaultdict


"""Here we can find out if Bunning's compares two financial years, in financial year 1 they do not
 offer any discount and in financial year 2 they apply the discount of 'beating competitors prices by 10%'
 """


"""this looks at each item in a category individually to see how much each item loses 
value if the discount is applied due to a competitor having a lower priced
item"""
def loss_on_discount_per_item(cs:dict, comp:dict):
    discount = beat_it_by_10.discounted_prices(cs,comp)

    copy_discount = collections.Counter(discount)
    copy_cs = collections.Counter(cs)
    profit_loss = dict(copy_cs - copy_discount)

    loss_per_product = dict()
    for key in profit_loss:
        loss_per_product[key] = round(profit_loss[key], 2)

    total_loss = sum(loss_per_product.values())

    return loss_per_product ,'$', total_loss

"""This function measures the profits and loses per item in a category over two financial years """
def profit_loss_by_year_by_category_items(fy1:dict, fy2:dict):
    fy1_copy = collections.Counter(fy1)
    fy2_copy = collections.Counter(fy2)

    profits = dict(fy2_copy- fy1_copy)
    losses = dict(fy1_copy- fy2_copy)
    return "profits $", str(profits),"losses $",str(losses)

"""This function measures the profits and loses per item in a category over two financial years """
def profit_loss_by_year_category_total(fy1:dict, fy2:dict):
    fy1_copy = collections.Counter(fy1)
    fy2_copy = collections.Counter(fy2)

    profits = dict(fy2_copy- fy1_copy)
    losses = dict(fy1_copy- fy2_copy)
    total = round(sum(profits.values()) - sum(losses.values()),2)
    return total


"""this function will multiple the units sold in a financial year by the price of the products 
duirng that same financial year"""
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


