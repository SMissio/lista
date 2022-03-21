#!/usr/bin/env python
# coding: utf-8

# In[87]:


lista = ['1', '2', '3', '4', '5','6','7','8','9','10','11','12']
lista2=[]
i = 0
while i <len(lista):
    print(lista[i])
    i=i+2
lista2=lista[8:9]
print(lista2)


# In[78]:



def calcula(inicial,final):
 lista_inicial = []
 num = inicial
 while num <= final:
     lista_inicial.append(num)
     num+=1
 nova_lista = lista_inicial
 ultimo_valor = -1
 while len(nova_lista)>1:
     
     indice = 0
     if ultimo_valor == nova_lista[len(nova_lista)-1]:
         indice = 1
     ultimo_valor = nova_lista[len(nova_lista)-1]
     nova_lista = reduz_lista(nova_lista,indice)
 
 return nova_lista


def reduz_lista(lista,indice_inicial):
 nova_lista =[]    
 for i in range(indice_inicial,len(lista),2):
     nova_lista.append(lista[i])
 return nova_lista

print(calcula(1,12))
     


# In[38]:





# In[ ]:





# In[ ]:




