import polars as pl
import numpy as np

def main():

    # サンプルデータの作成
    df = pl.DataFrame({
        "x": np.linspace(0, 2 * np.pi),
        "y": np.sin(np.linspace(0, 2 * np.pi)),
        "z": np.cos(np.linspace(0, 2 * np.pi))
    })

    # プロット
    df.plot(x="x", y=["y", "z"])


if __name__ == "__main__":
    main()