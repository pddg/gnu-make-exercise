# Ex.5 Pattern/Target Specific Variable

## 問題

以下の要件を満たすように、Makefileに変更を加えよ。

- `.csv` および `.json` の拡張子を持つファイル（ `CSVS` および `JSONS` ）を生成するルールを一つにまとめよ
- また、 `large_data` という文字列をファイル名に含む場合、生成するデータ数を 100 （ `-n 100` ）とせよ。

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
