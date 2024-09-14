.DELETE_ON_ERROR:

AS = armips
PYTHON = python3

ASM = hack.asm
ROM = cotm.gba
HACK = hack.gba
SCRIPT = change_text.py

$(HACK): $(ASM) $(SCRIPT)
	$(PYTHON) $(SCRIPT)
	$(AS) $<

.PHONY: all clean test
clean:
	rm -rf $(HACK)
