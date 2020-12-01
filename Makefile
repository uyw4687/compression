PYTHON = python3
DATADIR = ./data/
NAMES = dnaas englishas sd1 sd2 sd3 sd4 xmlas
DATA = $(foreach name,$(NAMES),$(DATADIR)$(name))

.PHONY: huffman adaptive-huffman tunstall arithmetic lzss lzw golomb
all: huffman adaptive-huffman tunstall arithmetic lzss lzw golomb

huffman:
	$(foreach input,$(DATA),$(PYTHON) huffman/Huffman.py -c $(input);)
	$(foreach input,$(DATA),$(PYTHON) huffman/Huffman.py -d $(input).huffman;)

adaptive-huffman:
	$(foreach input,$(DATA),$(PYTHON) adaptive-huffman/fgk.py -e $(input);)
	$(foreach input,$(DATA),$(PYTHON) adaptive-huffman/fgk.py -d $(input).adaptivehuffman;)

tunstall:
	$(foreach input,$(DATA),$(PYTHON) tunstall/Tunstall_code/tun_enc_doc.py 10 $(input);)

arithmetic:
	$(foreach input,$(DATA),$(PYTHON) arithmetic/python/arithmetic-compress.py $(input);)
	$(foreach input,$(DATA),$(PYTHON) arithmetic/python/arithmetic-decompress.py $(input).arithmetic;)

lzss:
	pip3 install bitarray
	$(foreach input,$(DATA),$(PYTHON) LZ77/mainlz77.py -c $(input);)
	$(foreach input,$(DATA),$(PYTHON) LZ77/mainlz77.py -d $(input);)

lzw:
	$(foreach input,$(DATA),$(PYTHON) LZW/mainlzw.py -c $(input);)
	$(foreach input,$(DATA),$(PYTHON) LZW/mainlzw.py -d $(input);)

golomb:
	pip3 install golomb-coding
	$(foreach input,$(DATA),$(PYTHON) Golomb/maingolomb.py -c $(input);)
	$(foreach input,$(DATA),$(PYTHON) Golomb/maingolomb.py -d $(input);)
