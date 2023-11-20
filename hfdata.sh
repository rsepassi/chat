#!/bin/sh

set -e

download_data(){
    # download the parquet data from hugging face
    mkdir hf_data 
    cd hf_data 
    wget https://huggingface.co/datasets/hugfaceguy0001/stanford_plato/resolve/main/data/train-00000-of-00001-65b5548e09cbc609.parquet
    mv train-00000-of-00001-65b5548e09cbc609.parquet hf_sep.parquet
    cd ..
}

process_data(){
    # process the data
    rm -rf hf_data/articles
    mkdir -p hf_data/articles 
    python3 hfdata.py
}

download_data
process_data