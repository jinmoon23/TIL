# Markdown 문법을 배우다!
1. 제목 1~6
2. 나열하는 다양한 방식
3. [링크](https://naver.com)와 ![이미지](https://health.chosun.com/site/data/img_dir/2020/05/07/2020050702573_0.jpg)
4. `코드` 삽입 
```python
print("Hi~")
def makeHotItem() 
    a = hot
    b = item
    return a+b
```
1. **문자열**에 적용하는 *다양한* 문법 ~~아싸~~
2. 추가적인 마크다운 문법 [마크다운Docs](https://www.markdownguide.org/basic-syntax/)
<br>
> 이것은 인용문?!  

아아 이것은 수평선 이라는 것이다.  

---
# CLI(Command Line Interface)
`cmd` 또는 `bash`를 통해 폴더와 파일을 만들고 접근하는 방법을 배움(**GUI와 비교**하며)  
간단하지만 강력한 명령어 모음  
   1. cd: change_directory, 폴더(디렉토리)를 이동할 때 쓰인다. GUI에서의 폴더 더블**클릭**과 동일한 기능을 함.
   `cd <디렉토리 명>` 또는 `cd ..` 의 형식으로 이동한다. 
   2. ls: list, 디렉토리의 파일 리스트를 모두 볼 때 쓰인다.
   `ls -a` 또는 `ls` 의 형식으로 쓰이며 `ls -a` 할 경우 .git 디렉토리도 식별할 수 있다.
   3. touch: 파일을 생성하는 명령어.
   `touch a.txt` 의 형식으로 쓰이며, 확장자를 꼭 명시해주어야 한다.
   4. mkdir: 디렉토리를 생성하는 명령어.
   `mkdir test_directory` 의 형식으로 사용됨. 디렉토리 생성은 반드시 `mkdir` 명령어를 사용해야 한다.  
   5. rm: 파일 또는 디렉토리를 삭제하는 명령어
   디렉토리의 경우 반드시 `rm -r <디렉토리 명>` 의 형식으로 지정해주어야 정상적으로 삭제가 진행된다.   
<br>

# git을 활용한 분산버전관리를 배우다!

   3가지 단계를 통한 **버전관리**
   - **Working Directory** -> *Staging Area* -> ~~Repository~~
   - `git add`: Staging Area(임시 저장소)로 이동
   - `git commit`: Staging Area에서 Local Repository(영구저장소)로 이동

        첫번째 커밋을 위해선 **Auth 정보**를 등록해야함!
   - `git status`:  .git 파일의 상태를 보여줌
   - `git commit --amend`: 갓! 찍은 커밋의 커밋 **메세지**만 수정할 때 필요한 커맨드. 수정하고 싶은 커밋 이후에 계속 *커밋이 쌓인 경우 수정하고 싶었던 커밋의 메세지는 수정이 불가능하다*.  
    VIM 에디터 진입 후
    ![](240711_git_markdown/2024-07-11-16-05-44.png) 
    I를 눌러 Insert Mode 진입
     ![](240711_git_markdown/2024-07-11-16-08-16.png)
    이후 commit 메세지를 수정하고 esc를 눌러 에디터 모드에서 나간 후 `:wq` 로 터미널 복귀.
    ![](240711_git_markdown/image.png)

<br>

# 240712 TIL

## 첫 번째 실습
   1. 새로운 폴더 생성 후 로컬 저장소 설정
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/6d4ad117-265f-4583-88a2-3ddab5a93b0a/Untitled.png?id=23482cbd-4656-46d3-8865-6f8654a4407f&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=dC4bKwfiggZYpJ_rufj9FVm7dll86H37Hn17lpRcoOg&downloadName=Untitled.png)
   2. commit 목록 생성
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/c0f2c829-fca2-4efe-859c-1d1d0cb54dc4/Untitled.png?id=a149dd8f-226d-4ba1-aa10-204c5b457425&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=w1r6aI8ZSnSQ1bcpiTDNoNL1O2sObN5onoCG7SdNuJ4&downloadName=Untitled.png)
   
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/198d9c9a-30db-4a5b-9683-0289af2117d0/Untitled.png?id=bc2f554c-564c-4aef-978c-2cb2fe2e85a3&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=OJUrBNYEw9xEtPi2EZvuxn56B9lu8vy57blFa7TauNg&downloadName=Untitled.png)
   3. 새로운 Github repository 생성
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/c8ac554d-64c6-495f-8c2b-306efccf61e2/Untitled.png?id=74d1be33-2cd0-41f3-a113-a328b38a529c&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=AdWSK1G3vspUslTviQpAVRLx6RtjSsvy9QKeJ-8Y5xU&downloadName=Untitled.png)
   4. 원격 저장소 추가
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/4ee5bd8d-d49d-4715-bf09-143c0595e278/Untitled.png?id=0bfd7654-a7e4-4cab-a100-6be48549dd73&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=YkgRWc5JPU4pGn18FXXKcw-TXcGQ48qlHi0zPeYnq1k&downloadName=Untitled.png)
   5. commit 목록 push
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/a81b66d1-945b-4188-a2de-df5c2182e342/Untitled.png?id=0b3c0ead-680c-41d6-aa21-71de4e13b466&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=9eZdPiQkrJjZuz5dN91b2JyUfiDGgc4mOQEj7guR24U&downloadName=Untitled.png)
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/7181076a-4d81-4f11-9365-969f32e41365/Untitled.png?id=ade02c50-bdbc-4b9f-bf19-33c6851f5eec&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=Fkdo3ZOtrFzwY2V9hNraEkSY4Mrut6DCkriFRDxDLZU&downloadName=Untitled.png)


## 두 번째 실습
1. 기존에 이미 origin을 지정한 로컬 저장소에 이어서 진행함
2. 새로운 Github repo 생성
   ![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/58d2db5b-26b7-46d4-bd38-3089be8a7693/Untitled.png?id=ad77244d-9419-4dfc-b931-2d015b83400b&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=RbaC2pfS8p_X7VfVShsORE0ycGnXmHdpL3o975W6d2c&downloadName=Untitled.png)
3. origin이 아닌 다른 이름(prime)으로 원격 저장소 추가
![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/9950003d-52de-45b2-a3f3-6e7ed693daf8/Untitled.png?id=f702d776-2f81-43e6-a5b9-89cf8e5953cc&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=fZwm8rjL4F57Nbf_RdMHPfXL0vTXduxTY-zwNBkCvS8&downloadName=Untitled.png)
4. commit 목록 생성
![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/68ed3c2d-e2c8-4147-b485-0046d3be24cd/Untitled.png?id=fe460b87-8107-44d9-bcb7-9edcb0c3ec8a&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=dNMUb5qSiEVVFJ3YMuO3StAo45oKBTqi7T0GG_Rbsrk&downloadName=Untitled.png)


## 세 번째 실습(끝말잇기)
1. 게임을 위한 repo 생성 및 README.md 초기 설정
![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/e77c8c3d-64e9-45ff-a031-f576510ae3d3/Untitled.png?id=4fa9a696-08ff-4f53-8171-442134b53dc9&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=adKcjlgvAKrZ5s4Mv4zvfaDMJrtCTSXihmskq_82TSo&downloadName=Untitled.png)
2. 게임의 상대방인 선생님이 2번째 응답을 입력하고 push 하려 하였으나 permission 관련 오류가 발생함!
![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/b93e7361-da1a-4a85-9414-298ce4175455/Untitled.png?id=a1f83a40-3a5b-4599-b6c2-d1faaa4f711a&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=DVgKVD2wcbYDqRds2XE9HV5T9A99qyWVTV1FxnQlSQY&downloadName=Untitled.png)
이 처럼 Collaborator를 설정해주면 push가 가능해짐!
3. 게임을 진행하는 과정
![이미지](https://file.notion.so/f/f/0e6f57f1-72bb-4512-9abe-ab1b43b05d2c/aaaed79c-0a21-4f3f-8aae-cc44cef44981/Untitled.png?id=cacbea74-6d88-4733-8cd7-7ce614d1bdc9&table=block&spaceId=0e6f57f1-72bb-4512-9abe-ab1b43b05d2c&expirationTimestamp=1720843200000&signature=nHKiwy1NxbSWCU1tdtK9EPQobAz56GRbR5Bl1NNtCaE&downloadName=Untitled.png)