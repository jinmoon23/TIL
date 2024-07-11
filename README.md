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
>> 이것은 인용문?!  

아아 이것은 수평선 이라는 것이다.  

---
# CLI(Command Line Interface)
- cmd 또는 bash를 통해 폴더와 파일을 만들고 접근하는 방법을 배움(**GUI와 비교**하며)
<br>
<br>

# git을 활용한 분산버전관리를 배우다!

   3가지 단계를 통한 버전관리
   - **Working Directory** -> *Staging Area* -> ~~Repository~~
   - `git add`: Staging Area(임시 저장소)로 이동
   - `git commit`: Staging Area에서 Local Repository(영구저장소)로 이동

        첫번째 커밋을 위해선 **Auth 정보**를 등록해야함!
   - `git status`:  .git 파일의 상태를 보여줌
   - `git commit --amend`: 갓! 찍은 커밋의 커밋 **메세지**만 수정할 때 필요한 커맨드. 수정하고 싶은 커밋 이후에 계속 커밋이 쌓인 경우 수정하고 싶었던 커밋의 메세지는 수정이 불가능하다.  
    VIM 에디터 진입 후
    ![](2024-07-11-16-05-44.png) 
    I를 눌러 Insert Mode 진입
    ![](2024-07-11-16-08-16.png)
    이후 commit 메세지를 수정하고 esc를 눌러 에디터 모드에서 나간 후 `:wq` 로 터미널로 복귀.
    ![alt text](image.png)
