test_hoge.csv:
	python3 gen_data.py test_hoge.csv -n 10

test_fuga.csv:
	python3 gen_data.py test_fuga.csv -n 10

test_piyo.csv:
	python3 gen_data.py test_piyo.csv -n 10

test_poe.csv:
	python3 gen_data.py test_poe.csv -n 10

foo.csv:
	python3 gen_data.py foo.csv -n 10

bar.csv:
	python3 gen_data.py bar.csv -n 10

baz.csv:
	python3 gen_data.py baz.csv -n 10

.PHONY: all
all: test_hoge.csv test_fuga.csv test_piyo.csv test_poe.csv foo.csv bar.csv foo.csv

.PHONY: clean
clean:
	rm *.csv