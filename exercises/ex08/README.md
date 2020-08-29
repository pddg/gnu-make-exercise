# Ex.08 Type of Variable

## 問題

以下の要件を満たすように、Makefileに変更を加えよ。

- ファイルの生成後、拡張子を除いたファイル名が同じ物同士の組を、一つのアーカイブにまとめる
  - 例えば `foo.csv` と `foo.json` から `foo.tar.gz` を作る

ただし、アーカイブ名にはビルド時の時間を加え、 例えば `foo_20200830-00:00:00.tar.gz` となるようにすること。
また、同時に生成したアーカイブ名の日時が揃うように注意すること。

## 補足情報

指定フォーマットの日時の生成方法

```
date +%Y%m%d-%H:%M:%S
```

指定したファイルをtarでアーカイブにする

```
tar czf アーカイブ名 ファイル1 ファイル2…
```

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
