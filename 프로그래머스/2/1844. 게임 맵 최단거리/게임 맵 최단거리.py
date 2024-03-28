from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # 방향 벡터
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 방문처리
    visited = [[0] * m for _ in range(n)]
    
    #BFS
    q = deque([(0, 0, 1)])
    visited[0][0] = 1 # 시작 위치 방문 표시
    
    while q:
        x, y, dist = q.popleft()
        
        if x == n-1 and y == m-1:
            return dist
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵의 범위를 벗어나지 않고, 방문하지 않았으며, 이동할 수 있는 위치라면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] == 1:
                visited[nx][ny] = 1 # 방문 표시
                q.append((nx, ny, dist + 1)) # 큐에 추가            
    # 목적지에 도달했을 경우 -1을 반환             
    return -1