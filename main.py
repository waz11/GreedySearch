from Graph.graphFromJson import GraphFromJson
from Query.query import Query
from Searcher.GreedySearch import GreedySearch


def testGreedySearch():
    graph = GraphFromJson('./Files/graphs/src1.json')
    query = Query("class list implements iterable,class list contains class node")
    # query = Query("class list extends class iterable")
    searcher = GreedySearch(graph)
    result = searcher.search(query)
    print(result.rank, result.graph)
    result.graph.draw()


def main():
    testGreedySearch()


if __name__ == '__main__':
    main()
