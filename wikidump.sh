#!/bin/sh

set -e

download_data() {
  # Download data
  mkdir full_data
  cd full_data
  wget https://dumps.wikimedia.org/simplewiki/20231020/simplewiki-20231020-pages-articles.xml.bz2
  bzip -d simplewiki-20231020-pages-articles.xml.bz2
  ln -s simplewiki-20231020-pages-articles.xml simplewiki.xml
  cd ..
}

process_data() {
  # Process data
  rm -rf full_data/articles
  mkdir -p full_data/articles
  ./wikidump.py
}

sample_data() {
  # Sample data
  rm -rf data
  mkdir data
  ls -1 full_data/articles | shuf | head -n 10 | xargs -I {} ln -s $PWD/full_data/articles/{} data/
}

download_data
process_data
sample_data
