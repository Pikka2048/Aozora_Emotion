# 青空文庫の小説の物語の時系列に沿った感情をグラフにする

<img width="1000" height="600" alt="寡婦とその子" src="https://github.com/user-attachments/assets/9310c1ee-5fb5-47fb-bc03-547c8738900f" />
<img width="1000" height="600" alt="ジョン・ブル" src="https://github.com/user-attachments/assets/6674659c-85d9-47da-9a34-0565b7045c61" />
<img width="1000" height="600" alt="ウェストミンスター寺院" src="https://github.com/user-attachments/assets/87c688db-2cc4-4e2f-adf9-545a2c1fd432" />

Huggingfaceのデータセット`globis-university/aozorabunko-clean`を活用して、コードを簡潔にしている。

各行を改行区切りで抜き出して、`koheiduck/bert-japanese-finetuned-sentimen`モデルで感情を["POSITIVE", "NEGATIVE", "NEUTRAL"]のいずれかに推論、統合スコアを求め行ごとにスコアを記録する。そのあとにMatplotlibにて描画。

物語の感情の推移をグラフとして見られる。概ね王道とされているような展開のグラフが得られる。（起承転結）

