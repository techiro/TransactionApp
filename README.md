TransactionApp
==============

Overview
==============
ATMシステムをCILで操作することができるアプリケーションになっている。一元管理のデータベースを用いて取引を請求したり自分の口座に振り込まれる金額の確認，取引の一覧表示を行うことができる。
また，口座にお金を入金したりできる。，基本的なATMの機能をDBMSとPythonを用いて開発を行った。

Installation
==============

- Pythonのインストール(Pythonの2.x.xと3.x.xがあるがPython3.x.xをインストール)

- 外部モジュールインストール(Linux系にはインストールされていると思われるがエラーが出たらpipを用いてインストール)
	$pip install sqlite3
	$pip install datetime
	$pip install sys

Getting Started
==============

# TransactionAppの起動方法

```
$python3 controller.py
```

アカウント名がないとログインできないため例を示す。

アカウント名の入力
tanaka

パスワードの入力
0000

認証が完了すると，Appが起動する。
取引マネージャーと口座マネージャー，終了が選べる。

	==========================
	取引マネージャーを起動する         1
	口座マネージャーを起動する         2
	終了する。                         f
	あなたがしたいことを1,2,fで選んでください
	==========================


# 取引マネージャーについて

	==========================
	取引を確認         1
	利益を確認         2
	取引を追加         3
	MENUに戻る         b
	あなたがしたいことを1,2,3,bで選んでください
	==========================

入力が1だった場合:
自分のアカウントに関係する取引一覧を表示させる．そこで取引金額がどのくらいかや締め切りがいつまでなのかなどを知ることができる．

入力が2だった場合：
自分のアカウントに入金されるであろう金額が表示される．ここでどのくらい利益があるかを確認することができる．

入力が3だった場合：
他の人にお金を請求することができる．お金を請求するためにまず誰に請求するか締め切り日金額を入力することで自動的に帳簿を作成してそれをデータベースに追加してくれる．


# 口座マネージャーについて

	==========================
	口座を確認         1
	口座に入金         2
	MENUに戻る         b
	あなたがしたいことを1,2,bで選んでください
	==========================


入力が1だった場合:
自分のアカウントに関係する銀行の口座一覧を表示させる。そこで現在の口座の残高を表示させることで，どの程度銀行にお金が存在しているのかを知ることができる。

入力が2だった場合：
自分のアカウントに入金を行うことができる．上の入力1を用いて残高が少なくなってきたことを確認した後に指定の口座にお金を入金することができる．もし，入力が間違っていたら確認のアラートが表示されるのでそこで中断することもできる．
	

	
