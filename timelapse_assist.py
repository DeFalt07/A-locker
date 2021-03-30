from tkinter import *
import tkinter.messagebox as mess


root=Tk( )
root.geometry('385x280')
root.iconbitmap(r'icon.ico')
root.title('Timelapse Assist')


frame_1=Frame(root).pack(side=TOP)
ground=Label(frame_1,text='OPTION',bg='green',font=('arial',40,'bold')).pack()


def cal():
    try:
        if (x.get() == 0 or i.get() == 0):
            mess.showinfo('Alert','! Entry is required !')

        y = int(x.get()) * 30
        tt = (y - 1) * int(i.get())
        #print('Number of photos should be,', y)
        value_1='Number of photos should be, ' + str(y)
        re.insert(1,value_1)

        if tt >= 60:
            htt = tt // 60
            rec2=htt+1
            value_2='That should take ~ '+ str(htt)+ ' to '+ str(rec2) + ' mins '
            #print('That should take ~', htt, 'to', htt + 1, 'mins')
            re.insert(2,value_2)
            if htt > 60:
                hhtt = htt / 60
                #print('That is equivalent to', hhtt, 'hrs')
                value_3= 'That is equivalent to ' + str(hhtt) + ' hrs '
                re.insert(3,value_3)

        else:
            rec= tt+1
            #print('That should take ~', tt, 'to', tt + 1, 'sec')
            value_4='That should take ~ '+ str(tt) + ' to '+ str(rec) + ' sec '
            re.insert(4,value_4)
    except Exception :
        mess.showinfo('Alert','Enter Valid Number')

def timelapse_1():
    
    win =  Toplevel(root)
    win.iconbitmap(r'icon.ico')
    win.title('TimeLapse I')
    win.geometry('385x580')

    global x
    global i
    global re
    label=Label(win,text='TIMELAPSE I',font=('American Captain',40),fg='steelblue').pack()

    x = IntVar()               #stores duration of the video
    label1=Label( win, text='''Enter duration of the video:
        ( in sec)''', font=('consolas', 14)).place(x=10,y=100)

    enput=Entry (win,textvariable = x, width=11, bg='cyan').place(x=310,y=105)
    lable2=Label (win, text='Enter time interval (in sec):',font=('consolas',14)).place (x=10,y=200)

    i=IntVar()        #store interval 
    enput2=Entry (win,textvariable = i, width=11, bg='cyan').place(x=310,y=205)

    button=Button (win, text='GO!',font=('terminal',20,'bold'),fg='cyan',bg='red',command=cal).place(x=150,y=450)
    button2=Button (win, text = 'quit',bg ='black',fg='white',command=win.destroy).place(x=350,y=10)

    re = Listbox(win, width=45, height=7,bg='#404040',fg='#40FFF9',font=('Courier',9))
    re.place(x=38, y=300)

def cal2():
    try:

        if (t.get()==0 or I.get()==0):
            mess.showinfo('Alert','! Entry Required !')
        n=int(t.get())*60/(int(I.get()))+1
        T=n/30
        Print='Number of photos should be ~ '+ str(n)
        time='Duration of the video(in sec):'+ str(T)
        lst.insert(1,Print)
        lst.insert(2,time)
    except Exception :
        mess.showinfo('Alert','Enter Valid Number')



def timelapse_2():
    win2= Toplevel(root)
    win2.iconbitmap(r'icon.ico')
    win2.title('TimeLapse II')
    win2.geometry('385x580')
    global t
    global I
    global lst

    label=Label(win2,text='TIMELAPSE II',font=('American Captain',40),fg='steelblue').pack()

    t = IntVar()               #stores duration of the video
    label1=Label( win2, text='''Enter your essential time:
      (in min)''', font=('consolas', 14)).place(x=10,y=100)
    enput=Entry (win2,textvariable = t, width=11, bg='cyan').place(x=310,y=105)
    lable2=Label (win2, text='Enter time interval (in sec):',font=('consolas',14)).place (x=10,y=200)

    I=IntVar()        #store interval
    enput2=Entry (win2,textvariable = I, width=11, bg='cyan').place(x=310,y=205)
    button=Button (win2, text='GO!',font=('terminal',20,'bold'),fg='cyan',bg='red',command=cal2).place(x=150,y=450)
    button2=Button (win2, text = 'quit',bg ='black',fg='white',command=win2.destroy).place(x=350,y=10)

    lst=Listbox(win2,width=45, height=7,bg='#404040',fg='#40FFF9',font=('Courier',9))
    lst.place(x=38, y=300)

def Help ():
    win3= Toplevel(root)
    win3.iconbitmap(r'icon.ico')
    win3.title('Help')
    win3.geometry('385x280')
    lable=Label(win3,text=''' TimeLapse I ''',font=('Muli Black',14)).pack(side=TOP)
    lst=Listbox(win3,width= 45, height=13,bg='#404040',fg='#40FFF9',font=('system'))
    lst.pack()
    lst.insert(1,'If you know the duration of the video. Enter it, App will do rest of the work to you.  ')
    
    
frame_2=Frame (root).pack(side=BOTTOM)
option_1=Button(frame_2,text='TimeLapse I',font=('arial',20,'bold'),bg='lightgreen',command=timelapse_1).pack(side=LEFT)
option_2=Button(frame_2,text='TimeLapse II',font=('arial',20,'bold'),bg='pink',command=timelapse_2).pack(side=LEFT)
button2=Button (frame_1, text = 'Exit',bg ='black',fg='white',command=root.destroy    ).place(x=345,y=10)
button3 = Button (root, text='?',bg='black',fg='white',command=Help).place(x=10,y=210)
root.mainloop()


