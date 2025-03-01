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
    
    // 현재 위치까지 이동한 비용  +  되돌아가는 비용  +  나머지 처리 비용
    horizontal = Math.min(horizontal, i + i + n - j);
  }
  
  return totalMoves + horizontal;
}

// 예시 실행
console.log(solution("JEROEN")); // 예: 최소 이동 횟수 출력
console.log(solution("JAN"));
