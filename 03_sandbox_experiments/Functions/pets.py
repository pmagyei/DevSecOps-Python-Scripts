def describe_pet(pet_name, animal_type='dog'):  #default value can be assigned to the parameters
    #default value will be assigned if not specified in call function argument
    #default parameter is ignored when the parameter in call function is provided
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet() #no arguments, information is missing from the function call causes a TypeError

# describe_pet(pet_name='wille') #assigns each argument to the parameter, irrespective of the order
#
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
