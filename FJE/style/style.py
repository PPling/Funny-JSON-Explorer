from abc import ABC, abstractmethod

class Style(ABC):
    """
    样式抽象基类，所有样式类都应该继承自该类并实现 draw 方法。
    """
    @abstractmethod
    def draw(self, data, icon_family):
        """
        绘制方法，子类必须实现此方法。
        
        参数:
        data (Container): 树结构的根容器节点。
        icon_family (IconFamily): 包含容器图标和叶子图标的图标族。
        """
        pass