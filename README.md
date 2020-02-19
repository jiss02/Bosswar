
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://user-images.githubusercontent.com/42693808/70032692-51afd180-15f1-11ea-899e-dbdede5c70fa.png" alt="Logo" width="250" height="230">
  </a>
  <h3 align="center">누구나 보스가 될수있다, 보스대전</h3>
  <p align="center">
    다양한 주제로 경쟁하며 1위를 가려내는 대전 서비스 <br/>
    <br />
   </p>

&nbsp;
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [Details](#details) 
  * [Deploy](#deploy)
  * [Links](#links)
  * [Demo](#demo)
 * [Contanct](#contact)

&nbsp;
<!-- ABOUT THE PROJECT -->

## About The Project

<div align="center">
<br/>
멋쟁이 사자처럼 2019년도 여름 해커톤 프로젝트 <br/>
    <b>누구나 보스가 될수있다, 보스대전</b>
</div>



"아.. 이런 대회가 있다면 내가 일등할 수 있는데.." 라는 생각해보신적 있으신가요? "보스대전"은 이런 생각으로부터 시작하여 만들어진 서비스입니다. 

지우개똥 크게만들기, 누가 가장 특이한 웃음소리를 내는 지와 같은 사소한 것들이 대회 주제가 됩니다. 이미지와 유튜브 영상을 이용해 자신이 가장 뛰어나다는 것을 보여주세요! 유저들의 투표에 따라 공정한 심사가 이루어집니다. 어떤 사소한 것이라도 누구나 보스가 될 수 있습니다. 



### What is the bosswar?

가입시 500 포인트가 증정되며, 대회에 참가하기위해 게시글을 쓸 떄 500포인트가 차감됩니다. 해당 대회에 쌓인 포인트는 1등에게로 돌아가며, 해당 포인트는 현금화가 가능합니다.
> 무한 투표를 방지하기 위해 대회에 참여한 사람만 투표가 가능하게 설계하였습니다.

&nbsp;
### Built With

* Python Django
* HTML5 + CSS3 + Javascript
* SQLite3

&nbsp;
<!-- GETTING STARTED -->
## Getting Started



### Prerequisites

Setup project environment with [venv](https://docs.python.org/3/library/venv.html) and [pip](https://pip.pypa.io).

* setting venv
```bash
$ python -m venv venv
$ . venv/Scripts/activate
```

* Django
```bash
$ pip install django
```


&nbsp;
### Requirements
```
Babel==2.7.0
certifi==2019.6.16
chardet==3.0.4
defusedxml==0.6.0
dj-database-url==0.5.0
Django==2.2.3
django-bootstrap4==0.0.8
django-phonenumber-field==3.0.1
gunicorn==19.9.0
idna==2.8
phonenumbers==8.10.14
Pillow==6.1.0
psycopg2-binary==2.8.3
PyJWT==1.7.1
python3-openid==3.1.0
pytz==2019.1
requests==2.22.0
six==1.12.0
sqlparse==0.3.0
urllib3==1.25.3
whitenoise==4.1.3
```
&nbsp;
### Installation

1. Clone the repo
```sh
$ git clone https://github.com/jiss02/Bosswar.git
```
2. Migrate Database
```sh
$ python manage.py migrate
```
3. Create config folder and key.json

```sh
$ mkdir config
$ cd config
$ vim key.json
```

4. Run server

```
$ python manage.py runserver
```

## Details 

### Deploy
* Heroku
&nbsp;
### Links
* Project Link: https://github.com/jiss02/Bosswar.git
* Website Link: [https://bossofwar.herokuapp.com](https://bossofwar.herokuapp.com)
&nbsp;
### Demo



<div align="center">

| main 1 | main 2 |
| :---: |:---:|
| <img width="380" height="710" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032577-0bf30900-15f1-11ea-9223-db9e7894254e.jpg"> | <img width="380" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032569-0ac1dc00-15f1-11ea-8fcb-340a11f596ce.jpg"> |
| about | detail |
| <img width="380" height="710" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032571-0ac1dc00-15f1-11ea-845a-4906fc556de8.jpg"> | <img width="380" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032576-0b5a7280-15f1-11ea-9b5e-8af88911b233.jpg"> |
| idea board | winners |
| <img width="380" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032572-0ac1dc00-15f1-11ea-8246-bff83f1f2248.jpg"> | <img width="380" height="710" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032573-0b5a7280-15f1-11ea-9974-e28112103c41.jpg"> |
| my page | ... |
| <img width="380" alt="스크린샷 2019-11-08 오전 3 35 40" src="https://user-images.githubusercontent.com/42693808/70032575-0b5a7280-15f1-11ea-8b5a-764dd8e60b8b.jpg"> | ... |

</div>


