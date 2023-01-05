# text_classification
yelp data semantic classification

<p align="center">
  <br>
  <img src="./images/common/logo-sample.jpeg">
  <br>
</p>

목차

## 프로젝트 소개

<p align="justify">
프로젝트 개요/동기
</p>

<p align="center">
GIF Images
</p>

<br>

## 기술 스택

|   Python   |   Pytorch  |  Pandas  | Matplotlib |
| :--------: | :--------: | :------: |   :-----:  |
|    ![py]   |   ![pt]    |   ![pd]  |   ![mtpt]  |

<br>

## 성능을 높이기 위한 방법

### 다양한 모델 사용 -> HARD VOTING

Albert , Electra , Roberta , Distilbert , GPT-2, T5 등 많은 모델을 TRAIN 해보았다.

결과를 모아서 hard voting했다.

### 불용어 제거, 특정 토큰 제거

전처리 과정에서 불용어를 정제하고 test file에서 사용하지 않는 __num__ 토큰을 제거했다.

### hyper parameter tuning

wandb framework로 batch_size, learning_rate , the number of epochs 의 최적값을 찾았다.

<br>

## 배운 점 & 아쉬운 점

버그를 해결한  baseline의 accuracy가 98.1로 꽤 높았다. 여기서 성능을 1프로 올리는게 매우 힘든일 이었다. 


1. 많은 모델들을 train하고 이를 ensemble했다. 

ensemble 방법 중 하나인 hard voting은 성능을 꽤 올려주었다. 

voting하기전 각 모델이 예측한 결과를 비교해 보았다.

98.7% 의 accuracy를 기록한 roberta모델도 

사람이 보았을 때 pos, neg를 쉽게 구분할 수 있는 문장이지만 모델은 이를 제대로 구분하지 못한 경우가 있었다.

이런 문장을 다른 모델이 해결해 주었고 최종적으로 99.0%의 정확도를 얻을 수 있었다.



1. 데이터의 비대칭성을 해결하기 위해 전처리를 했다. 

하지만 좋은 성능을 내지 못했다. 



3. wandb를 이용해 hyper parameter tuning을 하였다.

얀 르쿤 선생님이 NLP task에서 batch size는 32가 적당하다고 했지만.

모든 모델에서 동일하게 batch size를 키웠을때 lowest_validation_loss가 작아졌다.


위 3가지 방법 말고도 train set 과 validation set을 여러번 교차 검증하는 k-fold validation을 시도해 보고 싶었다.
시간이 문제였다. 기본 baseline code가 어덯게 동작하는지 이해하는데 주어진 5일 중 절반 가까이 사용했다.

NLP task pretrained model을 어덯게 fine tuning하는지 기본적인 파이프라인을 이해했다.

text classification 말고도 다른 task가 주어지더라도 잘 해낼 수 있을 것이다.

<p align="justify">

</p>

<br>

<!-- Stack Icon Refernces -->
|    ![py]   |   ![pt]    |   ![pd]  |   ![mtpt]  |
[py]: /images/stack/javascript.svg
[pt]: /images/stack/typescript.svg
[pd]: /images/stack/react.svg
[mtpt]: /images/stack/node.svg

