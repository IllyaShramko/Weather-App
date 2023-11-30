import os, sqlite3, customtkinter

import modules.font as m_font
sign_up_scr = customtkinter.CTk()
sign_up_scr.geometry("460x645")
sign_up_scr.config(bg="#5DA7B1")
sign_up_scr.resizable(False, False)

path = os.path.abspath(__file__ + "/../database")
os.chdir(path)
connect = sqlite3.connect("databas31.db")
cursor = connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Signed (id, INTEGER PRIMARY KEY)")
try:
    cursor.execute("ALTER TABLE Signed ADD COLUMN signid BOOLEAN")
except:
    pass

def get_value(cursor: object, name_table: str, name_column: str):
    cursor.execute(f"SELECT {name_column} FROM {name_table}")
    return cursor.fetchall()


text_for_header = "Реєстрація Користувача"
text_for_button = "Зберегти"



fontr = m_font.font

if bool(get_value(cursor, "Signed", "signid")) == True:
    sign_up_scr.destroy()
    import modules.cabinet as m_cabinka
    m_cabinka.cabinet_scr.mainloop()

country_text = customtkinter.CTkLabel(
    master= sign_up_scr,
    width= 87,
    height= 31,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Країна:",
    text_color="#FFFFFF",
    font=(fontr, 22)
)
city_text = customtkinter.CTkLabel(
    master= sign_up_scr,
    width= 87,
    height= 31,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Місто:",
    text_color="#FFFFFF",
    font=(fontr, 22)
)
name_text = customtkinter.CTkLabel(
    master= sign_up_scr,
    width= 87,
    height= 31,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Ім'я:",
    text_color="#FFFFFF",
    font=(fontr, 22)
)
lastname_text = customtkinter.CTkLabel(

    master= sign_up_scr,
    width= 121,
    height= 31,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Призвіще:",
    text_color="#FFFFFF",
    font=(fontr, 22)
)

def commandbutton():
    cursor.execute("ALTER TABLE Signed ADD COLUMN country TEXT")

    cursor.execute("ALTER TABLE Signed ADD COLUMN city TEXT")
    
    cursor.execute("ALTER TABLE Signed ADD COLUMN name TEXT")
    
    cursor.execute("ALTER TABLE Signed ADD COLUMN lastname TEXT")

    cursor.execute(f"INSERT INTO Signed (country, city, name, lastname, signid) VALUES (?, ?, ?, ?, ?)", (country_entry.get(), city_entry.get(), name_entry.get(), lastname_entry.get(), True))

    connect.commit()
    connect.close()

    sign_up_scr.destroy()
    import modules.cabinet as m_cabinka
    m_cabinka.cabinet_scr.mainloop()
    


# d = commandbutton
# d()

header_text = customtkinter.CTkLabel(
master= sign_up_scr,
width= 380,
height= 55,
fg_color= "#5DA7B1",
bg_color= "#5DA7B1",
text="Реєстрація користувача",
text_color= "#FFFFFF",
font=(fontr, 28)
)

button_save = customtkinter.CTkButton(
master= sign_up_scr,
width= 218,
height=46,
fg_color="#096C82",
bg_color="#5DA7B1",
border_width=3,
border_color="#FFFFFF",
text= "Зберегти",
text_color="#FFFFFF",
font=(fontr, 18),
corner_radius=20,
command=commandbutton
)
country_entry = customtkinter.CTkEntry(
    master= sign_up_scr,
    width= 218,
    height= 46,
    fg_color= "#096C82",
    bg_color="#5DA7B1",
    border_color= "#FFFFFF",
    border_width= 3,
    corner_radius= 20,
    font = (fontr, 22),
    text_color="#FFFFFF"
)
city_entry = customtkinter.CTkEntry(
    master= sign_up_scr,
    width= 218,
    height= 46,
    fg_color= "#096C82",
    bg_color="#5DA7B1",
    border_color= "#FFFFFF",
    border_width= 3,
    corner_radius= 20,
    font = (fontr, 22),
    text_color="#FFFFFF"
)
name_entry = customtkinter.CTkEntry(
    master= sign_up_scr,
    width= 295,
    height= 46,
    fg_color= "#096C82",
    bg_color="#5DA7B1",
    border_color= "#FFFFFF",
    border_width= 3,
    corner_radius= 20,
    font = (fontr, 22),
    text_color="#FFFFFF"
)
lastname_entry = customtkinter.CTkEntry(
    master= sign_up_scr,
    width= 295,
    height= 46,
    fg_color= "#096C82",
    bg_color="#5DA7B1",
    border_color= "#FFFFFF",
    border_width= 3,
    corner_radius= 20,
    font = (fontr, 22),
    text_color="#FFFFFF"
)
country_text.place(x=46,y=108)
city_text.place(x=46,y=207)
name_text.place(x=46,y=306)
lastname_text.place(x=46,y=405)
header_text.place(x=38, y=42)
country_entry.place(x=38,y=150)
city_entry.place(x=38,y=249)
name_entry.place(x=38,y=348)
lastname_entry.place(x=38,y=447)
button_save.place(x=119, y=546)

# def commandbuttonleft():
#     connect1 = sqlite3.connect("databas31.db")
#     cursor1 = connect1.cursor()
#     cursor1.execute(f"INSERT INTO Signed (country, city, name, lastname, signid) VALUES (?, ?, ?, ?, ?)", (None, None, None, None, False))
#     connect1.commit()
#     connect1.close()
# button_left_of_acc = customtkinter.CTkButton(
#     master= sign_up_scr,
#     width= 36,
#     height= 13,
#     hover= False,
#     fg_color="#5DA7B1",
#     bg_color= "#5DA7B1",
#     text="Вихід",
#     text_color="#FFFFFF",
#     font= (fontr, 12)
#     # command= commandbuttonleft
# )
# header_text = customtkinter.CTkLabel(
# master= sign_up_scr,
# width= 380,
# height= 55,
# fg_color= "#5DA7B1",
# bg_color= "#5DA7B1",
# text="Особистий кабінет",
# text_color= "#FFFFFF",
# font=(fontr, 28)
# )

# button_save = customtkinter.CTkButton(
# master= sign_up_scr,
# width= 218,
# height=46,
# fg_color="#096C82",
# bg_color="#5DA7B1",
# border_width=3,
# border_color="#FFFFFF",
# text= "Перейти до додатку",
# text_color="#FFFFFF",
# font=(fontr, 18),
# corner_radius=20,
# command=commandbutton
# )

# country_info = get_value(cursor, "Signed", "country")
# city_info = get_value(cursor, "Signed", "city")
# name_info =  get_value(cursor, "Signed", "name")
# last_name_info = get_value(cursor, "Signed", "lastname")

# country_info_text =customtkinter.CTkLabel(
#     master= sign_up_scr,
#     width= 196,
#     height= 31,
#     fg_color="#5DA7B1",
#     bg_color= "#5DA7B1",
#     text_color="#FFFFFF",
#     text=country_info,
#     font= (fontr, 28)
# )
# city_info_text = customtkinter.CTkLabel(
#     master= sign_up_scr,
#     width= 196,
#     height= 31,
#     fg_color="#5DA7B1",
#     bg_color= "#5DA7B1",
#     text_color="#FFFFFF",
#     text=city_info,
#     font= (fontr, 28)
# )
# name_info_text = customtkinter.CTkLabel(
#     master= sign_up_scr,
#     width= 196,
#     height= 31,
#     fg_color="#5DA7B1",
#     bg_color= "#5DA7B1",
#     text_color="#FFFFFF",
#     text=name_info,
#     font= (fontr, 28)
# )
# last_name_info_text = customtkinter.CTkLabel(
#     master= sign_up_scr,
#     width= 196,
#     height= 31,
#     fg_color="#5DA7B1",
#     bg_color= "#5DA7B1",
#     text_color="#FFFFFF",
#     text=last_name_info,
#     font= (fontr, 28)
# )

# country_text.place(x=46,y=108)
# city_text.place(x=46,y=207)
# name_text.place(x=46,y=306)
# lastname_text.place(x=46,y=405)
# country_info_text.place(x=119,y=157)
# city_info_text.place(x=121,y=256)
# name_info_text.place(x=121,y=352)
# last_name_info_text.place(x=119,y=455)
# button_left_of_acc.place(x=370 ,y=26)
# text_for_header = "Особистий кабінет"
# header_text.place(x=38, y=42)

# text_for_button = "Перейти до додатку"
# button_save.place(x=119, y=546)