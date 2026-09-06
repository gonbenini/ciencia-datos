def descargar(urls, force=False):
    from urllib import request as req
    import os

    for url in urls:
        file_name = url.split('/')[-1]
        file_path = f"./{file_name}"
        
        if os.path.exists(file_path) and not force:
            continue
            
        req.urlretrieve(url, file_path)

def mostrar_archivo(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        descripcion = f.read()
        print(descripcion)

# No lo meto en un `if __name__ == "__main__":` a propositoo asi solo con hacer `import utils` ya se descarga
descargar([
    "https://ignaciorlando.github.io/datasets/data-science/ObesityDataSet_raw_and_data_sinthetic.txt",
    "https://ignaciorlando.github.io/datasets/data-science/ObesityDataSet_raw_and_data_sinthetic.csv"
])