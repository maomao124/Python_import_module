"""
 * Project name(项目名称)：Python导入模块
 * Package(包名): 
 * File(文件名): test7
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:36
 * Version(版本): 1.0
 * Description(描述)： form...import 导入模块成员时，支持一次导入多个成员
 """

# 导入sys模块的argv,winver成员
from sys import argv, winver

if __name__ == '__main__':
    # 使用导入成员的语法，直接使用成员名访问
    print(argv[0])
    print(winver)
