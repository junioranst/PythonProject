# ==============================================================================
# Passo 1: Importar Bibliotecas e Carregar Dados
# ==============================================================================
import tensorflow as tf
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical

# Carregar conjunto de dados Iris
iris = load_iris()
X = iris.data
y = iris.target

# ==============================================================================
# Passo 2: Pré-processamento dos Dados
# ==============================================================================
# 1. Dividir em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Converter rótulos em one-hot encoding
y_train = to_categorical(y_train, num_classes=3)
y_test = to_categorical(y_test, num_classes=3)


# ==============================================================================
# Passo 3: Construir o Modelo
# ==============================================================================
model = tf.keras.Sequential([

    tf.keras.layers.Dense(10, activation='relu', input_shape=(4,)),

    tf.keras.layers.Dense(8, activation='relu'),

    tf.keras.layers.Dense(3, activation='softmax')
])

# Compilar o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print("--- Resumo da Arquitetura do Modelo ---")
model.summary()
print("---------------------------------------")


# ==============================================================================
# Passo 4: Treinar o Modelo
# ==============================================================================

history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=5,
    validation_split=0.2,
    verbose=0
)
# ==============================================================================
# Passo 5: Avaliar o Modelo
# ==============================================================================
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"\n=======================================================")
print(f"Acurácia Final no Conjunto de Teste: {accuracy*100:.2f}%")
print(f"Perda (Loss) Final no Conjunto de Teste: {loss:.4f}")
print(f"=======================================================")


# ==============================================================================
# Passo 6: Fazer as Previsões
# ==============================================================================
y_pred_prob = model.predict(X_test)

# Converter as probabilidades em classes
import numpy as np
y_pred_classes = np.argmax(y_pred_prob, axis=1)

print("\n--- Primeiras 5 Previsões ---")
print("Probabilidades (Saída Softmax):")
print(y_pred_prob[:5])
print("\nClasses Previstas (0, 1 ou 2):")
print(y_pred_classes[:5])
print("\nClasses Reais:")
print(np.argmax(y_test[:5], axis=1))