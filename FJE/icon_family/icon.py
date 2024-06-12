class IconFamily:
    """
    图标族类，包含图标族的名称以及对应的图标。
    """
    def __init__(self, name, container, leaf):
        """
        初始化 IconFamily 实例。
        
        参数:
        name (str): 图标族的名称。
        container (object): 容器图标。
        leaf (object): 叶子图标。
        """
        self.name = name
        self.container = container
        self.leaf = leaf

    def get_container_icon(self):
        """
        获取容器图标。
        
        返回:
        object: 容器图标。
        """
        return self.container

    def get_leaf_icon(self):
        """
        获取叶子图标。
        
        返回:
        object: 叶子图标。
        """
        return self.leaf

class IconFamilyManager:
    """
    图标族管理器类，用于管理多个图标族。
    """
    def __init__(self):
        """
        初始化 IconFamilyManager 实例。
        """
        self.icon_families = {}

    def add_icon_family(self, name, container, leaf):
        """
        添加新的图标族到管理器中。
        
        参数:
        name (str): 图标族的名称。
        container (object): 容器图标。
        leaf (object): 叶子图标。
        """
        self.icon_families[name] = IconFamily(name, container, leaf)

    def get_icon_family(self, name):
        """
        获取指定名称的图标族。
        
        参数:
        name (str): 图标族的名称。
        
        返回:
        IconFamily: 图标族实例，如果未找到则返回 None。
        """
        return self.icon_families.get(name, None)

    def get_all_icon_families(self):
        """
        获取所有图标族。
        
        返回:
        dict: 包含所有图标族的字典。
        """
        return self.icon_families
