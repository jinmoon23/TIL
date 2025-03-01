function solution(name) {
  const alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  let count = 0
  
  for (let i=0; i<name.length; i++) {
      if (name[i] === 'A') {
          if (i+1 < name.length && name[i+1] !== 'A' && i+1 === name.length-1) {
            count += 1            
          }
      } else {
          alphabet.forEach((char,idx) => {
              if (char === name[i] && idx < 13) {
                  if (i === 0) {
                      count += idx
                  } else {
                      count += idx + 1
                  }
              } else if (char === name[i] && idx >= 13) {
                if (i-1 >=0 && name[i-1] !== 'A') {
                  count += alphabet.length - idx +1
                }else {
                  count += alphabet.length - idx
                }
              }
          })
      }
  }
  return count
}

solution("JEROEN")
solution("JAN")