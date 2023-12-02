import os, sqlite3, customtkinter
import modules.main_window as main_app

# cab_scr = None

cabinet_scr = customtkinter.CTk()
cabinet_scr.geometry("460x645")
cabinet_scr.config(bg="#5DA7B1")
cabinet_scr.resizable(False, False)

def create_win_cabinka():

    path = os.path.abspath(__file__ + "/../database")
    os.chdir(path)
    connect = sqlite3.connect("databas31.db")
    cursor = connect.cursor()

    def get_value(cursor: object, name_table: str, name_column: str):
        try:
            cursor.execute(f"SELECT {name_column} FROM {name_table}")
            return cursor.fetchall()
        except:
            print("Error Epta")

    fontr = 'Roboto Slab Bold'

    country_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Країна:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    city_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Місто:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    name_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 87,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Ім'я:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )
    lastname_text = customtkinter.CTkLabel(

        master= cabinet_scr,
        width= 121,
        height= 31,
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        text="Призвіще:",
        text_color="#FFFFFF",
        font=(fontr, 22)
    )

    country_info = get_value(cursor, "Signed", "country")
    city_info = get_value(cursor, "Signed", "city")
    name_info =  get_value(cursor, "Signed", "name")
    last_name_info = get_value(cursor, "Signed", "lastname")
        
    country_info_text =customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=country_info,
        font= (fontr, 28)
    )
    city_info_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=city_info,
        font= (fontr, 28)
    )
    name_info_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=name_info,
        font= (fontr, 28)
    )
    last_name_info_text = customtkinter.CTkLabel(
        master= cabinet_scr,
        width= 196,
        height= 31,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text_color="#FFFFFF",
        text=last_name_info,
        font= (fontr, 28)
    )

    def commandbuttonleft():
        try:
            cursor.execute("ALTER TABLE Signed DROP COLUMN country")
            cursor.execute("ALTER TABLE Signed DROP COLUMN city")
            cursor.execute("ALTER TABLE Signed DROP COLUMN name")
            cursor.execute("ALTER TABLE Signed DROP COLUMN lastname")
            cursor.execute("ALTER TABLE Signed DROP COLUMN signid")
        except:
            print("errororor")
        import modules.sign_up as m_sign
        m_sign.sign_up_scr = customtkinter.CTk()
        m_sign.sign_up_scr.geometry("460x645")
        m_sign.sign_up_scr.config(bg="#5DA7B1")
        m_sign.sign_up_scr.resizable(False, False)
        m_sign.app_reg()
        m_sign.sign_up_scr.mainloop()
    button_left_of_acc = customtkinter.CTkButton(
        master= cabinet_scr,
        width= 36,
        height= 13,
        hover= False,
        fg_color="#5DA7B1",
        bg_color= "#5DA7B1",
        text="Вихід",
        text_color="#FFFFFF",
        font= (fontr, 12),
        # command= commandbuttonleft
    )
    header_text = customtkinter.CTkLabel(
    master= cabinet_scr,
    width= 380,
    height= 55,
    fg_color= "#5DA7B1",
    bg_color= "#5DA7B1",
    text="Особистий кабінет",
    text_color= "#FFFFFF",
    font=(fontr, 28)
    )

    def go_app():
        cabinet_scr.destroy()
        main_app.main_scr = customtkinter.CTk()
        main_app.main_scr.geometry("1200x800")
        main_app.main_scr.config(bg="#5DA7B1")
        main_app.main_scr.resizable(False, False)
        main_app.app_main()
        main_app.main_scr.mainloop()

    button_go_app = customtkinter.CTkButton(
    master= cabinet_scr,
    width= 218,
    height=46,
    fg_color="#096C82",
    bg_color="#5DA7B1",
    border_width=3,
    border_color="#FFFFFF",
    text= "Перейти до додатку",
    text_color="#FFFFFF",
    font=(fontr, 18),
    corner_radius=20,
    command=go_app
    )

    country_text.place(x=46,y=108)
    city_text.place(x=46,y=207)
    name_text.place(x=46,y=306)
    lastname_text.place(x=46,y=405)
    country_info_text.place(x=119,y=157)
    city_info_text.place(x=121,y=256)
    name_info_text.place(x=121,y=352)
    last_name_info_text.place(x=119,y=455)

    header_text.place(x=38, y=42)
    button_left_of_acc.place(x=370 ,y=26)
    # text_for_button = "Перейти до додатку"
    button_go_app.place(x=119, y=546)
create_win_cabinka()
