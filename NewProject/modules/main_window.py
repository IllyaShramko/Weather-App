import os , customtkinter, sqlite3, time
from PIL import Image
import modules.font as m_font
import modules.api as m_api


def main_waether():

    data = m_api.get_data_weth()['weather'][0]['main']

    if data == "Clouds":
        text_weath = "Хмарно"
    elif data == "Snow":
        text_weath = "Сніжно"
    elif data == "Rain":
        text_weath = "Дощ"
    elif data == "Mist":
        text_weath = "Туман"
    elif data == "Clear":
        text_weath = "Ясно"
    return text_weath

def app_main():
    global main_scr
    main_scr = customtkinter.CTkToplevel()
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
        m_cab.cabinet_scr = customtkinter.CTk()
        m_cab.cabinet_scr.geometry("460x645")
        m_cab.cabinet_scr.config(bg="#5DA7B1")
        m_cab.cabinet_scr.resizable(False, False)
        m_cab.create_win_cabinka()
        m_cab.cabinet_scr.mainloop()


    go_cabinka = customtkinter.CTkButton(
        master= main_scr,
        width= 0,
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

    time22 = customtkinter.CTkLabel(
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
    fram3 = customtkinter.CTkButton(
        master = main_scr,
        text = "",
        width = 818,
        height = 240,
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        border_width = 5,
        border_color = "#FFFFFF",
        corner_radius= 20,
        hover = False
    )
    fram3.place(x = 325, y = 430)

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

    name = str(get_value(cursor= cursor, name_table= "Signed", name_column= "name"))

    surname = str(get_value(cursor= cursor, name_table= "Signed", name_column= "lastname"))

    name_and_surname_text = f"{name} {surname}"

    name_and_surname = customtkinter.CTkButton(
        master= main_scr,
        height= 31,
        text= name_and_surname_text,
        text_color= "#FFFFFF",
        font=(m_font.font,14),
        fg_color= "#5DA7B1",
        bg_color= "#5DA7B1",
        command= go_to_toiletik
    )
    city_info = get_value(cursor, "Signed", "city")
    city_super = customtkinter.CTkLabel(
        master=main_scr,
        text=city_info,
        text_color="#FFFFFF",
        width=87,
        height=31,
        font=(m_font.font,22),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
    )
    gradus1 = customtkinter.CTkLabel(
        master = main_scr,
        text = m_api.temper(m_api.get_data_weth()["main"]['temp']) + "°",
        width = 79,
        height = 71,
        font = ("Inter Bold",80),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    
    day = customtkinter.CTkLabel(
        master= main_scr,
        text= "Понеділок",
        width= 105,
        height= 31,
        font= (m_font.font,18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )


    weather1 = customtkinter.CTkLabel(
        master= main_scr,
        text = main_waether(),
        width = 140,
        height = 31,
        font = (m_font.font,30),
        bg_color = "#5DA7B1",
        fg_color = "#5DA7B1",
        text_color = "#FFFFFF"
    )
    
    img1_1 = Image.open(os.path.abspath(__file__ + "/../../images/lata.png"))
    img1 = customtkinter.CTkImage(dark_image= img1_1, size= [171, 159])
    img1_lbl = customtkinter.CTkLabel(master= main_scr,width= 171,height=159,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img1)

    img2_1 = Image.open(os.path.abspath(__file__ + "/../../images/user.png"))
    img2_2 = customtkinter.CTkImage(dark_image= img2_1, size= [48.48, 50])
    img2_lbl = customtkinter.CTkLabel(master= main_scr,width= 48.48,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img2_2)



    img3_1 = Image.open(os.path.abspath(__file__ + "/../../images/lata.png"))
    img3_2 = customtkinter.CTkImage(dark_image= img3_1, size= [50, 52.08])
    img3_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=52.08,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img3_2)

    img4_1 = Image.open(os.path.abspath(__file__ + "/../../images/sun.png"))
    img4_2 = customtkinter.CTkImage(dark_image= img4_1, size= [54, 50])
    img4_lbl = customtkinter.CTkLabel(master= main_scr,width= 54,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img4_2)

    img5_1 = Image.open(os.path.abspath(__file__ + "/../../images/sun.png"))
    img5_2 = customtkinter.CTkImage(dark_image= img5_1, size= [54, 50])
    img5_lbl = customtkinter.CTkLabel(master= main_scr,width= 54,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img5_2)
    
    img6_1 = Image.open(os.path.abspath(__file__ + "/../../images/sun1.png"))
    img6_2 = customtkinter.CTkImage(dark_image= img6_1, size= [50, 50])
    img6_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img6_2)

    img7_1 = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
    img7_2 = customtkinter.CTkImage(dark_image= img7_1, size= [50, 50])
    img7_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img7_2)

    img8_1 = Image.open(os.path.abspath(__file__ + "/../../images/night.png"))
    img8_2 = customtkinter.CTkImage(dark_image= img8_1, size= [50, 50])
    img8_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img8_2)

    img9_1 = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
    img9_2 = customtkinter.CTkImage(dark_image= img9_1, size= [50, 50])
    img9_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img9_2)

    img10_1 = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
    img10_2 = customtkinter.CTkImage(dark_image= img10_1, size= [50, 50])
    img10_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img10_2)

    img11_1 = Image.open(os.path.abspath(__file__ + "/../../images/rain.png"))
    img11_2 = customtkinter.CTkImage(dark_image= img11_1, size= [50, 50])
    img11_lbl = customtkinter.CTkLabel(master= main_scr,width= 50,height=50,fg_color = "#5DA7B1",bg_color= "#5DA7B1",text="",image= img11_2)


    gradus = customtkinter.CTkLabel(
        master = main_scr,
        text = m_api.temper(m_api.get_data_weth()["main"]['temp']) + "°",
        width = 41.02,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus2 = customtkinter.CTkLabel(
        master = main_scr,
        text = "12°",
        width = 45,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus3 = customtkinter.CTkLabel(
        master = main_scr,
        text = "10°",
        width = 48,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus4 = customtkinter.CTkLabel(
        master = main_scr,
        text = "9°",
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus5 = customtkinter.CTkLabel(
        master = main_scr,
        text = "8°",
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus6 = customtkinter.CTkLabel(
        master = main_scr,
        text = "8°",
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    gradus7= customtkinter.CTkLabel(
        master = main_scr,
        text = "7°",
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus8= customtkinter.CTkLabel(
        master = main_scr,
        text = "5°",
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )
    gradus9= customtkinter.CTkLabel(
        master = main_scr,
        text = "5°",
        width = 32.25,
        height = 30,
        font = ("Roboto Slab Bold", 30),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"  
    )

    time11 = customtkinter.CTkLabel(
        master = main_scr,
        text = "Зараз",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time2 = customtkinter.CTkLabel(
        master = main_scr,
        text = "15:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time3 = customtkinter.CTkLabel(
        master = main_scr,
        text = "16:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time4 = customtkinter.CTkLabel(
        master = main_scr,
        text = "16:05",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time5 = customtkinter.CTkLabel(
        master = main_scr,
        text = "17:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time6 = customtkinter.CTkLabel(
        master = main_scr,
        text = "18:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time7 = customtkinter.CTkLabel(
        master = main_scr,
        text = "19:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time8 = customtkinter.CTkLabel(
        master = main_scr,
        text = "20:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    time9 = customtkinter.CTkLabel(
        master = main_scr,
        text = "21:00",
        height = 31,
        font = ("Roboto Slab Bold", 18),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
        text_color = "#FFFFFF"
    )
    

    smaller = customtkinter.CTkLabel(
        master = main_scr,
        text = "<", 
        text_color = "#FFFFFF",
        height = 31,
        font = (m_font.font, 50),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
    )
    bigger = customtkinter.CTkLabel(
        master = main_scr,
        text = ">", 
        text_color = "#FFFFFF",
        height = 31,
        font = (m_font.font, 50),
        bg_color="#5DA7B1",
        fg_color="#5DA7B1",
    )

    search = customtkinter.CTkEntry(
        master = main_scr,
        width = 218,
        height = 46,
        # text = "пошук",
        # text_color = "#FFFFFF",
        font = (m_font.font, 18),
        bg_color ="#5DA7B1",
        fg_color ="#096C82",
        border_width = 3,
        corner_radius = 20,
        border_color = "#FFFFFF"      
    )


    search.place(x = 918, y = 31)
    smaller.place(x = 289, y = 524)
    bigger.place(x = 1160, y = 524)

    gradus.place(x = 351, y = 604)
    gradus2.place(x = 445, y = 604)
    gradus3.place(x = 534, y = 604)
    gradus4.place(x = 635, y = 604)
    gradus5.place(x = 731, y = 604)
    gradus6.place(x = 823, y = 604)
    gradus7.place(x = 915, y = 604)
    gradus8.place(x = 1007, y = 604)
    gradus9.place(x = 1099, y = 604)
    
    time11.place(x = 344,y = 485)
    time2.place(x = 441,y = 485)
    time3.place(x = 533,y = 485)
    time4.place(x = 625,y = 485)
    time5.place(x = 717,y = 485)
    time6.place(x = 809,y = 485)
    time7.place(x = 901,y = 485)
    time8.place(x = 993,y = 485)
    time9.place(x = 1085,y = 485)
    
    img3_lbl.place(x = 344, y = 534)
    img4_lbl.place(x = 437, y = 534)
    img5_lbl.place(x = 523, y = 534)
    img6_lbl.place(x = 621, y = 534)
    img7_lbl.place(x = 713, y = 534)
    img8_lbl.place(x = 805, y = 534)
    img9_lbl.place(x = 897, y = 534)
    img10_lbl.place(x = 989, y = 534)
    img11_lbl.place(x = 1081, y = 534)

    # name_and_surname.place(x = 380, y = 39)

    img2_lbl.place(x = 318, y= 29)
    img1_lbl.place(x= 380, y= 171)
    weather1.place(x=663, y= 284)
    day.place(x= 956, y= 191)
    gradus1.place(x = 683, y = 203)
    city_super.place(x = 689, y = 162)
    go_cabinka.place(x= 380,y= 39)
    left_widget.place(x = 0, y = 0)
    where.place(x = 576, y = 101)
    time22.place(x = 974, y = 274)
    date.place(x = 920, y = 227)
# app_main()