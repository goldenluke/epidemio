# Epidemiologia Reflexiva

Simulação computacional de sistemas epidemiológicos como sistemas observador–observado.

## Ideia

Em epidemiologia, assume-se que mais dados levam a melhores decisões.

Este projeto demonstra que:

Mais observação pode alterar a dinâmica do sistema e reduzir a utilidade da informação.

## Principais conceitos

- Sistema parcialmente observável
- Operador de observação (P)
- Erro estrutural
- Feedback entre observação e dinâmica
- Singularidade de Vigilância (T*)
- Trade-off entre controle e conhecimento

## Resultados

O modelo identifica três regimes:

- Baixo T → alta incerteza  
- T ótimo → melhor equilíbrio  
- Alto T → controle alto, perda de informação  

## Demonstração

O sistema gera:

- Curva de utilidade U(T)
- Ponto ótimo T*
- Comparação entre regimes
- Fronteira de Pareto (controle vs conhecimento)

## Como rodar

pip install -r requirements.txt  
streamlit run src/dashboard/app.py  

## Insight central

Não é possível maximizar controle e inferência ao mesmo tempo.

## Autor

Lucas Amaral Dourado

## Licença

MIT
