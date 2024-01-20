def solution(nums):
    # 해시 초기화
    pokemon_hash = {}
    
    # nums 배열에서 pokemon_hash 만들기
    for num in nums:
        if num in pokemon_hash:
            pokemon_hash[num] += 1
        else:
            pokemon_hash[num] = 1
    
    # 전체 포켓몬의 수, 유일한 폰켓몬 수 
    total_count = len(nums)
    unique_count = len(pokemon_hash)
    
    # N/2 와 유일한 폰켓몬 종류의 수를 비교 ->
    # 그 중 작은 값을 찾으면
    # 최대로 가질 수 있는 다양한 폰켓몬의 수를 구하시오.
    max_types = min(total_count // 2, unique_count)
    
    return max_types