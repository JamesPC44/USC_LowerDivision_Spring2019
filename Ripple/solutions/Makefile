ROOT=$(dir $(lastword $(MAKEFILE_LIST)))
BUILD=build

.PHONY: all clean
all: $(BUILD)/runjava

$(BUILD)/runjava: $(BUILD)/solution.class
	echo '#! /bin/sh\njava -cp "$(abspath $(BUILD))" $(patsubst $(BUILD)/%.class,%,$<)' > $@
	chmod +x $@

$(BUILD)/%.class: $(ROOT)/%.java | $(BUILD)
	javac -d $(BUILD) $<

$(BUILD):
	mkdir -p $@

clean:
	$(RM) -r $(BUILD)
