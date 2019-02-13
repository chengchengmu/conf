TEST_DIR=tests
RUNTEST=python -m unittest discover -v $(TEST_DIR) "*.py"
TESTS:=$(shell find $(TEST_DIR) -name '*.py')

.PHONY: all
all: test

test: conf.py $(TESTS)
	${RUNTEST}
	@touch test

clean:
	rm -f test *.pyc
