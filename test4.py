"""
 * Project name(项目名称)：Python导入模块
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:33
 * Version(版本): 1.0
 * Description(描述)： 在导入多个模块的同时，也可以为模块指定别名
 """

# 导入sys、os两个模块，并为sys指定别名s，为os指定别名o
import sys as s, os as o

if __name__ == '__main__':
    # 使用模块别名作为前缀来访问模块中的成员
    print(s.argv[0])
    print(o.sep)
    # 在子shell 中执行命令。
    print(o.system("start"))
