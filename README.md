# 👾 pseudonymization_tool

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.3-blue" alt="version badge" width="120">
  <img src="https://img.shields.io/badge/license-AGPL--3.0-red" alt="license badge" width="150">
</p>

## 💻 pseudonymization_tool 사용법
1. (1) 가명처리 (2) 가명처리결합 중에 선택
2. 가명처리 파일의 경로를 입력
3. (1) 삭제 기술 or (2) 통계 도구 or (3) 일반화 기술(라운딩, 범주화..) 중에 선택

#### 삭제 기술: 단순, 부분, 행항목 삭제, 로컬 삭제, 마스킹 등이 있습니다. 
#### 통계 도구: 총계 처리, 부분 총계 등이 있습니다. 
#### 일반화 기술: 라운딩, 상하단코딩, 로컬 일반화, 범위 방법, 문자데이터 범주화, 단어끼리 묶기 등이 있습니다. 

### ➕Combine_jys.py

1. csv파일을 불러옵니다. (우클릭 경로 복사로 가져오기)
2. 데이터 키로 가져올 컬럼 선택. ex) 이름, 생년월일, 휴대폰전화 + 주의! 실제 csv파일에 있는 내용을 칼럼을 넣어야 함.
3. 가명키 생성.
4. 데이터 결합.
5. 결합된 csv 파일 저장.
