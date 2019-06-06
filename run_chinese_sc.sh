#!/usr/bin/env bash

export CUDA_VISIBLE_DEVICES=0

# ./BERT_BASE_DIR/文件夹下有bert.model.*, vocab.txt, bert_config.json，若没有，执行以下：
bert_model_path=./BERT_BASE_DIR
if [ ! -d ${bert_model_path} ]; then
    mkdir ${bert_model_path}
    wget https://storage.googleapis.com/bert_models/2018_11_03/chinese_L-12_H-768_A-12.zip
    mv chinese_L-12_H-768_A-12.zip ${bert_model_path}
    unzip ${bert_model_path}/chinese_L-12_H-768_A-12.zip -d ${bert_model_path}
fi

#数据，包含train.tsv, dev.tsv, test.tsv
data_path=./data/chinese_sc/

bert_model_path=${bert_model_path}/chinese_L-12_H-768_A-12

python run_classifier.py \
  --task_name=chinese_sc \
  --do_train=true \
  --do_eval=true \
  --data_dir=${data_path} \
  --vocab_file=${bert_model_path}/vocab.txt \
  --bert_config_file=${bert_model_path}/bert_config.json \
  --init_checkpoint=${bert_model_path}/bert_model.ckpt \
  --max_seq_length=128 \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --output_dir=./tmp/chinese_sc_output/
