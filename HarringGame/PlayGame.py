from CreateGame import Game
import itertools
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def generate_training_data(num_scenarios):
    X_train = []
    y_train = []
    game = Game()  # Assuming Game class is defined as provided in the initial code
    
    for _ in range(num_scenarios):
        # Simulate a game scenario
        if game.p1Points < 1 or game.p2Points < 1:
            # Handle the case where points are not enough for wager
            continue
        
        p1_wager = np.random.randint(1, game.p1Points + 1)
        p2_wager = np.random.randint(1, game.p2Points + 1)
        game.wager(p1_wager, p2_wager)
        
        # Record the input-output pair
        wager_diff = p1_wager - p2_wager
        X_train.append(wager_diff)
        
        if p1_wager > p2_wager:
            y_train.append(1)  # Player 1 wins
        else:
            y_train.append(0)  # Player 1 loses or ties
    
    # Convert lists to numpy arrays
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    
    return X_train, y_train

# Generate training data
num_scenarios = 10000  # You can adjust this number based on your computational resources
X_train, y_train = generate_training_data(num_scenarios)

# Build the neural network model
model = Sequential([
    Dense(128, activation='relu', input_shape=(1,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Evaluate the model (optional)
# You can evaluate the model using a validation set or test set if available.

# Generate test data using the same function as training data
num_test_samples = 1000  # You can adjust the number of test samples as needed
X_test, y_test = generate_training_data(num_test_samples)

# Preprocess test data (if needed)
# Perform any preprocessing steps similar to what you did for training data

# Evaluate model performance on test data
loss, accuracy = model.evaluate(X_test, y_test)

print("Test Loss:", loss)
print("Test Accuracy:", accuracy)


