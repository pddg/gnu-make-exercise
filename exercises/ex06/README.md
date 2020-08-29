# Ex.5 Pattern/Target Specific Variable

## 問題

以下の要件を満たすように、Makefileに変更を加えよ。

- `DRYRUN` という変数が `true` であるとき、実際にターゲットを生成せず、代わりに実行コマンドを表示する
- `seed.txt` 以外が指定されたとき、警告を表示する
- `CI` という環境変数が設定されていたとき、`NUM=1` にする

ただし、CSVおよびJSONファイルはgen_data.pyを用いて生成するものとし、gen_data.py自体を変更することは不可とする。

## 補足情報

```bash
$ python3 gen_data.py -h
usage: gen_data.py [-h] [-s SEED] [-f {json,csv}] [-n NUMBER] filename

Test data generator

positional arguments:
  filename              Path to output file name

optional arguments:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  Path to seed file
  -f {json,csv}, --format {json,csv}
                        Format of output
  -n NUMBER, --number NUMBER
                        Number of data record to generate
```
