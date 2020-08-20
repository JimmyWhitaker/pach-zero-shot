SHELL := /bin/bash
PACHCTL := pachctl
KUBECTL := kubectl

zero-shot-base: 
	$(PACHCTL) create repo input_sequences
	$(PACHCTL) create repo candidate_labels
	$(PACHCTL) put file input_sequences@master:reviews.txt -f data/input/test_input.txt
	$(PACHCTL) put file candidate_labels@master:sentiment.txt -f data/labels/test_labels.txt
	$(PACHCTL) create pipeline -f zero_shot_prediction.json