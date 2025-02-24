import random

# `random.seed(valor)` -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

# `random.randrange(início, fim, passo)` -> Gera um número inteiro aleatório dentro de um intervalo específico
# gera um número inteiro aleatório entre 10 e 20, pulando de 2 em 2
random_range = random.randrange(10, 20, 2)
print(f'{random_range=}')

# `random.randint(início, fim)` -> Gera um número inteiro aleatório dentro de um intervalo, sem passo
# gera um número inteiro aleatório entre 10 e 20
random_int = random.randint(10, 20)
print(f'{random_int=}')

# `random.uniform(início, fim)` -> Gera um número flutuante aleatório dentro de um intervalo, sem passo
# gera um número de ponto flutuante aleatório entre 10 e 20
random_uniform = random.uniform(10, 20)
print(f'{random_uniform=}')

# `random.shuffle(SequenciaMutável)` -> Embaralha a sequência original
nomes = ['Gui', 'Mari', 'Maggie', 'Kurt', 'Guts', 'Red']
print(f'{nomes=}')
# random.shuffle(nomes)
# print(f'{nomes=}')

# `random.sample(Iterável, k=N)` -> Escolhe `k` elementos do iterável e retorna outro iterável com eles (não repete elementos)
nomes_sample = random.sample(nomes, k=2)
print(f'{nomes_sample=}')

# `random.choices(Iterável, k=N)` -> Escolhe `k` elementos do iterável e retorna outro iterável com eles (repete elementos)
nomes_coices = random.choices(nomes, k=2)
print(f'{nomes_coices=}')

# random.choice(Iterável) -> Escolhe e retorna um elemento do iterável
nomes_choice = random.choice(nomes)
print(f'{nomes_choice=}')
