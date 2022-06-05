

"""Compare two dictionaries, x is the current stock of Bunning's and y is the lowest found price
amongst competitors on a current stocked item. If an item sold by a competitor is found to be
lower than a stocked item, the stocked item for Bunning's is changed to be 10% less than that
of the competitor’s price."""
import competitors
import current_stock

"""Compare two dictionaries, cs is the current stock of Bunning's and comp is the lowest found price
amongst competitors on a current stocked item. If an item sold by a competitor is found to be
lower than a stocked item, the stocked items price for Bunning's is changed to be 10% less than that
of the competitor’s price."""


def compare_after_discount(cs: dict,comp:dict):
    discount = cs.copy()
    for key in discount:
        if key in comp:
            if discount[key] > comp[key]:
                discount[key] = round(comp[key]*.9,2), "reduced"
    return "original prices", cs, "new prices" , discount


def discounted_prices(cs: dict,comp:dict):
    discount = cs.copy()
    for key in discount:
        if key in comp:
            if discount[key] > comp[key]:
                discount[key] = round(comp[key]*.9,2)
    return discount

def by_product(name: str,price:int,category: dict):
    product = {name:price}
    for key in product:
        if key in category:
            original = category[key]
            print("Our price $", original)
            print("Your price $", price)
            if category[key] > product[key]:
                category[key] = round(product[key]*.9,2) , "reduced"
                print("we'll beat it by 10%")


