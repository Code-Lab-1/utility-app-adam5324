phone_menu = [
    { 
    'itemname' : 'Iphone 14','itemno' : 1,'price' : 5,
     },

         { 
    'itemname' : 'Iphone 14 pro','itemno' : 2,'price' : 6,
     },

         { 
    'itemname' : 'Iphone 13', 'itemno' : 3,'price' : 6,
     },

              { 
    'itemname' : 'Iphone 13 pro','itemno' : 4,'price' : 4,
     },

              { 
    'itemname' : 'Iphone 12','itemno' : 5,'price' : 5,
     },

         { 
    'itemname' : 'Iphone 12 pro','itemno' : 6,'price' : 4,
     },

         { 
    'itemname' : 'Iphone 11','itemno' : 7,'price' : 5,
     },

         { 
    'itemname' : 'Iphone 11 pro','itemno' : 8,'price' : 6,
     },

              { 
    'itemname' : 'Iphone X','itemno' : 9,'price' : 4,
     },

              { 
    'itemname' : 'Iphone 8', 'itemno' : 10, 'price' : 5,
     },

         { 
    'itemname' : 'Apple charger','itemno' : 11,'price' : 5,
     },

         { 
    'itemname' : 'Apple headset','itemno' : 12,'price' : 4,
     },

         { 
    'itemname' : 'Airpod pro','itemno' : 13,'price' : 4,
     },

              { 
    'itemname' : 'Airpod max','itemno' : 14,'price' : 4,
     },

              { 
    'itemname' : 'Apple wireless charger','itemno' : 15,'price' : 6,
     },

         { 
    'itemname' : 'Airtag ','itemno' : 16,'price' : 4,
     },

         { 
    'itemname' : 'Lightning adaptor','itemno' : 17,'price' : 4,
     },

         { 
    'itemname' : 'Apple magsafe cover','itemno' : 18,'price' : 4,
     },

              { 
    'itemname' : 'Apple lighning cable','itemno' : 19,'price' :6,
     },

              { 
    'itemname' : 'Apple pencil','itemno' : 20,'price' : 4,
     },
]

#printing phones and logo
def phone():
  print("〈〈〈〈〈〈 BATHSPA COFFEE 〉〉〉〉〉\n") 
  print("*************** PHONES ***************")
  phone = {
    "01. Iphone 14" : "5 AED", 
    "02. Iphone 14 pro" : "6 AED",
    "03. Iphone 13" : "6 AED",
    "04. Iphone 13 pro" : "4 AED",
    "05. Iphone 12" : "5 AED",
    "06. Iphone 12 pro" : "4 AED",
    "07. Iphone 11" : "5 AED",
    "08. Iphone 11 pro" : "6 AED",
    "09. Iphone X" : "4 AED",
    "10. Iphone 8" : "6 AED",
}
  for item, price in phone.items():
    print(f" {item:30}, {price}")

#printing accessories
def accessories():
  print("**************** ACCESSORIES ****************")
  accessories_items = {
    "11. Apple charger" : "5 AED", 
    "12. Apple headset" : "4 AED",
    "13. Airpod pro" : "4 AED",
    "14. Airpod max" : "4 AED",
    "15. Apple wireless charger" : "6 AED",
    "16. Airtag" : "4 AED",
    "17. Lightning adaptor" : "4 AED",
    "18. Apple magsafe cover" : "4 AED",
    "19. Apple lighning cable" : "6 AED",
    "20. Apple pencil" : "4 AED",
}
  for item, price in accessories_items.items():
    print(f" {item:30}, {price}")
  print()

def options():
  phone()
  accessories()

def order():

  while True:


    options()

    amount = int(input('Please Enter the ammount to be purchase items:\n'))

    if amount <= 0:
      print('Invalid Amount\n')
      order()

    itementer = int(input('Please choose the item to be dispensed\n'))

    if itementer >= 21 or itementer <= 0:
      print('Invalid Input')

    items = []
    total_sum = []

    for di in phone_menu:

          if itementer == di['itemno'] and amount <= di['price'] :
            print('Insufficient Amount\n')
            order()

          if itementer == di['itemno'] and amount >= di['price']:

            print('***************************************\n')
            print(f"You picked {di['itemname']}\n")
            print('***************************************\n')

            total_sum.append(di.get('price'))

            items.append(di.get('itemname'))

            print(f"Amount of {di['itemname']}\n")

            print('***************************************\n')
            print("You may now proceed a receive the following items that have been dispensed:\n")

            print(items, '\n')
            print('***************************************\n')

            total=sum(total_sum)
            print("And here is your total amount:\n\n\t", total, "AED\n")

            remaining_amount = amount - total
            print("And your change is:\n\n\t", remaining_amount, "AED\n")

            print('***************************************\n')
            print("Thank you for the purchase!\n")
            print('***************************************\n')

            break

def bathspaphone():
  order()

bathspaphone()