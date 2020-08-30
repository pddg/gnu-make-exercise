GO=go
GO_LIB_SRCS=$(wildcard lib/*/*.go) $(wildcard statik/*.go)
CMD_DIR=./cmd
BIN_DIR=./bin
.DEFAULT_GOAL=all

$(BIN_DIR)/%:
	$(GO) build -o $@ $(CMD_DIR)/$*

$(BIN_DIR)/hello: $(wildcard $(CMD_DIR)/hello/*.go) $(GO_LIB_SRCS) go.mod
$(BIN_DIR)/echo: $(wildcard $(CMD_DIR)/echo/*.go) $(GO_LIB_SRCS) go.mod
$(BIN_DIR)/server: $(wildcard $(CMD_DIR)/server/*.go) $(GO_LIB_SRCS) go.mod

.PHONY: all
all: $(addprefix $(BIN_DIR)/,hello echo server)

.PHONY: clean
clean:
	-rm -rf $(BIN_DIR)/*
