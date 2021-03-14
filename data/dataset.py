from typing import Tuple
from pathlib import Path
import pandas as pd


def load_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Utility function to load data and download it if data is not available locally"""

    if Path(path + "train.csv").is_file():
        print('Loading locally')
        df_train = pd.read_csv(path + "train.csv")
        df_test = pd.read_csv(path + "test.csv")
    else:
        print('Loading from web')
        df_train = pd.read_csv(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/00421/aps_failure_training_set.csv",
            na_values="na", skiprows=20)  # Skipping first 20 rows since it contains dataset description
        df_test = pd.read_csv(
            "https://archive.ics.uci.edu/ml/machine-learning-databases/00421/aps_failure_test_set.csv",
            na_values="na", skiprows=20)  # Skipping first 20 rows since it contains dataset description
        df_train.to_csv(path + "train.csv", index=False)
        df_test.to_csv(path + "test.csv", index=False)

    return df_train, df_test


if __name__ == '__main__':
    path = ''
else:
    path = '../data/'
