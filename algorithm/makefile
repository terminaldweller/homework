
PDF_LIST:=$(patsubst %.tex, %.pdf, $(shell find . -name '*.tex'))
.DEFAULT: all

all: $(PDF_LIST)

%.pdf:%.tex
	rm $@
	pdflatex --output-dirrectory=./ $<
