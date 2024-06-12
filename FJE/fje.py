import json
import argparse
from explorer.builder import ExplorerBuilder
from explorer.factory import ExplorerFactory
from explorer.explorer import FunnyJsonExplorer

def main():
    # 读取配置文件
    with open('config.json',encoding='utf-8') as config_file:
        config = json.load(config_file)

    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='JSON file to explore')
    parser.add_argument('-s', '--style', required=True, choices=config['styles'].keys(), help='Style to use')
    parser.add_argument('-i', '--icon', required=True, choices=config['icon_families'].keys(), help='Icon family to use')
    args = parser.parse_args()

    # 读取指定的JSON文件
    with open(args.file,encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # 创建工厂和建造者
    factory = ExplorerFactory()
    builder = ExplorerBuilder(factory)
    
    # 加载图标族
    factory.load_icon_families(config['icon_families'])
    
    # 根据命令行参数选择样式和图标族
    style_name = config['styles'][args.style]
    icon_family_name = args.icon
    
    # 创建 Explorer 实例
    explorer = builder.build(style_name, icon_family_name)
    
    # 显示数据
    explorer.show(data)

if __name__ == "__main__":
    main()