arr = [1,2,3]

// arr.forEach(console.log)
// 클라이언트 사이트 Web API가 포함된 소스코드는 Code Runner 확장 플러그인을 통해 실행하지 말고 
// 브라우저 환경에서 실행되어야 함.
// 일단 여기서 알고 갈 점은 클라이언트 사이드 web api는 node.js 환경에서 실행할 수 없다는 점.
arr.forEach(alert)

// 만약 live server를 통해 web에서 열게되면 정상 동작함!