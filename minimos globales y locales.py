import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Ejercicios de Mínimos Globales y Locales")

# Ejercicio 1
st.header("Ejercicio 1")
st.write("Verifica si los puntos son minimizadores globales o locales para \(f(x) = x^2 - 4x + 5\).")

# Gráfico de la función
x = np.linspace(-1, 5, 100)
f = x**2 - 4*x + 5

fig1, ax1 = plt.subplots()
ax1.plot(x, f, label=r"$f(x) = x^2 - 4x + 5$")
ax1.scatter([2], [1], color="red", label="Mínimo global en (2, 1)")
ax1.set_title("Parábola con mínimo global")
ax1.axhline(0, color="black", linewidth=0.5)
ax1.axvline(0, color="black", linewidth=0.5)
ax1.legend()
st.pyplot(fig1)

# Ejercicio 2
st.header("Ejercicio 2")
st.write("Dibuja la función \(f(x) = |x|\) y determina si tiene un mínimo global o local en \(x = 0\).")

x = np.linspace(-3, 3, 100)
f_abs = np.abs(x)

fig2, ax2 = plt.subplots()
ax2.plot(x, f_abs, label=r"$f(x) = |x|$")
ax2.scatter([0], [0], color="red", label="Mínimo global en (0, 0)")
ax2.set_title("Función módulo")
ax2.axhline(0, color="black", linewidth=0.5)
ax2.axvline(0, color="black", linewidth=0.5)
ax2.legend()
st.pyplot(fig2)

# Ejercicio 3
st.header("Ejercicio 3")
st.write("Utilizando el Teorema de Weierstrass, analiza \(f(x) = \sin(x)\) en \([0, \pi]\).")

x = np.linspace(0, np.pi, 100)
f_sin = np.sin(x)

fig3, ax3 = plt.subplots()
ax3.plot(x, f_sin, label=r"$f(x) = \sin(x)$")
ax3.scatter([0, np.pi], [0, 0], color="red", label="Mínimos globales en (0, 0) y (\(\pi\), 0)")
ax3.scatter([np.pi/2], [1], color="green", label="Máximo global en (\(\pi/2\), 1)")
ax3.set_title("Función seno en [0, π]")
ax3.axhline(0, color="black", linewidth=0.5)
ax3.axvline(0, color="black", linewidth=0.5)
ax3.legend()
st.pyplot(fig3)

# Ejercicio 4
st.header("Ejercicio 4")
st.write("Analiza \(f(x, y) = x^2 + y^2\) bajo la restricción \(x^2 + y^2 \leq 1\).")

theta = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)

fig4, ax4 = plt.subplots()
ax4.plot(x_circle, y_circle, label="Restricción \(x^2 + y^2 = 1\)")
ax4.scatter([0], [0], color="red", label="Mínimo global en (0, 0)")
ax4.set_title("Paraboloide restringido")
ax4.axhline(0, color="black", linewidth=0.5)
ax4.axvline(0, color="black", linewidth=0.5)
ax4.legend()
st.pyplot(fig4)

# Ejercicio 5
st.header("Ejercicio 5")
st.write("Ejemplo donde un mínimo global no es único: \(f(x) = x^4 - x^2\).")

x = np.linspace(-1.5, 1.5, 200)
f_unique = x**4 - x**2

fig5, ax5 = plt.subplots()
ax5.plot(x, f_unique, label=r"$f(x) = x^4 - x^2$")
ax5.scatter([-1/np.sqrt(2), 1/np.sqrt(2)], [-1/4, -1/4], color="red", label="Mínimos globales en \(\pm1/\sqrt{2}\)")
ax5.scatter([0], [0], color="green", label="Máximo local en (0, 0)")
ax5.set_title("Función con mínimos globales no únicos")
ax5.axhline(0, color="black", linewidth=0.5)
ax5.axvline(0, color="black", linewidth=0.5)
ax5.legend()
st.pyplot(fig5)
