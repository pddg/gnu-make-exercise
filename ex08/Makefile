GEN_DATA=python3 gen_data.py
NUM=10
SEED=seed.txt
.DEFAULT_GOAL=all

DATE := $(shell date +%Y%m%d-%H%M%S)

TARGETS := foo bar baz large_data
CSVS := $(addsuffix .csv,$(TARGETS))
JSONS := $(addsuffix .json,$(TARGETS))
ARCHIVES := $(addsuffix _$(DATE).tar.gz,$(TARGETS))

$(CSVS): FORMAT=csv
$(JSONS): FORMAT=json

$(CSVS) $(JSONS): $(SEED)
	$(GEN_DATA) $@ -n $(NUM) -s $< -f $(FORMAT)

%_$(DATE).tar.gz: %.csv %.json
	tar czf $@ $^

.PHONY: all
all: $(ARCHIVES)

.PHONY: clean
clean:
	-rm $(CSVS) $(JSONS) *.tar.gz