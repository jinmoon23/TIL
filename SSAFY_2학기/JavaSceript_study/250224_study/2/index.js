let i,j;

loop1: 
for (let i = 0; i < 3; i++) {
  loop2:
  for (let j = 0; j < 3; j++) {
    if (i === 1 && j === 1) {
      break loop1;      
    }
    console.log(i,j)
  }  
}