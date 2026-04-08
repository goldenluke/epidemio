# Epidemiologia Reflexiva

Simulação computacional de sistemas epidemiológicos como sistemas observador–observado, onde medir, inferir e intervir são processos acoplados.

---

## 🧠 Ideia Central

Em epidemiologia, assume-se que mais dados levam a melhores decisões.

Este projeto propõe uma visão alternativa:

> O ato de observar altera o sistema observado.

Ou seja, sistemas epidemiológicos são reflexivos — a vigilância influencia a dinâmica da doença.

---

## 🔬 Motivação

Indicadores epidemiológicos não refletem diretamente a realidade.  
Eles dependem de:

- Sintomas
- Acesso à testagem
- Processos de notificação
- Atrasos e agregações

Isso implica que:

- Parte dos casos permanece invisível  
- Diferentes realidades podem gerar os mesmos dados observados  
- A inferência é estruturalmente limitada  

---

## ⚙️ O Modelo

O sistema é definido por três componentes principais:

### 1. Realidade Epidemiológica
- Dinâmica baseada em modelo SIR
- Estados reais: R(t)

### 2. Observação
- Operador: P = A ∘ T ∘ Φ
- Inclui:
  - Geração de sintomas
  - Testagem
  - Atraso e notificação

### 3. Decisão (Feedback)
- Ações baseadas em dados observados
- Influenciam diretamente a dinâmica real

---

## 🔁 Acoplamento Fundamental

O sistema segue a dinâmica:

R(t+1) = f(R(t), P_T(R(t)))

Ou seja:

observar → decidir → alterar a realidade

---

## 📉 Resultados Principais

A simulação revela três regimes:

- Baixo T → alta incerteza, subnotificação  
- T ótimo (T*) → melhor equilíbrio entre inferência e estabilidade  
- Alto T → sistema controlado, mas com perda de informação  

---

## ⭐ Singularidade de Vigilância (T*)

Existe um ponto ótimo de observação:

- Antes de T* → aumentar observação melhora inferência  
- Após T* → aumenta instabilidade e reduz utilidade  

Mais dados não necessariamente melhoram decisões.

---

## 📊 Trade-off Fundamental

O modelo revela uma fronteira de Pareto entre:

- Controle epidemiológico  
- Qualidade da inferência  

Não é possível maximizar ambos simultaneamente.

---

## 📈 O que o sistema demonstra

- Diferença entre realidade e observação  
- Curva de utilidade da vigilância  
- Comparação entre regimes  
- Métricas de erro, variância e intensidade  
- Fronteira controle vs conhecimento  

---

## 🧪 Tecnologias Utilizadas

- Python  
- NumPy  
- Plotly  
- Streamlit  

---

## 🚀 Como rodar

1. Clonar o repositório:

git clone https://github.com/goldenluke/epidemio.git  
cd epidemio  

2. Criar ambiente virtual (opcional):

python -m venv venv  
source venv/bin/activate  (Linux/Mac)  
venv\Scripts\activate     (Windows)  

3. Instalar dependências:

pip install -r requirements.txt  

4. Executar aplicação:

streamlit run src/dashboard/app.py  

---

## 📁 Estrutura do Projeto

src/  
  simulation.py  
  utils.py  
  dashboard/  
    app.py  
    tradeoff_upgrade.py  

---

## 🧬 Conceitos-chave

- Sistema parcialmente observável  
- Operador de observação explícito  
- Não-identificabilidade  
- Erro estrutural  
- Feedback observação–dinâmica  
- Singularidade de vigilância  
- Trade-off controle vs conhecimento  

---

## 📚 Base Teórica

A ideia foi formalizada em artigo disponível no LinkedIn:

[https://www.linkedin.com/in/lucas-amaral-dourado-b5939b2aa/recent-activity/all/](https://www.linkedin.com/pulse/f%C3%ADsica-epidemiol%C3%B3gica-e-epistemologia-matem%C3%A1tica-dos-amaral-dourado-yhlof/)

---

## 💡 Insight Central

O limite da epidemiologia não está apenas no que não é observado, mas no ponto em que observar mais passa a alterar o sistema e reduzir o valor do conhecimento produzido.

---

## 🌍 Possíveis Aplicações

- Planejamento de vigilância epidemiológica  
- Avaliação de políticas públicas  
- Sistemas adaptativos de saúde  
- Modelagem de sistemas complexos  
- Otimização de testagem  

---

## 👨‍💻 Autor

Lucas Amaral Dourado  

---

## 📄 Licença

MIT
