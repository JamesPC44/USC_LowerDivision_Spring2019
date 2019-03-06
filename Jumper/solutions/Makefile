all: build/solution build/solution.class

build/%: %.c | build
	gcc -o $@ $<

build/%.class: %.java | build
	javac -d build $<

build:
	mkdir $@

.PHONY: clean
clean:
	$(RM) -r build
