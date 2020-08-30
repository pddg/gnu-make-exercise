GEN_DATA=python3 gen_data.py
NUM=10
.DEFAULT_GOAL=all

CSVS=test_hoge.csv test_fuga.csv test_piyo.csv test_poe.csv foo.csv bar.csv

$(CSVS):
	$(GEN_DATA) $@ -n $(NUM)

.PHONY: all
all: $(CSVS) 

.PHONY: clean
clean:
	-rm *.csv