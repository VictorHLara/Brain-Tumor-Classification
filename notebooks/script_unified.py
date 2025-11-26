import os
import shutil

origem = "/content/drive/MyDrive/brain_cancer"

destino = "/content/drive/MyDrive/brain_cancer_Unified"

os.makedirs(destino, exist_ok=True)

subpastas = ["train", "test"]

for subpasta in subpastas:
    caminho_sub = os.path.join(origem, subpasta)

    classes = os.listdir(caminho_sub)

    for classe in classes:
        caminho_classe = os.path.join(caminho_sub, classe)

        destino_classe = os.path.join(destino, classe)
        os.makedirs(destino_classe, exist_ok=True)

        arquivos = os.listdir(caminho_classe)

        for arquivo in arquivos:
            src = os.path.join(caminho_classe, arquivo)
            dst = os.path.join(destino_classe, arquivo)

            shutil.copy2(src, dst)

print("Dataset reorganizado com sucesso!")