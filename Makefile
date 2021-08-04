.PHONY: \
	check \
	clean \
	coverage \
	mutants \
	tests \
	tests_api \
	tests_shell

check:
	shellcheck --shell=bash src/*

clean:
	rm --force --recursive coverage
	rm --force obtained.json

coverage:
	shellspec --kcov --kcov-options "--include-path=src" --shell bash tests

mutants:
	@echo "🏹😞 No mutation testing on Bash 👾🎉👾"

start:
	@echo "▶️ Starting API:"
	uvicorn app.main:app --host 0.0.0.0 --port 80

tests: tests_api tests_shell

tests_api:
	tests/test_swapi.sh

tests_shell:
	shellspec --shell bash tests
