"""
 * Project name(项目名称)：Python导入模块
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:34
 * Version(版本): 1.0
 * Description(描述)： from  模块名 import 成员名
 """

# 导入sys模块的argv成员
import logging
from sys import argv

# 对日志系统进行基本配置。
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -- %(levelname)s -->  %(message)s')

if __name__ == '__main__':
    # 使用导入成员的语法，直接使用成员名访问
    logging.info(argv[0])
