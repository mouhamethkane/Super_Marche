from tkinter import *
from tkinter import messagebox, ttk
import tempfile
import random
from time import strftime
from PIL import ImageTk, Image
import os

class SuperMarche:
    def __init__(self, root):
        self.root = root
        self.root.title("Super marche")
        self.root.geometry("1920x1040+0+0")

        title = Label(self.root, text="Super Marche Mouhameth Kane", font=("Algerian", 45),
                       bg="yellow", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            heur = strftime("%H:%M:%S")
            lblheure.config(text=heur)
            lblheure.after(1000,heur)    

        lblheure = Label(self.root, text="HH:MM:SS", font=("times new roman", 15, "bold"), 
                         bg="yellow", fg="black")
        lblheure.place(x=0, y=25, width=120, height=40)

        heure()
        #non varable
        self.c_nom = StringVar()
        self.c_phon = StringVar()

        self.c_factu = StringVar()
        z = random.randint(1000,9999)
        self.c_factu.set(z)

        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.qte = IntVar()
        self.totalbruite = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar()

        #Liste Categorie
        self.list_categorie = ["Selection", "Vetment", "Style de vie", "Telephone"]

        #Souscategorie vetment
        self.list_souscategorieVetment = ["Pantelon", "T-Shirt", "Lacoste"]

        self.pantelon = ["Levis", "Mufti", "Skykar"]
        self.price_levis = 5000
        self.price_mufti = 1000
        self.price_skykar = 3000

        self.t_shirt = ["Polo", "Roadster", "Jack&Jones"]
        self.price_polo = 1500
        self.price_roadster = 2250
        self.price_Jack_Jones = 3600

        self.lacoste = ["Adidas", "Filla", "Unique"]
        self.price_adidas = 5900
        self.price_filla = 6800
        self.price_unique = 9000

        #Souscategorie Style de vie
        self.list_souscategoriestyle = ["Bath Soap", "Creme", "Huile de cheuveux"]

        self.bath_soap = ["LiveBuy", "Lux", "Santoor", "Pearl"]
        self.price_livebuy = 500
        self.price_lux = 1400
        self.price_santoor = 2400
        self.price_pearl = 2800

        self.creme = ["Faire&Lovely", "Ponds", "Olay", "Garnier"]
        self.price_faire_lovely = 1500
        self.price_ponds = 2350
        self.price_olay= 3100
        self.price_garnier= 4600

        self.huile = ["Parachute", "Jasmin", "Bajaj"]
        self.price_parachute = 1900
        self.price_jasmin = 2800
        self.price_bajaj = 7000

        #sousCategorie Telephone
        self.list_souscategorietel = ["Iphone", "Samsung", "Huawei", "Techno"]

        self.iphone = ["Iphone X", "Iphone 11", "Iphone 12"]
        self.price_ix = 45000
        self.price_i11 = 65000
        self.price_i12 = 950000

        self.samsung = ["Samsung M16", "Samsung M12", "Samsung M21"]
        self.price_sm16 = 15000
        self.price_sm12 = 23500
        self.price_sm21= 31000

        self.huawei = ["Huawei Y9S", "Huawei P8", "Huawei Mate"]
        self.price_y9s = 19000
        self.price_p8 = 28000
        self.price_mate = 70000

        self.techno = ["Techno Com11", "Techno Com12", "Techno Com13"]
        self.price_com11 = 29000
        self.price_com12 = 58000
        self.price_com13 = 68000

        Main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg="white")
        Main_Frame.place(x=10, y=100, width=1880, height=588)

        #Client
        client_Frame = LabelFrame(Main_Frame, text="Client", font=("times new roman", 15,), bg="white")
        client_Frame.place(x=10, y=5, width=350, height=150)

        self.lbl_contact = Label(client_Frame, text="Contact", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_contact.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_nomclient = Label(client_Frame, text="Nom client", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_nomclient.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_email = Label(client_Frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_email.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.text_contact = ttk.Entry(client_Frame, textvariable=self.c_phon, font=("times new roman", 15,))
        self.text_contact.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.text_nomclient = ttk.Entry(client_Frame, textvariable=self.c_nom, font=("times new roman", 15,))
        self.text_nomclient.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.text_email = ttk.Entry(client_Frame, textvariable=self.c_email, font=("times new roman", 15,))
        self.text_email.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        #produit
        produit_Frame = LabelFrame(Main_Frame, text="Produit", font=("times new roman", 15,), bg="white")
        produit_Frame.place(x=400, y=5, width=620, height=150)

        self.lbl_categorie = Label(produit_Frame, text="Selectioner Categorie", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_categorie.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_souscategorie = Label(produit_Frame, text="Sous Categorie", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_souscategorie.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_nomproduit = Label(produit_Frame, text="Nom Produit ", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_nomproduit.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.lbl_prix = Label(produit_Frame, text="Prix", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_prix.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.lbl_qte = Label(produit_Frame, text="Quantite", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_qte.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.text_categorie = ttk.Combobox(produit_Frame, font=("times new roman", 10), values=self.list_categorie,
                                            width=24, state="readonly")
        self.text_categorie.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.text_categorie.current(0)
        self.text_categorie.bind("<<ComboboxSelected>>", self.fonctionCategorie)

        self.text_souscategorie = ttk.Combobox(produit_Frame, font=("times new roman", 10), values=[""],
                                            width=24, state="readonly")
        self.text_souscategorie.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.text_souscategorie.current(0)
        self.text_souscategorie.bind("<<ComboboxSelected>>", self.fonctionsousCategorie)

        self.text_nomproduit = ttk.Combobox(produit_Frame, font=("times new roman", 10), textvariable=self.produit,
                                            width=24, state="readonly")
        self.text_nomproduit.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        

        self.text_prix = ttk.Combobox(produit_Frame, font=("times new roman", 10), textvariable=self.prix,
                                            width=20, state="readonly")
        self.text_prix.grid(row=0, column=3, sticky=W, padx=5, pady=2)
        self.text_nomproduit.bind("<<ComboboxSelected>>", self.fonctionnomproduit)
       

        self.text_qte = ttk.Entry(produit_Frame, font=("times new roman", 10), textvariable=self.qte,
                                            width=20,)
        self.text_qte.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        #recherche
        recher_Frame = LabelFrame(Main_Frame, bd=2, bg="white")
        recher_Frame.place(x=1060, y=10, width=300, height=70)

        self.lbl_rechercher = Label(recher_Frame, text="N Facture", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_rechercher.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.text_rechercher = ttk.Entry(recher_Frame, textvariable=self.rech_factu, font=("times new roman", 23,), width="15")
        self.text_rechercher.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.btn_rechercher = Button(recher_Frame, text="Rechercher",command=self.rechercher, font=("times new roman", 12, "bold"), bg="yellow", width=11, cursor="hand2")
        self.btn_rechercher.grid(row=3, column=1)

        #Espace facture
        Facture_label = LabelFrame(Main_Frame, text="Facture", font=("times new roman", 15, "bold"), bg="white")
        Facture_label.place(x=1060, y=80, width=290, height=321)

        scroll_y = Scrollbar(Facture_label, orient=VERTICAL)
        self.textarea = Text(Facture_label, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), bg="white", fg="blue")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #footer
        enbas_Frame = LabelFrame(Main_Frame, text="Bouton", font=("times new roman", 15), bg="white")
        enbas_Frame.place(x=0, y=400, width=1880, height=180)


        self.lbl_totalbruite = Label(enbas_Frame, text="Totale Bruite", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_totalbruite.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_taxe = Label(enbas_Frame, text="Taxe", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_taxe.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_totalnet = Label(enbas_Frame, text="Totale Net", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_totalnet.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.text_totalbruite = ttk.Entry(enbas_Frame, textvariable=self.totalbruite, font=("times new roman", 23), width=15, state="readonly")
        self.text_totalbruite.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.text_taxe = ttk.Entry(enbas_Frame, textvariable=self.taxe, font=("times new roman", 23), width=15, state="readonly")
        self.text_taxe.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.text_totalnet = ttk.Entry(enbas_Frame, textvariable=self.totalnet, font=("times new roman", 23), width=15, state="readonly")
        self.text_totalnet.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        #image

        self.image = ImageTk.PhotoImage(Image.open("./image/kane.jpg"))
        self.lbl_image = Label(image=self.image)
        self.lbl_image.place(x=80, y=270,  width=950, height=200)

        #Bouton

        btn_Frame = Frame(enbas_Frame, bd=2, bg="white")
        btn_Frame.place(x=450, y=0)

        self_ajoutPanier = Button(btn_Frame, text="Ajouter Cart",command=self.ajouter, height=2, font=("times new roman", 15, "bold"), bg="cyan", width=10, cursor="hand2")
        self_ajoutPanier.grid(row=0, column=0)

        self_generer = Button(btn_Frame, text="Generer",command=self.genererFacture, height=2, font=("times new roman", 15, "bold"), bg="green", width=10, cursor="hand2")
        self_generer.grid(row=0, column=1)

        self_sauvegarde = Button(btn_Frame, text="Sauvegarde",command=self.sauvegarde, height=2, font=("times new roman", 15, "bold"), bg="yellow", width=10, cursor="hand2")
        self_sauvegarde.grid(row=0, column=2)

        self_imprime = Button(btn_Frame, text="Imprimer",command=self.imprimer, height=2, font=("times new roman", 15, "bold"), bg="blue", width=10, cursor="hand2")
        self_imprime.grid(row=0, column=3)

        self_reini = Button(btn_Frame, text="Reinitialiser",command=self.reini, height=2, font=("times new roman", 15, "bold"), bg="gray", width=10, cursor="hand2")
        self_reini.grid(row=0, column=4)

        self_quitte = Button(btn_Frame, text="Quitter", height=2, font=("times new roman", 15, "bold"), bg="red", width=10, cursor="hand2")
        self_quitte.grid(row=0, column=5)

        self.bienvenu=[]
        self.l=[]

        ####### Fonction
    def bienvenu(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t\tBienvenu chez super marche Mouhameth")
        self.textarea.insert(END, f"\n\nNumero Facture : {self.c_factu.get()}")
        self.textarea.insert(END, f"\n\nNom Client : {self.c_nom.get()}")
        self.textarea.insert(END, f"\n\nTelephone : {self.c_phon.get()}")
        self.textarea.insert(END, f"\n\nEmail : {self.c_email.get()}")

        self.textarea.insert(END, "\n**************************************")

        self.textarea.insert(END, f"\nProduit\t\tQte\t\tPrix")

        self.textarea.insert(END, "\n**************************************")

    def sauvegarde(self):
        op=messagebox.askyesno("Souvegarde", "Voulez_vous sauvegarder la facture")
        if op==True:
            self.donneFacture=self.textarea.get(1.0,END)
            f1=open("C:/Users/kante/Desktop/mes projets/Sper_Marche/facture"+str(self.c_factu.get())+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarde", f"La facture numero {self.c_factu.get()} a ete enregistrer avec succes")
            f1.close()    

    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get()* self.n
        self.l.append(self.m)
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Selectionnez un produit")
        else:
            self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{self.m}")
            self.totalbruite.set(str("Rs.%.2f"%(sum(self.l))))
            self.taxe.set(str("Rs.%.2f"%((((sum(self.l)) - (self.prix.get())) * 1 )/100))) 
            self.totalnet.set(str("Rs.%.2f"%(((sum(self.l)) + ((((sum(self.l)) - (self.prix.get())) *1 )/100)))))

    def genererFacture(self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Ajouter d'abord un produit")
        else:
            text = self.textarea.get(10.0, (10.0+float(len(self.l))))
            self.bienvenu()
            text = self.textarea.insert(END, text)
            self.textarea.insert(END, "\n**************************************")
            self.textarea.insert(END, f"\nTotal Bruite : \t\t{self.totalbruite.get()}")
            self.textarea.insert(END, f"\nTaxe : \t\t{self.taxe.get()}")
            self.textarea.insert(END, f"\nTotal Net : \t\t{self.totalnet.get()}")

    def imprimer(self):
        fichier = tempfile.mkdtemp(".text")
        open(fichier, "w").write(self.textarea.get("1.0",END))
        os.startfile(fichier, "print")


    def rechercher(self):
        trouver ="non"
        for i in os.listdir("C:/Users/kante/Desktop/mes projets/Sper_Marche/facture"):
            if i.split("."[0]==self.rech_factu.get()):
                f1 = open("C:/Users/kante/Desktop/mes projets/Sper_Marche/facture{i}","r") 
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                    f1.close
                    trouver="oui"
            if trouver == "non":
                messagebox.showerror("Error", "La facture n'existe pas")

    def reini(self):
        self.textarea.delete("1.0",END)
        self.c_nom.set("") 
        self.c_phon.set("") 
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.c_factu.set(str(x))
        self.rech_factu.set("") 
        self.produit.set("") 
        self.prix.set(0)
        self.qte.set(0)
        self.l=[0]
        self.totalbruite.set("")
        self.taxe.set("")
        self.totalnet.set("") 
        self.bienvenu()                           


    def fonctionCategorie(self, even=""):
        #"", "Style de vie", "Telephone"
        if self.text_categorie.get()=="Vetment":
            self.text_souscategorie.config(values=self.list_souscategorieVetment)
            self.text_souscategorie.current(0)

        if self.text_categorie.get()=="Style de vie":
            self.text_souscategorie.config(values=self.list_souscategoriestyle)
            self.text_souscategorie.current(0)

        if self.text_categorie.get()=="Telephone":
            self.text_souscategorie.config(values=self.list_souscategorietel)
            self.text_souscategorie.current(0)

    def fonctionsousCategorie(self, even=""):               
        #Vetment
        if self.text_souscategorie.get()=="Pantelon":
            self.text_nomproduit.config(values=self.pantelon)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="T-Shirt":
            self.text_nomproduit.config(values=self.t_shirt)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="Lacoste":
            self.text_nomproduit.config(values=self.lacoste)
            self.text_nomproduit.current(0) 

        #style de vie
        if self.text_souscategorie.get()=="Bath Soap":
            self.text_nomproduit.config(values=self.bath_soap)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="Creme":
            self.text_nomproduit.config(values=self.creme)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="Huile de cheuveux":
            self.text_nomproduit.config(values=self.huile)
            self.text_nomproduit.current(0) 

        #Telephone
        if self.text_souscategorie.get()=="Iphone":
            self.text_nomproduit.config(values=self.iphone)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="Samsung":
            self.text_nomproduit.config(values=self.samsung)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="Huawei":
            self.text_nomproduit.config(values=self.huawei)
            self.text_nomproduit.current(0)

        if self.text_souscategorie.get()=="Techno":
            self.text_nomproduit.config(values=self.techno)
            self.text_nomproduit.current(0)        

#**********************************************************
        ####### Fonction
    def fonctionnomproduit(self, even=""):
        #Vetment
        if self.text_nomproduit.get()=="Levis":
            self.text_prix.config(values=self.price_lavis)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Mufti":
            self.text_prix.config(values=self.price_mufti)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Skykar":
            self.text_prix.config(values=self.price_skykar)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Polo":
            self.text_prix.config(values=self.price_polo)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Roadster":
            self.text_prix.config(values=self.price_roadster)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Jack&Jones":
            self.text_prix.config(values=self.price_Jack_Jones)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Adidas":
            self.text_prix.config(values=self.price_adidas)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Filla":
            self.text_prix.config(values=self.price_filla)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Unique":
            self.text_prix.config(values=self.price_unique)
            self.text_prix.current(0)
            self.qte.set(1)

                           

        if self.text_nomproduit.get()=="LiveBuy":
            self.text_prix.config(values=self.price_livebuy)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Lux":
            self.text_prix.config(values=self.price_lux)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Santoor":
            self.text_prix.config(values=self.price_santoor)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Pearl":
            self.text_prix.config(values=self.price_pearl)
            self.text_prix.current(0)
            self.qte.set(1)


            #Faire&Lovely", "Ponds", "Olay", "Garnier"

        if self.text_nomproduit.get()=="#Faire&Lovely":
            self.text_prix.config(values=self.price_faire_lovely)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Ponds":
            self.text_prix.config(values=self.price_ponds)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Olay":
            self.text_prix.config(values=self.price_olay)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Garnier":
            self.text_prix.config(values=self.price_garnier)
            self.text_prix.current(0)
            self.qte.set(1)

        #"Parachute", "Jasmin", "Bajaj"        
        if self.text_nomproduit.get()=="Parachute":
            self.text_prix.config(values=self.price_parachute)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Jasmin":
            self.text_prix.config(values=self.price_jasmin)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Bajaj":
            self.text_prix.config(values=self.price_bajaj)
            self.text_prix.current(0)
            self.qte.set(1)

            #Iphone X", "Iphone 11", "Iphone 12"       
        if self.text_nomproduit.get()=="Iphone X":
            self.text_prix.config(values=self.price_ix)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Iphone 11":
            self.text_prix.config(values=self.price_i11)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Iphone 12":
            self.text_prix.config(values=self.price_i12)
            self.text_prix.current(0)
            self.qte.set(1) 

            #Samsung M16", "Samsung M12", "Samsung M21"          
        if self.text_nomproduit.get()=="Samsung M16":
            self.text_prix.config(values=self.price_sm16)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Samsung M12":
            self.text_prix.config(values=self.price_sm12)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Samsung M21":
            self.text_prix.config(values=self.price_sm21)
            self.text_prix.current(0)
            self.qte.set(1) 

            #"Huawei Y9S", "Huawei P8", "Huawei Mate"   
        if self.text_nomproduit.get()=="Huawei Y9S":
            self.text_prix.config(values=self.price_y9s)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Huawei P8":
            self.text_prix.config(values=self.price_p8)
            self.text_prix.current(0)
            self.qte.set(1)

        if self.text_nomproduit.get()=="Huawei Mate":
            self.text_prix.config(values=self.price_mate)
            self.text_prix.current(0)
            self.qte.set(1)

            #Techno Com11", "Techno Com12", "Techno Com13" 
        if self.text_nomproduit.get()=="Techno Com11":
            self.text_prix.config(values=self.price_com11)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Techno Com12":
            self.text_prix.config(values=self.price_com12)
            self.text_prix.current(0)
            self.qte.set(1) 

        if self.text_nomproduit.get()=="Techno Com13":
            self.text_prix.config(values=self.price_com13)
            self.text_prix.current(0)
            self.qte.set(1)             



if __name__=="__main__":
    root=Tk()        
    obj = SuperMarche(root)
    root.mainloop()    