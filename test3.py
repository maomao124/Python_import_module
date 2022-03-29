"""
 * Project name(项目名称)：Python导入模块
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:30
 * Version(版本): 1.0
 * Description(描述)： 一次导入多个模块，多个模块之间用逗号隔开
 """

# 导入sys、os两个模块
import sys, os

if __name__ == '__main__':
    # 使用模块名作为前缀来访问模块中的成员
    print(sys.argv[0])
    # os模块的sep变量代表平台上的路径分隔符
    print(os.sep)
    # 在子shell 中执行命令。
    print(os.system("start"))
