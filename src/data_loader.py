import pandas as pd


class CartoonDataLoader:
    def __init__(self, original_csv: str, processed_csv: str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def loading_and_processing(self):
        df = pd.read_csv(self.original_csv, encoding="utf-8", error_bad_lines=False)
        df.dropna(inplace=True)

        required_columns = ["Name", "Genres", "synopsis"]
        df_cols = df.columns()

        for col in df_cols:
            if col not in required_columns:
                exception_ = f"Required column is missing: {col}"
                raise ValueError(exception_)

        df = df.loc[required_columns]
        df["chunks"] = (
            "Title :"
            + df["Name"]
            + " | "
            + "Overview: "
            + df["synopsis"]
            + " | "
            + "Genre: "
            + df["Genre"]
        )

        df["chunks"].to_csv(self.processed_csv, index=False, encoding="utf-8")

        return self.processed_csv
