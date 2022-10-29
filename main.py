import wikipedia

pesquisa = input ("o que você deseja saber?")
wikipedia.set_lang("pt")
result = wikipedia.summary(pesquisa)
print(result)

arquivo = open('pesquisa_2.txt','w')
arquivo.write(result) 
arquivo.close() 
