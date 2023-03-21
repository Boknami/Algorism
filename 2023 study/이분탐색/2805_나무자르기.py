# 나무 M 미터
# 이만큼 짤라라 높이 설정 H
# 20 10 15 (H = 10) -> 10 + 0 + 5 = 15M 가져가
# 최소 M 미터는 가져갈 높이 H의 최댓값

# 나무 최대 100만, 길이 최대20억 
import sys
input = sys.stdin.readline

cntWood, needLength = map(int, input().split())
woods = list(map(int, input().split()))

curLength = 0