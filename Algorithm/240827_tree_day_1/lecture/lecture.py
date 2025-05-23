'''
Tree
- 비선형 데이터 구조
- 원소들 간 1:n 관계를 가지는 자료구조
- 원소들 간 계층관계를 가지는 계층형 구조
- 부트리들은 모두 각자가 하나의 트리를 이룬다.(재귀적 정의)

Tree 용어정리
- 노드: 트리의 원소
- 간선: 노드를 연결하는 선. 부모 노드와 자식 노드를 연결한다.
- 루트 노드: 트리의 시작 노드
- 형제 노드: 같은 부모 노드의 자식 노드들 -> 형제 노드 간 연결은 불가능하다! ( == 사이클이 없다)
- 차수: 노드에 연결된 자식 노드의 수
- 높이: 트리의 깊이, level 이라는 단어로 표현 -> 중요!

이진트리
- 모든 노드들이 최대 2개(0,1,2 가능)의 서브트리를 갖는 특별한 형태의 트리
- level i 에서의 노드 최대 개수는 2**i개
- 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 h+1개. 최대 개수는 (2h**1 -1)

완전 이진 트리
- 포화 이진 트리의 노드번호 1번부터 n번까지 빈 '자리가 없는' 이진트리

Tree의 활용
1. 순회
- 트리의 노드들을 체계적으로 방문하는 것
    1-1. 전위순회
    - 현재 -> 좌 -> 우
    1-2. 중위순회
    - 좌 -> 현재 -> 우
    1-3. 후위순회
    - 좌 -> 우 -> 현재
- 복습할 때 꼭 그림으로 확인할 것!
'''