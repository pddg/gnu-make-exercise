# Ex.09 Portability

## 問題

Ex.08のMakefileを、Linuxのコマンドを使って記述した。
このMakefileがWindows、macOS、Linuxで動作するように再設計せよ。
ただし、動作自体を検証する必要は無い。

## 補足情報

各コマンドは以下のようにしてビルド出来る。

```
go build -o bin/コマンド名 ./cmd/コマンド名
```

Windowsにおいて、 `rm` コマンドは `del` に相当する
