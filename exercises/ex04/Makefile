GEN_DATA=python3 gen_data.py
NUM=10
SEED=main.seed
.DEFAULT_GOAL=all

foo.csv: $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f csv

bar.csv: $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f csv

baz.csv: $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f csv
	
foo.json: $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f json
	
bar.json: $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f json
	
baz.json: $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f json

.PHONY: all
all: foo.csv bar.csv baz.csv foo.json bar.json baz.json

.PHONY: clean
clean:
	-rm *.csv
	-rm *.json