HERE := $(abspath $(dir $(realpath $(lastword $(MAKEFILE_LIST)))))

.PHONY: test test-assets test-client clean

test: test-assets test-client

test-assets:
	@python -m unittest discover -s test -p 'test_assets.py'

test-client:
	@python -m unittest discover -s test -p 'test_client.py'

clean:
	@find . -type d -name '__pycache__' | xargs -I{} -L 1 rm -rf {}
