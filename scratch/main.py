# 最小限の動作コード

import re
from tqdm import tqdm
from emotion import IntegratedSentimentAnalyzer

analyzer = IntegratedSentimentAnalyzer()


def main():

    with open("data/merosu.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # クリーンアップ
    sentences = [s.replace("\u3000", "") for s in lines]

    # lines = lines[:5]
    print(len(lines))

    # 。ごとに区切る場合
    # sentences = [s for line in sentences for s in re.split("。", line) if s.strip()]

    scores = []
    for line in sentences:
        s = analyzer.get_score(line[:512])
        print(f"{s} : {line[:512]}")
        scores.append(s)

    with open("out.txt", "w") as f2:
        f2.write("\n".join(str(s) for s in scores))


main()
