class Graph:
    def __init__(self,edge):
        self.edge = edge
        self.nodes = {}
        for key,val in edge:
            if key in self.nodes:
                self.nodes[key].append(val)
            else:
                self.nodes[key] = [val]
        #print(self.nodes) 

    def get_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.nodes:
            return []
        paths = []

        for node in self.nodes[start]:
            if node not in path:
                paths += self.get_path(node,end,path)

        return paths

    def get_short_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path
        if start not in self.nodes:
            return []

        paths = None

        for node in self.nodes[start]:
            if node not in path:
                l = self.get_short_path(node,end,path)
                if paths is None or len(l) < len(paths):
                    paths = l

        return paths

if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    root = Graph(routes)
    print(root.get_path("Mumbai","Bangaluru"))
    print(root.get_short_path("Mumbai","Bangaluru"))