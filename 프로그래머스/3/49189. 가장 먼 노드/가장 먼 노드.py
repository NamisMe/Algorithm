from collections import deque 
def solution(n, vertex):
    #양방향 간선 
    graph = [[] for _ in range(n+1)]
    visited = False * (n+1) # 방문처리
    for v1, v2 in vertex:
        graph[v1].append(v2)
        graph[v2].append(v1)
    # print(graph)
    
    #최단 경로 이동 구현
    visited = [False] * (n+1) # 방문처리
    distance = [0] * (n+1) # 거리 저장
    
    # BFS
    queue = deque([1]) # 시작 노드 : 1
    visited[1] = True # 
    while queue:
        current_node = queue.popleft()
        for next_node in graph[current_node]: # 현재 노드와 연결되어있는 노드를 돌면서
            if not visited[next_node]: # 방문하지 않았을 경우에
                visited[next_node] = True
                distance[next_node] = distance[current_node] + 1
                queue.append(next_node)
            # print(current_node, queue)
    # print(visited, distance)
    # 최대 거리 찾기
    max_distance = max(distance)
    answer = distance.count(max(distance))
    return answer


