import polars as pl
import plotly.express as px

def main():
    # サンプルデータの作成
    data = {
        "時間": ["2024-07-01", "2024-07-02", "2024-07-03", "2024-07-04", "2024-07-05"],
        "理解度": [50, 60, 70, 65, 80]
    }

    # polarsのDataFrameを作成
    df = pl.DataFrame(data)

    # '時間'列をdatetime型に変換
    df = df.with_columns(pl.col("時間").str.strptime(pl.Datetime, "%Y-%m-%d"))

    # plotlyを使用して折れ線グラフを作成
    fig = px.line(df.to_pandas(), x="時間", y="理解度", markers=True)

    # グラフのレイアウトを調整
    fig.update_layout(
        title="時間と理解度の関係",
        xaxis_title="時間",
        yaxis_title="理解度"
    )

    # グラフを表示
    fig.show()

    # グラフを画像として保存
    fig.write_image("理解度グラフ.png")


if __name__ == "__main__":
    main()