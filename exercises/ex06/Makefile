GEN_DATA=python3 gen_data.py
NUM=10
SEED=seed.txt
.DEFAULT_GOAL=all

CSVS=foo.csv bar.csv baz.csv large_data.csv
JSONS=foo.json bar.json baz.json large_data.json


$(CSVS): FORMAT=csv
$(JSONS): FORMAT=json

$(CSVS) $(JSONS): $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f $(FORMAT)

.PHONY: all
all: $(CSVS) $(JSONS)

.PHONY: clean
clean:
	-rm $(CSVS) $(JSONS)