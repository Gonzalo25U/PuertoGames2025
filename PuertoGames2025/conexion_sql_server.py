import pyodbc

#Obtener Videojuego(mostrar)
def obtener_videojuegos(nombre_busqueda=None):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    if nombre_busqueda:
        consulta = """
            SELECT v.Titulo, v.Precio, v.Stock, p.Nombre AS Plataforma
            FROM Videojuego v
            JOIN Plataforma p ON v.IDPlataforma = p.IDPlataforma
            WHERE v.Titulo LIKE ?
        """
        cursor.execute(consulta, ('%' + nombre_busqueda + '%',))
    else:
        consulta = """
            SELECT v.Titulo, v.Precio, v.Stock, p.Nombre AS Plataforma
            FROM Videojuego v
            JOIN Plataforma p ON v.IDPlataforma = p.IDPlataforma
        """
        cursor.execute(consulta)

    resultados = cursor.fetchall()
    conn.close()
    return resultados

#Agregar Videojuego
def insertar_videojuego(titulo, precio, stock, plataforma):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    cursor.execute("SELECT IDPlataforma FROM Plataforma WHERE Nombre = ?", (plataforma,))
    resultado = cursor.fetchone()
    if resultado:
        id_plataforma = resultado[0]
    else:
#Si no existe la plataforma, puedes insertar o avisar error
        raise Exception("Plataforma no encontrada")

    cursor.execute(
        "INSERT INTO Videojuego (Titulo, Precio, Stock, IDPlataforma) VALUES (?, ?, ?, ?)",
        (titulo, precio, stock, id_plataforma)
    )
    conn.commit()
    conn.close()



#Actualizar base de datos

def actualizar_videojuego(titulo_original, nuevo_titulo, precio, stock, plataforma_nombre):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

#Obtener IDPlataforma
    cursor.execute("SELECT IDPlataforma FROM Plataforma WHERE Nombre = ?", (plataforma_nombre,))
    plataforma = cursor.fetchone()
    if plataforma is None:
        raise Exception("Plataforma no encontrada.")

    id_plataforma = plataforma[0]

#Actualizar videojuego
    cursor.execute("""
        UPDATE Videojuego
        SET Titulo = ?, Precio = ?, Stock = ?, IDPlataforma = ?
        WHERE Titulo = ?
    """, (nuevo_titulo, precio, stock, id_plataforma, titulo_original))

    conn.commit()
    conn.close()

#Eliminar
def eliminar_videojuego(titulo):
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Videojuego WHERE Titulo = ?", (titulo,))
    conn.commit()
    conn.close()
    
#Grafico

def obtener_estadisticas_por_plataforma():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=PuertoGames2025;'
        'Trusted_Connection=yes;'
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.Nombre, COUNT(*) AS cantidad
        FROM Videojuego v
        JOIN Plataforma p ON v.IDPlataforma = p.IDPlataforma
        GROUP BY p.Nombre
    """)
    
    resultados = cursor.fetchall()
    conn.close()
    return resultados
