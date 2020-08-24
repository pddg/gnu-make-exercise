# Ex.3 Variable

## 問題

以下の要件を満たすように、Makefileに変更を加えよ。

- CSVファイルを生成するプログラムが変更になった際に、変更箇所が1箇所で済む
- 生成するデータ量（ `-n 10` ）が変更になったとき（例えば `-n 100` ）に変更箇所が1箇所で済む

ただし、CSVファイルはgen_data.pyを用いて生成するものとし、gen_data.py自体を変更することは不可とする。

## 補足情報

```bash
$ python3 gen_data.py -h
usage: gen_data.py [-h] [-n NUMBER] filename

Test data generator

positional arguments:
  filename              Path to output file name

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Number of data record to generate
```
