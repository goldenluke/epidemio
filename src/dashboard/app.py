import streamlit as st
import numpy as np
import plotly.graph_objects as go

from src.simulation import run_simulation
from src.utils import utility

st.set_page_config(layout="wide")
st.title("Epidemiologia Reflexiva")

# ===== CONTROLES =====
col1, col2 = st.columns(2)

with col1:
    T = st.slider("Intensidade de Observação (T)", 0, 100, 30)

with col2:
    noise = st.slider("Incerteza observacional", 0.0, 0.5, 0.1)

# ===== SIMULAÇÃO PRINCIPAL =====
I, I_hat, actions = run_simulation(T, noise=noise)

# ===== GRÁFICO PRINCIPAL =====
fig = go.Figure()
fig.add_trace(go.Scatter(y=I, name="I real"))
fig.add_trace(go.Scatter(y=I_hat[:len(I)], name="I observado"))
st.plotly_chart(fig, use_container_width=True)

# ===== UTILIDADE =====
U = utility(I, I_hat, actions)
st.metric("Utilidade atual", round(U, 4))

# ===== CURVA U(T) =====
Ts = np.linspace(0, 100, 20)
utils = []

for t in Ts:
    I_r, I_h, a = run_simulation(t, noise=noise)
    utils.append(utility(I_r, I_h, a))

T_star = Ts[np.argmax(utils)]

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=Ts, y=utils, mode='lines', name='U(T)'))
fig2.add_vline(x=T_star, line_dash="dash", annotation_text=f"T*={round(T_star,2)}")
st.plotly_chart(fig2, use_container_width=True)

st.metric("T ótimo (T*)", round(T_star, 2))

# ===== COMPARAÇÃO =====
st.header("Comparação de Regimes")

T_low = max(1, int(T_star * 0.3))
T_high = min(100, int(T_star * 1.5))

colA, colB, colC = st.columns(3)

def monte_carlo(T, noise, runs=30):
    sims_I = []
    sims_Ihat = []

    for _ in range(runs):
        I, I_hat, _ = run_simulation(T, noise=noise)
        sims_I.append(I)
        sims_Ihat.append(I_hat[:len(I)])

    sims_I = np.array(sims_I)
    sims_Ihat = np.array(sims_Ihat)

    return (
        sims_I.mean(axis=0),
        sims_Ihat.mean(axis=0),
        np.var(sims_Ihat)
    )

for col, label, t_val in zip(
    [colA, colB, colC],
    ["T baixo", "T ótimo", "T alto"],
    [T_low, int(T_star), T_high]
):
    mean_I, mean_Ihat, var = monte_carlo(t_val, noise)

    fig = go.Figure()
    fig.add_trace(go.Scatter(y=mean_I, name="I real"))
    fig.add_trace(go.Scatter(y=mean_Ihat, name="I observado"))

    fig.update_layout(
        title=f"{label} (T={t_val}) | Var(obs)={round(var,2)}"
    )

    col.plotly_chart(fig, use_container_width=True)

# ===== MÉTRICAS DE REGIME =====
st.header("Diagnóstico dos Regimes")

def regime_metrics(T, noise):
    I, I_hat, _ = run_simulation(T, noise=noise)

    intensidade = np.max(I)
    erro = np.mean((I - I_hat[:len(I)])**2)
    variancia = np.var(I_hat)

    return intensidade, erro, variancia

col1, col2, col3 = st.columns(3)

for col, label, t_val in zip(
    [col1, col2, col3],
    ["T baixo", "T ótimo", "T alto"],
    [T_low, int(T_star), T_high]
):
    intensidade, erro, var = regime_metrics(t_val, noise)

    col.metric(f"{label} | Pico epidêmico", round(intensidade, 1))
    col.metric(f"{label} | Erro", round(erro, 1))
    col.metric(f"{label} | Variância", round(var, 1))


# ===== TRADE-OFF FUNDAMENTAL =====
st.header("Trade-off: Controle vs Conhecimento")

Ts_dense = np.linspace(1, 100, 30)

intensidades = []
erros = []

for t in Ts_dense:
    I, I_hat, _ = run_simulation(t, noise=noise)
    
    intensidade = np.max(I)
    erro = np.mean((I - I_hat[:len(I)])**2)
    
    intensidades.append(intensidade)
    erros.append(erro)

fig_trade = go.Figure()

fig_trade.add_trace(go.Scatter(
    x=intensidades,
    y=erros,
    mode='lines+markers',
    name='Fronteira'
))

fig_trade.update_layout(
    xaxis_title="Intensidade Epidêmica (controle ↓)",
    yaxis_title="Erro de Inferência (conhecimento ↓)",
    title="Fronteira Controle vs Conhecimento"
)

st.plotly_chart(fig_trade, use_container_width=True)


from src.dashboard.tradeoff_upgrade import plot_tradeoff

st.subheader("Fronteira com ponto ótimo (T*)")

fig_trade = plot_tradeoff(noise)
st.plotly_chart(fig_trade, use_container_width=True)

