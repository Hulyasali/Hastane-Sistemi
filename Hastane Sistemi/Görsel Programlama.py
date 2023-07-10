from tkinter import *
from datetime import date
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
import time
import datetime
from datetime import datetime
from datetime import timedelta
import smtplib
import mysql.connector



ekran=Tk()
ekran.geometry("1200x700+140+50")
ekran.title("Hastane Sistemi")
ekran.config(bg="antiquewhite")

ekran.rowconfigure(0, weight=1)
ekran.columnconfigure(0, weight=1)

guncelle=Frame(bg="whitesmoke")
kaydol=Frame(bg="whitesmoke")
tanırecete=Frame(bg="whitesmoke")
randevusilhasta=Frame(ekran,bg="whitesmoke")
randevusil=Frame(ekran,bg="whitesmoke")
randevubilgi=Frame(ekran,bg="whitesmoke")
randevugor=Frame(ekran,bg="whitesmoke")
randevual=Frame(ekran,bg="whitesmoke")
hastabilgi=Frame(ekran,bg="whitesmoke")
hastakabul=Frame(ekran,bg="whitesmoke")
doktorhastabilgi=Frame(ekran,bg="whitesmoke")
kullanıcı1in=Frame(ekran,bg="whitesmoke")
kullanıcı2in=Frame(ekran,bg="whitesmoke")
adminin=Frame(ekran,bg="whitesmoke")
admin=Frame(ekran,bg="whitesmoke")
kullanıcı2=Frame(ekran,bg="whitesmoke")
kullanıcı1=Frame(ekran,bg="whitesmoke")
anaekran=Frame(ekran,bg="whitesmoke")

def show_frame(frame):
    frame.tkraise()


randevual.grid(row=0,column=0,sticky="nsew")
guncelle.grid(row=0,column=0,sticky="nsew")
kaydol.grid(row=0,column=0,sticky="nsew")
tanırecete.grid(row=0,column=0,sticky="nsew")
randevusilhasta.grid(row=0,column=0,sticky="nsew")
randevusil.grid(row=0,column=0,sticky="nsew")
randevubilgi.grid(row=0,column=0,sticky="nsew")
randevugor.grid(row=0,column=0,sticky="nsew")
hastabilgi.grid(row=0,column=0,sticky="nsew")
hastakabul.grid(row=0,column=0,sticky="nsew")
doktorhastabilgi.grid(row=0,column=0,sticky="nsew")
kullanıcı1in.grid(row=0,column=0,sticky="nsew")
kullanıcı2in.grid(row=0,column=0,sticky="nsew")
adminin.grid(row=0,column=0,sticky="nsew")
anaekran.grid(row=0,column=0,sticky="nsew")
kullanıcı1.grid(row=0,column=0,sticky="nsew")
kullanıcı2.grid(row=0,column=0,sticky="nsew")
admin.grid(row=0,column=0,sticky="nsew")
muayene=Frame(hastakabul,width=400,height=420,background="antiquewhite",highlightbackground="black",highlightthicknes=3)
muayene.place(x=600,y=100)






#Frame pack v2#

ustbilgi=Frame(anaekran,bg="lightslategray",height=100,width=1900)
ustbilgi.pack(pady=0)
ustbilgi2=Frame(admin,bg="lightslategray",height=100,width=1900)
ustbilgi2.pack(pady=0)
ustbilgi3=Frame(kullanıcı1,bg="lightslategray",height=100,width=1900)
ustbilgi3.pack(pady=0)
ustbilgi4=Frame(kullanıcı2,bg="lightslategray",height=100,width=1900)
ustbilgi4.pack(pady=0)
ustbilgi5=Frame(kaydol,bg="lightslategray",height=100,width=1900)
ustbilgi5.pack(pady=0)
ustbilgi6=Frame(adminin,bg="lightslategray",height=100,width=1900)
ustbilgi6.pack(pady=0)
ustbilgi7=Frame(kullanıcı1in,bg="lightslategray",height=100,width=1900)
ustbilgi7.pack(pady=0)
ustbilgi8=Frame(kullanıcı2in,bg="lightslategray",height=100,width=1900)
ustbilgi8.pack(pady=0)
ustbilgi9=Frame(doktorhastabilgi,bg="lightslategray",height=100,width=1900)
ustbilgi9.pack(pady=0)
ustbilgi10=Frame(randevugor,bg="lightslategray",height=100,width=1900)
ustbilgi10.pack(pady=0)
ustbilgi11=Frame(hastabilgi,bg="lightslategray",height=100,width=1900)
ustbilgi11.pack(pady=0)
ustbilgi12=Frame(randevusil,bg="lightslategray",height=100,width=1900)
ustbilgi12.pack(pady=0)

ustbilgi13=Frame(guncelle,bg="lightslategray",height=100,width=1900)
ustbilgi13.pack(pady=0)
ustbilgi14=Frame(hastakabul,bg="lightslategray",height=100,width=1900)
ustbilgi14.pack(pady=0)

ustbilgi15=Frame(randevual,bg="lightslategray",height=100,width=1900)
ustbilgi15.pack(pady=0)

ustbilgi16=Frame(randevusilhasta,bg="lightslategray",height=100,width=1900)
ustbilgi16.pack(pady=0)

ustbilgi17=Frame(tanırecete,bg="lightslategray",height=100,width=1900)
ustbilgi17.pack(pady=0)

ustbilgi18=Frame(randevubilgi,bg="lightslategray",height=100,width=1900)
ustbilgi18.pack(pady=0)




style=ttk.Style()
style.configure("Treeview",
             bg="silver",
             fg="black",
             rowheight=40,
             fielbackground="gray")







def clearall():
    adminentry.delete(0,'end')
    adminentry2.delete(0,'end')
    kilname.delete(0,'end')
    tcname.delete(0,'end')








gırısres2=PhotoImage(file="g904.png")
gırısres=PhotoImage(file="g20314.png")
gırısres3=PhotoImage(file="g898.png")
gırısres4=PhotoImage(file="g923.png")

gerires=PhotoImage(file="image933.png")
cıkısres=PhotoImage(file="g43403.png")

gırısres5=PhotoImage(file="gir.png")

doktorbut=PhotoImage(file="rect31.png")
doktorbut2=PhotoImage(file="rect31-6.png")
doktorbut3=PhotoImage(file="rect31-0.png")
danısmanbut=PhotoImage(file="rect35.png")
danısmanbut2=PhotoImage(file="rect36.png")

hastabut=PhotoImage(file="rect38.png")
hastabut2=PhotoImage(file="rect37.png")
hastabut3=PhotoImage(file="rect39.png")
bilgibut=PhotoImage(file="rect40.png")
bilgibut2=PhotoImage(file="ara.png")
bilgibut3=PhotoImage(file="temizle.png")

ransilbut=PhotoImage(file="rect44.png")

bilgilistbut=PhotoImage(file="bilgilistele.png")
bilgbut=PhotoImage(file="bilg.png")

kaydetbut=PhotoImage(file="kayt.png")
muabut=PhotoImage(file="muayene2.png")
ransilbut2=PhotoImage(file="iptal.png")
gondbut=PhotoImage(file="gonder.png")
tambut=PhotoImage(file="tam.png")

kayıtvar=PhotoImage(file="kaydvar2.png")





y2=StringVar()
y3=StringVar()
y4=StringVar()
y45=StringVar()
y9=StringVar()
y10=StringVar()
y13=StringVar()




adminpage=Label(ustbilgi,text="HASTANE SİSTEMİ",font="times 35",bg="lightslategray",fg="white")
adminpage.pack(pady=15,ipadx=700)

ranpage=Label(ustbilgi18,text="HASTA BİLGİSİ",font="times 35",bg="lightslategray",fg="white")
ranpage.pack(pady=15,ipadx=700)



admininpage=Label(ustbilgi6,text="HOŞ GELDİNİZ",font="times 35",bg="lightslategray",fg="White")
admininpage.pack(pady=15,ipadx=700)

kullanıcı1inpage=Label(ustbilgi7,text="HOŞ GELDİNİZ",font="times 35",bg="lightslategray",fg="White")
kullanıcı1inpage.pack(pady=15,ipadx=700)

kullanıcı2inpage=Label(ustbilgi8,text="HOŞ GELDİNİZ",font="times 35",bg="lightslategray",fg="White")
kullanıcı2inpage.pack(pady=15,ipadx=700)

doktorhastabilgilabel=Label(ustbilgi9,text="HASTA BİLGİ SAYFASI",font="times 35",bg="lightslategray",fg="white")
doktorhastabilgilabel.pack(pady=15,ipadx=700)

ransilbas=Label(ustbilgi12,text="RANDEVU İPTALİ",font="times 35",bg="lightslategray",fg="white")
ransilbas.pack(pady=15,ipadx=700)

ranalbas=Label(ustbilgi15,text="RANDEVU AL ",font="times 35",bg="lightslategray",fg="white")
ranalbas.pack(pady=15,ipadx=700)

ranalbas=Label(ustbilgi16,text="RANDEVU İPTAL ET ",font="times 35",bg="lightslategray",fg="white")
ranalbas.pack(pady=15,ipadx=700)

ranalbas=Label(ustbilgi17,text="TANILAR VE REÇETELER ",font="times 35",bg="lightslategray",fg="white")
ranalbas.pack(pady=15,ipadx=700)


#bundan sonra buraya butonlar koyulacak#

gerigel7=Button(kullanıcı2in,image=cıkısres,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(anaekran),clearall()])
gerigel7.place(x=20,y=14)

gerigel9=Button(adminin,image=cıkısres,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(anaekran),clearall()])
gerigel9.place(x=20,y=14)

randevugorme=Button(adminin,image=doktorbut2,borderwidth=0,bg="whitesmoke",command=lambda:[show_frame(randevugor),goruntulee2()])
randevugorme.place(x=100,y=350)



gerigel8=Button(randevugor,image=gerires,bg="lightslategray",activebackground="lightslategray",borderwidth=0,command=lambda:show_frame(adminin))
gerigel8.place(x=20,y=30)

ranbaslık=Label(ustbilgi10,text="RANDEVU GÖRÜNTÜLEME ",font="times 35",bg="lightslategray",fg="white")
ranbaslık.pack(pady=15,ipadx=700)

gerigel8=Button(randevubilgi,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(randevugor),silbilgi(),textsil()])
gerigel8.place(x=20,y=30)

def textsil():
    text22.delete('1.0', END)
    text11.delete('1.0', END)
 

bilgibas=Label(ustbilgi11,text="HASTA BİLGİSİ",font="times 35",bg="lightslategray",fg="white")
bilgibas.pack(pady=15,ipadx=700)

guncelbut=Label(ustbilgi13,text="HASTA BİLGİLERİNİ GÜNCELLE",font="times 35",bg="lightslategray",fg="white")
guncelbut.pack(pady=15,ipadx=700)

kabulbut=Label(ustbilgi14,text="HASTA KABUL",font="times 35",bg="lightslategray",fg="white")
kabulbut.pack(pady=15,ipadx=700)










anaekranpage=Label(ustbilgi2,text="DOKTOR GİRİŞİ",font="times 35",bg="lightslategray",fg="White")
anaekranpage.pack(pady=15,ipadx=700)


kullanıcı1page=Label(ustbilgi3,text="Danışman Girişi",font="times 35",bg="lightslategray",fg="White")
kullanıcı1page.pack(pady=15,ipadx=700)

kullanıcı2page=Label(ustbilgi4,text="Hasta Girişi",font="times 35",bg="lightslategray",fg="White")
kullanıcı2page.pack(pady=15,ipadx=700)

kayıtlabel=Label(ustbilgi5,text="Hasta Kayıt Formu",font="times 35",bg="lightslategray",fg="White")
kayıtlabel.pack(pady=15,ipadx=700)


butonanaekran=Button(anaekran,image=gırısres2,bg="whitesmoke",borderwidth=0,command=lambda:show_frame(admin))
butonanaekran.place(x=250,y=200)

butonanaekran2=Button(anaekran,image=gırısres,bg="whitesmoke",borderwidth=0,command=lambda:show_frame(kullanıcı1))
butonanaekran2.place(x=250,y=300)

butonanaekran3=Button(anaekran,image=gırısres3,bg="whitesmoke",borderwidth=0,command=lambda:show_frame(kullanıcı2))
butonanaekran3.place(x=250,y=400)

kaydolbuton=Button(anaekran,image=gırısres4,bg="whitesmoke",borderwidth=0,command=lambda:show_frame(kaydol))
kaydolbuton.place(x=250,y=500)


admingeri=Button(admin,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:show_frame(anaekran))
admingeri.place(x=20,y=30)

kullanıcı1geri=Button(kullanıcı1,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:show_frame(anaekran))
kullanıcı1geri.place(x=20,y=30)

kullanıcı2geri=Button(kullanıcı2,image=gerires,borderwidth=0,bg="lightslategray",activebackground="lightslategray",command=lambda:show_frame(anaekran))
kullanıcı2geri.place(x=20,y=30)




def giris():
    
    mycursor=veritabanı.cursor()
    mycursor.execute("SELECT * FROM doktor WHERE mail ='"+adminmail.get()+ "' AND password ='"+adminpasswd.get()+"'")
    son=mycursor.fetchone()
    print(adminmail.get(),adminpasswd.get())
    if mycursor.rowcount <= 0:
        messagebox.showinfo("Hata"," Şifre veya Eposta yanlış, Tekrar deneyiniz")
    else:
        print("welcome")
        show_frame(adminin)
        mycursor.execute("select alanı from doktor where mail ='"+adminmail.get()+ "' AND password ='"+adminpasswd.get()+"'")
        son23=mycursor.fetchone()

        kilname.insert(0,son23)
        print(kilname.get())

    
def giris2():
    
    mycursor=veritabanı.cursor()
    mycursor.execute("SELECT * FROM kullanıcı1 WHERE email ='"+adminmail.get()+ "' AND password ='"+adminpasswd.get()+"'")
    son=mycursor.fetchone()
    print(adminmail.get(),adminpasswd.get())
    if mycursor.rowcount <= 0:
        messagebox.showinfo("Hata"," Şifre veya Eposta yanlış, Tekrar deneyiniz")
    else:
        print("welcome")
        show_frame(kullanıcı1in)
        kilname2.insert(0,son)
        


    
def giris3():
    
    mycursor=veritabanı.cursor()
    mycursor.execute("SELECT * FROM hasta WHERE eposta ='"+adminmail.get()+ "' AND sifre ='"+adminpasswd.get()+"'")
    son=mycursor.fetchone()
    print(adminmail.get(),adminpasswd.get())
    if mycursor.rowcount <= 0:
        messagebox.showinfo("Hata"," Şifre veya Eposta yanlış, Tekrar deneyiniz")
    else:
        print("welcome")
        show_frame(kullanıcı2in)
        mycursor.execute("select tckimlik from hasta where eposta ='"+adminmail.get()+ "' AND sifre ='"+adminpasswd.get()+"'")
        son40=mycursor.fetchone()

        tcname.insert(0,son40)
        print(tcname.get())

        












adminentrylabel=Label(admin,text="E Mail",fg="gray",font=("Jayes","15","bold"),bg="whitesmoke")
adminentrylabel.place(x=200,y=360)
adminentrylabel2=Label(admin,text="Şifre",fg="gray",font=("Jayes","15","bold"),bg="whitesmoke")
adminentrylabel2.place(x=200,y=440)

adminmail=StringVar()
adminpasswd=StringVar()

adminonay=Button(admin,image=gırısres5,bg="Whitesmoke",borderwidth=0,command=lambda:[giris()])
adminonay.place(x=220,y=520)

adminentry=Entry(admin,bd=3,textvariable=adminmail,width=28)
adminentry.place(x=200,y=400)
adminentry2=Entry(admin,bd=3,textvariable=adminpasswd,width=28)
adminentry2.place(x=200,y=480)




kullanıcı1entrylabel1=Label(kullanıcı1,text="E Mail",fg="gray",font=("Jayes","15","bold"),bg="whitesmoke")
kullanıcı1entrylabel1.place(x=200,y=360)
kullanıcı1entrylabel2=Label(kullanıcı1,text="Şifre",fg="gray",font=("Jayes","15","bold"),bg="whitesmoke")
kullanıcı1entrylabel2.place(x=200,y=440)

k1onay=Button(kullanıcı1,image=gırısres5,borderwidth=0,bg="whitesmoke",command=lambda:[giris2()])
k1onay.place(x=220,y=520)

kullanıcı1entry=Entry(kullanıcı1,bd=3,textvariable=adminmail,width=28)
kullanıcı1entry.place(x=200,y=400)
kullanıcı1entry2=Entry(kullanıcı1,bd=2,textvariable=adminpasswd,width=28)
kullanıcı1entry2.place(x=200,y=480)



kullanıcı2label1=Label(kullanıcı2,text="E Mail",fg="gray",font=("Jayes","15","bold"),bg="whitesmoke")
kullanıcı2label1.place(x=200,y=360)
kullanıcı2label2=Label(kullanıcı2,text="Şifre",fg="gray",font=("Jayes","15","bold"),bg="whitesmoke")
kullanıcı2label2.place(x=200,y=440)

k2onay=Button(kullanıcı2,image=gırısres5,borderwidth=0,bg="whitesmoke",command=lambda:[giris3()])
k2onay.place(x=220,y=520)

kullanıcıentry=Entry(kullanıcı2,bd=3,textvariable=adminmail,width=28)
kullanıcıentry.place(x=200,y=400)
kullanıcıentry2=Entry(kullanıcı2,bd=3,textvariable=adminpasswd,width=28)
kullanıcıentry2.place(x=200,y=480)


y5=StringVar()
y6=StringVar()
y7=StringVar()
y8=StringVar()
    
kilname=Entry(randevugor,textvariable=y5)
kilname2=Entry(randevugor,textvariable=y6)
kilname3=Entry(randevugor,textvariable=y7)
tcname=Entry(randevusilhasta,textvariable=y8)


hastabilgibuton=Button(adminin,image=doktorbut,bg="whitesmoke",borderwidth=0,command=lambda:[show_frame(doktorhastabilgi),goruntulee()])
hastabilgibuton.place(x=100,y=250)


scb3=Scrollbar(doktorhastabilgi)
scb3.pack(side=RIGHT,fill=Y)


hastabilgitablo = ttk.Treeview(doktorhastabilgi, columns=(1, 2, 3, 4), show='headings', height=8)
hastabilgitablo.pack(side=LEFT,padx=70)
hastabilgitablo.heading(1, text="TC Kimlik")
hastabilgitablo.heading(2, text="AD")
hastabilgitablo.heading(3, text="SOYAD")
hastabilgitablo.heading(4, text="KLİNİK")


scb3.config(command=hastabilgitablo.yview)








def goruntulee():



    
    hastabilgitablo.delete(*hastabilgitablo.get_children())
    mycursor=veritabanı.cursor()
    mycursor.execute("SELECt tc_kimlik,hasta_adı,hasta_soyadı,klinik from muayenetablosu where klinik='"+y5.get()+"'")
    diz=mycursor.fetchall()
    for row in diz:
        hastabilgitablo.insert('',END,values=row)


        

scb4=Scrollbar(randevugor)
scb4.pack(side=RIGHT,fill=Y)


rantablo = ttk.Treeview(randevugor, columns=( 2, 3, 4, 5, 6, 7), show='headings', height=7)
rantablo.pack(side=LEFT)


rantablo.heading(2, text="AD")
rantablo.heading(3, text="SOYAD")
rantablo.heading(4, text="TCKİMLİK")
rantablo.heading(5, text="KLİNİK")
rantablo.heading(6, text="RANDEVU TARİHİ")
rantablo.heading(7, text="RANDEVU SAATİ")



scb4.config(command=rantablo.yview)





def goruntulee2():

    rantablo.delete(*rantablo.get_children())
    mycursor=veritabanı.cursor()
    mycursor.execute("SELECt ad,soyad,tckimlik,klinik,randevu_tarih,randevu_saat from randevulist where klinik='"+y5.get()+"'")
    print(y5.get())
    diz2=mycursor.fetchall()
    for row in diz2:
        rantablo.insert('',END,values=row)



scb5=Scrollbar(randevusil)
scb5.pack(side=RIGHT,fill=Y)



siltablo=ttk.Treeview(randevusil,columns=(2,3,4,5,6,7),show="headings",height=7)
siltablo.pack(side=LEFT)

siltablo.heading(2, text="AD")
siltablo.heading(3, text="SOYAD")
siltablo.heading(4, text="TCKİMLİK")
siltablo.heading(5, text="KLİNİK")
siltablo.heading(6, text="RANDEVU TARİHİ")
siltablo.heading(7, text="RANDEVU SAATİ")



scb5.config(command=siltablo.yview)






def goruntulee3():
    siltablo.delete(*siltablo.get_children())
    mycursor=veritabanı.cursor()
    mycursor.execute("Select ad,soyad,tckimlik,klinik,randevu_tarih,randevu_saat from randevulist where klinik='"+y5.get()+"'")
    dizdiz=mycursor.fetchall()
    for rowrow in dizdiz:
        siltablo.insert('',END,values=rowrow)
        


def update(row2):
    hastabilgitablo.delete(*hastabilgitablo.get_children())
    for i in row2:
        hastabilgitablo.insert("","end",values=i)
def update2(row3):
    rantablo.delete(*rantablo.get_children())
    for i in row3:
        rantablo.insert("","end",values=i)
        
def update3(row4):
    siltablo.delete(*siltablo.get_children())
    for i in row4:
        siltablo.insert("","end",values=i)

sonuc=StringVar()
sonuc2=StringVar()
sonuc3=StringVar()

def arama():
    mycursor.execute("Select tc_kimlik,hasta_adı,hasta_soyadı,klinik from muayenetablosu where hasta_adı='"+sonuc.get()+"' or tc_kimlik='"+sonuc.get()+"'")
    row2=mycursor.fetchall()
    update(row2)

def arama2():
    mycursor.execute("Select ad,soyad,tckimlik,klinik,randevu_tarih,randevu_saat from randevulist where ad='"+sonuc2.get()+"' or tckimlik='"+sonuc2.get()+"'")
    row3=mycursor.fetchall()
    update2(row3)

def arama3():
    mycursor.execute("Select ad,soyad,tckimlik,klinik,randevu_tarih,randevu_saat from randevulist where ad='"+sonuc3.get()+"' or tckimlik='"+sonuc3.get()+"'")
    row4=mycursor.fetchall()
    update3(row4)




def tcal(event):
    rowid=hastabilgitablo.identify_row(event.y)
    item=hastabilgitablo.item(hastabilgitablo.focus())
    y2.set(item['values'][0])

def tcal2(event):
    rowid2=rantablo.identify_row(event.y)
    item2=rantablo.item(rantablo.focus())
    y3.set(item2['values'][2])

def tcal3(event):
    rowid2n=siltablo.identify_row(event.y)
    item2n=siltablo.item(siltablo.focus())
    y4.set(item2n['values'][4])
    y45.set(item2n['values'][5])
    

def tcal4(event):
    rowid2nn=hastasilran.identify_row(event.y)
    item2nn=hastasilran.item(hastasilran.focus())
    y9.set(item2nn['values'][4])
    y10.set(item2nn['values'][5])
    

def tcal5(event):
    rowid33=tanıtablo.identify_row(event.y)
    itemm=tanıtablo.item(tanıtablo.focus())
    y12.set(itemm['values'][0])

def tcal6(event):
    rowid34=duzentablo.identify_row(event.y)
    itemm1=duzentablo.item(duzentablo.focus())
    y13.set(itemm1['values'][0])






#doktor hasta bilgi ekranında arama tuşu#

aramaentry=Entry(doktorhastabilgi,textvariable=sonuc,width=20,bd=3)
aramaentry.place(x=170,y=620)
arabuton=Button(doktorhastabilgi,image=bilgibut2,borderwidt=0,bg="whitesmoke",command=arama)
arabuton.place(x=310,y=610)
temizle=Button(doktorhastabilgi,image=bilgibut3,borderwidth=0,bg="whitesmoke",command=goruntulee)
temizle.place(x=430,y=610)

aramalab=Label(doktorhastabilgi,font=("Jayes","10","bold"),text="TC Kimlik",bg="whitesmoke")
aramalab.place(x=170,y=595)

aramaentry2=Entry(randevugor,textvariable=sonuc2)
aramaentry2.place(x=170,y=620)
arabuton2=Button(randevugor,image=bilgibut2,borderwidth=0,bg="whitesmoke",command=arama2)
arabuton2.place(x=310,y=610)
temizle2=Button(randevugor,image=bilgibut3,borderwidth=0,bg="whitesmoke",command=goruntulee2)
temizle2.place(x=430,y=610)

aramalab2=Label(randevugor,font=("Jayes","10","bold"),text="TC Kimlik",bg="whitesmoke")
aramalab2.place(x=170,y=595)


aramaentry3=Entry(randevusil,textvariable=sonuc3)
aramaentry3.place(x=170,y=620)
arabuton3=Button(randevusil,image=bilgibut2,borderwidth=0,bg="whitesmoke",command=arama3)
arabuton3.place(x=310,y=610)
temizle3=Button(randevusil,image=bilgibut3,borderwidth=0,bg="whitesmoke",command=goruntulee3)
temizle3.place(x=430,y=610)

aramalab3=Label(randevusil,font=("Jayes","10","bold"),text="TC Kimlik",bg="whitesmoke")
aramalab3.place(x=170,y=595)



def silkabul():
    tcentry.delete(0,'end')
    adentry.delete(0,'end')
    soyadentry.delete(0,'end')
    cins.delete(0,'end')
    kangr.delete(0,'end')
    hastadogumyerien.delete(0,'end')
    hastadogumen.delete(0,'end')
    anaen.delete(0,'end')
    babaen.delete(0,'end')
    numaraen.delete(0,'end')
    adress.delete(0,'end')
    
    
    

#HASTA KABUL#

two=['Erkek','Kadın','Diğer']
kan=["0_RH_Pozitif","Rh_negatif","A_Rh_pozitif","A_Rh_negatif","B_Rh_pozitif","B_Rh_negatif","AB_Rh_pozitif","AB_Rh_negatif"]

hastatc=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta TC:",bg="whitesmoke")
hastatc.place(x=50,y=100)
tcentry=Entry(hastakabul)
tcentry.place(x=200,y=100)

hastaadı=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Adı:",bg="whitesmoke")
hastaadı.place(x=50,y=140)
adentry=Entry(hastakabul)
adentry.place(x=200,y=140)

hastasoyadı=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Soyadı",bg="whitesmoke")
hastasoyadı.place(x=50,y=180)
soyadentry=Entry(hastakabul)
soyadentry.place(x=200,y=180)

cinsiyeti=Label(hastakabul,font=("Jayes","10","bold"),text="Cinsiyeti",bg="whitesmoke")
cinsiyeti.place(x=50,y=220)
cins=ttk.Combobox(hastakabul,width=17)
cins['values']=two
cins.bind('<<ComboboxSelected>>')
cins.place(x=200,y=220)

kang=Label(hastakabul,font=("Jayes","10","bold"),text="Kan Grubu",bg="whitesmoke")
kang.place(x=50,y=260)
kangr=ttk.Combobox(hastakabul,width=17)
kangr['values']=kan
kangr.bind('<<ComboboxSelected>>')
kangr.place(x=200,y=260)


hastadogumyeri=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Doğum Yeri",bg="whitesmoke")
hastadogumyeri.place(x=50,y=300)
hastadogumyerien=Entry(hastakabul)
hastadogumyerien.place(x=200,y=300)

hastadogumtarihi=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Doğum Tarihi",bg="whitesmoke")
hastadogumtarihi.place(x=50,y=340)
hastadogumen=Entry(hastakabul)
hastadogumen.place(x=200,y=340)

anaadı=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Anne Adı:",bg="whitesmoke")
anaadı.place(x=50,y=380)
anaen=Entry(hastakabul)
anaen.place(x=200,y=380)

babaadı=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Baba Adı:",bg="whitesmoke")
babaadı.place(x=50,y=420)
babaen=Entry(hastakabul)
babaen.place(x=200,y=420)

numara=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Cep Telefonu:",bg="whitesmoke")
numara.place(x=50,y=460)
numaraen=Entry(hastakabul)
numaraen.place(x=200,y=460)


adres=Label(hastakabul,font=("Jayes","10","bold"),text="Hasta Adresi:",bg="whitesmoke")
adres.place(x=50,y=500)
adress=Entry(hastakabul)
adress.place(x = 200,
        y = 500,
        width=300)

dokt=StringVar()
dokt2=StringVar()

def hastakabulkaydet():
    mycursor=veritabanı.cursor()
    mycursor.execute("select * from hasta where tckimlik='"+tcentry.get()+"'")
    son50=mycursor.fetchall()
    if mycursor.rowcount > 0:
        messagebox.showinfo("HATA","BU KAYIT ZATEN VAR")
        
    elif len(adentry.get())==0 or len(soyadentry.get())==0 or len(tcentry.get())==0 or len(cins.get())==0 or len(numaraen.get())==0:
        messagebox.showinfo("EKSİK BİLGİ"," Formda eksik alanlar var")
   
        
    else:
        
        sorgu="INSERT INTO hasta (tckimlik,ad,soyad,cinsiyet,kan,dogumyeri,dogumtarihi,baba_adı,anne_adı,numara,adres)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        deger=(tcentry.get(),adentry.get(),soyadentry.get(),cins.get(),kangr.get(),hastadogumyerien.get(),hastadogumen.get(),babaen.get(),anaen.get(),numaraen.get(),adress.get())
        mycursor.execute(sorgu,deger)
        veritabanı.commit()
        print("Kayıt eklendi")
        sonson2=Label(hastakabul,bg="whitesmoke",fg="green",text="Veri Tabanına Kaydedildi",font=("Open Sans","11","bold"))
        sonson2.place(y=590,x=50)
        sonson2.after(3000, sonson2.destroy)



k=['Anesteziyoloji_ve_Reanimasyon','Çocuk_Sağlığı_ve_Hastalıkları','Deri_ve_zührevi_Hastalıkları','Diş_Hekimliği','Enfeksiyon_astalıkları','Fiziksel_Tıp_ve_Rehabilitasyon','Genel_Cerrahi','Göğüs_Hastalıkları','Göz_Hastalıkları','İç_Hastalıklar','Kadın_Hastalıkları_ve_Doğum','Kardiyoloji','Kulak_Burun_Boğaz_Hastalıkları','Nöroloji','Ortopedi_ve_Travmaloji','Psikiyatri','Sağlık_Kurulu','Üroloji']

r=['Anesteziyoloji_ve_Reanimasyon','Çocuk_Sağlığı_ve_Hastalıkları','Deri_ve_zührevi_Hastalıkları','Diş_Hekimliği','Enfeksiyon_astalıkları','Fiziksel_Tıp_ve_Rehabilitasyon','Genel_Cerrahi','Göğüs_Hastalıkları','Göz_Hastalıkları','İç_Hastalıklar','Kadın_Hastalıkları_ve_Doğum','Kardiyoloji','Kulak_Burun_Boğaz_Hastalıkları','Nöroloji','Ortopedi_ve_Travmaloji','Psikiyatri','Sağlık_Kurulu','Üroloji']



kaydet=Button(hastakabul,image=kaydetbut,borderwidth=0,bg="whitesmoke",command=lambda:[hastakabulkaydet()])
kaydet.place(x=50,y=550)

mu=Button(hastakabul,image=muabut,borderwidth=0,bg="whitesmoke",command=lambda:[muayenee()])
mu.place(x=190,y=550)

mu2=Button(hastakabul,image=kayıtvar,borderwidth=0,bg="whitesmoke",command=lambda:kaydımvar())
mu2.place(x=350,y=100)

k1=StringVar()
k2=StringVar()


kayıt1=Entry(muayene,textvariable=k1)
kayıt2=Entry(muayene,textvariable=k2)

def kaydımvar():
    
    adentry.config(state="disabled")
    soyadentry.config(state="disabled")
    cins.config(state="disabled")
    kangr.config(state="disabled")
    hastadogumyerien.config(state="disabled")
    hastadogumen.config(state="disabled")
    anaen.config(state="disabled")
    babaen.config(state="disabled")
    numaraen.config(state="disabled")
    adress.config(state="disabled")
    




def muayenee():

        


    def dokt(event):
        
        
        def kayıtson():
            

            
            if len(tcentry.get())==0:
                messagebox.showinfo("EKSİK BİLGİ"," Formda eksik alanlar var")
            else:
            
                mycursor=veritabanı.cursor()
                sorgu1="insert into muayenetablosu (tc_kimlik,hasta_adı,hasta_soyadı,klinik) Values(%s,%s,%s,%s)"
                deger1=(tcentry.get(),k1.get(),k2.get(),klinik.get())
                mycursor.execute(sorgu1,deger1)
                veritabanı.commit()
                onay51=Label(muayene,font=("Jayes","10","bold"),text="KAYIT ALINDI",bg="antiquewhite",fg="green")
                onay51.place(x=150,y=350)
                onay51.after(3000, onay51.destroy)

        
        mycursor=veritabanı.cursor()
        mycursor.execute("SELECT ad from doktor where alanı='"+klinik.get()+"'")
        son=mycursor.fetchall()

        mycursor.execute("Select ad from hasta where tckimlik='"+tcentry.get()+"'")
        son51=mycursor.fetchone()
        mycursor.execute("Select soyad from hasta where tckimlik='"+tcentry.get()+"'")
        son52=mycursor.fetchone()

        kayıt1.insert(0,son51)
        kayıt2.insert(0,son52)
        
    
        dok=Label(muayene,font=("Jayes","10","bold"),text="Doktor",bg="antiquewhite")
        dok.place(x=50,y=160)
        doktor=ttk.Combobox(muayene,width=30)
        doktor['values']=son
        doktor.bind('<<ComboboxSelected>>')
        doktor.place(x=130,y=160)

        buton3=Button(muayene,image=kaydetbut,borderwidth=0,bg="antiquewhite",command=kayıtson)
        buton3.place(x=250,y=260)


    

        
            
            

    klin=Label(muayene,font=("Jayes","10","bold"),text="Klinik",bg="antiquewhite")
    klin.place(x=50,y=100)
    klinik=ttk.Combobox(muayene,width=30)
    klinik['values']=k
    klinik.bind("<<ComboboxSelected>>",dokt)
    klinik.place(x=130,y=100)

gerigel3=Button(hastakabul,image=gerires,bg="lightslategray",activebackground="lightslategray",borderwidth=0,command=lambda:[show_frame(kullanıcı1in),silkabul(),ackayıt()])
gerigel3.place(x=20,y=30)

gerigel21=Button(kullanıcı1in,image=cıkısres,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(anaekran),clearall()])
gerigel21.place(x=20,y=14)





 #HASTA BİLGİ EKRANI (tablo tanı reçete bilgiler falan)#


hben=Entry(doktorhastabilgi,textvariable=y2,width=20,state="disabled")
hben.place(x=950,y=340)

gerigel5=Button(doktorhastabilgi,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:(show_frame(adminin)))
gerigel5.place(x=20,y=30)



hb1=Label(hastabilgi,font=("Jayes","10","bold"),text="TC Kimlik",bg="Whitesmoke")
hb1.place(x=100,y=200)
hben1=Entry(hastabilgi)
hben1.place(x=200,y=200)

hb2=Label(hastabilgi,font=("Jayes","10","bold"),text="Ad",bg="Whitesmoke")
hb2.place(x=100,y=240)
hben2=Entry(hastabilgi)
hben2.place(x=200,y=240)

hb3=Label(hastabilgi,font=("Jayes","10","bold"),text="Soyad",bg="Whitesmoke")
hb3.place(x=100,y=280)
hben3=Entry(hastabilgi)
hben3.place(x=200,y=280)

hb4=Label(hastabilgi,font=("Jayes","10","bold"),text="Cinsiyet",bg="Whitesmoke")
hb4.place(x=100,y=320)
hben4=Entry(hastabilgi)
hben4.place(x=200,y=320)

hb5=Label(hastabilgi,font=("Jayes","10","bold"),text="Kan Grubu",bg="Whitesmoke")
hb5.place(x=100,y=360)
hben5=Entry(hastabilgi)
hben5.place(x=200,y=360)
hb6=Label(hastabilgi,font=("Jayes","10","bold"),text="Doğum Yeri",bg="Whitesmoke")
hb6.place(x=100,y=400)
hben6=Entry(hastabilgi)
hben6.place(x=200,y=400)
hb7=Label(hastabilgi,font=("Jayes","10","bold"),text="Doğum Tarihi",bg="Whitesmoke")
hb7.place(x=100,y=440)
hben7=Entry(hastabilgi)
hben7.place(x=200,y=440)
hb8=Label(hastabilgi,font=("Jayes","10","bold"),text="Baba Adı",bg="Whitesmoke")
hb8.place(x=100,y=480)
hben8=Entry(hastabilgi)
hben8.place(x=200,y=480)
hb9=Label(hastabilgi,font=("Jayes","10","bold"),text="Anne Adı",bg="Whitesmoke")
hb9.place(x=100,y=520)
hben9=Entry(hastabilgi)
hben9.place(x=200,y=520)
hb10=Label(hastabilgi,font=("Jayes","10","bold"),text="Numara",bg="Whitesmoke")
hb10.place(x=100,y=560)
hben10=Entry(hastabilgi)
hben10.place(x=200,y=560)
hb11=Label(hastabilgi,font=("Jayes","10","bold"),text="Eposta",bg="Whitesmoke")
hb11.place(x=100,y=600)
hben11=Entry(hastabilgi)
hben11.place(x=200,y=600)



text1=Text(hastabilgi,width=30,height=15)
text1.place(x=450,y=300)

text2=Text(hastabilgi,width=30,height=15)
text2.place(x=900,y=300)

tanı=Label(hastabilgi,font=("Jayes","10","bold"),text="TANI",bg="Whitesmoke")
tanı.place(x=450,y=280)
tanı2=Label(hastabilgi,font=("Jayes","10","bold"),text="REÇETE",bg="Whitesmoke")
tanı2.place(x=900,y=280)



def otosil():
    mycursor=veritabanı.cursor()
    mycursor.execute("Delete from muayenetablosu where tc_kimlik='"+hben1.get()+"'")
    veritabanı.commit()


def bilgis():
    if len(hben.get())==0 :
        messagebox.showinfo("Hata","Hasta Seçiniz")
    else:
        
        show_frame(hastabilgi)

        gerigel4=Button(hastabilgi,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[(show_frame(doktorhastabilgi)),silbilgi2()])
        gerigel4.place(x=20,y=30)

        
        mycursor=veritabanı.cursor()
        mycursor.execute("SELECT ad from hasta where tckimlik='"+hben.get()+"'")
        son=mycursor.fetchone()

        mycursor.execute("select soyad from hasta where tckimlik='"+hben.get()+"'")
        son5=mycursor.fetchone()

        mycursor.execute("select cinsiyet from hasta where tckimlik='"+hben.get()+"'")
        son6=mycursor.fetchone()
        
        mycursor.execute("select kan from hasta where tckimlik='"+hben.get()+"'")
        son7=mycursor.fetchone()

        mycursor.execute("select dogumyeri from hasta where tckimlik='"+hben.get()+"'")
        son8=mycursor.fetchone()

        mycursor.execute("select dogumtarihi from hasta where tckimlik='"+hben.get()+"'")
        son9=mycursor.fetchone()

        mycursor.execute("select baba_adı from hasta where tckimlik='"+hben.get()+"'")
        son10=mycursor.fetchone()

        mycursor.execute("select anne_adı from hasta where tckimlik='"+hben.get()+"'")
        son11=mycursor.fetchone()

        mycursor.execute("select numara from hasta where tckimlik='"+hben.get()+"'")
        son12=mycursor.fetchone()

        mycursor.execute("select eposta from hasta where tckimlik='"+hben.get()+"'")
        son13=mycursor.fetchone()
        
        


        
        hben1.insert(0,hben.get())
        hben2.insert(0,son)
        hben3.insert(0,son5)
        hben4.insert(0,son6)
        hben5.insert(0,son7)
        hben6.insert(0,son8)
        hben7.insert(0,son9)
        hben8.insert(0,son10)
        hben9.insert(0,son11)
        hben10.insert(0,son12)
        hben11.insert(0,son13)



def silbilgi2():
    hben1.delete(0,'end')
    hben2.delete(0,'end')
    hben3.delete(0,'end')
    hben4.delete(0,'end')
    hben5.delete(0,'end')
    hben6.delete(0,'end')
    hben7.delete(0,'end')
    hben8.delete(0,'end')
    hben9.delete(0,'end')
    hben10.delete(0,'end')
    hben11.delete(0,'end')
    
kk1=StringVar()
kimlikal=Entry(tanırecete,textvariable=kk1)




  
def tanı():

    klin=Label(muayene,font=("Jayes","10","bold"),text="Klinik",bg="antiquewhite")
    klin.place(x=50,y=100)
    klinik=ttk.Combobox(muayene,width=30)
    klinik['values']=k
    klinik.bind("<<ComboboxSelected>>",dokt)
    klinik.place(x=130,y=100)

    mycursor=veritabanı.cursor()
    sorgu="INSERT INTO tanıverecete (hasta_adı,soyadı,tckimlik,tanı,recete,klinik)VALUES (%s,%s,%s,%s,%s,%s)"
    deger=(hben2.get(),hben3.get(),hben1.get(),text1.get("1.0",END),text2.get("1.0",END),klinik.get())
    mycursor.execute(sorgu,deger)
    veritabanı.commit()
    onay55=Label(hastabilgi,font=("Jayes","10","bold"),text="GÖNDERİLDİ",fg="Green",bg="whitesmoke")
    onay55.place(x=760,y=650)
    onay55.after(3000, onay55.destroy)
   

































  
gonder=Button(hastabilgi,image=gondbut,bg="whitesmoke",borderwidth=0,command=lambda:[tanı(),otosil()])
gonder.place(x=750,y=600)


hastabilgitablo.bind('<Double 1>',tcal)
hastabak=Button(doktorhastabilgi,image=bilgibut,borderwidth=0,bg="whitesmoke",command=lambda:bilgis())
hastabak.place(x=950,y=380)



gor=Button(kullanıcı1in,image=danısmanbut2,borderwidth=0,bg="whitesmoke",command=lambda:[show_frame(hastakabul)])
gor.place(x=200,y=360)

def ackayıt():
    adentry.config(state="normal")
    soyadentry.config(state="normal")
    cins.config(state="normal")
    kangr.config(state="normal")
    hastadogumyerien.config(state="normal")
    hastadogumen.config(state="normal")
    anaen.config(state="normal")
    babaen.config(state="normal")
    numaraen.config(state="normal")
    adress.config(state="normal")
    




  #-------------------------------------------------------------------------RANDEVU AL ; HASTA EKRANI---------------------------------------------------------------#


rben1=Entry(randevual)
rben2=Entry(randevual)
rben3=Entry(randevual)
rben4=Entry(randevual)

rben5=Entry(randevual)





def randevuekle():
    
    def randevu2(event):
        
            
    
        

        def randevuson():

                 
            

            
            mycursor=veritabanı.cursor()
            mycursor.execute("Select ad from hasta where eposta='"+adminmail.get()+"' and sifre='"+adminpasswd.get()+"'")
            rson1=mycursor.fetchone()

            mycursor=veritabanı.cursor()
            mycursor.execute("Select soyad from hasta where eposta='"+adminmail.get()+"' and sifre='"+adminpasswd.get()+"'")
            rson2=mycursor.fetchone()

            mycursor=veritabanı.cursor()
            mycursor.execute("Select tckimlik from hasta where eposta='"+adminmail.get()+"' and sifre='"+adminpasswd.get()+"'")
            rson3=mycursor.fetchone()

            mycursor=veritabanı.cursor()
            mycursor.execute("Select id from hasta where eposta='"+adminmail.get()+"' and sifre='"+adminpasswd.get()+"'")
            rson4=mycursor.fetchone()

            
            rben1.insert(0,rson1)
            rben2.insert(0,rson2)
            rben3.insert(0,rson3)
            rben4.insert(0,rson4)

            mycursor=veritabanı.cursor()
            mycursor.execute("select randevu_saat,randevu_tarih from randevulist where randevu_tarih='"+tarih.get()+"' and randevu_saat='"+saatsec.get()+"'")
            son14=mycursor.fetchall()
            
 
            
            
            if len(doktor2.get())==0 or len(klinikran.get())==0 or len(rben3.get())==0 or len(saatsec.get())==0 or len(tarih.get())==0 : #BURAYA TARİH EKLEME ŞARTINI KOY#
                messagebox.showinfo("EKSİK BİLGİ"," Formda eksik alanlar var")
            
            elif mycursor.rowcount <=0 and len(doktor2.get())>0:
                mycursor=veritabanı.cursor()
                sorgu2="insert into randevulist (ad,soyad,tckimlik,hasta_id,klinik,doktorname,randevu_saat,randevu_tarih) Values(%s,%s,%s,%s,%s,%s,%s,%s)"
                deger2=(rben1.get(),rben2.get(),rben3.get(),rben4.get(),klinikran.get(),doktor2.get(),saatsec.get(),tarih.get())
                mycursor.execute(sorgu2,deger2)
                veritabanı.commit()
                onay53=Label(randevual,font=("Jayes","10","bold"),text="RANDEVU ALINDI",bg="whitesmoke",fg="green")
                onay53.place(x=400,y=420)
                rben1.delete(0,'end')
                rben2.delete(0,'end')
                rben3.delete(0,'end')
                rben4.delete(0,'end')
                onay53.after(5000, onay53.destroy)
                
            else:
                messagebox.showinfo("Hata","Bu saat dolu, Lütfen başka saat seçiniz /n ve Doktor alanını boş bırakmayınız")
                print(tarih.get())
                
                
                
            
        mycursor=veritabanı.cursor()
        mycursor.execute("SELECT search_name from doktor where alanı='"+klinikran.get()+"'")
        dosec=mycursor.fetchone()

        sat=["09.00","10.00","11.00","12.00","13.00","14.00","15.00","16.00"]

        gün=["01","02","03","04","05","06","08","09","10","11","12","13","14","15","16",
             "17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]

        ay=["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim",
            "Kasım","Aralık"]

        yıl=["2021"]

        gozreng=["Seçiniz","mavi","yeşil","kahverengi","Ela","Siyah"]

        tenreng=["Seçiniz","Kumral ","Esmer","Buğday","Sarı","Siyahi","Beyaz"]

        ogrenımdur=["Seçiniz","Okur yazar","Okur yazar olmayan","İlkokul ","Ortaokul","Lise","Üniversite","Eğitimsiz"]

        def tarihdog(event):
            a=((dogumy.get()),"-",(doguma.get()),"-",(dogumg.get()))

            tarih.insert(0,a)

        dogumg=ttk.Combobox(randevual,width=3)
        dogumg['values']=gün
        dogumg.bind('<<ComboboxSelected>>')
        
        dogumg.place(x=340,y=300)


        doguma=ttk.Combobox(randevual,width=6)
        doguma['values']=ay
        doguma.bind('<<ComboboxSelected>>')
       
        doguma.place(x=400,y=300)

        dogumy=ttk.Combobox(randevual,width=5)
        dogumy['values']=yıl
        dogumy.bind('<<ComboboxSelected>>',tarihdog)
        
        dogumy.place(x=470,y=300)
        
        tarih=Entry()

        

        tarihe=Label(randevual,font=("Jayes","13","bold"),text="Tarih",bg="whitesmoke")
        tarihe.place(x=200,y=300)
        
        

        saat=Label(randevual,font=("Jayes","13","bold"),text="Saat",bg="whitesmoke")
        saat.place(x=200,y=360)
        saatsec=ttk.Combobox(randevual,width=30)
        saatsec['values']=sat
        saatsec.bind('<<ComboboxSelected>>')
        saatsec.place(x=340,y=360)

        

        dok2=Label(randevual,font=("Jayes","13","bold"),text="Doktor",bg="whitesmoke")
        dok2.place(x=200,y=240)
        doktor2=ttk.Combobox(randevual,width=30)
        doktor2['values']=dosec
        doktor2.bind('<<ComboboxSelected>>')
        doktor2.place(x=340,y=240)

        buton9=Button(randevual,image=kaydetbut,borderwidth=0,bg="whitesmoke",command=randevuson)
        buton9.place(x=250,y=400)

       


        
    klinikran=ttk.Combobox(randevual,width=30)
    klinikran['values']=r
    klinikran.bind("<<ComboboxSelected>>",randevu2)
    klinikran.place(x=340,y=200)

randevuklinik=Label(randevual,font=("Jayes","13","bold"),text="Klinik Seçiniz",bg="whitesmoke")
randevuklinik.place(x=200,y=200)

randevualma=Button(kullanıcı2in,image=hastabut,borderwidth=0,bg="whitesmoke",command=lambda:[show_frame(randevual),randevuekle()])
randevualma.place(x=100,y=250)


gerigel6=Button(randevual,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(kullanıcı2in)])
gerigel6.place(x=20,y=30)







#----------------------------------------------------------------DOKTOR RANDEVU GÖRÜNTÜLEME EKRANI------------------------------------------------------------------------------#




hbenn=Entry(randevugor,textvariable=y3,state="disabled")
hbenn.place(x=950,y=585)

hb30=Label(randevubilgi,font=("Jayes","10","bold"),text="TC Kimlik",bg="whitesmoke")
hb30.place(x=100,y=200)
hben30=Entry(randevubilgi)
hben30.place(x=200,y=200)

hb31=Label(randevubilgi,font=("Jayes","10","bold"),text="Ad",bg="whitesmoke")
hb31.place(x=100,y=240)
hben31=Entry(randevubilgi)
hben31.place(x=200,y=240)

hb32=Label(randevubilgi,font=("Jayes","10","bold"),text="Soyad",bg="whitesmoke")
hb32.place(x=100,y=280)
hben32=Entry(randevubilgi)
hben32.place(x=200,y=280)

hb33=Label(randevubilgi,font=("Jayes","10","bold"),text="Cinsiyet",bg="whitesmoke")
hb33.place(x=100,y=320)
hben33=Entry(randevubilgi)
hben33.place(x=200,y=320)


hb20=Label(randevubilgi,font=("Jayes","10","bold"),text="Kan Grubu",bg="whitesmoke")
hb20.place(x=100,y=360)
hben20=Entry(randevubilgi)
hben20.place(x=200,y=360)
hb21=Label(randevubilgi,font=("Jayes","10","bold"),text="Doğum Yeri",bg="whitesmoke")
hb21.place(x=100,y=400)
hben21=Entry(randevubilgi)
hben21.place(x=200,y=400)
hb22=Label(randevubilgi,font=("Jayes","10","bold"),text="Doğum Tarihi",bg="whitesmoke")
hb22.place(x=100,y=440)
hben22=Entry(randevubilgi)
hben22.place(x=200,y=440)
hb23=Label(randevubilgi,font=("Jayes","10","bold"),text="Baba Adı",bg="whitesmoke")
hb23.place(x=100,y=480)
hben23=Entry(randevubilgi)
hben23.place(x=200,y=480)
hb24=Label(randevubilgi,font=("Jayes","10","bold"),text="Anne Adı",bg="whitesmoke")
hb24.place(x=100,y=520)
hben24=Entry(randevubilgi)
hben24.place(x=200,y=520)
hb25=Label(randevubilgi,font=("Jayes","10","bold"),text="Numara",bg="whitesmoke")
hb25.place(x=100,y=560)
hben25=Entry(randevubilgi)
hben25.place(x=200,y=560)
hb26=Label(randevubilgi,font=("Jayes","10","bold"),text="Eposta",bg="whitesmoke")
hb26.place(x=100,y=600)
hben26=Entry(randevubilgi)
hben26.place(x=200,y=600)

hben27=Entry(randevubilgi)




text11=Text(randevubilgi,width=30,height=15)
text11.place(x=450,y=300)

text22=Text(randevubilgi,width=30,height=15)
text22.place(x=900,y=300)

tanı1=Label(randevubilgi,font=("Jayes","10","bold"),text="TANI",bg="Whitesmoke")
tanı1.place(x=450,y=280)
tanı22=Label(randevubilgi,font=("Jayes","10","bold"),text="REÇETE",bg="Whitesmoke")
tanı22.place(x=900,y=280)



def bilgis2():
    if len(hbenn.get())==0 :
        messagebox.showinfo("Hata","Hasta Seçiniz")
    else:
        
        show_frame(randevubilgi)

        
        mycursor=veritabanı.cursor()
        mycursor.execute("SELECT ad from hasta where tckimlik='"+hbenn.get()+"'")
        son20=mycursor.fetchone()

        mycursor.execute("select soyad from hasta where tckimlik='"+hbenn.get()+"'")
        son21=mycursor.fetchone()

        mycursor.execute("select cinsiyet from hasta where tckimlik='"+hbenn.get()+"'")
        son22=mycursor.fetchone()
        
        mycursor.execute("select kan from hasta where tckimlik='"+hbenn.get()+"'")
        son23=mycursor.fetchone()

        mycursor.execute("select dogumyeri from hasta where tckimlik='"+hbenn.get()+"'")
        son24=mycursor.fetchone()

        mycursor.execute("select dogumtarihi from hasta where tckimlik='"+hbenn.get()+"'")
        son25=mycursor.fetchone()

        mycursor.execute("select baba_adı from hasta where tckimlik='"+hbenn.get()+"'")
        son26=mycursor.fetchone()

        mycursor.execute("select anne_adı from hasta where tckimlik='"+hbenn.get()+"'")
        son27=mycursor.fetchone()

        mycursor.execute("select numara from hasta where tckimlik='"+hbenn.get()+"'")
        son28=mycursor.fetchone()

        mycursor.execute("select eposta from hasta where tckimlik='"+hbenn.get()+"'")
        son29=mycursor.fetchone()

        mycursor.execute("select klinik from randevulist where tckimlik='"+hbenn.get()+"'")
        son30=mycursor.fetchone()
        


        tanı=Button(hastabilgi,text="Tanı Koy",command="")
        tanı.place(x=250,y=620)

        hben30.insert(0,hbenn.get())
        hben31.insert(0,son20)
        hben32.insert(0,son21)
        hben33.insert(0,son22)
        hben20.insert(0,son23)
        hben21.insert(0,son24)
        hben22.insert(0,son25)
        hben23.insert(0,son26)
        hben24.insert(0,son27)
        hben25.insert(0,son28)
        hben26.insert(0,son29)
        hben27.insert(0,son30)
  
    
def tanıiki():
    mycursor=veritabanı.cursor()
    mycursor.execute("select randevu_tarih from randevulist where tckimlik='"+hbenn.get()+"'")
    son53=mycursor.fetchone()

    kimlikal.insert(0,son53)

    
    if len(kimlikal.get())==0:
        messagebox.showinfo("HATA","LÜTFEN RANDEVU SEÇİNİZ")

        
        
    else:
        print(kimlikal.get())
        sorgu="INSERT INTO tanıverecete (hasta_adı,soyadı,tckimlik,tanı,recete,klinik,randevu_tarih)VALUES (%s,%s,%s,%s,%s,%s,%s)"
        deger=(hben31.get(),hben32.get(),hbenn.get(),text11.get("1.0",END),text22.get("1.0",END),hben27.get(),kimlikal.get())
        mycursor.execute(sorgu,deger)
        veritabanı.commit()
        onay60=Label(randevubilgi,font=("Jayes","10","bold"),text="GÖNDERİLDİ",fg="green",bg="Whitesmoke")
        onay60.place(x=770,y=650)
        onay60.after(3000, onay60.destroy)
        

def silbilgi():
    hben30.delete(0,'end')
    hben31.delete(0,'end')
    hben32.delete(0,'end')
    hben33.delete(0,'end')
    hben20.delete(0,'end')
    hben21.delete(0,'end')
    hben22.delete(0,'end')
    hben23.delete(0,'end')
    hben24.delete(0,'end')
    hben25.delete(0,'end')
    hben26.delete(0,'end')
    hben27.delete(0,'end')
  
    


  
gonder=Button(randevubilgi,image=gondbut,borderwidth=0,bg="whitesmoke",command=lambda:[tanıiki()])
gonder.place(x=760,y=600)
  
hastagor=Button(randevugor,image=bilgibut,borderwidth=0,bg="whitesmoke",command=lambda:[bilgis2()])
hastagor.place(x=950,y=620)



rantablo.bind('<Double 1>',tcal2)




#-------------------------------------------------------------------DOKTOR RANDEVU SİLME EKRANI-(fonksiyon yukarda)--------------------------------------------------------------------#

def silran2():
    if len(hbe3n.get())==0:
        messagebox.showinfo("HATA","LÜTFEN RANDEVU SEÇİNİZ")
    else:
        mycursor=veritabanı.cursor()
        mycursor.execute("Delete from randevulist where randevu_tarih='"+hbe3n.get()+"' and randevu_saat='"+konty.get()+"'")
        veritabanı.commit()
        goruntulee3()
        



hbe3n=Entry(randevusil,textvariable=y4,state="disabled")
hbe3n.place(x=950,y=570)

konty=Entry(randevusil,textvariable=y45,state="disabled")
konty.place(x=950,y=610)

siltablo.bind('<Double 1>',tcal3)
silbak=Button(randevusil,image=ransilbut,borderwidth=0,bg="whitesmoke",command=lambda:silran2())
silbak.place(x=950,y=640)






rangeri=Button(randevusil,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:show_frame(adminin))
rangeri.place(x=20,y=30)





buton16=Button(adminin,image=doktorbut3,bg="whitesmoke",borderwidth=0,command=lambda:[show_frame(randevusil),goruntulee3()])
buton16.place(x=100,y=450)



#---------------------------------------------------------------------------HASTA PROFİLİ RANDEVU İPTALİ-----------------------------------------------------------------------------#





scb6=Scrollbar(randevusilhasta)
scb6.pack(side=RIGHT,fill=Y)


hastasilran = ttk.Treeview(randevusilhasta, columns=( 2, 3, 4,5,6,7), show='headings', height=8)
hastasilran.pack(side=LEFT)


hastasilran.heading(2, text="AD")   
hastasilran.heading(3, text="SOYAD")
hastasilran.heading(4, text="KLİNİK")
hastasilran.heading(5, text="DOKTOR")
hastasilran.heading(6, text="RANDEVU SAATİ")
hastasilran.heading(7, text="RANDEVU TARİHİ")




scb6.config(command=hastasilran.yview)


def goruntulee4():
    hastasilran.delete(*hastasilran.get_children())
    mycursor=veritabanı.cursor()
    mycursor.execute("Select ad,soyad,klinik,doktorname,randevu_tarih,randevu_saat from randevulist where tckimlik='"+y8.get()+"'")
    dizdiz2=mycursor.fetchall()
    for rowrow2 in dizdiz2:
        hastasilran.insert('',END,values=rowrow2)
        







gerigel19=Button(randevusilhasta,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:show_frame(kullanıcı2in))
gerigel19.place(x=20,y=30)

tarihal=Entry(randevusilhasta,textvariable=y9)
tarihal.place(x=800,y=600)

saatal=Entry(randevusilhasta,textvariable=y10)
saatal.place(x=800,y=650)





hastasiltablo=Button(kullanıcı2in,image=hastabut3,borderwidth=0,bg="whitesmoke",command=lambda:[show_frame(randevusilhasta),goruntulee4()])
hastasiltablo.place(x=100,y=350)

hastasilran.bind('<Double 1>',tcal4)
altc=Button(randevusilhasta,image=ransilbut2,borderwidth=0,bg="whitesmoke",command=lambda:silran())
altc.place(x=950,y=615)


def silran():
    if len(saatal.get())==0 or len(tarihal.get())==0:
        messagebox.showinfo("HATA","LÜTFEN RANDEVU SEÇİNİZ")
    else:
        mycursor=veritabanı.cursor()
        mycursor.execute("Delete from randevulist where randevu_saat='"+saatal.get()+"' and randevu_tarih='"+tarihal.get()+"'")
        veritabanı.commit()
        goruntulee4()
        onay52=Label(randevusilhasta,font=("Jayes","10","bold"),text="RANDEVU İPTAL EDİLDİ",bg="whitesmoke",fg="green")
        onay52.place(x=1000,y=670)
        onay52.after(3000, onay52.destroy)









#--------------------------------------------------------------------------------HASTA REÇETE VE TANILARIM EKRANI----------------------------------------------------------------------#
y11=StringVar()
tcname2=Entry(tanırecete,textvariable=y11)

scb=Scrollbar(tanırecete)
scb.pack(side=RIGHT,fill=Y)





tanıtablo = ttk.Treeview(tanırecete,yscrollcommand=scb.set, columns=(1, 2, 3, 4,5), show='headings', height=8)
tanıtablo.pack(side=LEFT,padx=80)

tanıtablo.heading(1, text="TC KİMLİK")
tanıtablo.heading(2, text="RANDEVU TARİHİ")
tanıtablo.heading(3, text="KLİNİK")
tanıtablo.heading(4, text="TANI")
tanıtablo.heading(5, text="RECETE")

scb.config(command=tanıtablo.yview)




def goruntulee5():
    
    mycursor=veritabanı.cursor()
    mycursor.execute("select tckimlik from hasta where eposta ='"+adminmail.get()+ "' AND sifre ='"+adminpasswd.get()+"'")
    son55=mycursor.fetchone()

    
    tanıtablo.delete(*tanıtablo.get_children())
    mycursor.execute("Select tckimlik,randevu_tarih,klinik,tanı,recete from tanıverecete where tckimlik='"+tcname.get()+"'")
    dizdiz3=mycursor.fetchall()
    for rowrow4 in dizdiz3:
        tanıtablo.insert('',END,values=rowrow4)
   



gerigel20=Button(tanırecete,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(kullanıcı2in)])
gerigel20.place(x=20,y=30)

tanıbuton=Button(kullanıcı2in,image=hastabut2,borderwidth=0,bg="whitesmoke",command=lambda:[show_frame(tanırecete),goruntulee5()])
tanıbuton.place(x=100,y=450)





#*****************************************************************************KAYIT FORMU*****************************************************************#




hastatc2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta TC:",bg="Whitesmoke")
hastatc2.place(x=50,y=100)
tcentry2=Entry(kaydol)
tcentry2.place(x=200,y=100)

hastaadı2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Adı:",bg="Whitesmoke")
hastaadı2.place(x=50,y=140)
adentry2=Entry(kaydol)
adentry2.place(x=200,y=140)

hastasoyadı2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Soyadı",bg="Whitesmoke")
hastasoyadı2.place(x=50,y=180)
soyadentry2=Entry(kaydol)
soyadentry2.place(x=200,y=180)

cinsiyeti2=Label(kaydol,font=("Jayes","10","bold"),text="Cinsiyeti",bg="Whitesmoke")
cinsiyeti2.place(x=50,y=220)
cins2=ttk.Combobox(kaydol,width=17)
cins2['values']=two
cins2.bind('<<ComboboxSelected>>')
cins2.place(x=200,y=220)

kang2=Label(kaydol,font=("Jayes","10","bold"),text="Kan Grubu",bg="Whitesmoke")
kang2.place(x=50,y=260)
kangr2=ttk.Combobox(kaydol,width=17)
kangr2['values']=kan
kangr2.bind('<<ComboboxSelected>>')
kangr2.place(x=200,y=260)


hastadogumyeri2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Doğum Yeri",bg="Whitesmoke")
hastadogumyeri2.place(x=50,y=300)
hastadogumyerien2=Entry(kaydol)
hastadogumyerien2.place(x=200,y=300)

hastadogumtarihi2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Doğum Tarihi",bg="Whitesmoke")
hastadogumtarihi2.place(x=50,y=340)
hastadogumen2=Entry(kaydol)
hastadogumen2.place(x=200,y=340)

anaadı2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Anne Adı:",bg="Whitesmoke")
anaadı2.place(x=50,y=380)
anaen2=Entry(kaydol)
anaen2.place(x=200,y=380)

babaadı2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Baba Adı:",bg="Whitesmoke")
babaadı2.place(x=50,y=420)
babaen2=Entry(kaydol)
babaen2.place(x=200,y=420)

numara2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Cep Telefonu:",bg="Whitesmoke")
numara2.place(x=50,y=460)
numaraen2=Entry(kaydol)
numaraen2.place(x=200,y=460)



adres2=Label(kaydol,font=("Jayes","10","bold"),text="Hasta Adresi:",bg="Whitesmoke")
adres2.place(x=50,y=500)
adress2=Entry(kaydol)
adress2.place(x = 200,
        y = 500,
        width=300)

sifree2=Label(kaydol,font=("Jayes","10","bold"),text="Eposta:",bg="Whitesmoke")
sifree2.place(x=50,y=540)
sifre2=Entry(kaydol)
sifre2.place(x=200,y=540)

eposta3=Label(kaydol,font=("Jayes","10","bold"),text="Şifre Belirle:",bg="Whitesmoke")
eposta3.place(x=50,y=580)
epostaen3=Entry(kaydol)
epostaen3.place(x=200,y=580)


def hastakaydol():
    mycursor=veritabanı.cursor()
    mycursor.execute("select * from hasta where tckimlik='"+tcentry2.get()+"'")
    son50=mycursor.fetchall()
    if mycursor.rowcount > 0:
        messagebox.showinfo("HATA","BU KAYIT ZATEN VAR")
        

    elif len(adentry2.get())==0 or len(soyadentry2.get())==0 or len(tcentry2.get())==0 or len(cins2.get())==0 or len(numaraen2.get())==0 or len(sifre2.get())==0 or len(epostaen3.get())==0:
        messagebox.showinfo("EKSİK BİLGİ"," Formda eksik alanlar var")

        
    else:
        
        sorgu="INSERT INTO hasta (tckimlik,ad,soyad,cinsiyet,kan,dogumyeri,dogumtarihi,baba_adı,anne_adı,numara,adres,eposta,sifre)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        deger=(tcentry2.get(),adentry2.get(),soyadentry2.get(),cins2.get(),kangr2.get(),hastadogumyerien2.get(),hastadogumen2.get(),babaen2.get(),anaen2.get(),numaraen2.get(),adress2.get(),sifre2.get(),epostaen3.get())
        mycursor.execute(sorgu,deger)
        veritabanı.commit()
        print("Kayıt eklendi")
        sonson=Label(kaydol,bg="Whitesmoke",fg="green",text="Veri Tabanına Kaydedildi",font=("Open Sans","11","bold"))
        sonson.place(y=615,x=60)
        sonson.after(3000, sonson.destroy)
        
    




#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

def bilgisil20():
    tcentry2.delete(0,'end')
    adentry2.delete(0,'end')
    soyadentry2.delete(0,'end')
    cins2.delete(0,'end')
    kangr2.delete(0,'end')
    hastadogumyerien2.delete(0,'end')
    hastadogumen2.delete(0,'end')
    anaen2.delete(0,'end')
    babaen2.delete(0,'end')
    numaraen2.delete(0,'end')
    adress2.delete(0,'end')
    sifre2.delete(0,'end')
    epostaen3.delete(0,'end')
    



kaydolbuton2=Button(kaydol,image=tambut,borderwidth=0,bg="whitesmoke",command=lambda:[hastakaydol()])
kaydolbuton2.place(x=100,y=650)




gerige21=Button(kaydol,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:[show_frame(anaekran),bilgisil20()])
gerige21.place(x=20,y=30)





#**********************************************************************HASTA BİLGİSİ DÜZENLEME*************************************************************************#



def yazdır():
    tcentry3.config(state="normal")
    soyadentry3.config(state="normal")
    adentry3.config(state="normal")
    cins3.config(state="normal")
    kangr3.config(state="normal")
    hastadogumyerien3.config(state="normal")
    hastadogumen3.config(state="normal")
    anaen3.config(state="normal")
    babaen3.config(state="normal")
    numaraen3.config(state="normal")
    adress3.config(state="normal")
    sifre3.config(state="normal")
    epostaen4.config(state="normal")

    tcentry3.delete(0,"end")
    soyadentry3.delete(0,"end")
    adentry3.delete(0,"end")
    cins3.delete(0,"end")
    kangr3.delete(0,"end")
    hastadogumyerien3.delete(0,"end")
    hastadogumen3.delete(0,"end")
    anaen3.delete(0,"end")
    babaen3.delete(0,"end")
    numaraen3.delete(0,"end")
    adress3.delete(0,"end")
    sifre3.delete(0,"end")
    epostaen4.delete(0,"end")

    tcentry3.config(state="normal")
    soyadentry3.config(state="normal")
    adentry3.config(state="normal")
    cins3.config(state="normal")
    kangr3.config(state="normal")
    hastadogumyerien3.config(state="normal")
    hastadogumen3.config(state="normal")
    anaen3.config(state="normal")
    babaen3.config(state="normal")
    numaraen3.config(state="normal")
    adress3.config(state="normal")
    sifre3.config(state="normal")
    epostaen4.config(state="normal")

    mycursor=veritabanı.cursor()
    mycursor.execute("select tckimlik from hasta where tckimlik='"+taketc.get()+"'" )
    son60=mycursor.fetchone()

    mycursor.execute("select ad from hasta where tckimlik='"+taketc.get()+"'" )
    son61=mycursor.fetchone()

    mycursor.execute("select soyad from hasta where tckimlik='"+taketc.get()+"'" )
    son62=mycursor.fetchone()

    mycursor.execute("select cinsiyet from hasta where tckimlik='"+taketc.get()+"'" )
    son63=mycursor.fetchone()

    mycursor.execute("select kan from hasta where tckimlik='"+taketc.get()+"'" )
    son64=mycursor.fetchone()

    mycursor.execute("select dogumyeri from hasta where tckimlik='"+taketc.get()+"'" )
    son65=mycursor.fetchone()

    mycursor.execute("select dogumtarihi from hasta where tckimlik='"+taketc.get()+"'" )
    son66=mycursor.fetchone()

    mycursor.execute("select anne_adı from hasta where tckimlik='"+taketc.get()+"'" )
    son67=mycursor.fetchone()

    mycursor.execute("select baba_adı from hasta where tckimlik='"+taketc.get()+"'" )
    son68=mycursor.fetchone()

    mycursor.execute("select numara from hasta where tckimlik='"+taketc.get()+"'" )
    son69=mycursor.fetchone()

    mycursor.execute("select adres from hasta where tckimlik='"+taketc.get()+"'" )
    son70=mycursor.fetchone()

    mycursor.execute("select sifre from hasta where tckimlik='"+taketc.get()+"'" )
    son71=mycursor.fetchone()

    mycursor.execute("select eposta from hasta where tckimlik='"+taketc.get()+"'" )
    son72=mycursor.fetchone()

    tcentry3.insert(0,son60)
    soyadentry3.insert(0,son62)
    adentry3.insert(0,son61)
    cins3.insert(0,son63)
    kangr3.insert(0,son64)
    hastadogumyerien3.insert(0,son65)
    hastadogumen3.insert(0,son66)
    anaen3.insert(0,son67)
    babaen3.insert(0,son68)
    numaraen3.insert(0,son69)
    adress3.insert(0,son70)
    sifre3.insert(0,son71)
    epostaen4.insert(0,son72)

    



def update6():
    mycursor=veritabanı.cursor()
    mycursor.execute("UPDATE hasta SET tckimlik='"+tcentry3.get()+"',ad='"+adentry3.get()+"',soyad='"+soyadentry3.get()+"',cinsiyet='"+cins3.get()+"',kan='"+kangr3.get()+"',dogumyeri='"+hastadogumyerien3.get()+"',dogumtarihi='"+hastadogumen3.get()+"',anne_adı='"+anaen3.get()+"',baba_adı='"+babaen3.get()+"',numara='"+numaraen3.get()+"',adres='"+adress3.get()+"',sifre='"+sifre3.get()+"',eposta='"+epostaen4.get()+"' where tckimlik='"+taketc.get()+"'")
    veritabanı.commit()
    tcentry3.delete(0,'end')
    adentry3.delete(0,'end')
    soyadentry3.delete(0,'end')
    cins3.delete(0,'end')
    kangr3.delete(0,'end')
    hastadogumyerien3.delete(0,'end')
    hastadogumen3.delete(0,'end')
    anaen3.delete(0,'end')
    babaen3.delete(0,'end')
    numaraen3.delete(0,'end')
    adress3.delete(0,'end')
    sifre3.delete(0,'end')
    epostaen4.delete(0,'end')

    tcentry3.config(state="disabled")
    soyadentry3.config(state="disabled")
    adentry3.config(state="disabled")
    cins3.config(state="disabled")
    kangr3.config(state="disabled")
    hastadogumyerien3.config(state="disabled")
    hastadogumen3.config(state="disabled")
    anaen3.config(state="disabled")
    babaen3.config(state="disabled")
    numaraen3.config(state="disabled")
    adress3.config(state="disabled")
    sifre3.config(state="disabled")
    epostaen4.config(state="disabled")
    
    








taketc=Entry(guncelle,textvariable=y13,state="disabled")
taketc.place(x=100,y=570)

scb2=Scrollbar(guncelle)
scb2.pack(side=RIGHT,fill=Y)



duzentablo = ttk.Treeview(guncelle, columns=(1, 2, 3, 4), show='headings', height=8)
duzentablo.place(x=50,y=200)

duzentablo.heading(1, text="TC Kimlik")
duzentablo.heading(2, text="AD")
duzentablo.heading(3, text="SOYAD")
duzentablo.heading(4, text="eposta")



scb2.config(command=duzentablo.yview)

def disable():
  
    tcentry3.config(state="disabled")
    soyadentry3.config(state="disabled")
    adentry3.config(state="disabled")
    cins3.config(state="disabled")
    kangr3.config(state="disabled")
    hastadogumyerien3.config(state="disabled")
    hastadogumen3.config(state="disabled")
    anaen3.config(state="disabled")
    babaen3.config(state="disabled")
    numaraen3.config(state="disabled")
    adress3.config(state="disabled")
    sifre3.config(state="disabled")
    epostaen4.config(state="disabled")



def goruntulee6():
    duzentablo.delete(*duzentablo.get_children())
    mycursor=veritabanı.cursor()
    mycursor.execute("SELECt tckimlik,ad,soyad,eposta from hasta")
    diz5=mycursor.fetchall()
    for row5 in diz5:
        duzentablo.insert('',END,values=row5)



duzentablo.bind('<Double 1>',tcal6)

takebuton=Button(guncelle,image=bilgilistbut,borderwidth=0,bg="whitesmoke",command=lambda:[yazdır()])
takebuton.place(x=100,y=600)









hastatc3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta TC:",bg="whitesmoke")
hastatc3.place(x=860,y=100)
tcentry3=Entry(guncelle)
tcentry3.place(x=1050,y=100)

hastaadı3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Adı:",bg="whitesmoke")
hastaadı3.place(x=860,y=140)
adentry3=Entry(guncelle)
adentry3.place(x=1050,y=140)

hastasoyadı3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Soyadı",bg="whitesmoke")
hastasoyadı3.place(x=860,y=180)
soyadentry3=Entry(guncelle)
soyadentry3.place(x=1050,y=180)

cinsiyeti3=Label(guncelle,font=("Jayes","10","bold"),text="Cinsiyeti",bg="whitesmoke")
cinsiyeti3.place(x=860,y=220)
cins3=ttk.Combobox(guncelle,width=17)
cins3['values']=two
cins3.bind('<<ComboboxSelected>>')
cins3.place(x=1050,y=220)

kang3=Label(guncelle,font=("Jayes","10","bold"),text="Kan Grubu",bg="whitesmoke")
kang3.place(x=860,y=260)
kangr3=ttk.Combobox(guncelle,width=17)
kangr3['values']=kan
kangr3.bind('<<ComboboxSelected>>')
kangr3.place(x=1050,y=260)


hastadogumyeri3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Doğum Yeri",bg="whitesmoke")
hastadogumyeri3.place(x=860,y=300)
hastadogumyerien3=Entry(guncelle)
hastadogumyerien3.place(x=1050,y=300)

hastadogumtarihi3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Doğum Tarihi",bg="whitesmoke")
hastadogumtarihi3.place(x=860,y=340)
hastadogumen3=Entry(guncelle)
hastadogumen3.place(x=1050,y=340)

anaadı3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Anne Adı:",bg="whitesmoke")
anaadı3.place(x=860,y=380)
anaen3=Entry(guncelle)
anaen3.place(x=1050,y=380)

babaadı3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Baba Adı:",bg="whitesmoke")
babaadı3.place(x=860,y=420)
babaen3=Entry(guncelle)
babaen3.place(x=1050,y=420)

numara3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Cep Telefonu:",bg="whitesmoke")
numara3.place(x=860,y=460)
numaraen3=Entry(guncelle)
numaraen3.place(x=1050,y=460)



adres3=Label(guncelle,font=("Jayes","10","bold"),text="Hasta Adresi:",bg="whitesmoke")
adres3.place(x=860,y=500)
adress3=Entry(guncelle)
adress3.place(x = 1050,
        y = 500,
        width=300)

sifree3=Label(guncelle,font=("Jayes","10","bold"),text="Eposta:",bg="whitesmoke")
sifree3.place(x=860,y=540)
sifre3=Entry(guncelle)
sifre3.place(x=1050,y=580)

eposta4=Label(guncelle,font=("Jayes","10","bold"),text="Şifre Belirle:",bg="whitesmoke")
eposta4.place(x=860,y=580)
epostaen4=Entry(guncelle)
epostaen4.place(x=1050,y=540)












gerige22=Button(guncelle,image=gerires,bg="lightslategray",borderwidth=0,activebackground="lightslategray",command=lambda:show_frame(kullanıcı1in))
gerige22.place(x=20,y=30)


guncelbuton=Button(kullanıcı1in,image=danısmanbut,borderwidth=0,bg="whitesmoke",command=lambda:[show_frame(guncelle),goruntulee6(),disable()])
guncelbuton.place(x=200,y=250)





guncelbuton2=Button(guncelle,image=bilgbut,borderwidth=0,bg="whitesmoke",command=lambda:[update6(),goruntulee6(),onay50()])
guncelbuton2.place(x=860,y=650)



    
def onay50():
    onayy50=Label(guncelle,font=("Jayes","10","bold"),text="BİLGİLER GÜNCELLENDİ",bg="whitesmoke",fg="green")
    onayy50.place(x=990,y=650)
    onayy50.after(3000, onayy50.destroy)







#----------------------------------------------------------------------------SCROLLBAR---------------------------------------------------------------------#




















veritabanı=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gorsel2",
    buffered=True)

mycursor=veritabanı.cursor()


print(mycursor.rowcount,"kayıt eklendi")
mainloop()

