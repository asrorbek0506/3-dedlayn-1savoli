# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1csLHk1-dNt7uBhRlijcU94EKrQarfkvS
"""

import numpy as np
import matplotlib.pyplot as plt

# X qiymatlari uchun oraliq
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# Sinus funksiyasi
y = np.sin(x)

# Grafikni chizish
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=r"$y = \sin(x)$", color="blue")

# Koordinata o'qlari
plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # gorizontal chiziq
plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # vertikal chiziq

# Grafikning sarlavhasi va o'qlar nomlari
plt.title("Sinus funksiyasining grafigi", fontsize=14)
plt.xlabel("$x$", fontsize=12)
plt.ylabel("$y$", fontsize=12)

# O'qlar bo'yicha shkalalar va ularning belgilari
plt.xticks(
    ticks=[-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
    labels=[r"$-2\pi$", r"$-\pi$", "$0$", r"$\pi$", r"$2\pi$"]
)
plt.yticks(ticks=[-1, 0, 1])

# Panjara va afsona
plt.grid(alpha=0.5)
plt.legend(fontsize=12)

# Grafikni ko'rsatish
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Tasodifiy ma'lumotlarni yaratish
x = np.random.rand(100)  # 100 ta tasodifiy x qiymatlari
y = np.random.rand(100)  # 100 ta tasodifiy y qiymatlari

# Scatter grafikni chizish
plt.scatter(x, y, color='blue', marker='o')  # Nuqtalarni chizish
plt.title('Tasodifiy Nuqtalar Scatter Grafiği')  # Grafik nomi
plt.xlabel('X o\'qi')  # X o'qi nomi
plt.ylabel('Y o\'qi')  # Y o'qi nomi

# Grafikni ko'rsatish
plt.show()