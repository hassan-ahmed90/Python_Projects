

do_cont=True
while do_cont:
    def band_name_generator():
        print("Welcome to brand name generator !")
        city_name=input("In What city you grew up?\n")
        pet_name=input("What is your pet name?\n")
        brand_name=city_name+" "+pet_name
        print(f"Your Band Name could be '{brand_name}' !!!!")

    band_name_generator()
    do_cont=input("Do you want to continue y/n ?\n")
    if do_cont=='y':
        print("\n"*20)
    elif do_cont=='n':
        print("\n"*20)
        print("Good Bye")
        do_cont=False
