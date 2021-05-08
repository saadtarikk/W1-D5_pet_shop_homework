import pdb

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, enter_amount): 
    pet_shop["admin"]["total_cash"] += enter_amount
    
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, enter_amount):
    pet_shop["admin"]["pets_sold"] += enter_amount
    # pet_shop["admin"]["pets_sold"] = enter_amount + get_pets_sold(pet_shop)

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, what_breed):
    breed = [] 
    for pet in pet_shop["pets"]: 
        if pet["breed"] == what_breed: 
            breed.append(pet)
    return breed 
        
def find_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]: 
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    # for pet in pet_shop["pets"]:
    #     if pet["name"] == pet_name:
    #         return pet_shop["pets"].remove(pet)
            # return pet_shop["pets"]
    
    # pet = find_pet_by_name(pet_shop, pet_name)
    # pet_shop["pets"].remove(pet)
     
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, pet_name))

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
def get_customer_cash(customers):
    return customers["cash"]   

def remove_customer_cash(customers, give_amount):
    customers["cash"] -= give_amount

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet) # we need to tell function where to append inside customers list.


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

