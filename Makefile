# Makefile for LeetCode problem management

.PHONY: new help

# Create a new problem template
# Usage: make new NUM=128
#        make new NUM=128 TITLE="Two Sum" DIFF=Easy CAT=Array
new:
	@python3 utils/create_problem.py $(NUM) $(TITLE) $(DIFF) $(CAT)

help:
	@echo "Usage:"
	@echo "  make new NUM=128                                    # Auto-fetch from LeetCode"
  @echo "  make new NUM=128 DIFF=Medium CAT=Array             # With difficulty and category"
  @echo "  make new NUM=1 TITLE=\"Two Sum\" DIFF=Easy CAT=Array  # Full manual"
	@echo ""
	@echo "Or use the wrapper script:"
	@echo "  ./new 128"
  @echo "  ./new 128 \"Two Sum\" Easy Array"

