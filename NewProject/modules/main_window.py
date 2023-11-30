import os , customtkinter, sqlite3, time
import modules.font as m_font
from PIL import Image

main_scr = customtkinter.CTk()
main_scr.geometry("1200x800")
main_scr.config(bg="#5DA7B1")
main_scr.resizable(False, False)

today = time.localtime()

text_for_date = f"{today.tm_mday}.{today.tm_mon}.{today.tm_year}"
print(today)

text_time = f"{today.tm_hour}:{today.tm_min}"

def go_to_toiletik():
    main_scr.destroy()
    import modules.cabinet as m_cab
    m_cab.cabinet_scr.mainloop()


go_cabinka = customtkinter.CTkButton(
    master= main_scr,
    width= 220,
    height= 31,
    fg_color="#5DA7B1",
    bg_color="#5DA7B1",
    font= (m_font.font, 14),
    hover= False,
    border_width=0,
    command=go_to_toiletik,
    text= "Особистий Кабінет",
    text_color= "#FFFFFF"
)

locate = customtkinter.CTkLabel(
    master= main_scr,
    width= 87,
    height= 31,
    text= "Dnipro",
    text_color= "#FFFFFF",
    font= (m_font.font,22),
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1"
)

temp = customtkinter.CTkLabel(
    master= main_scr,
    width= 79,
    height= 71,
    text= "11",
    text_color= "#FFFFFF",
    font= (m_font.font, 80),
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1" 
)

date = customtkinter.CTkLabel(
    master= main_scr,
    width= 160,
    height= 47,
    text= text_for_date,
    text_color= "#FFFFFF",
    font= (m_font.font,40),
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1"     
)

time2 = customtkinter.CTkLabel(
    master= main_scr,
    width= 70,
    height= 47,
    text= text_time,
    text_color= "#FFFFFF",
    font= (m_font.font,30),
    fg_color="#5DA7B1",
    bg_color="#5DA7B1"
)

where = customtkinter.CTkLabel(
    master= main_scr,
    width= 214,
    height= 61,
    text= "Поточна позиція",
    text_color= "#FFFFFF",
    font=(m_font.font,35),
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1"
)

left_widget = customtkinter.CTkButton(
    master= main_scr,
    width= 275,
    height= 800,
    fg_color="#096C82",
    bg_color="#5DA7B1",
    border_width=3,
    border_color="#FFFFFF",
    text= " ",
    hover= False
)

path = os.path.abspath(__file__ + "/../database")
os.chdir(path)
connect = sqlite3.connect("databas31.db")
cursor = connect.cursor()

def get_value(cursor: object, name_table: str, name_column: str):
    cursor.execute(f"SELECT {name_column} FROM {name_table}")
    return cursor.fetchall()

# name = get_value(cursor= cursor, name_table= "Signed", name_column= "name")

# surname = get_value(cursor= cursor, name_table= "Signed", name_column= "lastname")

# name_and_surname_text = f"{name} {surname}"

name_and_surname = customtkinter.CTkLabel(
    master= main_scr,
    width= 220,
    height= 31,
    text= "name_and_surname_text",
    text_color= "#FFFFFF",
    font=(m_font.font,14),
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1"
)

go_cabinka.place(x= 380,y= 39)
# name_and_surname.place(x = 380, y = 39)
left_widget.place(x = 0, y = 0)
where.place(x = 576, y = 101)
time2.place(x = 974, y = 274)
date.place(x = 920, y = 227)