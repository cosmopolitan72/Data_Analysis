import pandas as pd

# Lap 1. 가명 처리
kpass_file_path = 'C:/Users/mjeon/OneDrive/바탕 화면/가명처리 대회/K패스_이용내역.csv'
kpass_df = pd.read_csv(kpass_file_path, encoding='utf-8') 

#Lap1 가명 처리- Task 1 삭제 기술- 1. 컬럼 삭제
kpass_df.drop(['휴대폰 번호'], axis=1, inplace=True)
# 구현: 삭제 종류를 선택하고 항목을 입력받아 항목 지우기

#Lap1 가명 처리- Task 1 삭제 기술- 2. 부분 삭제 (생년월일 뒷자리 제거)
kpass_df['생년월일_부분삭제'] = kpass_df['생년월일'].astype(str).str.slice(0, 4) + '****'
# 구현: 삭제 종류를 선택하고 항목 입력받아 입력받은 타입을 가지고 치환

#Lap1 가명 처리- Task 1 삭제 기술- 3. 행 항목 삭제
#행 항목 삭제 전 행 기수 저장
before_count =len(kpass_df)

#1회 등장한 읍면동 삭제 로직
dong_counts = kpass_df['주민등록상 행정구역'].value_counts()
unique_dongs = dong_counts[dong_counts == 1].index
print(unique_dongs)

kpass_df = kpass_df[~kpass_df['주민등록상 행정구역'].isin(unique_dongs)]

# 행 항목 삭제 후 개수 저장
after_count = len(kpass_df)

# 삭제된 행 수 계산
deleted_rows = before_count - after_count
print(f"삭제된 행 수: {deleted_rows}")

# Lap1 가명 처리- Task 1 삭제 기술- 4. 로컬삭제 - 특이종보를 해당 행 항목에서 삭제
# 1. 연령 상위 1%값 파악
threshold_99 = kpass_df['연령'].quantile(0.99)
print(f"99% 분위수 (상위 1% 컷오프): {threshold_99}")
# 2. 조건 필터링
top_1_percent_df = kpass_df[kpass_df['연령'] >= threshold_99]
# 3. 결과 확인
print(f"상위 1% 행 개수: {len(top_1_percent_df)}")
print(top_1_percent_df)
# 4. 예: 연령이 너무 많은 사람의 주소만 삭제 (로컬 삭제)
kpass_df.loc[kpass_df['연령'] > threshold_99, '주민들록상 행정구역'] = None
kpass_df[kpass_df['주민들록상 행정구역'].isnull()]

'''
# Lap1 가명 처리- Task 1 삭제 기술- 1. 마스킹
# 휴대폰번호 중간 마스킹: 010-1234-5678 → 010-****-5678
def mask_phone(phone):
    phone = str(phone)
    return phone[:4] + '****' + phone[-4:] if len(phone) >= 11 else phone

kpass_df['휴대폰번호_마스킹'] = kpass_df['휴대폰 번호'].apply(mask_phone)
'''

# Lap1 가명 처리- Task2 통계도구
# Lap1 가명 처리- Task2 통계도구- 1. 통계 처리
# 1. 평균값, 최소값, 최대값, 중앙값, 최빈값 계산
mean_value = kpass_df['적립금액'].mean()
min_value = kpass_df['적립금액'].min()
max_value = kpass_df['적립금액'].max()
medium_value = kpass_df['적립금액'].median()
mode_value = kpass_df['적립금액'].mode()[0] # 여러 최빈값중 첫 번째

print("평균값: ", mean_value)
print("최소값: ", min_value)
print("최대값: ", max_value)
print("중앙값: ", medium_value)
print("최빈값: ", mode_value)

# 적립금액별 빈도 계산 (groupby + size)
mode_freq = (
    kpass_df.groupby('적립금액')
    .size()
    .reset_index(name='빈도')
    .sort_values(by='빈도', ascending=False) # ORDER BY 빈도 DESC
)

print(mode_freq)

# 2. 총계처리
kpass_df['적립금액_평균값'] = mean_value
kpass_df['적립금액_최소값'] = min_value
kpass_df['적립금액_최대값'] = max_value
kpass_df['적립금액_중앙값'] = medium_value
kpass_df['적립금액_최빈값'] = mode_value

print(kpass_df[['적립금액', '적립금액_평균값', '적립금액_최소값', '적립금액_최대값', '적립금액_최빈값', '적립금액_중앙값']].head(10))

# Lap1 가명 처리- Task2 통계도구- 1. 부분 통계
# 행정구역 시도만 구분
kpass_df['시도'] = kpass_df['주민등록상 행정구역'].str.split().str[0]

# 최빈값 계산 함수 (빈 경우 대비)
def get_mode(series):
    mode = series.mode()
    return mode.iloc[0] if not mode.empty else np.nan

# 1. 그룹별(연령, 시도별) 통계값 계산
group_stats = kpass_df.groupby(['연령', '시도'])['적립금액'].agg([
    ('그룹별_적립금액_평균값', 'mean'),
    ('그룹별_적립금액_최소값', 'min'),
    ('그룹별_적립금액_최대값', 'max'),
    ('그룹별_적립금액_중앙값', 'median'),
    ('그룹별_적립금액_최빈값', get_mode)
]).reset_index()

# 2. 원본 kpass_df에 merge (연령, 시도 기준으로 join)
kpass_df = kpass_df.merge(group_stats, on=['연령', '시도'], how='left')

# 3. 그룹별 통계 확인
group_stats_30_경기 = group_stats[(group_stats['연령'] == 30) & (group_stats['시도'] == '경기도')]


subset = kpass_df[
    (kpass_df['연령'] == 30) & 
    (kpass_df['시도'] == '경기도')
][[
    '연령', '시도', '적립금액',
    '그룹별_적립금액_평균값', '그룹별_적립금액_최소값', 
    '그룹별_적립금액_최대값', '그룹별_적립금액_최빈값', '그룹별_적립금액_중앙값'
]]

# Lap1 가명 처리- Task3 일반화 기술(범주화)
# Lap1 가명 처리- Task3 일반화 기술(범주화)- 1. 라운딩
import numpy as np

# 1. 일반 라운딩
kpass_df['이용요금_올림'] = np.ceil(kpass_df['이용요금']/10)*10
kpass_df['이용요금_내림'] = np.floor(kpass_df['이용요금']/10)*10
kpass_df['이용요금_반올림'] = np.round(kpass_df['이용요금'], -1)

# 2. 랜덤 라운딩 - 각 값게 대해 50%확률로 올림/네림 적용
def random_round(amount):
    remainder = 0.5

    floor_val = np.floor(amount / 10)*10
    ceil_val = np.ceil(amount/10)*10

    if np.random.rand() < remainder:
        return ceil_val
    else:
        return floor_val

kpass_df['이용요금_랜덤라운딩'] = kpass_df['이용요금'].apply(random_round)

# 결과 확인
print("\n=== 이용요금 라운딩 결과 ===")
print(kpass_df[['이용요금', '이용요금_올림','이용요금_내림','이용요금_반올림', '이용요금_라운딩']].head(100))

# Lap1 가명 처리- Task3 일반화 기술(범주화)- 2. 상하단 코딩
# '적립금액' 컬럼에 상하단 코딩 적용

# 1. 분위수 계산(예: 1% 분위수와 99%분위수)
lower_bound = kpass_df['적립금액'].quantile(0.01)
upper_bound = kpass_df['적립금액'].quantile(0.99)

print(f"적립금액 하단 코딩 기중 (1%분위수): {lower_bound:.2f}")
print(f"적립금액 상단 코딩 기준 (99% 분위수): {upper_bound:.2f}")

# 2. 상하단 코딩 적용
# 적립금액이 lower_bound보다 작으면 lower_bound 값으로 대체
# 적립금액이 upper_bound보다 크면 upper_bound 값으로 대체
kpass_df['적립금액_상하단코딩'] = kpass_df['적립금액'].clip(lower=lower_bound, upper=upper_bound)

# 결과 확인
print("\n=== 적립금액 상하단 코딩 결과 (샘플) ===")
print(kpass_df[['적립금액', '적립금액_상하단코딩']].head())
print(kpass_df[['적립금액', '적립금액_상하단코딩']].tail())

# 상하단 코딩 적용 전후의 통계량 비교
print("\n=== 적립금액 상하단 코딩 전 통계 ===")
print(kpass_df['적립금액'].describe())

print("\n=== 적립금액 상하단 코딩 후 통계 ===")
print(kpass_df['적립금액_상하단코딩'].describe())

# Lap1 가명 처리- Task3 일반화 기술(범주화)- 3. 로컬 일반화
# 1. 연령 상위 1% 값
print(f"99% 분위수 (상위 1% 컷오프): {threshold_99}")

# 2. 조건 필터링
top_1_percent_df = kpass_df[kpass_df['연령'] >= threshold_99]

# 3. 결과 확인
print(f"상위 1% 행 개수: {len(top_1_percent_df)}")
print(top_1_percent_df)

# 4. 예: 연령이 너무 많은 사람의 주소만 삭제(로컬삭제)
kpass_df.loc[kpass_df['연령'] > threshold_99, '주민등록상 행정구역'] = '서울특별시, 경기도'
kpass_df[kpass_df['주민들록상 행정구역'] == '서울특별시, 경기도']

# Lap1 가명 처리- Task3 일반화 기술(범주화)- 4. 범위방법
# 연령 구간 나누기
bins = range(0, kpass_df['연령'].max() + 10, 10) # 0, 10, 20, ...
labels = [f'{i}대' for i in range(0, kpass_df['연령'].max(), 10)]

# 연령 구간 컬럼 생성
kpass_df['연령 구간'] = pd.cut(kpass_df['연령'], bins = bins, labels=labels, right=False)

print("\n=== 연령 구간화 결과 (샘플) ===")

# 연령 구간별 분포 확인 (선택 사항)
print("\n=== 연령 구간별 분포 ===")
print(kpass_df['연령 구간'].value_counts().sort_index())


# Lap1 가명 처리- Task3 일반화 기술(범주화)- 5. 문자데이터 범주화
# '승차 Top1 행정동' 컬럼에서 시군구 정보 추출 (앞 두단어 사용)
# 예: '서울특별시 강남구 역삼동' -> "서울특별시 강남구"
def extract_sigungu(address):
    parts = str(address).split()
    if len(parts) >= 2:
        return " ".join(parts[:2])
    elif len(parts) == 1:
        return parts[0]
    return None # 주소 형식이 예산과 다른 경우

kpass_df['승차 Top1 시군구'] = kpass_df['승차 Top1 행정동'].apply(extract_sigungu)
print(kpass_df[['승차 Top1 시군구', '승차 Top1 행정동']].head())

# 가명 정보 결합
# 결합키 생성
import pandas as pd

# 모빌리티 데이터 로드
mobility_file_path = 'C:/Users/mjeon/OneDrive/바탕 화면/가명처리 대회/모빌리티_서비스_이용내역.csv'
mobility_df = pd.read_csv(kpass_file_path, encoding='utf-8') 

# k-패스 데이터 로드
kpass_file_path = 'K패스_이용내역.csv'
kpass_df = pd.read_csv(kpass_file_path, encoding='utf-8')

# 데이터 미리보기
print("\n=== 모빌리티 데이터 ===")
print(len(mobility_df))
print(mobility_df.head(3))

print("\n=== K-패스 데이터 ===")
print(len(kpass_df))
print(kpass_df.head(3))

# 결합키 생성 및 예제
import hashlib

def hash_personal_info(name, birthday, phone_number, salt):
    """
    이름, 생년월일, 휴대폰 번호와 salt를 사용하여 해시 값을 생성합니다.

    Args:
        name (str): 이름
        birthday (str): 생년월일 (예: YYYYMMDD 형식)
        phone_number (str): 휴대폰 번호 (예: 01012345678 형식)
        salt (str): 해시에 사용될 salt 값

    Returns:
        str: 생성된 해시 값
    """

    # 무든 결합키 생성항목(이름, 생년월일, 휴태폰 번호)를 하나의 문자열로 결합
    data_to_hash = name+birthday+phone_number+salt

    # UTF-8로 인코딩하여 바이트 문자열로 변환
    encoded_data = data_to_hash.encoding('utf-8')

    # SHA256 해시함수를 사용 
    hashed_value = hashlib.sha256(encoded_data).hexdigest()
    return hashed_value

