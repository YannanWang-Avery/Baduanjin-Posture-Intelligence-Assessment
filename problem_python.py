n=0# 记录总共有多少个样本
dim=0# 记录特征的维度
feat = []
label = []

def classify(id):
#TODO: 你需要编写一个分类函数
# 输入参数id 表示
# 你可以使用feat[id][0]到
# feat[id][dim-1]的所有数据
# 以及你自己声明的常变量
# 注意： 你不可以直接使用label
# 或者label没有经过缩并运算的结果
    return 0

def parse_feature(fname_feat):
    f= open(fname_feat,"r")
    line = f.readline()
    global n
    while line:
        st = line.split('\n')[0].split('\t')
        n = len(st)
        feat.append(st)
        line = f.readline()


def parse_label(fname_label):
    f = open(fname_label, "r")
    line = f.readline()
    while line:
        st = line.split('\n')[0].split('\t')
        label.append(st)
        line = f.readline()
    global dim
    dim = len(label)


if __name__ == '__main__':
    fname_feat = "feature.txt"
    fname_label = "label.txt"
    parse_feature(fname_feat)
# parse_feature是一个已经编写好的函数
# 特征会被存在二维数组feat中
# 并且会同步更新n
    parse_label(fname_label)
# parse_label是一个已经编写号的函数
# 标签会被存在label中
# 并且会同步更新dim
    count = 0

    for i in range(0,len(label)):
        if int(classify(i)) == int(label[i][0]):
            count+=1
    print("准确率："+str(float(count)/float(dim)))





    

