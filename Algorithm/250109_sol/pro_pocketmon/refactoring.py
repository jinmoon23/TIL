def solution(nums):
    # 최대로 선택할 수 있는 폰켓몬 수
    max_choice = len(nums) // 2
    # 중복이 제거된 폰켓몬 리스트
    unique_pokemons = set(nums)
    return min(len(unique_pokemons), max_choice)