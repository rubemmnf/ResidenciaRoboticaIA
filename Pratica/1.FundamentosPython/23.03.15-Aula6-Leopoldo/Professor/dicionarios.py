class Aluno: 
    def __init__(self, nome, endereco, telefone) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.historico = {}
    def __str__(self) -> str:
        return f'{self.nome}, mora em {self.endereco}'
    def __repr__(self) -> str:
        return self.__str__()
    def lancarNota(self, codigoDisciplina, nota):
        self.historico[codigoDisciplina] = nota
        return self.__str__()
    def qualFoiNota(self,codigoDisciplina):
        if codigoDisciplina in self.historico:
            return self.historico[codigoDisciplina]
        else:
            return 'Ainda sem nota'
    def imprime_historico(self):
        for k,v in self.historico.items():
            print(f'{k} : Nota {v}')
        # for disciplina in self.historico:
        #     print(f'{disciplina} : Nota {self.historico[disciplina]}')

    
alexsandro = Aluno('Alexsandro', 'Rua tal...', '12345678')
print(alexsandro.historico)
alexsandro.lancarNota('java',5)
print(alexsandro.historico)
alexsandro.lancarNota('python',9.5)
print(alexsandro.historico)
##...



print(alexsandro.historico['java'])
print(alexsandro.qualFoiNota('testes'))
print('------')
alexsandro.imprime_historico()








# alunosOO = {123:Aluno('Alexsandro', 'Rua tal...', '12345678'), 
#           456:Aluno('Milena', 'Av. xyz...', '987654321'),
#           789:Aluno('Eduardo', 'Praça Leopoldo Teixeira...', '6238472683'),
#           654:Aluno('Bruno Reis', 'Rua sem nome...', '999999999'),
#           876:Aluno('Bruno Teles', 'Outra rua...', '8888888')}

# alunosDict = {123:{'nome':'Alexsandro',   'endereco':'Rua tal...',      'telefone':'12345678'}, 
#           456:{'nome':'Milena',       'endereco':'Av. xyz...',      'telefone':'987654321'},
#           789:{'nome':'Eduardo',      'endereco':'Praça...',        'telefone':'6238472683'},
#           654:{'nome':'Bruno Reis',   'endereco':'Rua sem nome...', 'telefone':'999999999'},
#           876:{'nome':'Bruno Teles',  'endereco':'Outra rua...',    'telefone':'8888888'}}

# eduardoOO = alunosOO[789]
# eduardoDict = alunosDict[789]

# print(eduardoOO.nome)
# print(eduardoDict['nome'])
