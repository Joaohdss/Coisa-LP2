# Joao Henrique
class Conta_Laboratorio(object):
	def __init__(self,nome,cota = 2000, espaco = 0):
		self.nome = nome
		self.cota = cota
		self.espaco = espaco
	def consome_espaco(self,num):
		self.espaco = self.espaco + num
	def liberar_espaco(self,num):
		self.espaco = self.espaco - num
	def imprime(self):
		return('%s %i/%i' %(self.nome,self.espaco,self.cota))

	def atingiu_cota(self):
		if(self.espaco >= self.cota):
			return True
		else:
			return False
class Conta_Cantina(object):
	def __init__(self,nome,debito = 0,quantidade = 0, acumulado = 0):
		self.nome_disciplina = nome
		self.debito = debito
		self.quantidade = quantidade
		self.acumulado = acumulado

	def cadastra_lanche(self,quantidade, preco):
		self.quantidade += quantidade
		self.debito += preco
		self.acumulado += preco
	def get_debito(self):
		return self.debito
	def pagar_conta(self,dinheiro):
		self.debito -= dinheiro
	def toStr(self):
		return '%s %i %i' %(self.nome_disciplina, self.quantidade,self.acumulado)
# Saude
class Saude(object):
	def __init__(self,saude_fisica = 'boa',saude_mental = 'boa'):
		self.saude_fisica = saude_fisica
		self.saude_mental = saude_mental

	def define_saude_mental(self, mental):
		self.saude_mental = mental
	def define_saude_fisica(self,fisica):
		self.saude_fisica = fisica
	def get_status_geral(self):
		if(self.saude_fisica == self.saude_mental):
			return self.saude_fisica
		else:
			return 'ok'
## Conta Laboratio

lcc = Conta_Laboratorio('LCC2')
lcc.consome_espaco(1999)
print lcc.atingiu_cota()
lcc.consome_espaco(2)
print lcc.atingiu_cota()
lcc.liberar_espaco(1)
print lcc.atingiu_cota()
lcc.liberar_espaco(1)
print lcc.atingiu_cota()
print lcc.imprime()

## Conta Cantina

cantina = Conta_Cantina('Seu Joao')
cantina.cadastra_lanche(2,500)
cantina.cadastra_lanche(1,500)
cantina.pagar_conta(200)
print(cantina.get_debito())
print(cantina.toStr())

