# Hotel-Management
Using GUI interface from library tkinter created a software for adding the content ordered by the customer providing the total and a inbuilt caluculato
from tkinter import*
import random
import time

root=Tk()
root.geometry("1365x769+0+0")

text_Input=StringVar()
operator=""

Tops=Frame(root,width=1600,height=200,bg="red",relief='raise')
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=700,relief='raise')
f1.pack(side=LEFT)

f2=Frame(root,width=800,height=700,bg="powder blue",relief='raise')
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

info=Label(Tops,font=('arial',50,'bold'),text="Hotel Management System",fg="blue",bd=10,anchor='w')
info.grid(row=0,column=0)
info=Label(Tops,font=('arial',20,'bold'),text=localtime,fg="black",bd=10,anchor='w')
info.grid(row=1,column=0)
 #------------------------------------------------------------------------
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)

def cleardisplay():
    global operator
    operator=""
    text_Input.set(operator)

def totalequal():
    global operator
    evaluate=str(eval(operator))
    text_Input.set(evaluate)
    
 #------------------------------------------------------------------------   
txtdisplay=Entry(f2,font=('arial',20,'bold'),text=text_Input,bd=20,insertwidth=4,bg="silver",justify='right')
txtdisplay.grid(columnspan=4)
 #------------------------------------------------------------------------
btn7=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='7',bg="powder blue",command=lambda :btnClick(7))
btn7.grid(row=2,column=0)
btn8=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='8',bg="powder blue",command=lambda :btnClick(8))
btn8.grid(row=2,column=1)
btn9=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='9',bg="powder blue",command=lambda :btnClick(9))
btn9.grid(row=2,column=2)
addition=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='+',bg="powder blue",command=lambda :btnClick('+'))
addition.grid(row=2,column=3)
#----------------------------------------------------------------------------
btn4=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='4',bg="powder blue",command=lambda :btnClick(4))
btn4.grid(row=3,column=0)
btn5=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='5',bg="powder blue",command=lambda :btnClick(5))
btn5.grid(row=3,column=1)
btn6=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='6',bg="powder blue",command=lambda :btnClick(6))
btn6.grid(row=3,column=2)
subtraction=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='-',bg="powder blue",command=lambda :btnClick('-'))
subtraction.grid(row=3,column=3)
#--------------------------------------------------------------------------------
btn1=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='1',bg="powder blue",command=lambda :btnClick(1))
btn1.grid(row=4,column=0)
btn2=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='2',bg="powder blue",command=lambda :btnClick(2))
btn2.grid(row=4,column=1)
btn3=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='3',bg="powder blue",command=lambda :btnClick(3))
btn3.grid(row=4,column=2)
multiplication=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='*',bg="powder blue",command=lambda :btnClick('*'))
multiplication.grid(row=4,column=3)
#--------------------------------------------------------------------------
clear=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='C',bg="powder blue",command=cleardisplay)
clear.grid(row=5,column=0)
division=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='/',bg="powder blue",command=lambda :btnClick('/'))
division.grid(row=5,column=2)
btn0=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='0',bg="powder blue",command=lambda :btnClick(0))
btn0.grid(row=5,column=1)
equals=Button(f2,padx=12,pady=12,bd=8,fg="black",font=('arial',20,'bold'),
            text='=',bg="powder blue",command=totalequal)
equals.grid(row=5,column=3)
#--------------------------------------------------------------------------
rand=StringVar()
idli=StringVar()
vada=StringVar()
dosa=StringVar()
puri=StringVar()
tea=StringVar()
coffee=StringVar()
upma=StringVar()
cooldrinks=StringVar()
subtotal=StringVar()
total=StringVar()
gst=StringVar()

Ref=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Reference',justify='left',fg='black').grid(row=0,column=0)
txtRef=Entry(f1,font=('arial',20,'bold'),bd=10,justify='right',text=rand,bg='silver',fg='black').grid(row=0,column=1)

Idli=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Idli',fg='black').grid(row=1,column=0)
txtIdli=Entry(f1,font=('arial',20,'bold'),bg='silver',text=idli,insertwidth=4,justify='right',fg='black',bd=8).grid(row=1,column=1)

Vada=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Vada',fg='black').grid(row=2,column=0)
txtVada=Entry(f1,font=('arial',20,'bold'),bg='silver',text=vada,insertwidth=4,justify='right',fg='black',bd=8).grid(row=2,column=1)

Dosa=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Dosa',fg='black').grid(row=3,column=0)
txtDosa=Entry(f1,font=('arial',20,'bold'),bg='silver',text=dosa,insertwidth=4,justify='right',fg='black',bd=8).grid(row=3,column=1)

Puri=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Puri',fg='black').grid(row=4,column=0)
txtPuri=Entry(f1,font=('arial',20,'bold'),bg='silver',text=puri,insertwidth=4,justify='right',fg='black',bd=8).grid(row=4,column=1)

Upma=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Upma',fg='black').grid(row=5,column=0)
txtUpma=Entry(f1,font=('arial',20,'bold'),bg='silver',text=upma,insertwidth=4,justify='right',fg='black',bd=8).grid(row=5,column=1)

Tea=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Tea',fg='black').grid(row=0,column=2)
txtTea=Entry(f1,font=('arial',20,'bold'),insertwidth=4,text=tea,justify='right',fg='black',bd=8).grid(row=0,column=3)

Coffe=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Coffee',fg='black').grid(row=1,column=2)
txtCoffe=Entry(f1,font=('arial',20,'bold'),insertwidth=4,text=coffee,justify='right',fg='black',bd=8).grid(row=1,column=3)

Cooldrinks=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Cool Drinks',fg='black').grid(row=2,column=2)
txtCooldrinks=Entry(f1,font=('arial',20,'bold'),insertwidth=4,text=cooldrinks,justify='right',fg='black',bd=8).grid(row=2,column=3)

Subtotal=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Subtotal',fg='black').grid(row=3,column=2)
txtSubtotal=Entry(f1,font=('arial',20,'bold'),insertwidth=4,text=subtotal,justify='right',fg='black',bd=8).grid(row=3,column=3)

Total=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='Total',fg='black').grid(row=5,column=2)
txtTotal=Entry(f1,font=('arial',20,'bold'),insertwidth=4,text=total,justify='right',fg='black',bd=8).grid(row=5,column=3)

Gst=Label(f1,font=('arial',16,'bold'),bd=10,anchor='w',text='GST',fg='black').grid(row=4,column=2)
txtGst=Entry(f1,font=('arial',20,'bold'),insertwidth=4,text=gst,justify='right',fg='black',bd=8).grid(row=4,column=3)


#--------------------------------------------------------------------------------------------------------------------------------------
def btnTotal():
    rand.set(str(random.randint(1254869,9875412)))

    tI= 0 if idli.get()=="" else 30*float(idli.get())
    tV= 0 if vada.get()=="" else 40*float(vada.get())
    tD= 0 if dosa.get()=="" else 40*float(dosa.get())
    tU= 0 if upma.get()=="" else 30*float(upma.get())
    tT= 0 if tea.get()=="" else 10*float(tea.get())
    tC= 0 if coffee.get()=="" else 50*float(coffee.get())
    tP= 0 if puri.get()=="" else 35*float(puri.get())
    tCD= 0 if cooldrinks.get()=="" else 20*float(cooldrinks.get())
    SB=tI+tV+tD+tU+tC+tT+tP+tCD
    subtotal.set('₹'+str(SB))
    GST=SB*0.18
    gst.set('₹'+str(GST))
    total.set('₹'+str(GST+SB))
 
    
def btnexit():
    root.destroy()

def btnreset():
    rand.set("")
    idli.set("")
    vada.set("")
    dosa.set("")
    puri.set("")
    tea.set("")
    coffee.set("")
    upma.set("")
    cooldrinks.set("")
    subtotal.set("")
    total.set("")
    gst.set("")
    
    
btntotal=Button(f1,text='TOTAL',bd=8,bg='powder blue',fg='black',font=('arial',20,'bold'),command=btnTotal).grid(row=8,column=1)

btnquit=Button(f1,text='QUIT',bd=8,bg='powder blue',fg='black',font=('arial',20,'bold'),command=btnexit).grid(row=8,column=2)

btnres=Button(f1,text='RESET',bd=8,bg='powder blue',fg='black',font=('arial',20,'bold'),command=btnreset).grid(row=8,column=3)

