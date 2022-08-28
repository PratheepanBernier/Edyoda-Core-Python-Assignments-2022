"Food Ordering App"

"Admin Module"

class admin :
    food_details = dict() 
    food_id=3
    food_details[1] = {"Food ID": 1, "Name": "Tandoori Chicken","Quantity":"4 pieces","Price":240,"Discount":0,"Stock":50}  
    food_details[2] = {"Food ID": 2, "Name": "Vegan Burger","Quantity":"1 piece","Price":320,"Discount":0,"Stock":60} 
    food_details[3] = {"Food ID": 3, "Name": "Truffle Cake","Quantity":"500 gms","Price":900,"Discount":0,"Stock":100}
    def __init__(self):
        pass                                                                       

    def admin_login(self):
        email_id = "bernier@gmail.com"                                                                                                                         
        password = "123@bernier"                                                                                                                         
        print("-----Food Ordering App------")
        user_id = input("Enter Email ID: ")                                                                                                    
        passcode = input("Enter Password: ")                                                                                                   
        if user_id==email_id and passcode==password :                                                                                             
            self.choice(admin.food_id)
        else:
            print("Enter correct credentials !")

    def choice(self,food_id):
        self.food_id = food_id
        print("1.Add new Food Item \n2.Edit food item \n3.View list of all food items \n4.Remove food item from the menu \n5.Logout") 
        choice=int(input("Enter your choice(eg.Enter 1 for adding new food item...) : "))                                             
        if choice == 1:                                                                                                               
            admin.food_id = admin.food_id + 1                                                                                           
            self.add_new_item(admin.food_id)
        if choice == 2:                                                                                                              
            self.edit_item()
        if choice == 3:                                                                                                               
            self.view_item()
            self.choice(self)
        if choice == 4 :
            self.remove_item()
        if choice == 5 :
            option()

    def add_new_item(self,food_id):
        print("Food ID : ",food_id)                                                                                               
        name = input("Name : ")                                                                                                   
        quantity = input("Quantity(in gm/kg/pieces) : ")                                                                          
        price = int(input("Price(in INR) : "))                                                                                         
        discount= int(input("Discount(in %) : "))                                                                                      
        stock = int(input("Stock left(in quantity) : "))   
        admin.food_details[food_id] = {"Food ID": food_id, "Name": name,"Quantity":quantity,"Price":price,"Discount":discount,"Stock":stock}                    
        print(f"Food item named {name} is added to the menu")                                                                     
        self.choice(self)

    def edit_item(self):
        id = int(input("Enter food ID of the Food item that need to be edited : "))                                                      
        edited_name = input("Name : ")                                                                                                   
        edited_quantity = input("Quantity(in gm/kg/pieces) : ")                                                                          
        edited_price = int(input("Price(in INR) : "))                                                                                         
        edited_discount= int(input("Discount(in %) : "))                                                                                      
        edited_stock = int(input("Stock left(in quantity) : "))                                                                               
        admin.food_details[id] = {"Food ID": id,"Name": edited_name,"Quantity":edited_quantity,"Price":edited_price,"Discount":edited_discount,"Stock":edited_stock}                                                                                            
        print(f"Food item is edited and updated")
        self.choice(self)

    def view_item(self):
        for k in admin.food_details.values():
            for v,w in k.items():
                print(f'{v} : {w}')                                                                    
        print("-----All food items displayed-----")
    def remove_item(self):
        remove_id=int(input("Enter the food id of the food item that need to be removed : "))
        admin.food_details.pop(remove_id)
        print(f"Food item with food id : {remove_id} is removed !")
        self.choice(self)
   
"User module"

class user:
    storer = dict()
    history_viewer = dict()
    choice2=0
    def __init__(self):
        pass
    def user_login(self):
        choice1=int(input("1.Register \n2.Login \nEnter your choice(eg.1 for register...):"))
        if choice1 == 1:
            self.register()
        elif choice1 == 2 :
            self.login()
        else:
            print("Enter either 1 or 2 ...Bye")
            self.option()

    def register(self):
        full_name = input("Welcome !!! Register your details...\nFull Name : ")
        phone_number = int(input("Phone Number : "))
        email = input("Email id : ")

        address = input("Address : ")
        password = input("Password : ")
        user.storer = {email: {"Full Name": full_name,"Phone Number" : phone_number,"Email":email,"Address":address,"Password":password}}
        user.login(self)

    def update_profile(self):
        e_full_name = input("Profile Updation \nFull Name : ")
        e_phone_number = int(input("Phone Number : "))
        e_address = input("Address : ")
        e_password = input("Password : ")
        user.storer = {self.email: {"Full Name": e_full_name,"Phone Number" : e_phone_number,"Address":e_address,"Password":e_password}}
        print("----Profile updated---")

    def new_order(self):
        food_order=[]
        m=int(input("Enter food id of the item you wish to order..(eg. type 1 to order food item with food id 1) :"))
        food_order.append(m)
        for i in food_order:
            user.history_viewer[i] = admin.food_details[i]
        print("----------Order placed !--------")
    
    def order_history(self):
        for j in user.history_viewer.values():
            for l,m in j.items():
                print(f'{l} : {m}')                                                                    
        print("-----All food items displayed-----")
        
    def login(self):
        mail_id = input("Login...\nEmail id: ")
        passcode = input("Password : ")
        if user.storer[mail_id]["Password"] == passcode :
            user.choice2 = int(input("1.Place New Order \n2.Order History \n3.Update Profile \n4.Logout \nEnter your Choice (eg. enter 1 for placing new order...) : "))
            if user.choice2 == 1 :
                user.view_item(self)
                print("Place your order...")
                self.new_order()
            elif user.choice2 == 2 :
                user.order_history(self)
            elif user.choice2 == 3 :
                self.update_profile()
            elif user.choice2 == 4 :
                exit
            else :
                print("Enter any number between 1 to 4...\nBye")
    def view_item(self):
        admin_obj.view_item()

#main module:

admin_obj=admin()
user_obj = user() 
def option ():
    print("--------Food Ordering App------\n1.Admin Login \n2.User Login/User Registration \n3.Exit")
    option = int(input("Enter your Choice(eg. Enter 1 for admin login...) : "))
    if option == 1 :
        admin_obj.admin_login()
    elif option == 2 :
        user_obj.user_login()
    else :
        print("Enter 1 or 2...")
        option()
option()