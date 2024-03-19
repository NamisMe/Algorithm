def solution(genres, plays):
    answer = []
    genre_dict = {}
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_dict:
            genre_dict[genre] = {'total': 0, 'songs': []} # 초기화
        genre_dict[genre]['total'] += play
        genre_dict[genre]['songs'].append((play, i))
    # print(genre_dict)
    # 총 재생 횟수 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_dict.items(), key=lambda x:x[1]['total'], reverse=True)
    # print(sorted_genres)
    
    for genre, value in sorted_genres:
        sorted_songs = sorted(value['songs'], key=lambda x:(-x[0], x[1]))
        answer.extend([song[1] for song in sorted_songs[:2]])
    return answer