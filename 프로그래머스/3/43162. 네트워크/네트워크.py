def dfs(computers, visited, start):
    # 시작 컴퓨터 방문 처리
    visited[start] = True
    for i in range(len(computers)): # 컴퓨터 개수 만큼 
        if computers[start][i] == 1 and not visited[i]:
            dfs(computers, visited, i)
            
def solution(n, computers):    
    visited = [False] * n # 방문 배열
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            count += 1
    return count 