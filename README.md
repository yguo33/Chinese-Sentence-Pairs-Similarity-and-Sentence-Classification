### chinese question pairs
1. 数据保存在文件夹./data/chinese_qp下，包含train.tsv, dev.tsv, test.tsv，每个文件的格式为：q1 \t q2 \t label (中间无空格)
    若只有一个文件，可用以下命令生成python ./data/split_qp_to_train_dev_test.py your_file ./data/train.tsv ./data/dev.tsv ./data/test.tsv
 
2. 运行run_chinese_qp.sh

### chinese sentence classification
1. 数据保存在文件夹./data/chinese_sc下，包含train.tsv, dev.tsv, test.tsv，每个文件的格式为：sentence \t label (中间无空格)
    若只有一个文件，可用以下命令生成python ./data/split_sc_to_train_dev_test.py your_file ./data/train.tsv ./data/dev.tsv ./data/test.tsv
 
2. 运行run_chinese_sc.sh
