import os
import random
import argparse
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import mlflow
import mlflow.sklearn

def set_seed(seed):
    # Seed all libraries for full reproducibility
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)

def load_data():
    # Load Elliptic dataset features and labels
    df_features = pd.read_csv("data/elliptic_bitcoin_dataset/elliptic_txs_features.csv", header=None)
    df_classes  = pd.read_csv("data/elliptic_bitcoin_dataset/elliptic_txs_classes.csv")

    # Rename first column as transaction id
    df_features.rename(columns={0: "txId"}, inplace=True)

    # Merge features with labels
    df = df_features.merge(df_classes, on="txId")

    # Keep only labeled rows: class is "1" (illicit) or "2" (licit)
    df = df[df["class"].isin(["1", "2"])].copy()

    # illicit=1, licit=0
    df["label"] = (df["class"] == "1").astype(int)

    print(f"Label distribution: {df['label'].value_counts().to_dict()}")

    X = df.drop(columns=["txId", "class", "label"]).values
    y = df["label"].values
    return X, y

def main(seed=42):
    set_seed(seed)
    X, y = load_data()
    print(f"Dataset shape: {X.shape}")

    # Split BEFORE any preprocessing — no data leakage
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=y)

    # Fit scaler on TRAIN only, then transform both
    scaler = StandardScaler().fit(X_train)
    X_train = scaler.transform(X_train)
    X_test  = scaler.transform(X_test)

    # Train model
    clf = LogisticRegression(max_iter=1000, random_state=seed)
    clf.fit(X_train, y_train)

    # Evaluate
    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"seed={seed}  accuracy={acc:.4f}")
    print(classification_report(y_test, clf.predict(X_test),
                                 target_names=["licit", "illicit"]))
    return clf, scaler, acc

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=42)
    main(ap.parse_args().seed)
