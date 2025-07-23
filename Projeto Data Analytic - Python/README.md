## Analisando Dados com Python

### Case: Cancelamento de Clientes

### Descrição
Este projeto faz parte de um estudo de dados em que uma empresa com mais de **800 mil clientes** quer entender os motivos pelos quais a maioria de seus clientes se tornaram inativos, ou seja, cancelaram o serviço. O objetivo é identificar padrões de comportamento que possam explicar os cancelamentos e sugerir ações para reduzir esse número.

### Objetivo
- **Análise de cancelamentos**: Identificar os principais fatores que levam os clientes a cancelarem o serviço.
- **Ações corretivas**: Sugerir estratégias para a empresa com base nos insights extraídos, de modo a melhorar a retenção de clientes.

### Etapas do Projeto

1. **Importação de Dados**: Carregar os dados dos clientes ativos e inativos para análise.
2. **Análise Exploratória**: Explorar os dados para identificar padrões de comportamento, como:
3. **Modelagem**: Utilizar técnicas de machine learning para prever cancelamentos e determinar quais variáveis são mais importantes na decisão dos clientes.
4. **Recomendações**: Baseado nos resultados, sugerir ações práticas que a empresa pode tomar para reduzir o churn (taxa de cancelamento).

### Resultado
Principais Insights:
Todos os clientes com contrato mensal cancelaram
Ação sugerida: Oferecer descontos em contratos anuais e trimestrais.

Clientes com mais de 20 dias de atraso cancelaram o serviço 
Ação sugerida: Implementar um sistema que ative alertas com 10 dias de atraso.

Clientes que ligaram mais de 4 vezes para o call center cancelaram 
Ação sugerida: Criar alertas quando o cliente fizer mais de 2 ligações.

Após aplicar essas estratégias, foi verificado através do Python que a taxa de cancelamento pode ser reduzida de 56% para 18%.

   
### Ferramentas Utilizadas
**Linguagem**: Python
**Bibliotecas**:
- pandas para manipulação de dados
- numpy para cálculos matemáticos
- openpyxl para manipulação de arquivos Excel
- nbformat e ipykernel para trabalhar com notebooks Jupyter
- plotly para visualização de dados interativa


