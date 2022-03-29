"""
 * Project name(项目名称)：Python导入模块
 * Package(包名): 
 * File(文件名): test8
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:38
 * Version(版本): 1.0
 * Description(描述)： 一次导入多个模块成员时，也可指定别名
 """

# 导入sys模块的argv,winver成员，并为其指定别名v、wv
import logging
from sys import argv as a, winver as w

# 对日志系统进行基本配置。
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -- %(levelname)s -->  %(message)s')

if __name__ == '__main__':
    # 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
    logging.info(a[0])
    logging.info(w)
