import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, enter_amount): # test wants us to return totalcash in petshop["admin"] dict 
    pet_shop["admin"]["total_cash"] += enter_amount # we use += to add or subsrtact value in variable enter_amount it will perform + and - because -10 + 100 is still = 90
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, enter_amount):
    # pet_shop["admin"]["pets_sold"] += enter_amount
    pet_shop["admin"]["pets_sold"] = enter_amount + get_pets_sold(pet_shop)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, what_breed):
    breed = [] # ==>    we create a variable here because we want to get back all the pets in dictionary by name
    for pet in pet_shop["pets"]: # means it goes through every pet in list of pet dictionary in pet_shop dictionary
        if pet["breed"] == what_breed: # if pet[breed] in list of pet dictionary == to what_gread which is a given variable
            breed.append(pet)# add pet[breed] into empty breed =[] variable
    return breed # return the value breed[] variable
        
def find_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]: #for every pet in pet_shop dict "pets" list if its == pet_name 
        if pet["name"] == pet_name:
            return pet # return value

def remove_pet_by_name(pet_shop, pet_name):
    # for pet in pet_shop["pets"]:
    #     if pet["name"] == pet_name:
    #         return pet_shop["pets"].remove(pet)
            # return pet_shop["pets"]
    
    # pet = find_pet_by_name(pet_shop, pet_name)
     
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, pet_name))

    



def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
def get_customer_cash(customers):
    return customers["cash"]   

def remove_customer_cash(customers, give_amount):
    customers["cash"] -= give_amount

def get_customer_pet_count(customers):
    return len(customers["pets"]) #why do we use len here but in when getting customer cash

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet) # we need to tell function where to append inside customers list.


def customer_can_afford_pet(customer, new_pet):
    # if customer["cash"] >= new_pet["price"]:
    #     return True
    # else:
    #     return False
    # ternary operator return// 
    return True if customer["cash"] >= new_pet["price"] else False

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet and customer_can_afford_pet(customer, pet): 
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        add_pet_to_customer(customer, pet)
        increase_pets_sold(pet_shop, 1)
            


  

        
                                         #self.assertEqual(1, get_customer_pet_count(customer))
                                      # self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
                                      # self.assertEqual(100, get_customer_cash(customer))
                                      # self.assertEqual(1900, get_total_cash(self.cc_pet_shop))
                                        # "name": "Alice",
                                        # "pets": [],
                                        # "cash": 1000

