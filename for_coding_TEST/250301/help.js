function solution(name) {
  const n = name.length;
  let totalMoves = 0;
  
  // 세로 이동: 각 문자를 'A'에서 변경하는 비용 계산
  for (let i = 0; i < n; i++) {
    const diff = name.charCodeAt(i) - 'A'.charCodeAt(0);
    totalMoves += Math.min(diff, 26 - diff);
  }
  
  // 좌우 이동: 최적의 커서 이동 경로 계산
  let horizontal = n - 1;
  for (let i = 0; i < n; i++) {
    let j = i + 1;
    
    // 연속된 'A' 구간 건너뛰기
    while (j < n && name[j] === 'A') {
      j++;
    }
    
    // (a) 오른쪽으로 i번 이동 후, 다시 왼쪽으로 돌아가 남은 구간(n - j)을 이동
    // (b) 오른쪽으로 i번 이동 후, 남은 구간(n - j)까지 바로 이동 (즉, 왼쪽 이동을 먼저 해서 처리)
    // 예를 들어, 가운데에 연속된 'A'가 많아서 어느 한쪽 끝만 바꿔주면 되는 경우,
    // 두 번째 경우 (i + 2·(n - j))가 더 적은 이동 비용을 줄 수 있습니다.
    horizontal = Math.min(horizontal, i + i + n - j, i + 2 * (n-j));
  }
  
  return totalMoves + horizontal;
}

// 예시 실행
console.log(solution("JEROEN")); // 예: 최소 이동 횟수 출력
console.log(solution("JAN"));
