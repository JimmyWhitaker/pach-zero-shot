FROM huggingface/transformers-pytorch-cpu

WORKDIR /workspace/
RUN rm -rf transformers\
    && git clone https://github.com/huggingface/transformers \
    && cd transformers \
    && pip install .

# Download the model into the container
RUN (echo "from transformers import pipeline" ; echo "pipeline(\"zero-shot-classification\")") | python3

COPY zs_predict.py ./