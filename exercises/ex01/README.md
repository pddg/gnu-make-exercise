# Ex.1 Hello world!

## 問題

以下の要件を満たすMakefileを書け

1. main.cをコンパイルし、`hello` というバイナリを作成する
2. main.cに変更があれば `hello` を再ビルドし、変更が無ければ何もしない
3. `make hello` で `hello` が作成できる

## 補足情報

- コンパイラは `gcc` を使用する
- `-o` オプションで出力するバイナリ名を指定できる
