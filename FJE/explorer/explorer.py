from abc import ABC, abstractmethod

class Leaf:
    """
    叶子节点类，用于表示树结构中的叶子节点。
    
    参数:
    name (str): 叶子节点的名称。
    icon (optional): 叶子节点的图标，默认为 None。
    """
    def __init__(self, name, icon=None):
        self.name = name
        self.icon = icon

    def draw(self):
        """
        绘制叶子节点的方法，可以在子类中实现具体的绘制逻辑。
        """
        pass

class Container:
    """
    容器类，用于表示树结构中的容器节点，可以包含其他容器或叶子节点。
    
    参数:
    name (str): 容器节点的名称。
    level (int): 容器节点在树结构中的层级。
    """
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.icon = None
        self.children = []

    def add_child(self, child):
        """
        向容器节点添加子节点（可以是叶子节点或其他容器节点）。
        
        参数:
        child (Leaf 或 Container): 要添加的子节点。
        """
        self.children.append(child)
        
    def draw(self):
        """
        绘制容器节点的方法，可以在子类中实现具体的绘制逻辑。
        """
        pass

class FunnyJsonExplorer:
    """
    用于探索和显示 JSON 数据的类，通过树结构表示并使用指定样式渲染。
    
    参数:
    style (object): 用于渲染树结构的样式对象。
    icon_family (object): 用于提供图标的图标族对象。
    """
    def __init__(self, style, icon_family):
        self.style = style
        self.icon_family = icon_family
        self.root_container = Container("root", level=0)

    def show(self, data):
        """
        显示 JSON 数据的方法，构建树结构并使用样式渲染。
        
        参数:
        data (dict): 要显示的 JSON 数据。
        """
        # 构建树结构
        self._load(data, self.root_container)
        # 使用样式渲染数据
        self.style.draw(self.root_container, self.icon_family)

    def _load(self, data, parent_container):
        """
        递归加载 JSON 数据到树结构中。
        
        参数:
        data (dict): 当前要处理的 JSON 数据。
        parent_container (Container): 当前数据所属的父容器节点。
        """
        for key, value in data.items():
            if isinstance(value, dict):
                # 如果值是字典，则创建新的容器节点并递归加载
                new_container = Container(key, parent_container.level + 1)
                parent_container.add_child(new_container)
                self._load(value, new_container)
            else:
                # 如果值不是字典，则创建叶子节点
                if isinstance(value, str):
                    key = f"{key}: {value}"
                leaf = Leaf(key)
                parent_container.add_child(leaf)
