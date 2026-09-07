datasets = [
    "https://ignaciorlando.github.io/datasets/data-science/ObesityDataSet_raw_and_data_sinthetic.txt",
    "https://ignaciorlando.github.io/datasets/data-science/ObesityDataSet_raw_and_data_sinthetic.csv",
    "https://ignaciorlando.github.io/datasets/data-science/netflix_titles.txt",
    "https://ignaciorlando.github.io/datasets/data-science/netflix_titles.csv",

    # tp 4
    "https://ignaciorlando.github.io/datasets/data-science/movies.csv",
    "https://ignaciorlando.github.io/datasets/data-science/food.zip",
]

def extract_if_zip(file_name, file_path):
    import zipfile

    if file_name.lower().endswith(".zip"):
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall(".") 

def descargar(urls=datasets, force=False):
    from urllib import request as req
    import os

    for url in urls:
        file_name = url.split('/')[-1]
        file_path = f"./{file_name}"
        
        if os.path.exists(file_path) and not force:
            continue
            
        req.urlretrieve(url, file_path)

        extract_if_zip(file_name, file_path)

def mostrar_archivo(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        descripcion = f.read()
        print(descripcion)

# No lo meto en un `if __name__ == "__main__":` a propositoo asi solo con hacer `import utils` ya se descarga
descargar()