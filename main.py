import wikipedia

pesquisa = input ("o que você deseja saber?")
wikipedia.set_lang("pt")
result = wikipedia.summary(pesquisa)

salvar_arquivo = input("qual nome deseja dar ao arquivo")
salvar_arquivo += ".txt"

arquivo = open(salvar_arquivo,'w')
arquivo.write(result) 
arquivo.close() 
