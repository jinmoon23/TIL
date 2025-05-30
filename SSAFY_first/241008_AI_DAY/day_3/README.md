# Day_3

## 최근에 왜 많이 활용될까?
1. CPU(직렬 데이터 처리) -> GPU(병렬 데이터 처리) -> 접근성이 높아짐
2. 데이터가 많아짐과 동시에 데이터 처리 기술이 활성화됨
3. 적절한 알고리즘이 많이 개발됨
4. 알렉스넷(Model Architectures)이 등장해 뉴럴 네트워크의 효용성을 입증함
  - 더 좋은 활성화함수(ReLU)의 개발
  - CNN(합성곱 신경망)모델

## ResNet(2016)
특징
   1. Residual Connection: 입력 값을 그대로 더해주면서 초기 정보를 잃지 않게 함 -> 현재의 GPT 같은 느낌
   2. 레이어가 많아질수록 성능이 더 향상되는 것을 증명 -> Over Fitting 걱정 안해도 된다!

## EfficientNet(2019)
특징
  1. ResNet과 비슷하게 깊이가 깊어질수록 성능 향상
  2. 업스케일링 계속해~~
  3. FLOPS -> 모델 성능 평가모델 -> 업스케일링 하면 할수록 더 높은 성능을 보여줌
결론
- 깊이 / 너비 / 이미지 해상도 `모두 키우는 것이 가장 성능이 좋다.`(아직까지 Over Fitting은 없다!)

## Unet(2015)
- Segmentation: 이미지 내에 있는 객체들을 분할하는 작업
- image segmentation 알고리즘 중 특징적인 알고리즘 모델
- 굉장히 좋은 성능을 보여줌 -> 세포 분석과 의료 영상 분야에서 많이 사용됨

## CNN Segmentation Model
- Defusion

## 인코더와 디코더
인코더: 입력 -> 압축된 특징
디코더: 압축된 특징 -> 출력
