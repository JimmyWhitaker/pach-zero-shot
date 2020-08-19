import argparse
import os
from transformers import pipeline
import json


parser = argparse.ArgumentParser(description="Zero Shot Predictor")
parser.add_argument("--sequences",
                    metavar="DIR",
                    help="input video or directory of videos",
                    default="./input")
parser.add_argument("--labels",
                    metavar="DIR",
                    help="input video or directory of videos",
                    default="./labels")
parser.add_argument("--output",
                    metavar="DIR",
                    default="./output",
                    help="output directory for extracted frames")

def get_single_file_from_path(input_path):
    """
    Return the file or first file in a directory 
    (useful for Pachyderm datums)
    """
    paths = []
    if os.path.isfile(input_path):  # path is a file
        paths.append(input_path)
    elif os.path.isdir(input_path):  # path is a directory
        for f in os.listdir(input_path):
            paths.append(os.path.join(input_path, f))
    return paths[0]

def get_file_basename(file_path):
    """
    Get the basename of a path without the extension
    """
    return os.path.splitext(os.path.split(file_path)[1])[0]

def txt_file_to_list(file_path):
    """
    Read a text file into a list delimited by line
    """
    with open(file_path) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def main():
    args = parser.parse_args()

    sequences_path = get_single_file_from_path(args.sequences)
    labels_path = get_single_file_from_path(args.labels)
    
    print("Loading model...")
    classifier = pipeline("zero-shot-classification")

    print("Loading sequences and labels...")
    sequences = txt_file_to_list(sequences_path)
    candidate_labels = txt_file_to_list(labels_path)

    print("Classifying...")
    result = classifier(sequences, candidate_labels)

    print(str(result))
    sequences_basename = get_file_basename(sequences_path)
    labels_basename = get_file_basename(labels_path)


    
    output_file = os.path.join(args.output, sequences_basename + 
            '_' + labels_basename + '.json')
    print("Saving output to: ", output_file)
    with open(output_file, 'w') as fp:
        json.dump(result, fp)

if __name__ == "__main__":
    main()