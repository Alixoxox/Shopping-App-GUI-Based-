from PIL import Image
import tkinter as tk
import customtkinter as ct
# Initialize the CTk window
r = ct.CTk()

# Set the default color theme and appearance mode
ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("dark")
r.geometry('1024x768')
r.minsize(200, 200)
r.title("OCEAN MALL")
current_frame = None  ##MAIN FRAME

# Function to create a frame with content and handle previous frame
'''MAIN FUNCTION
this is the main frame function which implements the method for creating and desroying different functions'''
def frame_wrapper(content_function):
    global current_frame
    # Destroy the current frame if it exists
    if current_frame is not None:
        current_frame.destroy()

    # Create a new frame
    current_frame = ct.CTkFrame(r, width=1024, height=768)
    current_frame.pack(fill='both', expand=True)  # Fill the entire window
    
    # Call the content function to populate the frame
    content_function(current_frame)

def write_user_data(user_data):
    with open("user_data.txt",'w') as f:
        for user in user_data:
            f.write(f"{user['username']}:{user['password']}:{user['name']}:{user["phone"]}:{user["email"]}\n")

def load_user_data(user_data):
    with open('user_data.txt', 'r') as f:
               content = f.read().strip()
               if content:
                   lines = content.split('\n')
                   for line in lines:
                       username, password, name, phone, email = line.split(':')
                       user_data.append({
                           "username": username,
                           "password": password,
                           "name": name,
                           "phone": phone,
                           "email": email
                       })

# Function to create the welcome page
"""PAGE-1"""
def welcome_page():
    # Function to create the welcome page content
    def welcome_page_content(frame):
        welcome_label = ct.CTkLabel(frame, text="WELCOME TO OCEAN MALL\nTO ACCESS THIS APPLICATION :", font=('calibri', 50,'bold'),text_color='grey')
        welcome_label.pack(padx=150, pady=40)  # Set pady to (30, 0) to eliminate bottom padding
        ##BUTTONS FOR MAIN 
        b_log_ac = ct.CTkButton(frame, text="LOGIN ",font=("calibri",25,"bold"),width=400,height=100,corner_radius=20,command=lambda: Login()).pack(pady=40)
        b_create_ac = ct.CTkButton(frame, text="CREATE AN ACCOUNT ",font=("calibri",25,"bold"),width=400,height=100,corner_radius=20,command=lambda: Create_acc(user_data)).pack(pady=40)
        load_user_data(user_data)
    # Call frame_wrapper with the welcome_page_content function
    frame_wrapper(welcome_page_content)
"""LOGIN ACCOUNT FUNCTION-PAGE 2"""
def Login():
    def submit_results(user_frame, entry_log_user, entry_log_pas, error_label_log):
        log_username = entry_log_user.get()
        log_password = entry_log_pas.get()

        for user in user_data:
            if user["username"] == log_username and log_password == user["password"]:  # Use secure password validation
                error_label_log.configure(text="Login Successful",text_color='green')
                return main_task_page()   
        error_label_log.configure(text="Login Unsccessful",text_color='red')      
        create_acc_button = ct.CTkButton(user_frame, text="Create Account", font=('roboto', 22, 'bold'), text_color='grey', height=30, command=lambda: Create_acc(user_data))
        create_acc_button.grid(row=5, column=0, pady=15)
        return False


    def show_password(entry):
        current_show_state = entry.cget('show')
        entry.configure(show='' if current_show_state == "*" else '*')

    def Login_page_content(frame):
        log_l = ct.CTkLabel(frame, text="PLEASE LOG IN YOUR CREDENTIALS:", font=('calibri', 40, 'bold'), text_color='grey')
        log_l.pack(padx=150, pady=20)

        user_frame = ct.CTkFrame(frame)
        user_frame.pack(pady=20)

        user_log = ct.CTkLabel(user_frame, text="Enter Username : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        user_log.grid(row=0, column=0, padx=30, pady=25, sticky='e')
        entry_log_user = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'), text_color='black', fg_color='white', corner_radius=30, width=400, height=50, show="*")
        entry_log_user.grid(row=0, column=1, padx=30, pady=25, sticky='w')

        Togle_privacy_1 = ct.CTkButton(user_frame, text=' 👁 ', fg_color='black', hover_color='grey', width=50, command=lambda: show_password(entry_log_user))
        Togle_privacy_1.grid(row=0, column=2, padx=10, pady=25, sticky='w')

        user_pas = ct.CTkLabel(user_frame, text="Enter Password : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        user_pas.grid(row=1, column=0, padx=30, pady=25, sticky='e')
        entry_log_pas = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'), text_color='black', fg_color='white', corner_radius=30, width=400, height=50, show="*")
        entry_log_pas.grid(row=1, column=1, padx=30, pady=25, sticky='w')

        Togle_privacy_2 = ct.CTkButton(user_frame, text=' 👁 ', fg_color='black', hover_color='grey', width=50, command=lambda: show_password(entry_log_pas))
        Togle_privacy_2.grid(row=1, column=2, padx=10, pady=25, sticky='w')

        error_label_log = ct.CTkLabel(user_frame, text='', font=('roboto', 25, 'bold'), height=30)
        error_label_log.grid(row=3, column=0, columnspan=3, padx=10, pady=20)

        submit_log = ct.CTkButton(user_frame, text='SUBMIT', font=('roboto', 25, 'bold'), text_color='grey', height=50, command=lambda: submit_results(user_frame, entry_log_user, entry_log_pas, error_label_log))
        submit_log.grid(row=2, column=1, padx=10, pady=20, sticky='nsew')

        """"TO BE CONTINUED IMPLEMENT BACK-END FUNCTIONALITIES AND IMPLEMENT FEATURE TO CREATE ACCOUNT IF THE USER HAS NOT FIGURED OUT THE CREDS AFTER A COUPLE OF TRIES and submit button too"""

    frame_wrapper(Login_page_content)
'''ACCOUNT CREATION FUNCTION -PAGE-3'''
def Create_acc(user_data):
    def submit(entry_ca_email,entry_ca_name,entry_ca_pass,entry_ca_phoneno,entry_ca_usernme,error_label):
        AC_name = entry_ca_name.get()
        AC_username = entry_ca_usernme.get()
        AC_pass = entry_ca_pass.get()
        AC_email = entry_ca_email.get()
        AC_phone = entry_ca_phoneno.get()
    
        if any(user['username'] == AC_username for user in user_data):
            error_msg = "Username already exists"
        elif not AC_name.isalpha():
            error_msg = "Name must contain only letters"
        elif not AC_phone.isdigit():
            error_msg = "Phone number must contain only digits"
        elif not (AC_email.endswith("@gmail.com") or AC_email.endswith("@neduet.edu.pk")):
            error_msg = "Email must end with @gmail.com or @neduet.edu.pk"
        elif len(AC_pass) < 8:
            error_msg = "Password must be at least 8 characters long"
        else:
            user_data.append({"username": AC_username, "password": AC_pass, "name": AC_name, "phone": AC_phone, "email": AC_email})
            write_user_data(user_data)
            return main_task_page()
    
        error_label.configure(text=error_msg, font=('roboto', 18), text_color='red')
        entry_ca_name.delete(0, 'end')
        entry_ca_email.delete(0, 'end')
        entry_ca_pass.delete(0, 'end')
        entry_ca_phoneno.delete(0, 'end')
        entry_ca_usernme.delete(0, 'end')

    def Create_acc_content(frame):
        log_2 = ct.CTkLabel(frame, text="CREATE ACCOUNT:\nPLEASE ENTER THE FOLLOWING DETAILS:", font=('calibri', 40, 'bold'), text_color='grey')
        log_2.pack(padx=150, pady=20)
        # Using a frame to group the username label and entry field
        user_frame = ct.CTkFrame(frame)
        user_frame.pack(pady=20)
       
        ##name:
        ca_name = ct.CTkLabel(user_frame, text="Enter Your FULL Name : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        ca_name.grid(row=0, column=0, padx=30, pady=25, sticky='e')
        entry_ca_name = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'),placeholder_text='  XYZ ' ,text_color='black', fg_color='white', corner_radius=50,width=400,height=50)
        entry_ca_name.grid(row=0, column=1, padx=30, pady=22, sticky='w')
       
        ##Username:
        ca_usernme = ct.CTkLabel(user_frame, text="Enter Your User Name : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        ca_usernme.grid(row=1, column=0, padx=30, pady=25, sticky='e')
        entry_ca_usernme = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'),placeholder_text='   XYZ123  ', text_color='black', fg_color='white', corner_radius=50,width=400,height=50)
        entry_ca_usernme.grid(row=1, column=1, padx=30, pady=22, sticky='w')
        
        ##Password:
        ca_pass = ct.CTkLabel(user_frame, text="Enter Your Password : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        ca_pass.grid(row=2, column=0, padx=30, pady=25, sticky='e')
        entry_ca_pass = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'),placeholder_text="  ******** >= 8 digits  ", text_color='black', fg_color='white', corner_radius=50,width=400,height=50)
        entry_ca_pass.grid(row=2, column=1, padx=30, pady=22, sticky='w')
       
        ##Email address:
        ca_email = ct.CTkLabel(user_frame, text="Enter Your Email address : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        ca_email.grid(row=3, column=0, padx=30, pady=25, sticky='e')
        entry_ca_email = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'),placeholder_text="  ****@gmail.com  ", text_color='black', fg_color='white', corner_radius=50,width=400,height=50)
        entry_ca_email.grid(row=3, column=1, padx=30, pady=22, sticky='w')

        ##PHONE NUMBER:
        ca_phoneno = ct.CTkLabel(user_frame, text="Enter Your Phone Number : ", font=('roboto', 25, 'bold'), text_color='grey', compound=ct.LEFT)
        ca_phoneno.grid(row=4, column=0, padx=30, pady=25, sticky='e')
        entry_ca_phoneno = ct.CTkEntry(user_frame, font=('roboto', 25, 'bold'),placeholder_text="  123456789  ", text_color='black', fg_color='white', corner_radius=50,width=400,height=50)
        entry_ca_phoneno.grid(row=4, column=1, padx=30, pady=22, sticky='w')

        #submit:
        submit_but = ct.CTkButton(user_frame,text='SUBMIT',font=('roboto', 25, 'bold'), text_color='grey', height=50,command=lambda: submit(entry_ca_email,entry_ca_name,entry_ca_pass,entry_ca_phoneno,entry_ca_usernme,error_label))
        submit_but.grid(row=5, column=0,columnspan=2,padx=10,pady=18,sticky='nsew')

        #error label
        error_label = ct.CTkLabel(user_frame, text="", font=('roboto', 22,'bold'))
        error_label.grid(row=6, column=0, columnspan=2,pady=2)
    frame_wrapper(Create_acc_content)
"""page 4 which contains home (i.e:items) ,cart ,purchase history,contact info """

def main_task_page():
    def main_task_page_content(frame):
        ful_page = ct.CTkFrame(frame)
        ful_page.pack(fill='both', expand=True)

        option_menu = ct.CTkFrame(ful_page, height=75)
        option_menu.pack(pady=5, fill='x')

        content_frame = ct.CTkScrollableFrame(ful_page)
        content_frame.pack(fill='both', expand=True, padx=20,pady=30)

        home_page_(content_frame)

        home_btn = ct.CTkButton(option_menu, text='  Products  ', font=('arial', 25, 'bold'), fg_color='transparent', hover_color='#292929', corner_radius=20, width=40, height=20, command=lambda: home_page_(content_frame))
        home_btn.grid(row=0, column=0, padx=100)

        cart_btn = ct.CTkButton(option_menu, text='  Cart  ', font=('arial', 25, 'bold'), fg_color='transparent', hover_color='#292929', corner_radius=20, width=30, height=20, command=lambda: cart_page_(content_frame))
        cart_btn.grid(row=0, column=10, padx=115)

        shop_hist_btn = ct.CTkButton(option_menu, text='  Shop History  ', font=('arial', 25, 'bold'), fg_color='transparent', hover_color='#292929', corner_radius=20, width=30, height=20, command=lambda: shop_hist_page_(content_frame))
        shop_hist_btn.grid(row=0, column=20, padx=115)

        contact_btn = ct.CTkButton(option_menu, text='  Contact-Info  ', font=('arial', 25, 'bold'), fg_color='transparent', hover_color='#292929', corner_radius=20, width=30, height=20, command=lambda: contact_page_(content_frame))
        contact_btn.grid(row=0, column=30, padx=115)

    def extra_duplicate_frame(content_frame):
        for widget in content_frame.winfo_children():
            widget.destroy()

    def home_page_(content_frame):
        """IMPLEMENT THESE FUNCTIONS"""
        def Add_item_button(c_frame,x_row,y_colum,z_padx,c_pady):
            add_stuff=ct.CTkButton(c_frame,text=" +1 ",font=('arial', 25, 'bold'),width=20,height=15,corner_radius=60).grid(row=x_row,column=y_colum,padx=z_padx,pady=c_pady)
        def Delete_item_button(c_frame,x_row,y_colum,z_padx,c_pady):
            remove_stuff=ct.CTkButton(c_frame,text=" -1 ",font=('arial', 25, 'bold'),width=20,height=15,corner_radius=60).grid(row=x_row,column=y_colum,padx=z_padx,pady=c_pady)
        
        extra_duplicate_frame(content_frame)
        home_page = ct.CTkFrame(content_frame)  
        home_page.pack(fill='both', expand=True)
        
        sub_frame_img_1 = ct.CTkFrame(home_page)
        sub_frame_img_1.grid(row=0, column=0, padx=35, pady=25)  # Adjust the row and column as needed
        # Load and display image 1
        my_image = ct.CTkImage(dark_image=Image.open("items_pics_png/shirt.png"), size=(225, 225))
        image1_label = ct.CTkLabel(sub_frame_img_1, image=my_image, text='')
        image1_label.pack(padx=2,pady=2)
        img_1_butt = ct.CTkButton(sub_frame_img_1, text="Name:  T-shirt\nColor:  Black\nCost:  Rs. 500/-\nStock:  2500\nType:  Cotton", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_1_butt.pack(fill='both',expand=True)

        # Load and display image 2
        sub_frame_img_2 = ct.CTkFrame(home_page)
        sub_frame_img_2.grid(row=0, column=50, padx=35, pady=25)
        my_image_2 = ct.CTkImage(dark_image=Image.open("items_pics_png/shirt_white.png"), size=(225, 225))
        image2_label = ct.CTkLabel(sub_frame_img_2, image=my_image_2, text='')
        image2_label.pack(padx=2,pady=2)
        img_2_butt = ct.CTkButton(sub_frame_img_2, text="Name:  T-shirt\nColor:  White\nCost:  Rs. 500/-\nStock:  2500\nType:  Cotton", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_2_butt.pack(fill='both',expand=True)  

        # Load and display image 3
        sub_frame_img_3 = ct.CTkFrame(home_page)
        sub_frame_img_3.grid(row=0, column=100, padx=35, pady=25)
        my_image_3 = ct.CTkImage(dark_image=Image.open("items_pics_png/tapper_jeans.png"), size=(225, 225))
        image3_label = ct.CTkLabel(sub_frame_img_3, image=my_image_3, text='')
        image3_label.pack(padx=2,pady=2)
        img_3_butt = ct.CTkButton(sub_frame_img_3, text="Name:  Tapper Jeans\nColor:  Black\nCost:  Rs. 5000/-\nStock:  1000\nType:  Denim", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_3_butt.pack(fill='both',expand=True)  
        
        # Load and display image 4
        sub_frame_img_4 = ct.CTkFrame(home_page)
        sub_frame_img_4.grid(row=0, column=150, padx=35, pady=25)
        my_image_4 = ct.CTkImage(dark_image=Image.open("items_pics_png/nike_air.png"), size=(225, 225))
        image4_label = ct.CTkLabel(sub_frame_img_4, image=my_image_4, text='')
        image4_label.pack(padx=2,pady=2)
        img_4_butt = ct.CTkButton(sub_frame_img_4, text="Name:  Air Jordans\nColor:  White\nCost:  Rs. 20,000/-\nStock:  500\nType:  Shoes", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_4_butt.pack(fill='both',expand=True) 

    # Load and display image 5
        sub_frame_img_5 = ct.CTkFrame(home_page)
        sub_frame_img_5.grid(row=0, column=200, padx=35, pady=25)
        my_image_5 = ct.CTkImage(dark_image=Image.open("items_pics_png/white_jordans.png"), size=(225, 225))
        image5_label = ct.CTkLabel(sub_frame_img_5, image=my_image_5, text='')
        image5_label.pack(padx=2,pady=2)
        img_5_butt = ct.CTkButton(sub_frame_img_5, text="Name:  Nike Jordans\nColor:  White\nCost:  Rs. 20,000/-\nStock:  1000\nType:  Shoe", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_5_butt.pack(fill='both',expand=True) 
    
    # Load and display image 6
        sub_frame_img_6 = ct.CTkFrame(home_page)
        sub_frame_img_6.grid(row=50, column=0, padx=35, pady=10)
        my_image_6 = ct.CTkImage(dark_image=Image.open("items_pics_png/out_bag.png"), size=(225, 225))
        image6_label = ct.CTkLabel(sub_frame_img_6, image=my_image_6, text='')
        image6_label.pack(padx=2,pady=2)
        img_6_butt = ct.CTkButton(sub_frame_img_6, text="Name:  Handcarry Bag\nColor:  Orange\nCost:  Rs. 5000/-\nStock:  1000\nType:  Cloth", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_6_butt.pack(fill='both',expand=True) 

    # Load and display image 7
        sub_frame_img_7 = ct.CTkFrame(home_page)
        sub_frame_img_7.grid(row=50, column=50, padx=35, pady=10)
        my_image_7 = ct.CTkImage(dark_image=Image.open("items_pics_png/jacket_hooded.png"), size=(225, 225))
        image7_label = ct.CTkLabel(sub_frame_img_7, image=my_image_7, text='')
        image7_label.pack(padx=2,pady=2)
        img_7_butt = ct.CTkButton(sub_frame_img_7, text="Name:  Hooded Jacket\nColor:  Black\nCost:  Rs. 7500/-\nStock:  1000\nType:  Leather", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_7_butt.pack(fill='both',expand=True) 

    # Load and display image 8
        sub_frame_img_8 = ct.CTkFrame(home_page)
        sub_frame_img_8.grid(row=50, column=100, padx=35, pady=10)
        my_image_8 = ct.CTkImage(dark_image=Image.open("items_pics_png/hoodie_batch.png"), size=(225, 225))
        image8_label = ct.CTkLabel(sub_frame_img_8, image=my_image_8, text='')
        image8_label.pack(padx=2,pady=2)
        img_8_butt = ct.CTkButton(sub_frame_img_8, text="Name:  Batch Hoodie\nColor:  Biege\nCost:  Rs. 4000/-\nStock:  2000\nType:  Furr", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_8_butt.pack(fill='both',expand=True) 

    # Load and display image 9
        sub_frame_img_9 = ct.CTkFrame(home_page)
        sub_frame_img_9.grid(row=50, column=150, padx=35, pady=10)
        my_image_9 = ct.CTkImage(dark_image=Image.open("items_pics_png/gucci_fitness_bag.png"), size=(225, 225))
        image9_label = ct.CTkLabel(sub_frame_img_9, image=my_image_3, text='')
        image9_label.pack(padx=2,pady=2)
        img_9_butt = ct.CTkButton(sub_frame_img_9, text="Name:  Fittness Bag\nColor:  Black\nCost:  Rs. 40,000/-\nStock:  200\nType:  Denim", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_9_butt.pack(fill='both',expand=True) 

    # Load and display image 10
        sub_frame_img_10 = ct.CTkFrame(home_page)
        sub_frame_img_10.grid(row=50, column=200, padx=35, pady=10)
        my_image_10 = ct.CTkImage(dark_image=Image.open("items_pics_png/gucci_cap.png"), size=(225, 225))
        image10_label = ct.CTkLabel(sub_frame_img_10, image=my_image_10, text='')
        image10_label.pack(padx=2,pady=2)
        img_10_butt = ct.CTkButton(sub_frame_img_10, text="Name:  Cap\nColor:  Black\nCost:  Rs. 5000/-\nStock:  1000\nType:  Leather", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_10_butt.pack(fill='both',expand=True) 
    
    # Load and display image 11
        sub_frame_img_11 = ct.CTkFrame(home_page)
        sub_frame_img_11.grid(row=100, column=0, padx=35, pady=10)
        my_image_11 = ct.CTkImage(dark_image=Image.open("items_pics_png/lv_handbag.png"), size=(225, 225))
        image11_label = ct.CTkLabel(sub_frame_img_11, image=my_image_11, text='')
        image11_label.pack(padx=2,pady=2)
        img_11_butt = ct.CTkButton(sub_frame_img_11, text="Name:  LV Hand-Bag\nColor:  Brown\nCost:  Rs. 50,000/-\nStock:  1000\nType:  Denim", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_11_butt.pack(fill='both',expand=True) 

    # Load and display image 12
        sub_frame_img_12 = ct.CTkFrame(home_page)
        sub_frame_img_12.grid(row=100, column=50, padx=35, pady=10)
        my_image_12 = ct.CTkImage(dark_image=Image.open("items_pics_png/dior_sauvage.png"), size=(225, 225))
        image12_label = ct.CTkLabel(sub_frame_img_12, image=my_image_12, text='')
        image12_label.pack(padx=2,pady=2)
        img_12_butt = ct.CTkButton(sub_frame_img_12, text="Name:  Dior Sauvage\nColor:  Blue\nCost:  Rs. 250,000/-\nStock:  1000\nType:  Perfume", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_12_butt.pack(fill='both',expand=True) 

    # Load and display image 13
        sub_frame_img_13 = ct.CTkFrame(home_page)
        sub_frame_img_13.grid(row=100, column=100, padx=35, pady=10)
        my_image_13 = ct.CTkImage(dark_image=Image.open("items_pics_png/dior_homme.png"), size=(225, 225))
        image13_label = ct.CTkLabel(sub_frame_img_13, image=my_image_13, text='')
        image13_label.pack(padx=2,pady=2)
        img_13_butt = ct.CTkButton(sub_frame_img_13, text="Name:  Dior Haumme\nColor:  Batch\nCost:  Rs. 250,000/-\nStock:  1000\nType:  Perfume", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_13_butt.pack(fill='both',expand=True) 

    # Load and display image 14
        sub_frame_img_14 = ct.CTkFrame(home_page)
        sub_frame_img_14.grid(row=100, column=150, padx=35, pady=10)
        my_image_14 = ct.CTkImage(dark_image=Image.open("items_pics_png/R.png"), size=(225, 225))
        image14_label = ct.CTkLabel(sub_frame_img_14, image=my_image_14, text='')
        image14_label.pack(padx=2,pady=2)
        img_14_butt = ct.CTkButton(sub_frame_img_14, text="Name:  Vincerro Watch\nColor:  Brown\nCost:  Rs. 100,000/-\nStock:  1000\nType:  Watch", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_14_butt.pack(fill='both',expand=True) 

    # Load and display image 15
        sub_frame_img_15 = ct.CTkFrame(home_page)
        sub_frame_img_15.grid(row=100, column=200, padx=35, pady=10)
        my_image_15 = ct.CTkImage(dark_image=Image.open("items_pics_png/OIP.png"), size=(225, 225))
        image15_label = ct.CTkLabel(sub_frame_img_15, image=my_image_15, text='')
        image15_label.pack(padx=2,pady=2)
        img_15_butt = ct.CTkButton(sub_frame_img_15, text="Name:  Breffling Watch\nColor:  Brown\nCost:  Rs. 150,000/-\nStock:  1000\nType:  Watch", font=('arial', 19),hover_color='#292929',fg_color='black',bg_color='transparent')
        img_15_butt.pack(fill='both',expand=True) 
    
    def cart_page_(content_frame):
        extra_duplicate_frame(content_frame)
        cart_page=ct.CTkFrame(content_frame)
        cart_page.pack(fill='both',expand=True)
        first_cart_label=ct.CTkLabel(cart_page,text="Welcome to cart page",font=('calibri', 40, 'bold'), text_color='grey').pack(pady=20)
    
    def shop_hist_page_(content_frame):
        extra_duplicate_frame(content_frame)
        shop_h_page = ct.CTkFrame(content_frame)
        shop_h_page.pack(fill='both', expand=True)
        label = ct.CTkLabel(shop_h_page, text="Welcome to Shopping History page", font=('calibri', 40, 'bold'), text_color='grey').pack(pady=20)

    def contact_page_(content_frame):
        extra_duplicate_frame(content_frame)
        contact_page = ct.CTkFrame(content_frame)
        contact_page.pack(fill='both', expand=True,padx=75,pady=75)  # Corrected the pack method invocation
        label_2_ = ct.CTkLabel(contact_page, text="Contact Information:\nAddress:\t123 Main Street Cityville, State, Zip Code\nPhone:\t+1 (123) 456-7890\nEmail:\tinfo@example.com\nSocial Media:\nFacebook:\txxxxxxxxxxxx\nTwitter:\txxxxxxxxxx\nInstagram:\txxxxxxxxxx\n\nFeel free to reach out to us via phone, email, or through our social media.\nWe look forward to hearing from you!", font=('roboto', 35, 'bold'),text_color='white').pack(padx=10,pady=10)

    frame_wrapper(main_task_page_content)
user_data=[]
# Call the welcome_page function to display the welcome page
welcome_page()

# Run the main loop
r.mainloop()
