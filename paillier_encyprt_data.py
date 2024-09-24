import pandas as pd
from phe import paillier
import pickle

def encrypt_data(file_path, output_encrypted_file, output_public_key_file, output_private_key_file):
    data = pd.read_csv(file_path).apply(pd.to_numeric, errors='coerce').fillna(0)
    public_key, private_key = paillier.generate_paillier_keypair()

    encrypted_data = data.map(lambda x: public_key.encrypt(x))
    
    # Save encrypted data, public key, and private key
    encrypted_data.to_pickle(output_encrypted_file)
    with open(output_public_key_file, 'wb') as f:
        pickle.dump(public_key, f)
    with open(output_private_key_file, 'wb') as f:
        pickle.dump(private_key, f)
    
    print(f"--- Encryption Done ---")

if __name__ == "__main__":
    encrypt_data("diabetes.csv", "encrypted_data.pkl", "public_key.pkl", "private_key.pkl")