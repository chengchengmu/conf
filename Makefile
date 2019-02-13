TEST_DIR=tests
RUNTEST=python -m unittest discover -v $(TEST_DIR) "*.py"
TESTS:=$(shell find $(TEST_DIR) -name '*.py')

.PHONY: all
all: test

test: conf.py $(TESTS)
	${RUNTEST}
	@touch test

.PHONY: freeze
freeze:
	pyinstaller conf.py

.PHONY: clean
clean:
	rm -f test *.pyc # conf.spec dist build

.PHONY: clean_freeze
clean_freeze:
	rm -rf conf.spec dist build
