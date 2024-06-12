from .style import Style
from explorer.explorer import Container, Leaf

class RectangleStyle(Style):
    """
    矩形样式类，用于绘制树结构的矩形表示。
    """
    def draw(self, data, icon_family):
        """
        绘制树结构数据，使用指定的图标族渲染节点。
        
        参数:
        data (Container): 树结构的根容器节点。
        icon_family (IconFamily): 包含容器图标和叶子图标的图标族。
        """
        def _print_rectangle(node, indent=0, is_last=True, is_first=True, parent_prefix=""):
            """
            递归绘制树结构节点。
            
            参数:
            node (Container 或 Leaf): 当前要绘制的节点。
            indent (int): 当前节点的缩进级别。
            is_last (bool): 是否为当前父节点的最后一个子节点。
            is_first (bool): 是否为当前父节点的第一个子节点。
            parent_prefix (str): 父节点前缀，用于保持树结构的连贯性。
            """
            if node.name == "root":
                # 特殊处理根节点，直接递归其子节点
                for i, child in enumerate(node.children):
                    _print_rectangle(child, indent=0, is_last=(i == len(node.children) - 1) and is_last, 
                                     is_first=(i == 0), parent_prefix="")
            else:
                # 根据节点位置确定连接符和前缀
                if is_first and indent == 0:
                    connector = "┌─"
                    next_prefix = "|   "
                    end_str = "┐"
                elif is_last and isinstance(node, Leaf):
                    connector = "└─"
                    next_prefix = "    "
                    end_str = "┘"
                else:
                    connector = "├─"
                    next_prefix = "|   "
                    end_str = "┤"
                
                # 根据节点类型确定输出内容
                if isinstance(node, Container):
                    if node.children:
                        print(parent_prefix + connector + f" {icon_family.get_container_icon()} {node.name} " + 
                              "─" * (40 - indent - len(connector) - len(node.name) - 1) + end_str)
                        for i, child in enumerate(node.children):
                            _print_rectangle(child, indent + 4, is_last=(i == len(node.children) - 1) and is_last, 
                                             is_first=(i == 0), parent_prefix=parent_prefix + next_prefix)
                elif isinstance(node, Leaf):
                    leaf_prefix = parent_prefix.replace('|', '└').replace(' ', '─') if is_last else parent_prefix
                    print(leaf_prefix + connector + f" {icon_family.get_leaf_icon()} {node.name} " + 
                          "─" * (40 - indent - len(connector) - len(node.name) - 1) + end_str)

        _print_rectangle(data)
