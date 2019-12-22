#coding:utf-8
from random import randint, choice
from tkinter import *


#script gestion password
def generate_password():
	password_min = 6
	password_max = 12
	digits = "0123456789"
	letter_lower = "abcdefghijklmnopqrstuvwxyz"
	letter_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	special_carac = "&!?/%@-+"
	if pwd_digits.get() == True and pwd_caps.get() == True and pwd_lower.get() == True and pwd_caracspec.get() == True:	
		all_chars = digits + letter_caps + letter_lower + special_carac
	elif pwd_digits.get() == True and pwd_caps.get() == True and pwd_lower.get() == True and pwd_caracspec.get() == False:	
		all_chars = digits + letter_caps + letter_lower
	elif pwd_digits.get() == True and pwd_caps.get() == True and pwd_lower.get() == False and pwd_caracspec.get() == False:		
		all_chars = digits + letter_caps
	elif pwd_digits.get() == True and pwd_caps.get() == False and pwd_lower.get() == False and pwd_caracspec.get() == False:	
		all_chars = digits
	elif pwd_digits.get() == True and pwd_caps.get() == True and pwd_lower.get() == False and pwd_caracspec.get() == True:	
		all_chars = digits + letter_caps + special_carac
	elif pwd_digits.get() == True and pwd_caps.get() == False and pwd_lower.get() == False and pwd_caracspec.get() == True:		
		all_chars = digits + special_carac
	elif pwd_digits.get() == False and pwd_caps.get() == True and pwd_lower.get() == True and pwd_caracspec.get() == True:	
		all_chars = letter_caps + letter_lower + special_carac
	elif pwd_digits.get() == False and pwd_caps.get() == False and pwd_lower.get() == True and pwd_caracspec.get() == True:	
		all_chars = letter_lower + special_carac
	elif pwd_digits.get() == False and pwd_caps.get() == False and pwd_lower.get() == False and pwd_caracspec.get() == True:		
		all_chars = special_carac
	elif pwd_digits.get() == False and pwd_caps.get() == True and pwd_lower.get() == False and pwd_caracspec.get() == False:	
		all_chars = letter_caps
	elif pwd_digits.get() == False and pwd_caps.get() == False and pwd_lower.get() == True and pwd_caracspec.get() == False:		
		all_chars = letter_lower
	elif pwd_digits.get() == False and pwd_caps.get() == True and pwd_lower.get() == True and pwd_caracspec.get() == False:	
		all_chars = letter_caps + letter_lower
	else:
		#label_final['text'] = "Merci de choisi au moins une option"
		all_chars = digits + letter_caps + letter_lower + special_carac
	label_final['text'] = "Voici votre mot de passe :"	
	password = "".join(choice(all_chars) for x in range(randint(pwd_nbr_carac.get(), pwd_nbr_carac.get())))
	password_entry.delete(0, END)
	password_entry.insert(0, password)
#initialisation fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
bg = "#61A28D"
window.config(background=bg)
frame = Frame(window, bg=bg)
#initialisation variable form
pwd_digits = BooleanVar()
pwd_digits.set(True)

pwd_lower = BooleanVar()
pwd_lower.set(True)

pwd_caps = BooleanVar()
pwd_caps.set(True)

pwd_caracspec = BooleanVar()
pwd_caracspec.set(True)

vals_nbr_carac = ['4', '6', '8', '12']
labs_nbr_carac = ['4 caractères', '6 caractères', '8 caractères', '12 caractères']
pwd_nbr_carac = IntVar()
pwd_nbr_carac.set(vals_nbr_carac[1])
#initialisation affichage
label_title = Label(frame, text="Générateur de mot de passe", font=("Helvetica",20), bg=bg, fg="white")
label_title.pack()

label_sstitle = Label(frame, text="Sélectionnez les options de votre mot de passe sécurisé:", font=("Helvetica",12), bg=bg, fg="white")
label_sstitle.pack()

text_form_digits = "Avec des chiffres [ 0 1 2 3 4 5 6 7 8 9 ]"
form_digits = Checkbutton(frame, text=text_form_digits, var=pwd_digits, font=("Helvetica",12), bg=bg)
form_digits.pack()

text_form_lower = "Avec des lettres minuscules [ a b c ... x y z ]"
form_lower = Checkbutton(frame, text=text_form_lower, var=pwd_lower, font=("Helvetica",12), bg=bg)
form_lower.pack()

text_form_caps = "Avec des lettres majuscules [ A B C ... X Y Z ]"
form_caps = Checkbutton(frame, text=text_form_caps, var=pwd_caps, font=("Helvetica",12), bg=bg)
form_caps.pack()

text_form_caracspec = "Avec des caractères spéciaux [ &!?/%@-+ ]"
form_caracspec = Checkbutton(frame, text=text_form_caracspec, var=pwd_caracspec, font=("Helvetica",12), bg=bg)
form_caracspec.pack()

label_radio = Label(frame, text="Nombre de caractères :", font=("Helvetica",12), bg=bg, fg="white")
label_radio.pack()

for i in range(4):
    form_nbr_carac = Radiobutton(frame, variable=pwd_nbr_carac, text=labs_nbr_carac[i], value=vals_nbr_carac[i],bg=bg,indicatoron=0)
    form_nbr_carac.pack(fill=X, expand=1)

generate_password_button = Button(frame, text="Créer votre mot de passe", font=("Helvetica",20), bg=bg, fg="white",command=generate_password)
generate_password_button.pack(fill=X)

label_final = Label(frame, font=("Helvetica",18), bg=bg, fg="red")
label_final.pack()

password_entry = Entry(frame, font=("Helvetica",20), bg=bg, fg="red")
password_entry.pack()

#affichage de la fenetre
frame.pack(expand=YES)
window.mainloop()
