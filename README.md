<img src="https://user-images.githubusercontent.com/53360337/194005461-b4ef4138-d62d-442c-9e73-f20a5733a38e.png" width="300" height="300">

# Home Sketcher
- 서비스명 : Home Sketcher
- 팀 구성원 : 권혁림, 강승훈, 김진산, 윤영훈, 이슬기, 조경민 
- 개발 기간 : 2022.08.29 ~ 2022.10.07 (6주)
- 서비스 개요 : 가구 추천 및 배치 웹 서비스
- [Notion](https://chalk-care-a87.notion.site/HomeSketcher-f421e3df82ab4274ba15d4493df85bdb)

# 목차
[1. 프로젝트 진행 중 발생한 문제에 대한 고민 및 해결 과정](#0)

[2. 서비스 소개](#1)

[3. 시스템 아키텍처](#2)

[4. 개발 설정](#3)

[5. 기술 스택](#4)

[6. 프로젝트 산출물](#5)

[7. 데이터 출처](#6)


<br/>
<div id = '0'>

# 프로젝트 진행 중 발생한 문제에 대한 고민 및 해결 과정

<h2> 실시간 가구 추천 쿼리 최적화 </h2>

<br>

### 문제점
![image](https://github.com/seungh1024/Multi-Module-Board/assets/77014020/817dd342-07c0-4e20-862f-8452af120d3c)

<br>

- 위의 결과는 KNN 알고리즘만 사용한 결과입니다.  가구 추천을 위해 KNN 알고리즘을 사용하여 가구의 스타일과 색 선호도가 비슷한 사용자들의 pk를 찾아서 해당 pk를 기반으로 찾아본 가구, 좋아 요한 가구를 조회하는 쿼리를 사용했습니다. 그 결과 사용자가 10000명 이상부터 소요 시간이 급속도로 증가하는 문제가 있었습니다.
- 또한 선호도가 비슷한 사용자가 없을 경우 추천이 제대로 되지 않았고 이는 사용자 수가 적고 다양하지 않을 때 더욱 자주 발생했습니다.

<br>

### 고민

- 이렇게 응답 시간이 길어지면 단순 쿼리를 최적화하여 사용하는 것이 좋다는 생각이 들었습니다.
- 꼭 알고리즘을 사용하지 않더라도 사용자가 선호하는 스타일과 색에 대한 가구가 조회된다면 굳이 추천 알고리즘을 사용하지 않아도 된다고 생각했습니다.

### 해결

- 가구의 스타일, 색상, 다른 사용자들의 연령대, 성별별로 선호하는 가구 기반으로 각각 4종류의 데이터를 따로 쿼리를 날려 필터링했습니다. 이후 각각의 가중치별로 랜덤하게 데이터를 추출하여 응답했습니다.

### 배운점

- 특정 기술이 좋다고 무작정 사용하는 것이 아닌, 사용했을 때 어떤 이점이 있는지 잘 파악하고 사용해야 한다는 것을 알게 되었습니다.



<br/>
<div id = '1'>

# 서비스 소개

<h2> 맞춤 가구 추천 및 배치 모델링 서비스 </h2>

<br>

## 주요 기능
### 다크 모드
- 다크모드

![다크모드](https://user-images.githubusercontent.com/53360337/194351952-27176b14-e955-48b7-a7bd-cb745b6018a9.gif)

<br>

### 취향 분석
- 취향 분석

![취향분석](https://user-images.githubusercontent.com/53360337/194352305-c03ad8e9-a6f4-4aa9-a831-6df63eb94284.gif)

<br>

### 가구 추천
- 가구 추천

![가구 추천](https://user-images.githubusercontent.com/53360337/194352395-56873f54-1cdf-4009-8bf8-614a77a0bc3b.gif)

<br>

### 3D 모델링
- 방 그리기

![사각형 그리기](https://user-images.githubusercontent.com/53360337/194352471-7b4806a2-5958-419c-8a98-96eefbeb9e24.gif)

- 방 가구 추가

![가구 추가](https://user-images.githubusercontent.com/53360337/194352528-055de6a1-c8c6-4c3e-950b-7ff492ab7177.gif)

- 가구 이동 및 변환

![가구 변환](https://user-images.githubusercontent.com/53360337/194352577-cea7899d-9a8c-41b7-a18a-4b25a4544837.gif)

- 벽 변경

![벽 색상 변경](https://user-images.githubusercontent.com/53360337/194352653-33ad3995-49ea-4831-9204-8258bffa3d29.gif)

- 시점 변경

![가구 뷰 변경](https://user-images.githubusercontent.com/53360337/194352752-838386eb-75fb-492a-aa4e-0d9596cd4ef3.gif)

- 캡쳐

![캡쳐](https://user-images.githubusercontent.com/53360337/194352809-4d4cad0e-62b1-4325-9b96-9028676db41c.gif)

- 저장 및 불러오기

![저장 및 불러오기](https://user-images.githubusercontent.com/53360337/194352960-3ed567fa-ec83-47c5-88ba-d743badbc891.gif)

<br>

### 이미지 스타일 분석 (Beta)
- 스타일 분석

![앤틱 이미지 검사](https://user-images.githubusercontent.com/53360337/193837665-a3088e60-31e4-4d2d-9863-4f759ea36c31.gif)

- 나이별 스타일

![나이별 스타일](https://user-images.githubusercontent.com/53360337/193837821-66722c66-d49f-4e06-8347-e2aaf3fba2b5.gif)

- 나이별 컬러

![나이별 컬러](https://user-images.githubusercontent.com/53360337/193837781-e7917878-d1f4-45ac-9b50-b7d5964523ce.gif)

- 성별별 스타일

![성별별 스타일](https://user-images.githubusercontent.com/53360337/193837744-6adab978-a4f3-4bc6-ae76-99618f8da237.gif)

- 성별별 컬러

![성별별 컬러](https://user-images.githubusercontent.com/53360337/193837711-b5f1efb8-e6f8-49ec-b176-d8b8cd8faae9.gif)


<div id = '2'>

<br>

# 시스템 아키텍처
![image](https://user-images.githubusercontent.com/53360337/193612741-8d4d745f-f230-4f2a-a97c-02b06d07a690.png)

<div id = '3'>

## 개발 설정

### 서비스별 포트 번호

| 구분 | 포트번호 |
| --- | --- |
| Jenkins | 8080 |
| Dhabgi | 8081 |
| React | 8002 |
| FastAPI | 8003 |
| MySQL | 3306 |
| Redis | 6379 |

<br>
    
### Dockerfile

```
# BE/Dockerfile (Django)

From python:3.9.4
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN apt-get -y install vim 
RUN mkdir /srv/docker-server
ADD . /srv/docker-server 
WORKDIR /srv/docker-server 
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt 
EXPOSE 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
```

```
# houseketcher/Dockerfile (React)

FROM node:16.15.0 as build-stage
WORKDIR /app
COPY package*.json ./
COPY package-lock.json ./
RUN npm install
COPY . .
RUN npm run build
FROM nginx:stable-alpine as production-stage
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build-stage /app/build /usr/share/nginx/html 
EXPOSE 8002
CMD ["nginx", "-g","daemon off;"]

```

```
# fastapi/Dockerfile (React)

FROM python:3.10
RUN apt-get -y update
RUN apt-get -y install vim 
RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt 
COPY . /app
EXPOSE 8003

```

### Docker-Compose.yml

```
version: "3.8"
services:
  react:
    container_name: homesketcher-react
    build: ./housesketcher/
    restart: on-failure
    volumes:
      - ./housesketcher/nginx/:/etc/nginx/conf.d/
    ports:
      - 8002:8002
 
 
  redis:
    container_name: redis
    image: redis:7-alpine
    ports:
      - 6379:6379
    command: redis-server --save 20 1 --loglevel warning --requirepass eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81
    volumes:
      - /redis/data:/data
      - /redis/conf/redis.conf:/usr/local/conf/redis.conf
 
  mysql:
    container_name: mysql
    image: mysql:latest
    restart: unless-stopped
    environment:
      - MYSQL_ROOT_PASSWORD=clsfurtkanth
      - MYSQL_DATABASE=ssafy
      - MYSQL_USER=ssafy
      - MYSQL_PASSWORD=clsfurtkanth
    ports:
      - 3306:3306
```

### Jenkins 설정 파일

```
pipeline {
    agent any
 
 
    stages {
        stage('Prepare') {
            steps {
                sh 'echo "Clonning Repository"'
                git branch: 'deploy',
                    url: 'https://lab.ssafy.com/s07-bigdata-recom-sub2/S07P22B304.git',
                    credentialsId: 'homesketcher'
            }
            post {
                success {
                     sh 'echo "Successfully Cloned Repository"'
                 }
                 failure {
                     sh 'echo "Fail Cloned Repository"'
                 }
            }
        }
 
 
        stage('Docker stop'){
            steps {
                dir('BE'){
                    sh 'echo "Docker Container Stop"'
    //              도커 컴포즈 다운
                    // sh 'curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose'
    //              해당 도커 컴포즈 다운한 경로로 권한 설정
                    // sh 'chmod -R 777 /usr/local/bin'
                    // sh 'chmod +x /usr/local/bin/docker-compose'
    //              기존 백그라운드에 돌아가던 컨테이너 중지
                    sh 'docker compose stop'
                }
 
 
            }
            post {
                 failure {
                     sh 'echo "Docker Fail"'
                }
            }
        }
 
        stage('RM Docker'){
            steps {
                
                sh 'echo "Remove Docker"'
 
                //정지된 도커 컨테이너 찾아서 컨테이너 ID로 삭제함
                sh '''
                    result=$( docker container ls -a --filter "name=homesketcher*" -q )
                    if [ -n "$result" ]
                    then
                        docker rm $(docker container ls -a --filter "name=homesketcher*" -q)
                    else
                        echo "No such containers"
                    fi
                '''
 
                // homesketcher로 시작하는 이미지 찾아서 삭제함
                sh '''
                    result=$( docker images -f "reference=homesketcher*" -q )
                    if [ -n "$result" ]
                    then
                        docker rmi -f $(docker images -f "reference=homesketcher*" -q)
                    else
                        echo "No such container images"
                    fi
                '''
 
                // 안쓰는이미지 -> <none> 태그 이미지 찾아서 삭제함
                sh '''
                    result=$(docker images -f "dangling=true" -q)
                    if [ -n "$result" ]
                    then
                        docker rmi -f $(docker images -f "dangling=true" -q)
                    else
                        echo "No such container images"
                    fi
                '''
 
            }
            post {
                 failure {
                     sh 'echo "Remove Fail"'
                }
            }
        }
 
        stage('Bulid & Run') {
            steps {
                dir('BE'){
                    sh 'echo " Image Bulid Start"'
                    script {
 
//                         업데이트된 코드로 빌드 및 실행
                        sh 'docker compose up -d'
                    }
                }
            }
 
            post {
                failure {
                    sh 'echo "Bulid Docker Fail"'
                }
            }
        }
    }
}

```

### Nginx 설정 파일(certbot 인증서 발급 필요)

```
server {
    listen 80;
    server_name j7b304.p.ssafy.io;

    location / {
        return 308 https://$host$request_uri;
    }

}

server {
    listen 443 ssl;
    server_name j7b304.p.ssafy.io; # 도메인으로 변경

    ssl_certificate /etc/letsencrypt/live/j7b304.p.ssafy.io/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/j7b304.p.ssafy.io/privkey.pem;


    location  / {
        proxy_pass http://localhost:8002;
    }

    location /api/v1/{
        proxy_pass  http://127.0.0.1:8001/api/v1/;
        proxy_set_header  X-Forwarded-Protocol  $scheme;
    }


}

```


<br>

<br>

<div id = '4'>

# 기술 스택
<div align=center></div>

<div align=center> 
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> 
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white"> 
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=Numpy&logoColor=white">
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white">
  <img src="https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white">
  <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white">
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white">

  <br>

  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white">
  <img src="https://img.shields.io/badge/Three.js-000000?style=for-the-badge&logo=Three.js&logoColor=white">
  <img src="https://img.shields.io/badge/Axios-5A29E4?style=for-the-badge&logo=Axios&logoColor=white">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">

  <br>

  <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=white">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white"> 
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white"> 
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=Firebase&logoColor=white"> 

  <br>

  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"> 
  <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=Jenkins&logoColor=white"> 
  <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white">

  <br>

  <img src="https://img.shields.io/badge/GitLab-FC6D26?style=for-the-badge&logo=GitLab&logoColor=white"> 
  <img src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white">
  <img src="https://img.shields.io/badge/Mattermost-0058CC?style=for-the-badge&logo=Amazon EC2&logoColor=white">

  <br>
</div>
<br>

## 기술스택 및 버전 상세

| 구분       | 기술스택                    | 상세내용                 | 버전          |
| -------- | ----------------------- | -------------------- | ----------- |
| 공통     |                     |                |         |
|          | 형상관리                    | Gitlab               | \-          |
|          | 이슈관리                    | Jira                 | \-          |
|          | 커뮤니케이션                  | Mattermost   | \-          |
|          | 커뮤니케이션                  | Notion   | \-          |
| Server   |                       |             |          |
|          | 서버                      | AWS EC2              | \-          |
|          | 플랫폼                     | Ubuntu               | 20.04         |
|          | 배포                      | Docker               | 20.10.17         |
|          | 배포                      | Docker Compose              |  2.6.0         |
|          | 배포                      | Jenkins              | 2.346.2          |
|          | 배포                      | Nginx              | 1.23.1         |
| BackEnd  |                      |                 |        |
|         | DB                      | MySQL                | 8.0.30         |
|         | DB                      | FireBase             | -         |
|          | Cache Storage           | Redis              | 7-alpine         |
|          | Python                    |                  | 3.9.4   |
|FastAPI          |                     |                  |    |
|          | Python                    |                  | 3.10   |
|          | Numpy                    |                  | 1.23.3   |
|          | Pandas                    |                  | -   |
|          | Keras                    |                  | 2.10.0   |
|          | Tensiflow                    |                  | 2.10.0   |
| FrontEnd |                    |                      |          |
|          | HTML5                   |                      | \-          |
|          | CSS3                    |                      | \-          |
|          | JavaScript(ES6)         |                      |\-           |
|          | React         |                      |  18.2.0       |
|          | Three.js         |                      | 0.144.0       |
|          | Build                   | Node               | 16.15.0        |
| IDE          |   Visual Studio Code                   |   |1.70.0          |

<br>

<div id = '5'>

# 프로젝트 산출물
- 세부 내용 : 노션 참조

<br>

## 시나리오

<img width="2811" alt="시연 시나리오 (2)" src="https://user-images.githubusercontent.com/53360337/194444031-e706b336-d1de-410c-9c90-0e827f355ba0.png">

<br>

## 기능 명세서
![image](https://user-images.githubusercontent.com/53360337/193490074-30c4e3de-e4d9-4e94-a36f-c789c0291fb2.png)

<br>

## ER-Diagram
![HomeSketcherErd (5)](https://user-images.githubusercontent.com/53360337/193612554-d9889d7b-0f0e-4329-8850-5f0896dc14ae.png)

<br>

## API 명세서
![image](https://user-images.githubusercontent.com/53360337/193490144-59334550-0d48-4fe6-8cd1-9264ca403bf7.png)

<br>

## 화면설계서
[화면설계서 - Figma](https://www.figma.com/file/thfT2MjPKNG0m5CTJXEjLT/%EC%9D%B8%ED%85%8C%EB%A6%AC%EC%96%B4%EC%B6%94%EC%B2%9C?node-id=0%3A1)

<br>

## EC2 포트

| 구분       | 포트번호                    | 
| -------- | ----------------------- |
| Jenkins         |  8080                | 
| Django         | 8081                    | 
| React         |  8002               | 
| FastAPI         |    8003              | 
| MySQL         |     3306             | 
| Redis         |   6379               | 

<br>

<div id="6">

# 데이터 출처
- 가구 Data : ikea-api 2.0.6
- OBJ Data : Alibaba - 3D-FUTURE: 3D Furniture Shape with Texture
