import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

# ファイルパス
file_path = "out.txt"

# データを読み込む
with open(file_path, "r") as f:
    data = [float(line.strip()) for line in f]

s = pd.Series(data)

# Savitzky-Golayフィルタ
# window_sizeは奇数
window_size_sg = 21
polyorder_sg = 3
savgol = savgol_filter(s, window_size_sg, polyorder_sg)

plt.figure(figsize=(10, 6))
plt.plot(s, label="Original Data", alpha=0.5, color="gray")
plt.plot(
    savgol,
    label=f"Savitzky-Golay (window={window_size_sg}, order={polyorder_sg})",
    color="C2",
)
plt.title("Smoothing with Savitzky-Golay Filter")
plt.xlabel("Time")
plt.ylabel("Value")
plt.ylim(-1.1, 1.1)
plt.legend()
plt.grid(True)
plt.savefig("2smoothing_savgol.png")
print("Savitzky-Golayフィルタグラフを 'smoothing_savgol.png' として保存しました。")
