import tkinter as tk

def generar_tabla():
    try:
        numero = int(entry_numero.get())
    except ValueError:
        numero = 1
    
    try:
        limite = int(entry_limite.get())
    except ValueError:
        limite = 10
    
    if numero > limite:
        resultado.config(state="normal")
        resultado.delete(1.0, tk.END)
        resultado.insert(tk.END, f"¡Ingresa un numero igual o menor a {limite}.")
        resultado.config(state="disabled")
    else:
        resultado.config(state="normal")
        resultado.delete(1.0, tk.END)
        for i in range(1, limite + 1):
            resultado.insert(tk.END, f"{numero} x {i} = {numero*i}\n")
        resultado.config(state="disabled")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Tablas de multiplicar por Tessy")
ventana.resizable(False, False)

# Crear y posicionar los widgets
label_numero = tk.Label(ventana, text="Ingrese un número:")
label_numero.grid(row=0, column=0, padx=10, pady=10)

entry_numero = tk.Entry(ventana)
entry_numero.insert(0, '1')  # Valor predeterminado para el número
entry_numero.grid(row=0, column=1, padx=10, pady=10)

label_limite = tk.Label(ventana, text="Ingrese el máximo de la tabla:")
label_limite.grid(row=1, column=0, padx=10, pady=10)

entry_limite = tk.Entry(ventana)
entry_limite.insert(0, '10')  # Valor predeterminado para el máximo
entry_limite.grid(row=1, column=1, padx=10, pady=10)

boton_generar = tk.Button(ventana, text="Generar tabla", command=generar_tabla)
boton_generar.grid(row=0, column=2, rowspan=2, padx=10, pady=10)

resultado = tk.Text(ventana, height=10, width=30, state="disabled")
resultado.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Ejecutar el bucle de eventos
ventana.mainloop()
