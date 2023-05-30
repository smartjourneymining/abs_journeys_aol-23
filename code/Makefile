
.DEFAULT_GOAL := run

.PHONY: compile
compile: journey.abs		## Compile the model
	absc -e journey.abs

.PHONY: run
run: compile	       ## Compile and run the model
	gen/erl/run | python extract-summary-files.py

.PHONY: serve
serve: compile	       ## Compile and run the model, including web api on port 8080
	gen/erl/run -p 8080

.PHONY: clean
clean:				## Clean build artifacts
	rm -rf gen/ *.csv

# "make print-PATH" prints the value of PATH, etc.
print-%: ; @echo $*=$($*)

.PHONY: help
help:				## Output this help message
	@grep -E '^[a-zA-Z_%-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
