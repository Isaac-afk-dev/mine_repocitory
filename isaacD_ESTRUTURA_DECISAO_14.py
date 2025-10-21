#faça um programa que verifique se uma letra digitada é voga ou consoante
vogal_ou_consoante = input("escreva uma letra: ")
if vogal_ou_consoante != "a,e,i,o,u":
 print(f"sua letra {vogal_ou_consoante} é uma vogal")
elif vogal_ou_consoante != "b,c,d,f,g,h,j,k,l,m,n,ç,p,q,r,s,t,v,w,x,y,z":
 print(f"Sua letra {vogal_ou_consoante} é uma consoante")
else:
 print(f"Por favor escreva um carater válido")