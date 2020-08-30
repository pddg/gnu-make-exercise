GEN_DATA=python3 gen_data.py
NUM=10
SEED=main.seed
.DEFAULT_GOAL=all

CSVS=foo.csv bar.csv baz.csv
JSONS=foo.json bar.json baz.json

%.csv:
	$(GEN_DATA) $@ -n $(NUM) -s $< -f csv

%.json:
	$(GEN_DATA) $@ -n $(NUM) -s $< -f json

$(CSVS): $(SEED)
$(JSONS): $(SEED)

.PHONY: all
all: $(CSVS) $(JSONS)

.PHONY: clean
clean:
	-rm *.csv
	-rm *.json