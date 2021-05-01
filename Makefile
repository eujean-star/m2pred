setup:
	conda env create --file environment.yml || conda env update --file environment.yml

analysis:
	cd notebooks && jupyter nbconvert --to html EDA.ipynb

