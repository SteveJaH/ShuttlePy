<div align="center"><img src="https://github.com/SteveJayH/ShuttlePy/blob/master/image/shuttlepy.png" height="150px"/></div>

<h2 align="center">ShuttlePy: Shuttle enroll macro for Yonsei Univ.</h2>

<p align="center"> <a href="https://www.codacy.com/gh/SteveJayH/ShuttlePy/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SteveJayH/ShuttlePy&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/2afcd0c32b0a49c49e96e1d0db33057c"/></a> </p>

**연세대학교 신촌 캠퍼스와 국제(송도) 캠퍼스 간 왕복 셔틀버스 신청 매크로.** 2020년 졸업하여 업데이트는 어려울 것 같습니다. :cry: 프로그램이 "신청이벤트"를 바로 전달하는 것이 아니라 버튼을 찾고 "클릭이벤트"를 전달하기 때문에 느립니다. 경쟁률 높은 건 못 잡을 수 있어요. \
**Macro for enrolling Shuttle bus for Yonsei University** (Shinchon, International Campus). Read Readme plz.

## How to Use

### 1-Reserv.txt 파일을 여세요. Open Reserv.txt
[연세포탈](https://www.portal.yonsei.ac.kr) ID, PW를 입력하세요. 코드를 보시면 알겠지만 '개발자'에게 사용자의 개인정보를 전송하는 등의 '불법적'인 일은 수행되지 않습니다. 코드를 볼 줄 안다면 코드를 읽어보시고 모르신다면 파이썬 수업을 들은 친구들한테 물어보세요.\
Put your ID, password of [Yonsei portal](https://www.portal.yonsei.ac.kr). There is no 'special illegal thing' for acquiring your ID and password, such that sending your ID and PW to 'me'. Don't worry about that.

### 2-질문들을 잘 읽고 채워넣으세요 Read Shuttle information and fill it
#### 1) 일주일에 몇 번의 셔틀 버스를 타는지(원하는지) How many shuttle do you want in one week
#### 2) 각각의 셔틀에 대해서 '요일', '방향', '시간' 3개를 입력해야 해요 You have to select 3 numbers for each shuttle, 'Day of the week', 'Direction' and 'Time'

##### 아래 표 참고해서 요일을 숫자로 바꿔서 Day of the week as number
Mon --- Sun \
0 1 --- 5 6

##### 방향을 숫자로 Direction (Shinchon to International, International to Shinchon)

##### 시간표(Reserv_txt에 있어요)을 숫자로 Time table

## Example
There is an example for Reserv.txt. You may copy and rename it to get help. Actual name of text which will used in python code must be "Reserv.txt".

## Issues
2020년에 졸업하여 확인하기는 어렵고 이슈가 발생하면 [Issues](https://github.com/SteveJayH/ShuttlePy/issues)에 올려주세요. 수정해보거나 본인이 수정하여 올려주셔도 좋습니다.

## License
복사, 수정, 개인적 사용을 허용하지만 상업적 이용(할 가치가 적지만), 배포를 금합니다.

## Legal
연세대학교 학칙상, 정보통신망법상 매크로, 특히 셔틀버스 신청 매크로는 불법이라고 보기 어렵습니다. 그러나 매크로를 사용하는 것은 여러 가지 관점에서 문제가 있어 보입니다. \
이 ShuttlePy는 **성능이 좋지 못하고**(높일 수 있습니다. 도전해보세요) Python 기반 Crawling, Selenium을 **공부해보고 재밌는 프로젝트를** 위해서 만들어봤습니다. 이로 인해 문제가 발생하지 않길 바랍니다.\
[정보통신망법을 고려하고 매크로 프로그램 개발, 유포자 무죄 확정 기사](https://www.legaltimes.co.kr/news/articleView.html?idxno=50251)\
[연세대학교 시간표 수강 신청을 다룬 Medium 블로그 포스트](https://medium.com/@whj2013123218/%EC%88%98%EA%B0%95-%EC%8B%A0%EC%B2%AD-%EB%B0%8F-%ED%8B%B0%EC%BC%80%ED%8C%85-%EC%84%B1%EA%B3%B5%EC%9D%84-%EC%9C%84%ED%95%9C-tip-%EB%B0%8F-python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8-facc9107abc7)
