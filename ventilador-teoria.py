import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import networkx as nx

fig, ax = plt.subplots()

# Desenhar o ventilador
circle = plt.Circle((0.5, 0.5), 0.4, fill=False)
ax.add_artist(circle)

lines = []
for i in range(3):
    line, = ax.plot([], [], 'k-')
    lines.append(line)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Atualizar função para animação
def update(num):
    for i, line in enumerate(lines):
        x = [0.5, 0.5 + 0.4 * np.cos(num * (i+1) / 100.)]
        y = [0.5, 0.5 + 0.4 * np.sin(num * (i+1) / 100.)]
        line.set_data(x, y)
    return lines

# Criar animação
ani = animation.FuncAnimation(fig, update, frames=range(0, 360), interval=100)

plt.show()

# Criar um autômato com 3 estados
G = nx.DiGraph()
G.add_edge('Desligado', 'Baixa', label='Ligar')
G.add_edge('Baixa', 'Média', label='Aumentar')
G.add_edge('Média', 'Alta', label='Aumentar')
G.add_edge('Alta', 'Desligado', label='Desligar')

pos = nx.spring_layout(G)  # posições para todos os nós

fig, ax = plt.subplots()

# nós
nx.draw_networkx_nodes(G, pos, node_size=700)

# rótulos
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# arestas
nx.draw_networkx_edges(G, pos, width=6)

# rótulos das arestas
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)


def update(num):
    ax.clear()
    state = list(G.nodes)[num % len(G.nodes)]
    node_colors = ['red' if node == state else 'black' for node in G.nodes]
    nx.draw(G, pos, node_color=node_colors, with_labels=True, font_color='white')
    return ax,

ani = animation.FuncAnimation(fig, update, frames=range(0, 4), interval=1000)

plt.axis('off')
plt.show()
