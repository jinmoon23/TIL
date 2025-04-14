# About Branch

1. branch 이전
- `git add` 전: working directory
- `git add`: working directory -> staging area
  - working directory <- staging area: 
- `git commit`: staging area의 변동사항을 하나의 버전으로 기록하고 staging area를 비움
- 그 버전들이 모여있는 곳을 repository라고 부른다.

2. branch
- 여러 갈래로 **작업공간을 나누어** 독립적으로 작업할 수 있도록 도와주는 도구.
- 어떤 원본의 **완전성**을 보장하면서 독립적인 개발환경을 구성할 수 있다.
- `git switch {branch_name}`: 브랜치 이동

컨플릭 어떻게 하면 발생해요??
- 같은 라인을 다른 브랜치에서 동시에 커밋하면 발생합니다.
- ex) master 브랜치 10번째 라인 수정 후 커밋 / bbogle 브랜치 10번째 라인 수정 후 커밋 -> 이후에 mastet에서 merge 진행하면 컨플릭 발생

3. branch 약속
- 생성 시 `팀 이름 / 기능명` 을 보통 사용한다.
- merge는 로컬에서 진행하지 않는다. 반드시 원격 저장소에서 진행해야 한다.