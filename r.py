from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import tkinter
from PIL import Image, ImageDraw, ImageFont,ImageTk
import os
from datetime import date
from datetime import datetime
import datetime

screen = Tk()
screen.geometry("500x600")
screen.title("PAGE Bill Generator")
screen.iconbitmap('.\\res\\icon.ico')
bg=ImageTk.PhotoImage(file=".\\res\\screen.png")
bglabel= Label(screen,image=bg)
bglabel.place(x=0,y=0,relwidth=1,relheight=1)

my_canvas = Canvas(screen, width=1200, height=1200)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0,0, image=bg, anchor="nw")

def resizer(e):
	global bg1, resized_bg, new_bg
	# Open our image
	bg1 = Image.open(".\\res\\screen.png")
	# Resize the image
	resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
	# Define our image again
	new_bg = ImageTk.PhotoImage(resized_bg)
	# Add it back to the canvas
	my_canvas.create_image(0,0, image=new_bg, anchor="nw")
	# Readd the text

def delete():
    screen1.destroy()



def error():
    global screen1
    
    screen1 = Toplevel(screen)
    screen1.geometry("200x90")
    screen1.title("Warning!")
    Label(screen1, text = "All fields required", fg = "red").pack()
    Button(screen1, text = "OK", command = delete).pack()

def error2():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("200x90")
    screen1.title("Warning!")
    Label(screen1, text = "You have added maximum data", fg = "red").pack()
    Button(screen1, text = "OK", command = delete).pack()

def added():
            global screen1
            screen1 = Toplevel(screen)
            screen1.geometry("200x90")
            screen1.title("Success!")
            Label(screen1, text = "Data Added", fg = "green").pack()
            Button(screen1, text = "OK", command = delete).pack()

img = Image.open('.\\res\\img.jpg')
docname="aa"
count=0
grandtotal=0

def check():
    print("ex")
    name_text = name.get()
    # global item
    item_text = item.get()
    price_text = price.get()
    qty_text = qty.get()
    global docname 
    docname = name_text
    # today = date.today()
    now = datetime.datetime.now()
    today = now.strftime("%d/%m/%Y")
    today=str(today)
    
	
    if name_text == "" or item_text=="" or price_text=="" or qty_text=="":        
        error()
    else:
        fontname = ImageFont.truetype('.\\res\\HelveticaNeueLTPro-BdCn.otf',50)
        font = ImageFont.truetype('.\\res\\HelveticaNeueLTPro-LtCn.otf',48)
        datefont = ImageFont.truetype('.\\res\\HelveticaNeueLTPro-LtCn.otf',44)
        rupeefont = ImageFont.truetype('.\\res\\MyriadPro-Regular.otf',44)
        global img
        global count
        if count ==0:
            draw1 = ImageDraw.Draw(img)
            draw1.text(xy=(408,997),text=name_text,fill=(0,0,0),font=fontname,)
            draw1.text(xy=(415,1596),text=item_text,fill=(0,0,0),font=font,)
            draw1.text(xy=(1779,1596),text=price_text,fill=(0,0,0),font=font,)
            draw1.text(xy=(1543,1596),text=qty_text,fill=(0,0,0),font=font,)
            draw1.text(xy=(1834,706),text=today,fill=(0,0,0),font=datefont,)
            
            total1=(int(qty_text)*int(price_text))
            global grandtotal
            grandtotal=grandtotal+total1
            b=str(total1)

            draw1.text(xy=(2048,1596),text=b,fill=(0,0,0),font=font,)
            added()
                  
        if count==1:
            item_text = item.get()
            draw2 = ImageDraw.Draw(img)
            draw2.text(xy=(415,1748),text=item_text,fill=(0,0,0),font=font,)
            draw2.text(xy=(1722,1750),text="₹",fill=(0,0,0),font=rupeefont,)
            draw2.text(xy=(1779,1748),text=price_text,fill=(0,0,0),font=font,)
            draw2.text(xy=(1543,1748),text=qty_text,fill=(0,0,0),font=font,)
            total2=(int(qty_text)*int(price_text))
            grandtotal=grandtotal+total2
            
            c=str(total2)
            draw2.text(xy=(2008,1750),text="₹",fill=(0,0,0),font=rupeefont,)
            draw2.text(xy=(2048,1748),text=c,fill=(0,0,0),font=font,)
            added()
        
        if count==2:
            item_text = item.get()
            draw2 = ImageDraw.Draw(img)
            draw2.text(xy=(415,1900),text=item_text,fill=(0,0,0),font=font,)
            draw2.text(xy=(1722,1902),text="₹",fill=(0,0,0),font=rupeefont,)
            draw2.text(xy=(1779,1900),text=price_text,fill=(0,0,0),font=font,)
            draw2.text(xy=(1543,1900),text=qty_text,fill=(0,0,0),font=font,)
            total3=(int(qty_text)*int(price_text))
            grandtotal=grandtotal+total3
            
            d=str(total3)
            draw2.text(xy=(2008,1902),text="₹",fill=(0,0,0),font=rupeefont,)
            draw2.text(xy=(2048,1900),text=d,fill=(0,0,0),font=font,)
            added()
        
        if count>2:
            error2()
        
    return
       
        
        
def register():
    global img
    global docname
    draw = ImageDraw.Draw(img)
    img2 = Image.open('.\\res\\cut.jpg')
    img.paste(img2,(2040,2475))

    gfont = ImageFont.truetype('.\\res\\HelveticaNeueLTPro-LtCn.otf',56)
    e=str(grandtotal)
    draw.text(xy=(2057,2538),text=e,fill=(0,0,0),font=gfont,)
    img.show()
    # desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    # print(desktop)
    path="D:\\"+docname+".pdf"
    print(path)
    img.save(path, "PDF")
    print(docname)
    
    # text = Entry(screen, font=('TimesNewRoman',20))
    # button = Button(screen,text='Save as',font=(r'C:\Users\user\Documents\python\bill\r\HelveticaNeueLTPro-Th.otf',10), width=30,bd=10)
    # button.pack(side=BOTTOM)           
   

heading = Label(text = "PAGE", fg = "black", bg = "grey", width = "500", height = "3").pack()

Label(text = "NAME of Buyer :",bg="#271c3a",foreground="white",font=("Dosis",16)).place(x = 25, y = 30)
Label(text = "ITEM Purchased:",bg="#271c3a",foreground="white",font=("Dosis",16)).place(x = 25, y = 110)
Label(text = "PRICE of Item:",bg="#271c3a",foreground="white",font=("Dosis",16)).place(x = 25, y = 190)
Label(text = "QUANTITY of Item:",bg="#271c3a",foreground="white",font=("Dosis",16)).place(x = 25, y = 270)

name = StringVar()
item = StringVar()
price=StringVar()
qty=StringVar()

Entry(screen,bg="yellow", textvariable = name).place(x = 28, y = 68)
Entry(screen,bg="yellow", textvariable = item).place(x = 28, y = 145)
Entry(screen, bg="yellow",textvariable = price).place(x = 28, y = 225)
Entry(screen,bg="yellow", textvariable = qty).place(x = 28, y = 305)

def clear():  
    item.set("")
    price.set("")
    qty.set("")
    global count
    count=count+1
    return

Button(screen, text = "ADD Data",font=("Dosis",12),width = "6",height="1",bg = "#c6c6c7", command =lambda:[check(),clear()] ).place(x = 220, y = 345)

Button(screen, text = "GENERATE Bill",font=("Dosis",12), width = "45", bg = "#c6c6c7", command = register,).place(x = 45, y = 410)
screen.bind('<Configure>', resizer)
screen.mainloop()
