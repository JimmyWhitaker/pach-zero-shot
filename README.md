# Zero Shot Pach
Scaling Zero Shot learning from Hugging Face to production with Pachyderm. 

Hugging Face came out with [this](https://discuss.huggingface.co/t/new-pipeline-for-zero-shot-text-classification/681), and I wanted to scale it with [Pachyderm](https://pachyderm.io/).

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