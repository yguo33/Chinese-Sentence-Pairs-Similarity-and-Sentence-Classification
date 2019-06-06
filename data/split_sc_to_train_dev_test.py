import sys
import codecs
from sklearn.model_selection import train_test_split


def split_files(input_file, output_train_file, output_dev_file, output_test_file):
    """
    input_file: sentence \t label
    """
    total_qq = []
    total_y = []
    with codecs.open(input_file, 'r', 'utf-8') as f:
        for line in f:
            line_split = line.strip().split('\t')
            if len(line_split) == 2:
                total_qq.append(line_split[0])
                total_y.append(line_split[1])

    X_train, X_test, y_train, y_test = train_test_split(total_qq, total_y, test_size=0.2, random_state=2)
    X_dev, X_test, y_dev, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=77)

    assert len(X_train) == len(y_train)
    assert len(X_dev) == len(y_dev)
    assert len(X_test) == len(y_test)

    print('train size: {}\ndev size:{}\ntest size:{}'.format(len(X_train), len(X_dev), len(y_dev)))

    with codecs.open(output_train_file, 'w', 'utf-8') as f:
        for i, x in enumerate(X_train):
            f.write(x + '\t' + y_train[i] + '\n')

    with codecs.open(output_dev_file, 'w', 'utf-8') as f:
        for i, x in enumerate(X_dev):
            f.write(x + '\t' + y_dev[i] + '\n')

    with codecs.open(output_test_file, 'w', 'utf-8') as f:
        for i, x in enumerate(X_test):
            f.write(x + '\t' + y_test[i] + '\n')


if __name__ == '__main__':
    split_files(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    # split_files('qq.txt', 'train.tsv', 'dev.tsv', 'test.tsv')
