GEN_DATA=python3 gen_data.py
NUM=10
SEED=seed.txt
.DEFAULT_GOAL=all

ifdef CI
	NUM=1
endif

CSVS=foo.csv bar.csv baz.csv large_data.csv
JSONS=foo.json bar.json baz.json large_data.json

$(CSVS): FORMAT=csv
$(JSONS): FORMAT=json

GEN_CMD=$(GEN_DATA) $@ -n $(NUM) -s $< -f $(FORMAT)
$(CSVS) $(JSONS): $(SEED)
ifneq "$(SEED)" "seed.txt"
	@echo "Warn: SEED is not seed.txt" 1>&2
endif
ifeq "$(DRYRUN)" "true"
	@echo $(GEN_CMD) 
else
	$(GEN_CMD)
endif
	

.PHONY: all
all: $(CSVS) $(JSONS)

.PHONY: clean
clean:
	-rm $(CSVS) $(JSONS)