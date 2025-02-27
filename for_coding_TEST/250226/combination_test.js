function combination(arr,n){
  let result=[]
  function dfs(current,idx){
      if(current.length===n){
          result.push([...current])
          return
      }
      for(let i=idx;i<arr.length;i++){
          // 조합은 요소의 중복을 허락하지 않는다. 따라서 현 인덱스를 넣었다면 다시 반복되지 않도록 다음 dfs에는 i+1을 넘겨주어야 함
          current.push(arr[i])
          dfs(current,i+1)
          current.pop()
      }
  }
  dfs([],0)
  return result
}

console.log(combination([6,10,2], 3))