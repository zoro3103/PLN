import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Sample training data
sentences = [
    "hello",
    "hi",
    "how are you",
    "what is your name",
    "bye"
]

responses = [
    "Hello!",
    "Hi there!",
    "I am fine.",
    "I am your virtual assistant.",
    "Goodbye!"
]

# Convert text to numbers
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

X = tokenizer.texts_to_sequences(sentences)
X = pad_sequences(X)

# Labels
y = np.array([0, 1, 2, 3, 4])

# Build LSTM Model
model = Sequential([
    Embedding(input_dim=50, output_dim=8, input_length=X.shape[1]),
    LSTM(16),
    Dense(5, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train Model
model.fit(X, y, epochs=200, verbose=0)

# Chat Function
def chatbot():
    print("Virtual Assistant (Type 'exit' to stop)")

    while True:
        text = input("You : ")

        if text.lower() == "exit":
            print("Bot : Goodbye!")
            break

        seq = tokenizer.texts_to_sequences([text])
        seq = pad_sequences(seq, maxlen=X.shape[1])

        prediction = np.argmax(model.predict(seq, verbose=0))

        print("Bot :", responses[prediction])

chatbot()