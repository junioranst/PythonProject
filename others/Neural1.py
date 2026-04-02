# ==============================================================================
# Passo 1: Importar Bibliotecas e Carregar Dados
# ==============================================================================
import tensorflow as tf
import pandas as pd # Importado, mas não usado diretamente, o que é comum.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical # Necessário para One-Hot Encoding

# Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data # Características (4: comprimento e largura de sépalas e pétalas)
y = iris.target # Rótulos (3 classes: 0, 1, 2)

# ==============================================================================
# Passo 2: Pré-processamento dos Dados
# ==============================================================================
# 1. Dividir em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42 # random_state garante reprodutibilidade
)

# 2. Normalizar os dados (Padronização)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train) # Aprende e transforma nos dados de treino
X_test = scaler.transform(X_test)       # Apenas transforma nos dados de teste

# Converter rótulos em one-hot encoding (Necessário para a perda categorical_crossentropy)
y_train = to_categorical(y_train, num_classes=3)
y_test = to_categorical(y_test, num_classes=3)


# ==============================================================================
# Passo 3: Construir o Modelo
# ==============================================================================
model = tf.keras.Sequential([
    # Camada Oculta 1: 10 neurônios, ativação 'relu', 4 entradas
    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),
    # Camada Oculta 2: 8 neurônios, ativação 'relu'
    tf.keras.layers.Dense(8, activation='relu'),
    # Camada de Saída: 3 neurônios (para 3 classes), ativação 'softmax' (probabilidades)
    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy', # Perda para classificação multi-classe
              metrics=['accuracy'])

print("--- Resumo da Arquitetura do Modelo ---")
model.summary()
print("---------------------------------------")


# ==============================================================================
# Passo 4: Treinar o Modelo
# ==============================================================================
print("\nIniciando o Treinamento...")
history = model.fit(
    X_train, y_train,
    epochs=50,        # Número de passagens completas pelos dados
    batch_size=5,     # Quantidade de amostras por atualização de peso
    validation_split=0.2, # 20% do treino usado para validação durante o treino
    verbose=0 # Mantido em 0 para não imprimir o log completo, mas pode ser 1 para ver o processo
)
print("Treinamento concluído.")

# ==============================================================================
# Passo 5: Avaliar o Modelo
# ==============================================================================
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n=======================================================")
print(f"Acurácia Final no Conjunto de Teste: {accuracy*100:.2f}%")
print(f"Perda (Loss) Final no Conjunto de Teste: {loss:.4f}")
print(f"=======================================================")


# ==============================================================================
# Passo 6: Fazer Previsões
# ==============================================================================
y_pred_prob = model.predict(X_test)

# Converter as probabilidades em classes (pegando o índice da maior probabilidade)
import numpy as np
y_pred_classes = np.argmax(y_pred_prob, axis=1)

print("\n--- Primeiras 5 Previsões ---")
print("Probabilidades (Saída Softmax):")
print(y_pred_prob[:5])
print("\nClasses Previstas (0, 1 ou 2):")
print(y_pred_classes[:5])
print("\nClasses Reais:")
# As classes reais precisam ser convertidas de volta de one-hot para ver o label
print(np.argmax(y_test[:5], axis=1))