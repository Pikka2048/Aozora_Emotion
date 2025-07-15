import japanize_matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter
import glob
import os

output_dir = "result"
os.makedirs(output_dir, exist_ok=True)

input_files = glob.glob("dist/*.txt")

if not input_files:
    print("処理対象のファイルがoutディレクトリに見つかりません。")

for file_path in input_files:
    try:
        with open(file_path, "r") as f:
            data = [float(line.strip()) for line in f]

        # Pandas Seriesに変換
        s = pd.Series(data)

        # Savitzky-Golayフィルタで平滑化
        # window_sizeは奇数である必要がある。
        window_size_sg = 21
        polyorder_sg = 3
        savgol = savgol_filter(s, window_size_sg, polyorder_sg)

        # グラフのプロット
        plt.figure(figsize=(10, 6))
        plt.plot(s, label="Original Data", alpha=0.5, color="gray")
        plt.plot(
            savgol,
            label=f"Savitzky-Golay (window={window_size_sg}, order={polyorder_sg})",
            color="C2",
        )
        plt.title(f"Smoothing for {os.path.basename(file_path)}")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.ylim(-1.1, 1.1)
        plt.legend()
        plt.grid(True)

        base_name = os.path.splitext(os.path.basename(file_path))[0]
        output_path = os.path.join(output_dir, f"{base_name}.png")

        plt.savefig(output_path)
        print(f"グラフを '{output_path}' として保存しました。")

        # メモリ解放
        plt.close()

    except Exception as e:
        print(f"ファイル '{file_path}' の処理中にエラーが発生しました: {e}")
