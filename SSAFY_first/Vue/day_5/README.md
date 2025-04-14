# JS에서 UUID 부여하기

https://www.daleseo.com/js-uuid/

`npm install uuid`

```javascript
import { v4 as uuidv4 } from "uuid"; // ES Modules
// const { v4: uuidv4 } = require("uuid"); // CommonJS

const id = uuidv4();
console.log(id); // "69c52380-f123-4523-a0c8-4bc78319cf6b"
```
Web 표준 API를 충실하게 구현하고 있는 모던 브라우저에서는 UUID 생성을 위해서 굳이 별도의 패키지를 설치하지 않아도 됩니다. 왜냐하면 Web Crypto API에서 UUID를 반환하는 randomUUID() 함수를 제공하고 있기 때문입니다.

```javascript
const id = crypto.randomUUID();
console.log(id); // "cbfc904b-b898-4deb-b736-ba433489904c"
```