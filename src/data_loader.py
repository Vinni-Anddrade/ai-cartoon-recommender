import pandas as pd


class CartoonDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def loading_and_processing(self):
        df = pd.read_csv(self.original_csv, encoding="utf-8", on_bad_lines="skip")
        df.dropna(inplace=True)

        required_columns = ["Name", "Genres", "sypnopsis"]
        df_cols = df.columns

        for col in required_columns:
            if col not in df_cols:
                exception_ = f"Required column is missing: {col}"
                raise ValueError(exception_)

        df = df.loc[:, required_columns]
        df["chunks"] = (
            "Title :"
            + df["Name"]
            + " | "
            + "Overview: "
            + df["sypnopsis"]
            + " | "
            + "Genres: "
            + df["Genres"]
        )

        df["chunks"].to_csv(self.processed_csv, index=False, encoding="utf-8")

        return self.processed_csv
