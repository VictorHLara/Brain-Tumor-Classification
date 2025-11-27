# 🧠 Brain-Tumor-Classification

Este projeto implementa um pipeline completo de classificação de tumores cerebrais utilizando Redes Neurais Convolucionais e modelos pré-treinados (ResNet-18, AlexNet, ViT-B/16), avaliando cenários com e sem Data Augmentation.
O código realiza treinamento, validação, teste, exportação de métricas, confusion matrix, e salvamento do modelo, seguindo práticas de reprodutibilidade.

## 📌 Descrição Detalhada do Projeto:

O objetivo é classificar imagens do dataset Brain Tumor MRI em diferentes categorias de tumores. O mesmo está disponível em https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset.

O projeto utiliza PyTorch e Torchvision e implementa todas as etapas:

✔ Organização do projeto:

- Leitura do dataset a partir de diretórios estruturados por classes.

- Split estratificado automático: treino / validação / teste.

- Dataset customizado (BrainDataset) para carregar imagens e rótulos.

## 🤖 Os modelos treinados foram:

- RESNET-18 -> sem data augmentation

- RESNET-18 -> com dataaugmentation

- VIT-B/16 -> sem data augmentation

- VIT-B/16 -> com data augmentation

## 💪 Treinamento

Otimizador: AdamW

Scheduler: CosineAnnealingLR

Loss: CrossEntropyLoss

Épocas: 50

Tamanho do batch: 64

## ⭐ Avaliação

No final:

- Calcula classificação no conjunto de teste

- Gera matriz de confusão

- Gera classification report

- Exporta métricas para CSV

- Exporta matriz de confusão em PNG

## 📁 Estrutura Esperada do Dataset:
```bash
brain_cancer/
    ├── class_1/
    │      ├── img1.png
    │      ├── img2.png
    │      └── ...
    ├── class_2/
    ├── class_3/
    └── class_4/
```

## 🚀 Instruções de Execução:

### ✅ 1. Requisitos:
Python 3.8+

 Dependências:
```bash
pip install torch torchvision scikit-learn numpy matplotlib seaborn pillow
```

## 📦 2. Configuração do Caminho do Dataset
```bash
ds_path = '/content/drive/My Drive/brain_cancer_Unified'
```
## ▶ 3. Como executar o treinamento

->Google Colab

- Faça download e abra o .ipynb

- Monte seu Google Drive

- Ajuste o dataset ao formato adequado para o código, há um script que pode ajudar na pasta `notebooks`

- Ajuste o ds_path

- Execute o script inteiro


## 💡 Observações Importantes

- O código inclui reprodutibilidade completa: seeds para numpy, random e PyTorch.

- Ele detecta automaticamente GPU.

- Funções de softmax e extração de probabilidades já estão implementadas.

- O treinamento usa fine-tuning em modelos pré-treinados.

## 📊 Créditos:

O código utilizado teve como base o código fornecido pelo professor João Mari na Disciplina,na Lecture 6 part 4, disponível em https://github.com/joaofmari/SIN393_Introduction-to-computer-vision_2023/tree/main/notebooks
