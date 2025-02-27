function solution(numbers) {
  // 1. 각각의 숫자를 이어붙이기 위해 문자열로 변환
  const str_numbers = numbers.map(String)
  str_numbers.sort((a,b) => {
    // 2. 이어붙인 숫자들을 비교
      const order1 = a + b;
      const order2 = b + a;
      if (order1 > order2) {
        // -1을 리턴하면 내림차순 정렬
          return -1
          // 1을 리턴하면 오름차순 정렬렬
      } else if (order1 < order2) {
          return 1
      }
      return 0
  })
  if (str_numbers[0] === "0") return "0";
  console.log(str_numbers)
  return str_numbers.join('')
}

solution([3,30,34,5,9])