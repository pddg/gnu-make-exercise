GEN_DATA=python3 gen_data.py
NUM=10
SEED=seed.txt
.DEFAULT_GOAL=all

TARGETS := foo bar baz large_data
CSVS := $(addsuffix .csv,$(TARGETS))
JSONS := $(addsuffix .json,$(TARGETS))


$(CSVS): FORMAT=csv
$(JSONS): FORMAT=json

$(CSVS) $(JSONS): $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f $(FORMAT)

.PHONY: all
all: $(CSVS) $(JSONS)

.PHONY: clean
clean:
	-rm $(CSVS) $(JSONS)