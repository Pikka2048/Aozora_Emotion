from transformers import pipeline
from typing import List


class IntegratedSentimentAnalyzer:
    """
    テキストの感情分析を行い、-1.0から1.0の統合スコアを返すクラス。
    """

    def __init__(self, model_name="koheiduck/bert-japanese-finetuned-sentiment"):
        """
        クラスの初期化時に、一度だけモデルを読み込む。
        """
        self.analyzer = pipeline("sentiment-analysis", model=model_name)
        print("モデルロード完了")

    def get_score(self, text: str) -> float:
        """
        単一のテキストを分析し、統合感情スコアを返す。

        Args:
            text (str): 分析したいテキスト。

        Returns:
            float: -1.0 (ネガティブ) から 1.0 (ポジティブ) のスコア。NEUTRALなら0となる。
        """
        if not isinstance(text, str) or not text.strip():
            return 0.0

        result = self.analyzer(text)[0]
        score = result["score"]
        label = result["label"]

        if label == "POSITIVE":
            return score
        elif label == "NEGATIVE":
            return -score
        else:  # NEUTRAL
            return 0.0

    def analyze_list(self, text_list: List[str]) -> List[float]:
        """
        テキストのリストをまとめて分析し、スコアのリストを返す。
        """
        return [self.get_score(text) for text in text_list]


# --- 使い方 ---
if __name__ == "__main__":
    analyzer = IntegratedSentimentAnalyzer()

    text1 = "このラーメンは本当に美味しい！感動した。"
    score1 = analyzer.get_score(text1)
    print(f"\nテキスト: '{text1}'")
    print(f"統合感情スコア: {score1:.4f}")
