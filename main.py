import wikipedia
try:
	pesquisa = input ("o que você deseja saber?\n")
	wikipedia.set_lang("pt")
	result = wikipedia.summary(pesquisa)
	salvar_arquivo = input("qual nome deseja dar ao arquivo:\n")
	salvar_arquivo += ".txt"
	arquivo = open(salvar_arquivo,'w')
	arquivo.write(result) 
	arquivo.close()
except:
	print("não foi possível encontrar nada na wikipedia, tente novamente")
