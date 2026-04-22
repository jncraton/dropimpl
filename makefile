all: build

format:
	uvx black@24.1.0 .

lint:
	uvx black@24.1.0 --check .

test:
	uvx pytest@7.4.2 -q

build:
	uvx hatch@1.14.2 build

clean:
	rm -rf build dist *.egg-info
	find . -name "__pycache__" -type d -exec rm -rf {} +

.PHONY: all format lint test build clean
