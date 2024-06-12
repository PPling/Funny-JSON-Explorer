from .explorer import FunnyJsonExplorer

class ExplorerBuilder:
    def __init__(self, factory):
        """
        初始化 ExplorerBuilder 实例。
        
        参数:
        factory (object): 一个工厂对象，用于创建样式和获取图标族。
        """
        self.factory = factory
    
    def build(self, style_name, icon_family_name):
        """
        根据给定的样式名称和图标族名称构建并返回 FunnyJsonExplorer 实例。
        
        参数:
        style_name (str): 样式的名称。
        icon_family_name (str): 图标族的名称。
        
        返回:
        FunnyJsonExplorer: 用于探索 JSON 数据的实例。
        
        异常:
        ValueError: 当指定的图标族未找到时抛出。
        """
        # 使用工厂创建样式对象
        style = self.factory.create_style(style_name)
        
        # 使用工厂获取图标族对象
        icon_family = self.factory.get_icon_family(icon_family_name)
        
        # 如果未找到指定的图标族，则抛出异常
        if not icon_family:
            raise ValueError(f"Icon family '{icon_family_name}' not found.")
        
        # 返回一个新的 FunnyJsonExplorer 实例，使用创建的样式和图标族
        return FunnyJsonExplorer(style, icon_family)
