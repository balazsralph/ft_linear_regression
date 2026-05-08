.PHONY: train predict clean

train:
	python train.py

predict:
	python predictPrice.py

clean:
	rm -f theta.csv
