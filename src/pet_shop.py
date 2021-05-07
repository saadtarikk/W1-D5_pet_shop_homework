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
    pet_shop["admin"]["pets_sold"] = enter_amount + get_total_cash(pet_shop["admin"]["total_cash"])

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, what_breed):
    breed = [] # ==>    we create a variable here because we want to get back all the pets in dictionary by name
    for pet in pet_shop["pets"]: # means it goes through every pet in list of pet dictionary in pet_shop dictionary
        if pet["breed"] == what_breed: # if pet[breed] in list of pet dictionary == to what_gread which is a given variable
            breed.append(pet)# add pet[breed] into empty breed =[] variable
    return breed # return the value breed[] variable
        
def find_pet_by_name(pet_shop, pet_name):

    for pet in pet_shop["pets"]: #for every pet in pet_shop dict "pets" fict if its == pet_name 
        if pet["name"] == pet_name:
            return pet # return value

# def remove_pet_by_name(pet_shop, pet_name):
    # for pet in pet_shop["pets"]:
    #     if  pet["name"] == pet_name:
    #         pet["name"].pop
    
