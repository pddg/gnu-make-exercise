# Write your answers here
GO=go
GO_BUILD_OPT=
GO_LIB_SRCS:=$(shell find lib/ -type f -path "*.go") $(shell find statik/ -type f -path "*.go")
.DEFAULT_GOAL=all

bin/%:
	$(GO) build $(GO_BUILD_OPT) -o $@ ./cmd/$*

HELLO_SRCS:=$(shell find cmd/hello/ -type f -path "*.go")
bin/hello: $(HELLO_SRCS) $(GO_LIB_SRCS) go.mod

ECHO_SRCS:=$(shell find cmd/echo/ -type f -path "*.go")
bin/echo: $(ECHO_SRCS) $(GO_LIB_SRCS) go.mod

SERVER_SRCS:=$(shell find cmd/server/ -type f -path "*.go")
bin/server: $(SERVER_SRCS) $(GO_LIB_SRCS) go.mod

.PHONY: all
all: $(addprefix bin/,hello echo server)

.PHONY: clean
clean:
	-rm -rf bin/*