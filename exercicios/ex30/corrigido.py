from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000
prazo_em_anos = 5
parcelas = prazo_em_anos * 12
valor_da_parcela = emprestimo / parcelas

# Crie a data do empréstimo
data_do_emprestimo = datetime.strptime('20/12/2020', '%d/%m/%Y')

# Crie a data do final do empréstimo
final_do_emprestimo = data_do_emprestimo + relativedelta(years=prazo_em_anos)

# Mostre todas as datas de vencimento e o valor de cada parcela.
for i in range(parcelas):
    vencimento = data_do_emprestimo + relativedelta(months=i+1)
    msg = f'{i+1}ª parcela'
    print(f'{msg} com vencimento para {vencimento.strftime("%d/%m/%Y")} no valor de R${valor_da_parcela:,.2f}.')
