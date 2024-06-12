import importlib
from icon_family.icon import IconFamilyManager

class StyleFactory:
    """
    样式工厂类，用于动态创建样式实例。
    """
    def create_style(self, style_name):
        """
        根据样式名称动态导入样式模块并创建样式实例。
        
        参数:
        style_name (str): 样式的名称。
        
        返回:
        object: 样式实例。
        """
        # 动态导入样式模块
        style_module = importlib.import_module(f"style.{style_name.replace('.py', '')}")
        # 获取样式类
        style_class = getattr(style_module, style_name.split('_')[0].capitalize() + 'Style')
        # 返回样式实例
        return style_class()

class IconFamilyFactory:
    """
    图标族工厂类，用于创建和管理图标族。
    """
    def __init__(self):
        """
        初始化 IconFamilyFactory 实例，创建图标族管理器。
        """
        self.manager = IconFamilyManager()

    def create_icon_family(self, icon_family_name, icons):
        """
        创建图标族并添加到管理器中。
        
        参数:
        icon_family_name (str): 图标族的名称。
        icons (dict): 包含图标容器和叶子图标的字典。
        """
        self.manager.add_icon_family(icon_family_name, icons['icon_container'], icons['icon_leaf'])

    def get_icon_family(self, icon_family_name):
        """
        获取指定名称的图标族。
        
        参数:
        icon_family_name (str): 图标族的名称。
        
        返回:
        object: 图标族实例。
        """
        return self.manager.get_icon_family(icon_family_name)

    def load_icon_families(self, icon_families_config):
        """
        加载多个图标族配置并创建图标族。
        
        参数:
        icon_families_config (dict): 包含图标族配置的字典。
        """
        for name, icons in icon_families_config.items():
            self.create_icon_family(name, icons)

class ExplorerFactory:
    """
    探索器工厂类，用于创建样式和加载图标族。
    """
    def __init__(self):
        """
        初始化 ExplorerFactory 实例，创建样式工厂和图标族工厂。
        """
        self.style_factory = StyleFactory()
        self.icon_family_factory = IconFamilyFactory()
    
    def create_style(self, style_name):
        """
        创建指定名称的样式实例。
        
        参数:
        style_name (str): 样式的名称。
        
        返回:
        object: 样式实例。
        """
        return self.style_factory.create_style(style_name)
    
    def load_icon_families(self, icon_families_config):
        """
        加载图标族配置并创建图标族。
        
        参数:
        icon_families_config (dict): 包含图标族配置的字典。
        """
        self.icon_family_factory.load_icon_families(icon_families_config)
    
    def get_icon_family(self, icon_family_name):
        """
        获取指定名称的图标族实例。
        
        参数:
        icon_family_name (str): 图标族的名称。
        
        返回:
        object: 图标族实例。
        """
        return self.icon_family_factory.get_icon_family(icon_family_name)
