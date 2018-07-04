import matplotlib.pyplot as plt
import numpy as np
import string
import random

def UcitavanjeR():
	rec=input()
	return(rec)

def UcitavanjeS():
	slovo=input()
	return(slovo);

#ucitati reci iz fajla
rec=[]
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for x in range(10):
	rec.append(letters[random.randint(0,25)])
rec = "mama"
#rec=list(s);
#rec='asdfg';
lista_crtica = []
br_zivota=45;

for i in rec:
	lista_crtica.append('_')

while(1):
	pogodjeno_sve=True
	ne_postoji_rec=True
	print("\nostalo je jos",br_zivota," zivota \n  unesi slovo ")

	slovo=input()
	if slovo in rec:
		ne_postoji_rec = False

	#zameni_crticu
		for i in range(len(rec)):
			if(rec[i]==slovo):
				lista_crtica[i]=slovo
				ne_postoji_rec=False


	if(ne_postoji_rec==True):
		br_zivota-=1

	if(br_zivota==0):
		print("umro si,rec je bila-")
		print(rec)
		exit()

	for i in lista_crtica:
		print(i, end=' ')

	for i in range(len(rec)):
		if(lista_crtica[i]=="_"):
			pogodjeno_sve=False;
	if(pogodjeno_sve==True):
		break;

print("\n\nBRAVO")
