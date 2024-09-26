class Restaurant:

    def __init__(self,):
        self.menu_items = {}
        self.book_table =[]
        self.customer_orders = []


    def add_items_to_menu(self, new_items):
        for key,value in new_items.items():
            self.menu_items[key] = value

    def make_table_reservation(self,table_number):
        self.book_table.append(table_number)

    def customer_order(self,table_number,order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)


restaurant = Restaurant()
restaurant.add_items_to_menu({'Fish':'10EUR','French Fries': '5EUR'})
restaurant.make_table_reservation(3)
restaurant.make_table_reservation(12)
restaurant.customer_order(3,{'French Fries': '5EUR'})

print("Display the Restaurant's menu : ",restaurant.menu_items)
print("Display the Restaurant's reservations : ",restaurant.book_table)
print("Display the Customer's order : ",restaurant.customer_orders)