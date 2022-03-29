"""
 * Project name(项目名称)：Python导入模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:29
 * Version(版本): 1.0
 * Description(描述)： import 模块名 as 别名
 """

# 导入sys整个模块，并指定别名为s
import sys as s

if __name__ == '__main__':
    # 使用s模块别名作为前缀来访问模块中的成员
    print(len(s.argv))
    print(s.argv[0])
