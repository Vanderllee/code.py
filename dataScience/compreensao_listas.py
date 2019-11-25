
# %%

minha_lista = [1, 2, 3, 4, 5]
print(minha_lista)

mesma_lista = [x for x in range(5)]

outra_lista = [2*x for x in range(5)]

#print(outra_lista)

# gerando números pares
numeros_pares =[x for x in range(10) if x % 2 == 0]
# print(numeros_pares)

# gerando números ímpares 
num_impares = [x for x in range(10) if x % 2 != 0]

print(num_impares)

# Listas com strings diferentes
pessoas = ['ANa', ' Manuela', 'felipe ', 'PEDRO']

nome_minisculo = pessoas[0].lower()
#print(nome_minisculo)

primeira_letra_maiscula = pessoas[2].capitalize()
print(primeira_letra_maiscula)

todas_letras_maisculas = pessoas[2].upper()
print(todas_letras_maisculas)

tirando_espaco = pessoas[1].strip()
print(tirando_espaco)

nova_lista_pessoas = [p.strip().capitalize() for p in pessoas]
print(nova_lista_pessoas)