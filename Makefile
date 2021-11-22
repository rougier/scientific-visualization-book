#
# The build requires docutils 0.17 since 0.18 breaks the build process.
#
TEX_DIR = tex
PDF_DIR = pdf
RST_DIR = rst
RST_FILES := $(wildcard $(RST_DIR)/*.rst)

DEPS := $(TEX_DIR)/book.tex            \
        $(TEX_DIR)/main.tex            \
        $(TEX_DIR)/00-dedication.tex   \
        $(TEX_DIR)/00-preface.tex      \
        $(TEX_DIR)/00-introduction.tex \
        $(TEX_DIR)/00-acknowledgments.tex \
        $(RST_FILES)

all: directories pdf

.PHONY: help
help:
	@echo  "Targets"
	@echo  "-------"
	@echo  ""
	@echo  "  pdf              - Build PDF (body + cover)"
	@echo  ""
	@echo  "  hardcover        - Build PDF (body + cover) for a hardcover printed book"
	@echo  "  hardcover-cmyk   - Convert hardcover PDF to CMYK colors"
	@echo  "  hardcover-count  - Enumerate color pages in the hardcover PDF (body)"
	@echo  ""
	@echo  "  softcover        - Build PDF (body + cover) for a softcover printed book"
	@echo  "  softcover-cmyk   - Convert softcover PDF to CMYK colors"
	@echo  "  softcover-count  - Enumerate color pages in the softcover PDF (body)"
	@echo  ""


.PHONY: directories
directories:
	mkdir -p pdf

hardcover: hardcover-body hardcover-cover

softcover: softcover-body softcover-cover

hardcover-cmyk: hardcover-body-cmyk hardcover-cover-cmyk

softcover-cmyk: softcover-body-cmyk softcover-cover-cmyk

pdf: $(DEPS) $(TEX_DIR)/front-cover.pdf $(TEX_DIR)/back-cover.pdf
	@latexmk -pdfxe -cd -bibtex -shell-escape -silent -jobname="book" -pretex="" -use-make -usepretex $(TEX_DIR)/book.tex
	@cp $(TEX_DIR)/book.pdf $(PDF_DIR)

pdf-compressed: pdf
	@gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/prepress -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$(PDF_DIR)/book-compressed.pdf $(PDF_DIR)/book.pdf



# Build front cover from the hardcover 
front-cover: softcover-cover
	@latexmk -cd -silent -pdf -use-make $(TEX_DIR)/front-cover.tex 

# Build back cover from the hardcover 
back-cover: softcover-cover
	@latexmk -cd -silent -pdf -use-make $(TEX_DIR)/back-cover.tex 



# Build softcover book (body)
softcover-body: $(DEPS)
	@latexmk -pdfxe -cd -silent -jobname="softcover-body" -pretex="\def\softcover{1}" -use-make -usepretex $(TEX_DIR)/book.tex
	@cp $(TEX_DIR)/softcover-body.pdf $(PDF_DIR)

# Build softcover book (cover)
softcover-cover: $(TEX_DIR)/full-cover.tex
	@latexmk -pdfxe -cd -silent -jobname="softcover-cover" -pretex="\def\softcover{1}" -use-make -usepretex $(TEX_DIR)/full-cover.tex
	@cp $(TEX_DIR)/softcover-cover.pdf $(PDF_DIR)

# Convert softcover book (body) to CMYK
softcover-body-cmyk: $(TEX_DIR)/softcover-body.pdf
	@gs -dSAFER -dNOPAUSE -dBATCH \
        -dAutoRotatePages=/None \
	    -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK \
        -dOverrideICC=true -dRenderIntent=3 -dDeviceGrayToK=true \
	    -sDEVICE=pdfwrite -sOutputFile=$(PDF_DIR)/softcover-body-cmyk.pdf \
	    $(TEX_DIR)/softcover-body.pdf

# Convert softcover book (body) to CMYK
softcover-cover-cmyk: $(TEX_DIR)/softcover-cover.pdf
	@gs -dSAFER -dNOPAUSE -dBATCH  \
	    -dAutoRotatePages=/None \
		-sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK \
        -dOverrideICC=true -dRenderIntent=3 -dDeviceGrayToK=true \
		-sDEVICE=pdfwrite -sOutputFile=$(PDF_DIR)/softcover-cover-cmyk.pdf \
	    $(TEX_DIR)/softcover-cover.pdf

softcover-count: $(TEX_DIR)/softcover-body.pdf
	@gs -o - -sDEVICE=inkcov $(TEX_DIR)/softcover-body.pdf \
        | tail -n +6 \
        | sed '/^Page*/N;s/\n//' \
        | sed -E '/Page [0-9]+ 0.00000  0.00000  0.00000  / d' \
        | cut -f 2 -d ' ' \
        | xargs -I {} echo -n {},; echo



# Build hardcover book (body)
hardcover-body: $(DEPS)
	@latexmk -pdfxe -cd -silent -jobname="hardcover-body" -pretex="\def\hardcover{1}" -use-make -usepretex $(TEX_DIR)/book.tex
	@cp $(TEX_DIR)/hardcover-body.pdf $(PDF_DIR)

# Build hardcover book (cover)
hardcover-cover: $(TEX_DIR)/full-cover.tex
	@latexmk -pdfxe -cd -silent -jobname="hardcover-cover" -pretex="\def\hardcover{1}" -use-make -usepretex $(TEX_DIR)/full-cover.tex
	@cp $(TEX_DIR)/hardcover-cover.pdf $(PDF_DIR)

# Convert hardcover book (body) to CMYK
hardcover-body-cmyk: $(TEX_DIR)/hardcover-body.pdf
	@gs -dSAFER -dNOPAUSE -dBATCH \
	    -dAutoRotatePages=/None \
	    -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK \
	    -sDEVICE=pdfwrite -sOutputFile=$(PDF_DIR)/hardcover-body-cmyk.pdf \
	    $(TEX_DIR)/hardcover-body.pdf

# Convert hardcover book (body) to CMYK
hardcover-cover-cmyk: $(TEX_DIR)/hardcover-cover.pdf
	@gs -dSAFER -dNOPAUSE -dBATCH  \
		-dAutoRotatePages=/None \
	    -sColorConversionStrategy=CMYK -sProcessColorModel=DeviceCMYK \
		-sDEVICE=pdfwrite -sOutputFile=$(PDF_DIR)/hardcover-cover-cmyk.pdf \
	    $(TEX_DIR)/hardcover-cover.pdf

hardcover-count: $(TEX_DIR)/hardcover-body.pdf
	@gs -o - -sDEVICE=inkcov $(TEX_DIR)/hardcover-body.pdf \
        | tail -n +6 \
        | sed '/^Page*/N;s/\n//' \
        | sed -E '/Page [0-9]+ 0.00000  0.00000  0.00000  / d' \
        | cut -f 2 -d ' ' \
        | xargs -I {} echo -n {},; echo



$(TEX_DIR)/00-%.tex: $(RST_DIR)/00-%.rst
	@echo "Building $@"
	@./rst2latex.py --documentclass=book   \
                    --no-doc-title         \
		            --table-style=booktabs \
                    --trim-footnote-reference-space \
				    --use-latex-citations  \
				    --figure-citations     \
                    --reference-label=ref* \
                    --strip-comments       \
                    --template=$(RST_DIR)/chapter.tex \
                    $< > $@

$(TEX_DIR)/%.tex: $(RST_DIR)/%.rst $(RST_FILES)
	@echo "Building $@"
	@./rst2latex.py --documentclass=book   \
                    --use-part-section     \
                    --no-doc-title         \
		            --table-style=booktabs \
				    --use-latex-citations  \
				    --figure-citations     \
                    --reference-label=ref* \
                    --strip-comments       \
                    --template=$(RST_DIR)/chapter.tex \
                    $< > $@

.PHONY: clean
clean:
	@rm -f $(TEX_DIR)/*.aux
	@rm -f $(TEX_DIR)/*.log
	@rm -f $(TEX_DIR)/*.blg
	@rm -f $(TEX_DIR)/*.fls
	@rm -f $(TEX_DIR)/*.run.xml
	@rm -f $(TEX_DIR)/*.bcf
	@rm -f $(TEX_DIR)/*.xdv
	@rm -f $(TEX_DIR)/*.toc
	@rm -f $(TEX_DIR)/*.out
	@rm -f $(TEX_DIR)/*.fdb_latexmk
	@rm -f $(TEX_DIR)/book.pdf
	@rm -f $(TEX_DIR)/hardcover-body.pdf
	@rm -f $(TEX_DIR)/softcover-body.pdf
	@rm -f $(TEX_DIR)/main.tex
	@rm -f $(TEX_DIR)/00-preface.tex
	@rm -f $(TEX_DIR)/00-introduction.tex
	@rm -f $(TEX_DIR)/00-dedication.tex
	@rm -f $(TEX_DIR)/00-acknowledgments.tex
	@echo "Cleanup complete!"
