import tkinter as tk
from tkinter import ttk, messagebox
from conexion_sql_server import obtener_videojuegos, insertar_videojuego, actualizar_videojuego, eliminar_videojuego, obtener_estadisticas_por_plataforma
import matplotlib.pyplot as plt

#Crear ventana
ventana = tk.Tk()
ventana.title("Catálogo de Videojuegos")
ventana.geometry("1100x800")

#Titulo
titulo_label = tk.Label(ventana, text="🎮 Catálogo de Videojuegos", font=("Arial", 18, "bold"))
titulo_label.pack(pady=15)

#Etiquetas y campos de entrada
frame_form = tk.LabelFrame(ventana, text="Crear Videojuego", padx=10, pady=10)
frame_form.pack(pady=10, fill="x", padx=20)

tk.Label(frame_form, text="Título:").grid(row=0, column=0, sticky="e")
entrada_titulo = tk.Entry(frame_form, width=30)
entrada_titulo.grid(row=0, column=1)

tk.Label(frame_form, text="Precio:").grid(row=0, column=2, sticky="e")
entrada_precio = tk.Entry(frame_form, width=20)
entrada_precio.grid(row=0, column=3)

tk.Label(frame_form, text="Stock:").grid(row=1, column=0, sticky="e")
entrada_stock = tk.Entry(frame_form, width=30)
entrada_stock.grid(row=1, column=1)

tk.Label(frame_form, text="Plataforma:").grid(row=1, column=2, sticky="e")
entrada_plataforma = tk.Entry(frame_form, width=20)
entrada_plataforma.grid(row=1, column=3)

#Crear videojuego 
def crear_videojuego():
    titulo = entrada_titulo.get()
    try:
        
        #Validamos que precio y stock sean numeros
        precio = float(entrada_precio.get())
        stock = int(entrada_stock.get())
    except ValueError:
        messagebox.showwarning("Error", "Precio y Stock deben ser numéricos.")
        return
    plataforma = entrada_plataforma.get()
    
    
        #Validar que ningun campo este vacio
    if not titulo or not plataforma:
        messagebox.showwarning("Error", "Todos los campos son obligatorios.")
        return
    try:
        insertar_videojuego(titulo, precio, stock, plataforma)
        messagebox.showinfo("Éxito", "Videojuego creado.")
        listar_videojuegos()  # Refresca la tabla
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
#Cargar los datos del videojuego seleccionado en el formulario (para edición)
def cargar_datos_edicion(event=None):
    seleccion = tabla.focus()
    if not seleccion:
        return
    valores = tabla.item(seleccion, "values")
    if valores:
        entrada_titulo.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_stock.delete(0, tk.END)
        entrada_plataforma.delete(0, tk.END)

        entrada_titulo.insert(0, valores[0])
        entrada_precio.insert(0, valores[1].replace("$", ""))
        entrada_stock.insert(0, valores[2])
        entrada_plataforma.insert(0, valores[3])
        tabla.bind("<<TreeviewSelect>>", cargar_datos_edicion)

#Eliminar videojuego seleccionado
def eliminar_videojuego_desde_tabla():
    seleccion = tabla.focus()
    
    #mensaje al no seleccionar
    if not seleccion:
        messagebox.showwarning("Atención", "Selecciona un videojuego para eliminar.")
        return

    valores = tabla.item(seleccion, "values")
    titulo = valores[0]
    
    #confirmacion de la eliminacion
    confirmacion = messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar '{titulo}'?")
    if confirmacion:
        try:
            eliminar_videojuego(titulo)
            messagebox.showinfo("Eliminado", "Videojuego eliminado correctamente.")
            listar_videojuegos()
        except Exception as e:
            messagebox.showerror("Error", str(e))


#Boton: Crear
btn_crear = tk.Button(frame_form, text="Crear Videojuego", command=crear_videojuego)
btn_crear.grid(row=2, column=0, columnspan=4, pady=10)

#Actualizar videojuego seleccionado
def actualizar_videojuego_desde_formulario():
    seleccion = tabla.focus()
    
    #mensaje al no seleccionar
    if not seleccion:
        messagebox.showwarning("Atención", "Selecciona un videojuego para editar.")
        return

    titulo_original = tabla.item(seleccion, "values")[0]
    nuevo_titulo = entrada_titulo.get()
    try:
    #Validamos que precio y stock sean numeros
        precio = float(entrada_precio.get())
        stock = int(entrada_stock.get())
    except ValueError:
        messagebox.showwarning("Error", "Precio y Stock deben ser numéricos.")
        return
    plataforma = entrada_plataforma.get()
    
    try:
        actualizar_videojuego(titulo_original, nuevo_titulo, precio, stock, plataforma)
        messagebox.showinfo("Éxito", "Videojuego actualizado.")
        listar_videojuegos()
    except Exception as e:
        messagebox.showerror("Error", str(e))
        
#Boton Actualizar
btn_actualizar = tk.Button(frame_form, text="Actualizar Videojuego", command=actualizar_videojuego_desde_formulario)
btn_actualizar.grid(row=3, column=0, columnspan=4, pady=5)

#Boton Eliminar
btn_eliminar = tk.Button(frame_form, text="Eliminar Videojuego", command=eliminar_videojuego_desde_tabla)
btn_eliminar.grid(row=5, column=0, columnspan=4, pady=10)

#Frame Busqueda 
frame_busqueda = tk.Frame(ventana)
frame_busqueda.pack(pady=10)

entrada_busqueda = tk.Entry(frame_busqueda, width=40)
entrada_busqueda.pack(side=tk.LEFT, padx=5)


#Buscar Videojuegos
def buscar_videojuego():
    query = entrada_busqueda.get()
    resultados = obtener_videojuegos(query)
    tabla.delete(*tabla.get_children())  # Limpiar tabla
    for vj in resultados:
        titulo, precio, stock, plataforma = vj
        tabla.insert("", tk.END, values=(titulo, f"${precio:.2f}", stock, plataforma))

#Boton de Buscar
btn_buscar = tk.Button(frame_busqueda, text="🔍 Buscar", command=buscar_videojuego)
btn_buscar.pack(side=tk.LEFT)


# Botones Frame 
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

#Lista de Videojuegos
def listar_videojuegos():
    tabla.delete(*tabla.get_children())
    videojuegos = obtener_videojuegos()
    for vj in videojuegos:
        titulo, precio, stock, plataforma = vj
        tabla.insert("", tk.END, values=(titulo, f"${precio:.2f}", stock, plataforma))

#Boton para ver la lista de Videojuegos de forma ordenada
btn_listar = tk.Button(frame_botones, text="📋 Listar Videojuegos", command=listar_videojuegos)
btn_listar.pack(side=tk.LEFT, padx=5)

#Boton de cerrar
btn_cerrar = tk.Button(frame_botones, text="❌ Cerrar", command=ventana.destroy)
btn_cerrar.pack(side=tk.LEFT, padx=5)

#funcion para ver el grafico
def mostrar_grafico_estadisticas():
    datos = obtener_estadisticas_por_plataforma()

    if not datos:
        messagebox.showinfo("Sin datos", "No hay datos para mostrar.")
        return

    plataformas = [fila[0] for fila in datos]
    cantidades = [fila[1] for fila in datos]

    # Gráfico de Torta
    plt.figure(figsize=(6, 6))
    plt.pie(cantidades, labels=plataformas, autopct="%1.1f%%", startangle=140)
    plt.title("Distribución de videojuegos por plataforma")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
    
#Boton para ver el grafico    
btn_estadisticas = tk.Button(ventana, text="📊 Ver estadísticas", command=mostrar_grafico_estadisticas)
btn_estadisticas.pack(pady=10)

#Frame de tabla
frame_tabla = tk.Frame(ventana)
frame_tabla.pack(padx=20, pady=10)

scrollbar = tk.Scrollbar(frame_tabla)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tabla = ttk.Treeview(frame_tabla, yscrollcommand=scrollbar.set, columns=("Titulo", "Precio", "Stock", "Plataforma"), show="headings", height=15)
tabla.pack(side=tk.LEFT)

scrollbar.config(command=tabla.yview)

# Configurar columnas
tabla.heading("Titulo", text="Título")
tabla.heading("Precio", text="Precio")
tabla.heading("Stock", text="Stock")
tabla.heading("Plataforma", text="Plataforma")

tabla.column("Titulo", width=300)
tabla.column("Precio", width=100)
tabla.column("Stock", width=80)
tabla.column("Plataforma", width=150)

#cargar los datos para mostrar la tabla al inicio
listar_videojuegos()

# Iniciar
ventana.mainloop()





