function solution(numbers) {
  var per_array = [];
  function permutation(arr, n) {
    const visited = Array(arr.length).fill(false);

    function dfs(current) {
      if (current.length === n) {
        per_array.push([...current]);
        return;
      }
      for (let i = 0; i < arr.length; i++) {
        if (visited[i] === false) {
          visited[i] = true;
          current.push(arr[i]);
          dfs(current);
          current.pop();
          visited[i] = false;
        }
      }
    }
    dfs([]);
  }
  permutation(numbers, numbers.length);
  var compareArray = [];
  per_array.forEach((per_elem) => {
    var dummy_str = "";
    per_elem.forEach((number) => {
      dummy_str += String(number);
    });
    compareArray.push(Number(dummy_str));
  });

  function returnMaxNumber(arr) {
    var max = 0;
    arr.forEach((number) => {
      if (number > max) {
        max = number;
      }
    });
    return max;
  }
  const result = returnMaxNumber(compareArray);
  return String(result);
}

solution([6, 10, 2]);
