'''
문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.
입출력 예
genres	plays	return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.
'''
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

from collections import Counter

def solution(genres, plays):
    from collections import defaultdict
    
    # Step 1: 장르별 총 재생 횟수를 계산
    genre_total_plays = defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_total_plays[genre] += play
    
    # Step 2: 장르 내 노래들에 대해 (재생 횟수, 고유번호) 튜플을 저장
    songs_by_genre = defaultdict(list)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        songs_by_genre[genre].append((play, idx))
    
    # Step 3: 장르별로 노래들을 재생 횟수와 고유번호로 정렬
    for genre in songs_by_genre:
        songs_by_genre[genre].sort(key=lambda x: (-x[0], x[1]))
    
    # Step 4: 장르별 총 재생 횟수로 장르를 정렬
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda g: -genre_total_plays[g])
    
    # Step 5: 베스트 앨범에 각 장르에서 최대 두 곡씩 수록
    best_album = []
    for genre in sorted_genres:
        best_album.extend([song[1] for song in songs_by_genre[genre][:2]])
    
    return best_album

print(solution(genres, plays))