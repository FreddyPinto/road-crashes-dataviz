import os
import pandas as pd


def read_excel_files(folder_path):
    """
    Lee todos los archivos .xlsx en una carpeta y los almacena en un diccionario de DataFrames.

    Parámetros:
    folder_path (str): La ruta de la carpeta que contiene los archivos .xlsx.
    dfs_name (str): El nombre del diccionario que almacenará los DataFrames.

    Retorna:
    dict: Un diccionario de DataFrames, donde cada clave es el nombre de un archivo y su valor es el DataFrame correspondiente.
    """
    # Obtiene la lista de archivos .xlsx en la carpeta
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

    # Crea un diccionario para almacenar los DataFrames e inicializa un contador para enumerarlos
    dfs = {}
    n = 1

    for file in files:
        # Define la ruta completa del archivo
        file_path = os.path.join(folder_path, file)

        # Lee el archivo .xlsx con pandas
        xls = pd.ExcelFile(file_path)

        # Obtiene la lista de nombres de las hojas en el archivo
        sheet_names = xls.sheet_names

        for sheet_name in sheet_names:
            # Lee cada hoja del archivo como un DataFrame
            df = xls.parse(sheet_name)

            # Almacena el DataFrame en el diccionario
            dfs[f'{file}_{sheet_name}'] = df

            # Imprime el nombre del DataFrame
            print(f'DataFrame {n}: {file}_{sheet_name}')

            # Incrementa el contador
            n += 1

    # imprime la cantidad de dfs
    print(f'Cantidad de DataFrames: {len(dfs.keys())}')

    return dfs

def dataframe_to_csv(dataframe:pd.DataFrame, folder_path:str, file_name:str):

    """
    Guarda un DataFrame en un archivo CSV.

    Args:
        dataframe: El DataFrame que queremos exportar.
        folder_path: La ruta de destino del archivo.
        file_name: El nombre del archivo.

    Returns:
        None
    """

    # Verificamos si el folder_path existe
    if not os.path.exists(folder_path):
        # Si no existe, lo creamos
        os.makedirs(folder_path)

    # Exportamos el DataFrame a un archivo CSV
    dataframe.to_csv(os.path.join(folder_path, file_name), index=False)

    print(f'El archivo {file_name} se guardó correctamente en {folder_path}')


