"""
Sally is only allowed to buy a toy under or equal to 5.00 dollars.
Write an app that tells sally which item which toy she can buy
(example: “you can buy, Train.”). The available items are below.
Create a list with the below items.

Train_3.00
Dolly_1.10
Slinky_7.50
Coloring Book_4.99
blocks_8.20
"""

items_dict = {"Train": 3.00,
              "Dolly": 1.10,
              "Slinky": 7.50,
              "Coloring Book": 4.99,
              "blocks": 8.20}


for items, price in items_dict.items():
    if price <= 5.00:
        print(f'you can buy, {items}')


print('Finally finished!')
