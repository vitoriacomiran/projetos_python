## Lead Score - Classificação de Leads

Este projeto é um modelo simples de **Lead Score** que classifica leads com base em três critérios:

- **Segmento da empresa** (15%)
- **Cargo do contato** (15%)
- **Quantidade de licenças desejadas** (70%)

###  Pontuação

Cada critério possui uma pontuação definida. A pontuação total (de 0 a 100) é usada para classificar o lead como:

- **≤ 20** → Lead Frio  
- **≤ 50** → Lead Morno  
- **≤ 70** → Lead Quente  
- **71+** → Lead Muito Quente  

### Como funciona

O código recebe os dados do lead (segmento, cargo e quantidade de licenças), aplica os pesos definidos e calcula o score total de forma proporcional. 

### Como testar

Execute o script em um terminal Python e preencha os dados quando solicitado (deixar o passo 1)

```bash
python lead_score.py
