from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib
import codecs


def clear():
     bathsoapEntry.delete(0,END)
     facecreamEntry.delete(0,END)
     hairsprayEntry.delete(0,END)
     hairgelEntry.delete(0,END)
     bodylotionEntry.delete(0,END)
     facewashEntry.delete(0,END)
 
     riceEntry.delete(0,END)
     oilEntry.delete(0,END)
     beansEntry.delete(0,END)
     garriEntry.delete(0,END)
     semoEntry.delete(0,END)
     pastaEntry.delete(0,END)

     cokeEntry.delete(0,END)
     pepsiEntry.delete(0,END)
     spriteEntry.delete(0,END)
     sosaEntry.delete(0,END)
     schweppesEntry.delete(0,END)
     fantaEntry.delete(0,END)

     bathsoapEntry.insert(0,0)
     facecreamEntry.insert(0,0)
     hairsprayEntry.insert(0,0)
     hairgelEntry.insert(0,0)
     bodylotionEntry.insert(0,0)
     facewashEntry.insert(0,0)

     riceEntry.insert(0,0)
     oilEntry.insert(0,0)
     beansEntry.insert(0,0)
     garriEntry.insert(0,0)
     semoEntry.insert(0,0)
     pastaEntry.insert(0,0)

     cokeEntry.insert(0,0)
     pepsiEntry.insert(0,0)
     spriteEntry.insert(0,0)
     sosaEntry.insert(0,0)
     schweppesEntry.insert(0,0)
     fantaEntry.insert(0,0)

     cosmetictaxEntry.delete(0,END)
     grocerytaxEntry.delete(0,END)
     colddrinktaxEntry.delete(0,END)

     cosmeticpriceEntry.delete(0,END)
     grocerypriceEntry.delete(0,END)
     colddrinkpriceEntry.delete(0,END)

     nameEntry.delete(0,END)
     phoneEntry.delete(0,END)
     billnumberEntry.delete(0,END)

     textarea.delete(1.0,END)

def send_email():
     def send_gmail():
         try: 
               ob=smtplib.SMTP('smtp.gmail.com',587)
               ob.starttls()
               ob.login(senderEntry.get(),passwordEntry.get())
               message=email_textarea.get(1.0,END)
               ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
               ob.quit()
               messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
               root1.destroy()
         except:
             messagebox.showerror('Error','Something went wrong,Please try again',parent=root1)    
     if textarea.get(1.0, END) == '\n':
          messagebox.showerror('Error', 'Bill is Empty')
     else:
          root1=Toplevel()
          root.grab_set()
          root1.title('Send gmail')
          root1.config(bg='Black')
          root1.resizable(0,0)

          senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='black',fg='white')
          senderFrame.grid(row=0,column=0,padx=40,pady=20)

          senderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bg='black',fg='white')
          senderLabel.grid(row=0,column=0,padx=10,pady=8)

          senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
          senderEntry.grid(row=0,column=1,padx=10,pady=8)


          passwordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bg='black',fg='white')
          passwordLabel.grid(row=1,column=0,padx=10,pady=8)

          passwordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
          passwordEntry.grid(row=1,column=1,padx=10,pady=8)


          recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='black',fg='white')
          recipientFrame.grid(row=1,column=0,padx=40,pady=20)

          recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bg='black',fg='white')
          recieverLabel.grid(row=0,column=0,padx=10,pady=8)

          recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
          recieverEntry.grid(row=0,column=1,padx=10,pady=8)

          messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bg='black',fg='white')
          messageLabel.grid(row=1,column=0,padx=10,pady=8)

     
          email_textarea=Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
          email_textarea.grid(row=2,column=0,columnspan=2)
          email_textarea.delete(1.0,END)
          email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))


          sendButton=Button(root1,text='SEND',font=('arial',16,'bold'),width=15,command=send_gmail)
          sendButton.grid(row=2,column=0,pady=20)


          root1.mainloop()
          


def print_bill():
     if textarea.get(1.0, END) == '\n':
          messagebox.showerror('Error', 'Bill is Empty')
     else:
          file = tempfile.mktemp('.txt')
          with codecs.open(file, 'w', encoding='utf-8') as f:
              f.write(textarea.get(1.0, END))
          os.startfile(file, 'print')



def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberEntry.get():
            f = open(f'bills/{i}', 'r',encoding='utf-8')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()    
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')

     

if not os.path.exists('bills'):
     os.mkdir('bills')

def save_bill():
    global billnumber
    result = messagebox.askyesno('Confirm', 'Do you want to save the bill?')
    if result:
        bill_content = textarea.get(1.0, END)
        with open(f'bills/{billnumber}.txt', 'w', encoding='utf-8') as file:
            file.write(bill_content)
        messagebox.showinfo('Success', f'Bill number {billnumber} is saved successfully')
        billnumber = random.randint(100, 1000)
 


billnumber=random.randint(100,1000)
def bill_area():
   if nameEntry.get()=='' or phoneEntry.get()=='':
      messagebox.showerror('Error','Customer Details Are Required')
   elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and colddrinkpriceEntry.get()=='':
      messagebox.showerror('Error','No Product Are Selected')
   elif cosmeticpriceEntry.get()=='₦ 0' and grocerypriceEntry.get()=='₦ 0' and colddrinkpriceEntry.get=='₦ 0':
      messagebox.showerror('Error','No Product Are Selected')
   else:
          textarea.delete(1.0,END)

          textarea.insert(END,'\t\t**WELCOME CUSTOMER**\n')
          textarea.insert(END,f'\nBill Number: {billnumber}')
          textarea.insert(END,f'\nCustomer Name:{nameEntry.get()}')
          textarea.insert(END,f'\nCustomer Phone Number:{phoneEntry.get()}')
          textarea.insert(END,'\n=======================================================')
          textarea.insert(END,'Product\t\t\tQuantity\t\tPrice')
          textarea.insert(END,'\n=======================================================')
          if bathsoapEntry.get()!='0':
               textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t₦{soapprice}')
          if facecreamEntry.get()!='0':
               textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t₦{facecreamprice}')
          if facewashEntry.get()!='0':
               textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t₦{facewashprice}')
          if hairsprayEntry.get()!='0':
               textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t₦{hairsprayprice}')
          if hairgelEntry.get()!='0':
               textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t₦{hairgelprice}')
          if bodylotionEntry.get()!='0':
               textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t₦{bodylotionprice}')

          if riceEntry.get()!='0':
               textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t₦{riceprice}')
          if oilEntry.get()!='0':
               textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t₦{oilprice}')
          if beansEntry.get()!='0':
               textarea.insert(END,f'\nBeans\t\t\t{beansEntry.get()}\t\t₦{beansprice}')
          if garriEntry.get()!='0':
               textarea.insert(END,f'\nGarri\t\t\t{garriEntry.get()}\t\t₦{garriprice}')
          if semoEntry.get()!='0':
               textarea.insert(END,f'\nSemo\t\t\t{semoEntry.get()}\t\t₦{semoprice}')   
          if pastaEntry.get()!='0':
               textarea.insert(END,f'\nPasta\t\t\t{pastaEntry.get()}\t\t₦{pastaprice}')      


          if cokeEntry.get()!='0':
               textarea.insert(END,f'\nCoca Cola\t\t\t{cokeEntry.get()}\t\t₦{cokeprice}')
          if fantaEntry.get()!='0':
               textarea.insert(END,f'\nFanta\t\t\t{fantaEntry.get()}\t\t₦{fantaprice}')   
          if pepsiEntry.get()!='0':
               textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t₦{pepsiprice}')   
          if spriteEntry.get()!='0':
               textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t₦{spriteprice}')         
          if sosaEntry.get()!='0':
               textarea.insert(END,f'\nSosa\t\t\t{sosaEntry.get()}\t\t₦{sosaprice}')  
          if schweppesEntry.get()!='0':
               textarea.insert(END,f'\nSchweppes\t\t\t{schweppesEntry.get()}\t\t₦{schweppesprice}')        
          textarea.insert(END,'\n-------------------------------------------------------')

          if cosmetictaxEntry.get()!='₦0.0':
               textarea.insert(END,f'\n Cosmetic Tax\t\t\t\t\t {cosmetictaxEntry.get()}')
          if grocerytaxEntry.get()!='₦0.0':
               textarea.insert(END,f'\n Grocery Tax\t\t\t\t\t {grocerytaxEntry.get()}')
          if colddrinktaxEntry.get()!='₦0.0':
               textarea.insert(END,f'\n Soda Tax\t\t\t\t\t {colddrinktaxEntry.get()}')
          textarea.insert(END,'\n=======================================================')
          textarea.insert(END,f'\nTotal Bill\t\t\t\t\t₦{totalbill}')
          textarea.insert(END,'\n=======================================================')
          save_bill()
def total():
   global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
   global riceprice,oilprice,beansprice,garriprice,semoprice,pastaprice
   global cokeprice,fantaprice,pepsiprice,spriteprice,sosaprice,schweppesprice
   global totalbill

   #cosmetics price calculation
   soapprice=int(bathsoapEntry.get())*1500
   facecreamprice=int(facecreamEntry.get())*2000
   facewashprice=int(facewashEntry.get())*3000
   hairsprayprice=int(hairsprayEntry.get())*1500
   hairgelprice=int(hairgelEntry.get())*700
   bodylotionprice=int(bodylotionEntry.get())*2200

   totalcometicprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
   cosmeticpriceEntry.delete(0,END)
   cosmeticpriceEntry.insert(0,f'₦ {totalcometicprice}')
   cosmetictax=totalcometicprice*0.075
   cosmetictaxEntry.delete(0,END)
   cosmetictaxEntry.insert(0,'₦'+str(cosmetictax))

   #grocery price calculation
   riceprice=int(riceEntry.get())*1000
   oilprice=int(oilEntry.get())*1500
   beansprice=int(beansEntry.get())*800
   garriprice=int(garriEntry.get())*400
   semoprice=int(semoEntry.get())*1200
   pastaprice=int(pastaEntry.get())*600

   totalgroceryprice=riceprice+oilprice+beansprice+garriprice+semoprice+pastaprice
   grocerypriceEntry.delete(0,END)
   grocerypriceEntry.insert(0,f'₦ {totalgroceryprice}')

   grocerytax=totalgroceryprice*0.0
   grocerytaxEntry.delete(0,END)
   grocerytaxEntry.insert(0,'₦'+str(grocerytax))

   #soda price calculation
   cokeprice=int(cokeEntry.get())*250 
   fantaprice=int(fantaEntry.get())*250
   pepsiprice=int(pepsiEntry.get())*250
   spriteprice=int(spriteEntry.get())*200
   sosaprice=int(sosaEntry.get())*700
   schweppesprice=int(schweppesEntry.get())*500

   totalcolddrinkprice=cokeprice+fantaprice+pepsiprice+spriteprice+sosaprice+schweppesprice
   colddrinkpriceEntry.delete(0,END)
   colddrinkpriceEntry.insert(0,f'₦ {totalcolddrinkprice}')

   colddrinktax=totalcolddrinkprice*0.01
   colddrinktaxEntry.delete(0,END)
   colddrinktaxEntry.insert(0,'₦'+str(colddrinktax))
                             
   totalbill=totalgroceryprice+totalcolddrinkprice+cosmetictax+grocerytax+colddrinktax+totalcometicprice


root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')

headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='Dark Orchid1',fg='gold',bd=12,relief=RIDGE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='Dark Orchid1')
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame, text='Name',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')
nameLabel.grid(row=0,column=0,padx=20,pady=2)


def validate_name_input(P):
    # P is the proposed input
    if P.isalpha() or P == "":
        return True
    else:
        return False

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18,validate="key",validatecommand=(validate_name_input, "%P"))
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame, text='Phone Number',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame, text='Bill Number',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='Dark Orchid1')
cosmeticFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black',)

bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)


facecreamLabel=Label(cosmeticFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black',)

facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)


facewashLabel=Label(cosmeticFrame,text='Face Wash',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black',)

facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)


hairsprayLabel=Label(cosmeticFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black',)

hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black',)

hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black',)

bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='Dark Orchid1')
groceryFrame.grid(row=0,column=1)


riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)


oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)


beansLabel=Label(groceryFrame,text='Beans',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

beansLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

beansEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
beansEntry.grid(row=2,column=1,pady=9,padx=10)
beansEntry.insert(0,0)


garriLabel=Label(groceryFrame,text='Garri',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

garriLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

garriEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
garriEntry.grid(row=3,column=1,pady=9,padx=10)
garriEntry.insert(0,0)

semoLabel=Label(groceryFrame,text='Semo',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

semoLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

semoEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
semoEntry.grid(row=4,column=1,pady=9,padx=10)
semoEntry.insert(0,0)


pastaLabel=Label(groceryFrame,text='Pasta',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

pastaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

pastaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pastaEntry.grid(row=5 ,column=1,pady=9,padx=10)
pastaEntry.insert(0,0)

colddrinkFrame=LabelFrame(productsFrame,text='Soda',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='Dark Orchid1')
colddrinkFrame.grid(row=0,column=2)


cokeLabel=Label(colddrinkFrame,text='Coca Cola',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

cokeLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cokeEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cokeEntry.grid(row=0,column=1,pady=9,padx=10)
cokeEntry.insert(0,0)

fantaLabel=Label(colddrinkFrame,text='Fanta',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

fantaLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

fantaEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fantaEntry.grid(row=1,column=1,pady=9,padx=10)
fantaEntry.insert(0,0)

pepsiLabel=Label(colddrinkFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

pepsiLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

pepsiEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=2,column=1,pady=9,padx=10)
pepsiEntry.insert(0,0)

spriteLabel=Label(colddrinkFrame,text='Sprite',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

spriteLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=3,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

sosaLabel=Label(colddrinkFrame,text='Sosa',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

sosaLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sosaEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sosaEntry.grid(row=4,column=1,pady=9,padx=10)
sosaEntry.insert(0,0)

schweppesLabel=Label(colddrinkFrame,text='Schweppes',font=('times new roman',15,'bold'),bg='Dark Orchid1',fg='black')

schweppesLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

schweppesEntry=Entry(colddrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
schweppesEntry.grid(row=5 ,column=1,pady=9,padx=10)
schweppesEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='Dark Orchid1')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',13,'bold'),bg='Dark Orchid1',fg='black')
cosmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',13,'bold'),bg='Dark Orchid1',fg='black')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

colddrinkpriceLabel=Label(billmenuFrame,text='Soda Price',font=('times new roman',13,'bold'),bg='Dark Orchid1',fg='black')
colddrinkpriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

colddrinkpriceEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinkpriceEntry.grid(row=2,column=1,pady=9,padx=10)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',13,'bold'),bg='Dark Orchid1',fg='black')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',13,'bold'),bg='Dark Orchid1',fg='black')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

colddrinktaxLabel=Label(billmenuFrame,text='Soda Tax',font=('times new roman',13,'bold'),bg='Dark Orchid1',fg='black')
colddrinktaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

colddrinktaxEntry=Entry(billmenuFrame,font=('times new roman',13,'bold'),width=10,bd=5)
colddrinktaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='TOTAL',font=('arial',16,'bold'),bg='Dark Orchid1',fg='black',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='BILL',font=('arial',16,'bold'),bg='Dark Orchid1',fg='black',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='EMAIL',font=('arial',16,'bold'),bg='Dark Orchid1',fg='black',bd=5,width=8,pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='PRINT',font=('arial',16,'bold'),bg='Dark Orchid1',fg='black',bd=5,width=8,pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='CLEAR',font=('arial',16,'bold'),bg='Dark Orchid1',fg='black',bd=5,width=8,pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)




root.mainloop() 