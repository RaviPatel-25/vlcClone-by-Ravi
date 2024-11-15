from tkinter import*
from PIL import Image, ImageTk

class App:

        def __init__(self,root):

        	self.root=root

        	self.w=self.root.winfo_screenwidth()

        	self.h=self.root.winfo_screenheight()

        	

        	self.root.overrideredirect(True)

        	self.root.geometry(str(self.w)+"x"+str(self.h)+"+0+0")

        	self.root.config(bg="#131313")

        	

        	image1 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Video.jpg')

        	image2 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Audio.jpg')

        	image3 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Browse.jpg')

        	image4 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Playlists.jpg')

        	image5 = Image.open('/storage/emulated/0/Pythonimage/Newpy/More.jpg')

        	image6 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Set.jpg')

        	image7 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Mode.jpg')

        	image8 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Logo.jpg')

        	image9 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Music.jpg')

        	image10 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Movies.jpg')

        	image11 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Download.jpg')

        	image12 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Internal.jpg')

        	image13 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Nocon.jpg')

        	image14 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Viderror.jpg')

        	image15 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Audiopic.jpg')

        	image16 = Image.open('/storage/emulated/0/Pythonimage/Newpy/Morepic.jpg')

        	

        	

        	resize_image1 = image1.resize((70, 70))

        	resize_image2 = image2.resize((70, 70))

        	resize_image3 = image3.resize((70, 70))

        	resize_image4 = image4.resize((70, 70))

        	resize_image5 = image5.resize((70, 70))

        	resize_image6 = image6.resize((70, 70))

        	resize_image7 = image7.resize((70, 70))

        	resize_image8 = image8.resize((300, 150))

        	resize_image9 = image9.resize((300, 300))

        	resize_image10 = image10.resize((300, 300))

        	resize_image11 = image11.resize((300, 300))

        	resize_image12 = image12.resize((300, 300))

        	resize_image13 = image13.resize((900, 350))

        	resize_image14 = image14.resize((1100, 600))

        	resize_image15 = image15.resize((self.w, self.h-150))

        	resize_image16 = image16.resize((self.w, self.h-150))

        

        

        

        	self.img1 = ImageTk.PhotoImage(resize_image1)

        	self.img2 = ImageTk.PhotoImage(resize_image2)

        	self.img3 = ImageTk.PhotoImage(resize_image3)

        	self.img4 = ImageTk.PhotoImage(resize_image4)

        	self.img5 = ImageTk.PhotoImage(resize_image5)

        	self.img6 = ImageTk.PhotoImage(resize_image6)

        	self.img7 = ImageTk.PhotoImage(resize_image7)

        	self.img8 = ImageTk.PhotoImage(resize_image8)

        	self.img9 = ImageTk.PhotoImage(resize_image9)

        	self.img10 = ImageTk.PhotoImage(resize_image10)

        	self.img11 = ImageTk.PhotoImage(resize_image11)

        	self.img12 = ImageTk.PhotoImage(resize_image12)

        	self.img13 = ImageTk.PhotoImage(resize_image13)

        	self.img14 = ImageTk.PhotoImage(resize_image14)

        	self.img15 = ImageTk.PhotoImage(resize_image15)

        	self.img16 = ImageTk.PhotoImage(resize_image16)

        	

        def main(self):

        	mainlbl=Label(self.root,bg="#131313")

        	mainlbl.place(x=0,y=0,width=self.w,height=self.h)

        	#header

        	labelh=Label(mainlbl,bg="#131313")

        	labelh.place(x=0,y=0,width=self.w,height=150)

        	lbllogo=Label(labelh,image=self.img8,bg="#131313")

        	lbllogo.place(x=20,y=0)

        	btnset=Button(labelh,bg="#2A3A2A",bd=0,image=self.img6)

        	btnmode=Button(labelh,bg="#2A2A2A",bd=0,image=self.img7)

        	

        	lblfav=Label(mainlbl,text="Favorites",font=("Arial",10),fg="#FF7D01",bg="#131313")

        	lblfav.place(x=50,y=230)

        	lblstore=Label(mainlbl,text="Storages",font=("Arial",10),fg="#FF7D01",bg="#131313")

        	lblstore.place(x=50,y=730)

        	lbllocal=Label(mainlbl,text="Local Network",font=("Arial",10),fg="#FF7D01",bg="#131313")

        	lbllocal.place(x=50,y=1250)

        	lblnocon=Label(mainlbl,image=self.img13,bg="#131313")

        	lblnocon.place(x=100,y=1350)

        	

        	btnmusic=Button(mainlbl,bg="#2A2A2A",bd=0,image=self.img9)

        	btnmovies=Button(mainlbl,bg="#2A2A2A",bd=0,image=self.img10)

        	btndownload=Button(mainlbl,bg="#2A2A2A",bd=0,image=self.img11)

        	btninternal=Button(mainlbl,bg="#2A2A2A",bd=0,image=self.img12)

        	

        	

        	btnmusic.place(x=690,y=330)

        	btnmovies.place(x=370,y=330)

        	btndownload.place(x=50,y=330)

        	btninternal.place(x=50,y=840)

        	

        	btnset.place(x=self.w-100,y=30,width=80,height=80)

        	btnmode.place(x=self.w-200,y=30,width=80,height=80)

        	#footer

        	label=Label(mainlbl,bg="#2A2A2A")

        	label.place(x=0,y=self.h-150,width=self.w,height=150)

        	txtlabel=Label(label,bg="#2A2A2A",fg="white",text="Video              Audio            Browse           Playlists            More",font=('Arial',6))

        	txtlabel.place(x=0,y=100,width=self.w,height=50)

        	btn1=Button(label,bg="#2A2A2A",bd=0,image=self.img1,command=self.video)

        	btn2=Button(label,bg="#2A2A2A",bd=0,image=self.img2,command=self.audio)

        	btn3=Button(label,bg="#2A2A2A",bd=0,image=self.img3,command=self.main)

        	btn4=Button(label,bg="#2A2A2A",bd=0,image=self.img4,command=self.playlists)

        	btn5=Button(label,bg="#2A2A2A",bd=0,image=self.img5,command=self.more)

       

        	btn1.place(x=100,y=10,width=80,height=80)

        	btn2.place(x=300,y=10,width=80,height=80)

        	btn3.place(x=500,y=10,width=80,height=80)

        	btn4.place(x=700,y=10,width=80,height=80)

        	btn5.place(x=900,y=10,width=80,height=80)

        	

        def video(self):

        	mainlbl=Label(self.root,bg="#131313")

        	mainlbl.place(x=0,y=0,width=self.w,height=self.h)

        	#header

        	labelh=Label(mainlbl,bg="#131313")

        	labelh.place(x=0,y=0,width=self.w,height=150)

        	lbllogo=Label(labelh,image=self.img8,bg="#131313")

        	lbllogo.place(x=20,y=0)

        	

        	labelerror=Label(mainlbl,image=self.img14,bg="#131313")

        	labelerror.place(x=0,y=900,width=1100,height=600)

        	

        	#footer

        	label=Label(mainlbl,bg="#2A2A2A")

        	label.place(x=0,y=self.h-150,width=self.w,height=150)

        	txtlabel=Label(label,bg="#2A2A2A",fg="white",text="Video              Audio            Browse           Playlists            More",font=('Arial',6))

        	txtlabel.place(x=0,y=100,width=self.w,height=50)

        	btn1=Button(label,bg="#2A2A2A",bd=0,image=self.img1,command=self.video)

        	btn2=Button(label,bg="#2A2A2A",bd=0,image=self.img2,command=self.audio)

        	btn3=Button(label,bg="#2A2A2A",bd=0,image=self.img3,command=self.main)

        	btn4=Button(label,bg="#2A2A2A",bd=0,image=self.img4,command=self.playlists)

        	btn5=Button(label,bg="#2A2A2A",bd=0,image=self.img5,command=self.more)

       

        	btn1.place(x=100,y=10,width=80,height=80)

        	btn2.place(x=300,y=10,width=80,height=80)

        	btn3.place(x=500,y=10,width=80,height=80)

        	btn4.place(x=700,y=10,width=80,height=80)

        	btn5.place(x=900,y=10,width=80,height=80)

        	

        def audio(self):

        	mainlbl=Label(self.root,image=self.img15,bg="#131313")

        	mainlbl.place(x=0,y=0,width=self.w,height=self.h-150)	

        	pass

        def playlists(self):

        	mainlbl=Label(self.root,bg="#131313")

        	mainlbl.place(x=0,y=0,width=self.w,height=self.h)

        	#header

        	labelh=Label(mainlbl,bg="#131313")

        	labelh.place(x=0,y=0,width=self.w,height=150)

        	lbllogo=Label(labelh,image=self.img8,bg="#131313")

        	lbllogo.place(x=20,y=0)

        	

        	labelerror=Label(mainlbl,image=self.img14,bg="#131313")

        	labelerror.place(x=0,y=900,width=1100,height=600)

        	

        	#footer

        	label=Label(mainlbl,bg="#2A2A2A")

        	label.place(x=0,y=self.h-150,width=self.w,height=150)

        	txtlabel=Label(label,bg="#2A2A2A",fg="white",text="Video              Audio            Browse           Playlists            More",font=('Arial',6))

        	txtlabel.place(x=0,y=100,width=self.w,height=50)

        	btn1=Button(label,bg="#2A2A2A",bd=0,image=self.img1,command=self.video)

        	btn2=Button(label,bg="#2A2A2A",bd=0,image=self.img2,command=self.audio)

        	btn3=Button(label,bg="#2A2A2A",bd=0,image=self.img3,command=self.main)

        	btn4=Button(label,bg="#2A2A2A",bd=0,image=self.img4,command=self.playlists)

        	btn5=Button(label,bg="#2A2A2A",bd=0,image=self.img5,command=self.more)

       

        	btn1.place(x=100,y=10,width=80,height=80)

        	btn2.place(x=300,y=10,width=80,height=80)

        	btn3.place(x=500,y=10,width=80,height=80)

        	btn4.place(x=700,y=10,width=80,height=80)

        	btn5.place(x=900,y=10,width=80,height=80)

        	pass

        def more(self):

        	mainlbl=Label(self.root,image=self.img16,bg="#131313")

        	mainlbl.place(x=0,y=0,width=self.w,height=self.h-150)	

        	pass

##FF7D01     

root=Tk()

obj=App(root)

obj.main()

root.mainloop()

