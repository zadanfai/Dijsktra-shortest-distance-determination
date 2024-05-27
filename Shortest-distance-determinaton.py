from collections import defaultdict #mengimpor modul defaultdict dari pustaka collections untuk membuat kamus dengan nilai default kosong jika kunci belum ada.

#mendefinisikan kelas graph
class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight): #menambahkan edge pada graf. 
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph() #buat object graph
edges = [
    ('A', 'B', 3890.0),
    ('A', 'C', 1730.0),
    ('A', 'D', 1580.0),
    ('A', 'E', 1580.0),
    ('A', 'F', 3220.0),
    ('B', 'C', 3220.0),
    ('B', 'D', 3500.0),
    ('B', 'A', 3890.0),
    ('B', 'E', 3350.0),
    ('B', 'F', 3210.0),
    ('C', 'E', 176.0),
    ('C', 'B', 3220.0),
    ('C', 'A', 1730.0),
    ('C', 'D', 319.0),
    ('C', 'F', 2660.0),
    ('D', 'E', 158.0),
    ('D', 'B', 3500.0),
    ('D', 'A', 1580.0),
    ('D', 'C', 319.0),
    ('D', 'F', 2700.0),
    ('E', 'D', 158.0),
    ('E', 'A', 1580.0),
    ('E', 'C', 176.0),
    ('E', 'B', 3350.0),
    ('E', 'F', 2590.0),
    ('F', 'A', 1590.0),
    ('F', 'B', 3210.0),
    ('F', 'C', 2660.0),
    ('F', 'D', 2700.0),
    ('F', 'E', 2590.0)
]
#menambahkan sisi (edge) ke graf dengan menambahkan simpul (node) baru ke daftar koneksi (edges) dan bobotnya ke kamus bobot (weights)
for edge in edges:
    graph.add_edge(*edge)

#def algoritma dijkstra
def dijsktra(graph, initial, end): #graph,initial(awal),end(akhir) = parameter
    shortest_paths = {initial: (None, 0)} #node awal jarak=0
    current_node = initial 
    visited = set() #Membuat sebuah set kosong untuk menyimpan node yang telah dikunjungi
    while current_node != end:
        visited.add(current_node) #Menambahkan current_node ke set visited
        destinations = graph.edges[current_node] #Mengambil semua node yang terhubung dengan current_node
        weight_to_current_node = shortest_paths[current_node][1] #Menyimpan jarak terpendek dari initial ke current_node

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node #Menentukan jarak dari initial ke next_node melalui current_node.
            if next_node not in shortest_paths: #Jika next_node belum ditambahkan ke shortest_paths, maka tambahkan next_node ke shortest_paths dengan nilai path terpendek dari initial ke next_node.
                shortest_paths[next_node] = (current_node, weight)
            else: #Jika next_node sudah ditambahkan ke shortest_paths, maka perbarui nilai path terpendek dari initial ke next_node jika jarak yang baru lebih pendek dari jarak sebelumnya.
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited} #Membuat dictionary next_destinations yang berisi path terpendek dari initial ke semua node yang belum dikunjungi.
        if not next_destinations:
            return "Route Not Possible"

        current_node = min(next_destinations,key=lambda k: next_destinations[k][1])

    #membuat Path
    path = []
    while current_node is not None: 
        path.append(current_node) #Menambahkan current_node ke path
        next_node = shortest_paths[current_node][0] #Menentukan node selanjutnya di path terpendek dari initial ke end
        current_node = next_node #Mengubah nilai current_node menjadi next_node
    path = path[::-1] #Membalik urutan elemen di dalam path
    return path #Mengembalikan path terpendek dari initial ke end.


print('Unsika -> Ciplaz')
print(dijsktra(graph, 'A', 'F'))

print('Gusta and CO -> HardTop Caffe')
print(dijsktra(graph, 'F', 'D'))
