import os
import argparse
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    default_model_dir = os.environ.get("SM_MODEL_DIR", "./model")
    default_train_dir = os.environ.get("SM_CHANNEL_TRAIN", "./data")
    
    parser.add_argument("--n-estimators", type=int, default=100)
    parser.add_argument("--model-dir", type=str, default=default_model_dir)
    parser.add_argument("--train", type=str, default=default_train_dir)
    
    args, _ = parser.parse_known_args()
    
    os.makedirs(args.model_dir, exist_ok=True)
    
    print("Loading training data...")
    train_file = os.path.join(args.train, "train.csv")
    
    if os.path.exists(train_file):
        df = pd.read_csv(train_file)
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
    else:
        print("Training file not found locally, using dummy data structure for pipeline structure verification.")
        import numpy as np
        X = np.random.rand(100, 5)
        y = np.randint(0, 2, size=100)

    print(f"Training model with {len(X)} samples...")
    model = RandomForestClassifier(n_estimators=args.n_estimators, random_state=42)
    model.fit(X, y)
    
    model_path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(model, model_path)
    print(f"Model saved successfully at {model_path}")
