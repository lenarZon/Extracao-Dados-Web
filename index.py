import pandas
import pandas as pd
import requests
import zipfile
from io import BytesIO
import urllib3

# Variaveis
path = "" # Pasta da gravação
link = "";


# Tirando o aviso
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Comecando o codigo
def extractArq(past, url):

        # Download do arquivo
        fyles = BytesIO (
                requests.get(url, verify=False).content
        )

        # Extraindo o arquivo zipado
        myzip = zipfile.ZipFile(fyles)
        myzip.extractall(past)


extractArq(path, link)
print("Arquivo Gravado!")