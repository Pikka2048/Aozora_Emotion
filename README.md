# 青空文庫の小説をテキスト分析し、物語の進行に沿った感情の推移をグラフで可視化。

Hugging FaceのデータセットとBERTモデルを利用し、文章を一行ずつ分析。物語の感情的な浮き沈みや「起承転結」のような構成を視覚的に捉えることができます。

Hugging Faceのデータセット globis-university/aozorabunko-clean を利用し、青空文庫の小説における物語の進行に沿った感情の推移をグラフで可視化します。

文章を一行ずつ koheiduck/bert-japanese-finetuned-sentimen モデルで分析し、["POSITIVE", "NEGATIVE", "NEUTRAL"] のいずれかの感情ラベルを付与。各行の感情スコアから全体の推移を算出し、Matplotlibでグラフを描画します。

これにより、物語の感情的な流れ、いわゆる「起承転結」のような構造を視覚的に捉えることができます。

## 実行方法

./Run.sh を実行してください。

詳細はスクリプト内を確認すること。

## 注意点

GPUの利用を推奨。

NVIDIA RTX 2080Tiを使用した場合でも、完了まで1時間以上かかります。


<img width="400" height="400" alt="寡婦とその子" src="https://github.com/user-attachments/assets/9310c1ee-5fb5-47fb-bc03-547c8738900f" />
<img width="400" height="400" alt="ジョン・ブル" src="https://github.com/user-attachments/assets/6674659c-85d9-47da-9a34-0565b7045c61" />
<img width="400" height="400" alt="ウェストミンスター寺院" src="https://github.com/user-attachments/assets/87c688db-2cc4-4e2f-adf9-545a2c1fd432" />
