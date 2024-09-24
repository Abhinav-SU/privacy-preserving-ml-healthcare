import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_and_train_model(encrypted_file, private_key_file, original_data_file):
    # Load encrypted data
    encrypted_data = pd.read_pickle(encrypted_file)

    # Load private key
    with open(private_key_file, 'rb') as f:
        private_key = pickle.load(f)

    # Decrypt data
    decrypted_data = encrypted_data.applymap(lambda x: private_key.decrypt(x))

    # Load and clean original data
    original_data = pd.read_csv(original_data_file)
    
    # Fill missing values instead of dropping rows
    original_data = original_data.apply(pd.to_numeric, errors='coerce').fillna(0)

    # Ensure there are rows left after cleaning
    if original_data.shape[0] == 0:
        raise ValueError("After data cleaning, no valid rows remain in the original dataset.")
    
    # Train model on decrypted data
    X_decrypted = decrypted_data.iloc[:, :-1]
    y_decrypted = decrypted_data.iloc[:, -1]

    # Ensure decrypted data has enough rows
    if X_decrypted.shape[0] == 0:
        raise ValueError("Decrypted data has no valid rows left for model training.")
    
    model = LinearRegression()
    model.fit(X_decrypted, y_decrypted)
    predictions = model.predict(X_decrypted)
    
    mse = mean_squared_error(y_decrypted, predictions)
    print(f"--- Decrypted Model MSE: {mse} ---")

    # Train model on original unencrypted data
    X_original = original_data.iloc[:, :-1]
    y_original = original_data.iloc[:, -1]

    # Ensure original data has enough rows
    if X_original.shape[0] == 0:
        raise ValueError("Original data has no valid rows left for model training.")
    
    model_original = LinearRegression()
    model_original.fit(X_original, y_original)
    predictions_original = model_original.predict(X_original)

    mse_original = mean_squared_error(y_original, predictions_original)
    print(f"--- Original Model MSE: {mse_original} ---")
    
def main():
    load_and_train_model("encrypted_data.pkl", "private_key.pkl", "diabetes.csv")

if __name__ == "__main__":
    main()
