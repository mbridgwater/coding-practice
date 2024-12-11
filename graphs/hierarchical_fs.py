"""
files = [
"/webapp/assets/html/a.html",
"/webapp/assets/html/b.html",
"/webapp/assets/js/c.js",
"/webapp/entrypoint.txt",
]

Write a program which intakes these filepaths, and prints them out in a hierarchial filesystem fashion. 

-- webapp
  -- assets
    -- html
      -- a.html
      -- b.html
    -- js
      -- c.js
  -- entrypoint.txt
"""

# Clarifying questions:
# Can there be forward slashes in the file names themselves?

"""----- BELOW IS A VERSION USING A DICTIONARY TO REPRESENT THE TREE -----"""


def build_tree(files):
    tree = {}
    for file in files:
        curr_dict = tree
        parts = file.strip("/").split("/")
        for part in parts:
            if part not in curr_dict:
                curr_dict[part] = {}
            curr_dict = curr_dict[part]

    return tree


def pre_order_traversal_dict(dict_tree, level=0):
    for child in dict_tree:
        print(level * "  " + "--" + child)
        pre_order_traversal_dict(dict_tree[child], level + 1)


"""----- BELOW IS A VERSION USING NODES TO REPRESENT THE TREE -----"""


class TreeNode:
    def __init__(self, file):
        self.file_name = file
        self.children = []

    def get_child(self, file_name):
        """gets the child or makes one if it doesn't exist"""
        for child in self.children:
            if child.file_name == file_name:
                return child
        # no child found
        # new_child = TreeNode(file_name)
        # self.children.append(new_child)
        # return new_child
        return None


class FileSystem:
    def __init__(self, files):
        self.tree = self._build_tree_from_files(files)

    def _build_tree_from_files(self, files):
        tree = TreeNode("/")  # filesystem root
        for file in files:
            curr_node = tree
            parts = file.strip("/").split("/")
            for part in parts:
                child_node = curr_node.get_child(part)
                if child_node is None:
                    child_node = TreeNode(part)
                    curr_node.children.append(child_node)
                curr_node = child_node
        return tree

    def _preorder_dfs_traversal(self, node, level=0):
        for child in node.children:
            print("  " * level, "--", child.file_name)
            self._preorder_dfs_traversal(child, level + 1)

    def print_filesystem(self):
        self._preorder_dfs_traversal(self.tree)


if __name__ == "__main__":
    files = [
        "/webapp/assets/html/a.html",
        "/webapp/assets/html/b.html",
        "/webapp/assets/js/c.js",
        "/webapp/entrypoint.txt",
    ]
    # my_dict = build_tree(files)
    # print(my_dict)
    # pre_order_traversal_dict(my_dict)
    fs = FileSystem(files)
    fs.print_filesystem()
