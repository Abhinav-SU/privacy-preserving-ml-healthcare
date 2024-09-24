# Privacy-Preserving Machine Learning Healthcare Project

This project explores privacy-preserving machine learning techniques using homomorphic encryption, specifically the Paillier cryptosystem. The goal is to enable secure data processing, where machine learning models can be trained and predictions can be made on encrypted data, ensuring the confidentiality of sensitive healthcare records.

## Project Overview

We have implemented encrypted data processing using the Paillier cryptosystem to preserve data privacy while allowing machine learning tasks. The project uses a diabetes dataset, which is encrypted, processed, and decrypted for model training.

### Key Features:
- **Data Encryption**: Secure encryption of healthcare data using Paillier cryptosystem.
- **Model Training on Encrypted Data**: Ability to train a machine learning model on encrypted data without decrypting it during processing.
- **Decryption and Model Evaluation**: Decrypted data is used for model evaluation and comparison to ensure consistency with unencrypted processing.

## Project Structure

- `paillier_encrypt_data.py`: Script to encrypt the dataset using the Paillier encryption scheme.
- `paillier_train_model.py`: Script to decrypt the encrypted data, train the model, and compare performance with unencrypted data.
- `diabetes.csv`: Sample dataset used for training the machine learning model.
- `requirements.txt`: Python dependencies needed to run the project.
- `LICENSE`: MIT License for this project.

## Getting Started

### Prerequisites

Ensure you have Python installed along with the following libraries:

- `pandas`
- `scikit-learn`
- `phe` (Paillier Homomorphic Encryption library)

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Running the Project

1. **Encrypt the Data**:
   Run the `paillier_encrypt_data.py` script to generate the encrypted dataset and save it as a .pkl file along with the public and private keys.

   ```bash
   python3 paillier_encrypt_data.py
   ```

2. **Train on Encrypted Data**:
   Use the `paillier_train_model.py` script to decrypt the data and train the model. This script compares the performance of the model trained on decrypted data against the model trained on unencrypted data.

   ```bash
   python3 paillier_train_model.py
   ```

3. **Evaluation**:
   The Mean Squared Error (MSE) for both the encrypted and unencrypted models will be displayed to ensure data integrity and correctness during encryption and decryption.

   Example Output:
   ```
   --- Decrypted Model MSE: 4690.493274594553 ---
   --- Original Model MSE: 4690.493274594553 ---
   ```
   This output shows that the encrypted and unencrypted models yield the same performance, ensuring that the encryption process did not alter the data.

## License

This project is licensed under the MIT License - see the LICENSE file for details.