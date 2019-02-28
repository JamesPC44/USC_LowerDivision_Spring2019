all: build/solution

build/%: %.c | build
	gcc -o $@ $<

build:
	mkdir $@

.PHONY: clean
clean:
	$(RM) -r build
