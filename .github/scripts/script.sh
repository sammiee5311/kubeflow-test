#!/bin/bash

set -ex

DIR="pipelines/iris"

REGISTRY="sammiee5311"

docker build ${DIR}/1_data_load -t ${REGISTRY}/iris-data-load
docker push ${REGISTRY}/iris-data-load
docker build ${DIR}/2_model_training -t ${REGISTRY}/iris-model-train
docker push ${REGISTRY}/iris-model-train
