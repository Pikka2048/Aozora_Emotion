import os
import re
from argparse import ArgumentParser
from emotion import IntegratedSentimentAnalyzer
from tqdm import tqdm
from datasets import load_dataset

parser = ArgumentParser(
    description="huggingFaceデータセットから作品ごとに感情分析をして、スコアが-1~1で記された改行区切りの中間ファイルに出力する。"
)

parser.add_argument("--n", type=int, help="データ件数の制限（テスト用）")
parser.add_argument("--output", default="dist", help="出力先")
args = parser.parse_args()

analyzer = IntegratedSentimentAnalyzer()
ds = load_dataset("globis-university/aozorabunko-clean", split="train")

output_dir = args.output
os.makedirs(output_dir, exist_ok=True)

for i, book in enumerate(ds):
    if args.n != None and i >= args.n:
        print("テスト件数制限で終了")
        break

    title = book["meta"]["作品名"]
    lines = book["text"].split("\n")
    sentences = [s.replace("\u3000", "") for s in lines]

    scores = []
    for line in tqdm(sentences):
        s = analyzer.get_score(line[:512])
        scores.append(s)

    with open(f"{output_dir}/{title}.txt", "w") as f:
        f.write("\n".join(str(s) for s in scores))
