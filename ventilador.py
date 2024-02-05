import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

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

# Adicionar texto para a velocidade do ventilador
speed_text = ax.text(0.5, 0.9, '', horizontalalignment='center')

# Atualizar função para animação
def update(num):
    # Definir a velocidade do ventilador
    if num // 100 % 3 == 0:
        speed = 1
        speed_text.set_text('Velocidade: Baixa')
    elif num // 100 % 3 == 1:
        speed = 2
        speed_text.set_text('Velocidade: Média')
    else:
        speed = 3
        speed_text.set_text('Velocidade: Alta')

    for i, line in enumerate(lines):
        x = [0.5, 0.5 + 0.4 * np.cos(num * speed * (i+1) / 100.)]
        y = [0.5, 0.5 + 0.4 * np.sin(num * speed * (i+1) / 100.)]
        line.set_data(x, y)

    return lines

# Criar animação
ani = animation.FuncAnimation(fig, update, frames=range(0, 36000), interval=10)

plt.show()