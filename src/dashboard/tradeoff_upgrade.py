import numpy as np
import plotly.graph_objects as go
from src.simulation import run_simulation
from src.utils import utility

def plot_tradeoff(noise):

    Ts = np.linspace(1, 100, 30)

    intensidades = []
    erros = []
    utils = []

    for t in Ts:
        I, I_hat, _ = run_simulation(t, noise=noise)

        intensidade = np.max(I)
        erro = np.mean((I - I_hat[:len(I)])**2)
        u = utility(I, I_hat, _)

        intensidades.append(intensidade)
        erros.append(erro)
        utils.append(u)

    Ts = np.array(Ts)
    intensidades = np.array(intensidades)
    erros = np.array(erros)
    utils = np.array(utils)

    T_star = Ts[np.argmax(utils)]

    fig = go.Figure()

    # curva principal
    fig.add_trace(go.Scatter(
        x=intensidades,
        y=erros,
        mode='lines+markers',
        name='Fronteira'
    ))

    # destacar T*
    idx = np.argmax(utils)

    fig.add_trace(go.Scatter(
        x=[intensidades[idx]],
        y=[erros[idx]],
        mode='markers+text',
        text=[f"T*={round(T_star,1)}"],
        textposition="top center",
        marker=dict(size=12),
        name='Ótimo'
    ))

    fig.update_layout(
        title="Fronteira Controle vs Conhecimento",
        xaxis_title="Intensidade Epidêmica (controle ↓)",
        yaxis_title="Erro de Inferência (conhecimento ↓)"
    )

    return fig
