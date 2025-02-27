function permutation(arr, n) {
  let result = [];
  const visited = Array(arr.length).fill(false);

  function dfs(current) {
    if (current.length === arr.length) {
      result.push([...current])
      return
    }
    for (let i = 0; i < arr.length; i++) {
      if (visited[i] === false) {
        visited[i] = true
        current.push(arr[i]);
        dfs(current);
        current.pop()
        visited[i] = false
      }
    }
  }
  dfs([]);

  return result
}

console.log(permutation([6,10,2], 3))