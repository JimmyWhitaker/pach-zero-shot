# Pach Zero Shot
Scaling Zero Shot learning from Hugging Face to production with Pachyderm. 

Hugging Face came out with [this](https://discuss.huggingface.co/t/new-pipeline-for-zero-shot-text-classification/681), and I wanted to scale it with [Pachyderm](https://pachyderm.io/).

## Running with Docker
```
docker run -v `pwd`/data/:/data/ --entrypoint=python3 jimmywhitaker/zero-shot:v0.1 zs_predict.py --sequences /data/input/test_input.txt --labels /data/labels/test_labels.txt --output /data/output/
```

## Running with Pachyderm
Start a Pachyderm cluster with [Pachyderm Hub](hub.pachyderm.com).

Run: 
```
make zero-shot-base
```


## The code

```
$ python zs_predict.py --help
usage: zs_predict.py [-h] [--sequences DIR] [--labels DIR] [--output DIR]

Zero Shot Predictor

optional arguments:
  -h, --help       show this help message and exit
  --sequences DIR  input video or directory of videos
  --labels DIR     input video or directory of videos
  --output DIR     output directory for extracted frames
```
