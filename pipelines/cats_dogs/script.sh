#!/bin/bash

set -ex

DIR="pipelines/cats_dogs"

REGISTRY="sammiee5311"

docker build ${DIR}/1_download_dataset -t ${REGISTRY}/download-dataset
docker push ${REGISTRY}/download-dataset
docker build ${DIR}/2_categorize_dataset -t ${REGISTRY}/categorize-dataset
docker push ${REGISTRY}/categorize-dataset
