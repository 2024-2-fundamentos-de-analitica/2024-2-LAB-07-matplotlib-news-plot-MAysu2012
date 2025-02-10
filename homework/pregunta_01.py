"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    ruta_S = "files/plots/news.png"
    ruta_E = "files/input/news.csv"
    
    os.makedirs(os.path.dirname(ruta_S), exist_ok=True)
    
    plt.figure()
    
    estilos = {
        "Television": {"color": "dimgray", "zorder": 1, "linewidth": 2},
        "Newspaper": {"color": "grey", "zorder": 1, "linewidth": 2},
        "Internet": {"color": "tab:blue", "zorder": 2, "linewidth": 4},
        "Radio": {"color": "Lightgrey", "zorder": 1, "linewidth": 2}
    }
    
    df = pd.read_csv(ruta_E, index_col=0)

    for medio, estilo in estilos.items():
        if medio in df.columns:
            plt.plot(
                df[medio],
                label=medio,
                color=estilo["color"],
                linewidth=estilo["linewidth"],
                zorder=estilo["zorder"]
            )
            
            primer_año = df[medio].index[0]
            plt.scatter(primer_año, df[medio].iloc[0], color=estilo["color"], zorder=estilo["zorder"])
            plt.text(primer_año - 0.2, df[medio].iloc[0], f"{medio} {df[medio].iloc[0]}%", ha="right", va="center", color=estilo["color"])

            ultimo_año = df[medio].index[-1]
            plt.scatter(ultimo_año, df[medio].iloc[-1], color=estilo["color"], zorder=estilo["zorder"])
            plt.text(ultimo_año + 0.2, df[medio].iloc[-1], f"{df[medio].iloc[-1]}%", ha="left", va="center", color=estilo["color"])

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    plt.xticks(ticks=df.index, labels=df.index, ha="center")
    
    plt.savefig(ruta_S)
    plt.show()
    
if __name__ == "__main__":
    pregunta_01()