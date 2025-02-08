import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo ETL con herramientas de Microsoft Fabric
G_fabric = nx.DiGraph()

# Definir los nodos del proceso ETL con herramientas de Microsoft Fabric
nodes_fabric = {
    "SQL Server - DB1": "Extracción",
    "SQL Server - DB2": "Extracción",
    "MySQL - DB1": "Extracción",
    "MySQL - DB2": "Extracción",
    "Extracción": "Transformación (Dataflows Gen2)",
    "Transformación (Dataflows Gen2)": "Carga",
    "OneLake (Bronze Layer)": "Carga",
    "OneLake (Silver Layer)": "Carga",
    "OneLake (Gold Layer)": "Carga",
    "Azure Data Factory": "Orquestación",
    "Power BI": "Visualización",
    "Synapse Analytics": "Análisis",
}

# Agregar nodos al grafo
for node in nodes_fabric.keys():
    G_fabric.add_node(node, label=node)

# Agregar relaciones entre nodos
edges_fabric = [
    ("SQL Server - DB1", "Extracción"),
    ("SQL Server - DB2", "Extracción"),
    ("MySQL - DB1", "Extracción"),
    ("MySQL - DB2", "Extracción"),
    ("Extracción", "Transformación (Dataflows Gen2)"),
    ("Transformación (Dataflows Gen2)", "OneLake (Bronze Layer)"),
    ("OneLake (Bronze Layer)", "OneLake (Silver Layer)"),
    ("OneLake (Silver Layer)", "OneLake (Gold Layer)"),
    ("OneLake (Gold Layer)", "Azure Data Factory"),
    ("Azure Data Factory", "Synapse Analytics"),
    ("Synapse Analytics", "Power BI"),
]

G_fabric.add_edges_from(edges_fabric)

# Dibujar el grafo
plt.figure(figsize=(14, 8))
pos_fabric = nx.spring_layout(G_fabric, seed=42, k=1.5)  # Posiciones de los nodos

# Dibujar nodos y etiquetas
nx.draw(
    G_fabric, pos_fabric, with_labels=True, node_size=3000, 
    node_color="lightblue", edge_color="gray", font_size=9, font_weight="bold"
)

# Mostrar el gráfico
plt.title("Diagrama ETL en Microsoft Fabric")
plt.show()

# Guardar el gráfico en un archivo PNG
output_filename = "diagrama_etl_fabric.png"

plt.figure(figsize=(14, 8))
nx.draw(
    G_fabric, pos_fabric, with_labels=True, node_size=3000, 
    node_color="lightblue", edge_color="gray", font_size=9, font_weight="bold"
)
plt.title("Diagrama ETL en Microsoft Fabric")

# Guardar el archivo en la ruta del script
plt.savefig(output_filename, format="png", dpi=300)
plt.close()

# Confirmar la ruta del archivo guardado
output_filename
