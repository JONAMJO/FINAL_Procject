# Final_Project

### :movie_camera: 영화 추천 서비스



### 1. 프로젝트 소개

------

##### 목표

>- 영화 추천 서비스 구현
>
>- HTML/CSS, Django, Database, Javascript(Vue.js) 등을 활용한 실제 서비스 설계
>- Git을 통한 소스코드 버전 관리 및 협업
>- 서비스 배포



### 2. 팀원 정보 및 개발 분담 내역

------

##### 팀명

> JONAMJO

#####  팀원

> 남승현, 조현호

#####  개발 분담 내역

> 공통
>
> - 기획, 데이터 모델링
>
> 남승현
>
> - Users App 구현, Vue.js 비동기화, 서비스 디자인
>
> 조현호
>
> - 데이터 시딩, Movies App 구현, Nav bar 구현



### 3. 핵심 기능 및 서비스

------

#### 데이터

#####  사용자 인증 및 사용자 정보

> 로그인, 로그아웃은 Django에 내장된 기능을 활용하여 구현
>
> 회원가입, 회원정보는 커스터마이징하여 구현

#####  영화 DataBase
> 영화 레코드 50개 이상 저장



#### 기능

#####  관리자 권한
> Django에 내장된 admin site와 superuser 기능을 활용

#####  추천 기능

> 메인 페이지 최상단에 userRating을 기준으로 가장 높은 순으로 영화가 소개됨
>
> 유저 상세 페이지에서 유저가 '좋아요'를 누른 영화를 보여줌
>
> 유저 상세 페이지에서 자신이 '팔로우'한 유저가 좋아요를 누른 영화를 보여줌

#####  영화 상세 페이지

> 영화의 상세 페이지에서 각 영화의 포스터 이미지 및 세부 정보, 배우 이미지를 확인할 수 있음
>
> 리뷰 등록 및 등록된 리뷰, 사용자 평점이 나열됨

#####  유저 영화 평가
> 평가 등록 및 자신이 작성한 평가의 수정, 삭제가 가능

#####  데이터 유효성 검사 및 에러 페이지
> Django에 내장된 기본 메소드, 데코레이터 등을 활용



### 4. 데이터베이스 모델링

------

##### User

> 사용자

```
followers - 팔로우
```

##### Movie

> 영화

```
title - 제목
title_en - 제목 영문
poster_url - 포스터 이미지
open_date - 개봉일자
audience - 관객수
show_time - 상영시간
user_rating - 평점
nation - 국가
watch_grade - 시청연령
description - 설명
like_users - 좋아요
genre - 장르
director - 감독
actor - 배우
```

##### Review

> 사용자가 영화에 남긴 리뷰

```
movie - 영화
score - 평점
review - 리뷰
user - 작성자
```

##### Genre

>장르

```
name - 장르명
```

##### Cast

> 배우

```
movie - 출연 영화
peopleNm - 배우 이름
peopleNmEn - 배우 이름 영문
cast - 역할
castEn - 역할 영문
img_url - 배우 사진
```



### 5. 목표 서비스 구현 및 실제 구현 정도

------

구현

- 좋아요 기능, 비동기화
- 팔로우 기능, 비동기화
- 평점이 높은 영화 추천
- 팔로우한 사람들이 좋아요 누른 영화 표시

구현 못함

- 해시태그 기능

* 영화 별 트레일러
* 감독, 배우 상세 페이지


- 리뷰 비동기화



### 6. 결과 화면

----

메인 페이지

![캡처1](https://user-images.githubusercontent.com/52685280/69832693-1e78e580-1273-11ea-8ca2-9ad804f9b902.PNG)

회원가입

![캡처2](https://user-images.githubusercontent.com/52685280/69832695-23d63000-1273-11ea-8fdc-6113368c73ab.PNG)

로그인

![캡처3](https://user-images.githubusercontent.com/52685280/69832696-259ff380-1273-11ea-950e-742fc3f37f92.PNG)

회원정보 수정

![캡처4](https://user-images.githubusercontent.com/52685280/69832698-28024d80-1273-11ea-8bc4-3e8ff601d9c2.PNG)

비밀번호 변경

![캡처5](https://user-images.githubusercontent.com/52685280/69832704-2c2e6b00-1273-11ea-9990-2d39927f9da0.PNG)

추천 영화

![캡처6](https://user-images.githubusercontent.com/52685280/69832722-30f31f00-1273-11ea-896a-431a1c6b78d5.PNG)

영화 목록

![캡처7](https://user-images.githubusercontent.com/52685280/69832724-32bce280-1273-11ea-9366-e16aea350b0d.PNG)

영화 상세 페이지

![캡처8](https://user-images.githubusercontent.com/52685280/69832730-35b7d300-1273-11ea-91d3-87f2a4c9390d.PNG)

리뷰 작성 전

![캡처9](https://user-images.githubusercontent.com/52685280/69832750-4700df80-1273-11ea-9094-af188cb047f8.PNG)

리뷰 작성 후

![캡처10](https://user-images.githubusercontent.com/52685280/69832752-49633980-1273-11ea-90d7-28cb32e7525e.PNG)

사용자 프로필 페이지

![캡처11](https://user-images.githubusercontent.com/52685280/69832738-3ea8a480-1273-11ea-9354-5f8f3ce6c881.PNG)

영화 검색 결과

![캡처12](https://user-images.githubusercontent.com/52685280/69832741-41a39500-1273-11ea-9285-552c7b170ed5.PNG)



### 7. 배포 사이트

----

http://ssafy-jomajo.ymy57v3p2g.ap-northeast-2.elasticbeanstalk.com/



### 8. 느낀점

------

#####  :heavy_check_mark: 남승현

- 데이터 모델을 여러차례 수정하면서, 데이터 수집에 많은 시간이 할당된 점이 아쉬웠다. 어떤 데이터를 수집할 것인가에 대한 계획이 무엇보다 중요한 것 같다.
- 팔로우랑 팔로워의 기본적인 구조를 이해하지 못해, 코드를 작성하는 부분에서 시간이 걸렸다, 
- 영화디자인에 맞는 배경화면과 navbar를 선택하는 것에 고민을 많이 했다.
- 일반적인 사진을 보여주는 것보다, hover 효과를 부여하니 시각적인 부분에서 개선이 되었다. 추천된 영화를 보여주는 carousel 부분의 hover효과와 여러 영화 목록을 보여주는 곳의 hover효과를 다르게 주었다.
- 처음 home화면에서 조건에 맞는 추천 영화에 carousel효과를 주었을 경우, 처음 active되는 공간에 넣는 조건이 까다로웠다. 이 부분은 영화를 선택한다는 사진을 따로 개별적으로 추가함으로써 해결하였다.
- 검색기능을 추가할 시 vue를 활용해 추가를 할 예정이었지만, vue를 다루는데 익숙하지 않아, 입력한 글좌와 Movie의 변수와 비교해서 추출하는 것으로 대체하였다.



#####  :heavy_check_mark: 조현호

- 데이터 수집을 하면서 여러 정보를 가져오려다 보니 처음 작성한 모델을 여러번 수정하게 되었고, 가져온 데이터가 리스트가 아닌 문자열로 되어 있어 출력이 안되어 데이터 구조를 변경하게 되었다.
- 메인 페이지에서 어떤 형식으로 영화 포스터를 보열줄지 고민을 많이 했고, 디자인적으로 수정하는데 시간이 많이 걸렸다.
- Navbar에 위치한 검색창과 영화 디테일 페이지의 리뷰를 Vue를 사용하여 비동기화 할 목표였으나, Vue를 다루는데 어려움이 많아 필요한 데이터를 가져와 출력하는 방식으로 변경이 있었다.
- 배포 서비스를 처음 사용해봤는데 생각보다 기다리는 시간이 좀 걸리고 하는 방법도 익숙하지 않았다.



