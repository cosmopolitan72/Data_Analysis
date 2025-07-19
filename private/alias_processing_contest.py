import pandas as pd
import numpy as np
import hashlib

""" def alias_file():
    while True:
        alias_file_path = input("가명처리 파일의 경로를 입력하세요>")
        
        try:
            alias_df = pd.read_csv(alias_file_path, encoding='utf-8')
            print("파일이 성공적으로 불러와졌습니다.")
            return alias_df
        
        except Exception as e:
            print(f"파일을 불러오는 도중 오류 발생: {e}\n다시 시도하세요.\n")

def save_file(alias_df):
    save_path = input("변경된 파일을 저장할 경로를 입력하세요 (예: ./output.csv) > ")
    try:
        alias_df.to_csv(save_path, index=False, encoding='utf-8-sig')
        print(f"파일이 '{save_path}' 로 저장되었습니다.")
    except Exception as e:
        print(f"파일 저장 실패: {e}") """

""" # 기본 틀
def 함수 정의():
    while True:
        함수 = input("입력 받기>")
d
        if 함수 in ['0', '뒤로가기', '0. 뒤로가기']:
            return

        if 함수 in ["경우의 수 인자"]
            return
        .
        .
        .
        
    else:
        print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")
 """


def prossing_():
    while True:
        prossing=input("0. 뒤로가기 or 1. 가명 처리 or 2. 가명정보 결합 중에 입력하시오\n>")

        if prossing in ['0', '뒤로가기', '0. 뒤로가기']:
            print("프로그램 종료 또는 뒤로가기 선택됨.")
            return

        if prossing in ['1', '가명 처리', "1. 가명 처리"]:
            print("1. 가명처리를 선택하셨습니다.")

            def alias_file():
                while True:
                    alias_file_path = input("가명처리 파일의 경로를 입력하세요>")
        
                    try:
                        global alias_df 
                        alias_df = pd.read_csv(alias_file_path, encoding='utf-8')
                        print("파일이 성공적으로 불러와졌습니다.")
                        return alias_file
        
                    except Exception as e:
                        print(f"파일을 불러오는 도중 오류 발생: {e}\n다시 시도하세요.\n")

            def save_file(alias_df):
                save_path = input("변경된 파일을 저장할 경로를 입력하세요 (예: ./output.csv) > ")
                try:
                    alias_df.to_csv(save_path, index=False, encoding='utf-8-sig')
                    print(f"파일이 '{save_path}' 로 저장되었습니다.")
                except Exception as e:
                    print(f"파일 저장 실패: {e}")

            alias_file()

            def Type_Of_Program_(alias_df):
                while True:
                    Type_Of_Program = input("0. 뒤로가기 or 1. 삭제 기술 or 2. 통계 도구 or 3. 일반화 기술(라운딩, 범주화..) 중에 고르시오\n>")

                    if Type_Of_Program in ['0', '뒤로가기', '0. 뒤로가기']:
                        print("프로그램 종료 또는 뒤로가기 선택됨.")
                        return

                    if Type_Of_Program in ['1', "삭제 기술", "1. 삭제 기술"]:
                        print("1. 가명처리 - 1. 삭제기술을 선택하셨습니다.")
                        
                        while True: 
                            Suppresion_Type = input("0. 뒤로가기, 1. 단순 삭제, 2. 부분 삭제, 3. 행 항목 삭제, 4. 로컬 삭제, 5. 마스킹 중에 고르시오\n>")

                            if Suppresion_Type in ['0', '뒤로가기', '0. 뒤로가기']:
                                return

                            if Suppresion_Type in ['1', "단순삭제", "1. 단순 삭제"]:
                                print("1. 가명처리 - 1. 삭제 기술 - 1. 단순 삭제를 선택하셨습니다.")
                                print("\n컬럼 삭제 입니다.")

                                # 컬럼 삭제
                                def suppression_column(alias_df):
                                    colum = input("어떤 컬럼을 삭제할 건지 적으세요\n>")
                                    if colum in alias_df.columns:
                                        alias_df.drop(columns=[colum],axis=1, inplace=True)
                                        print(f"{colum} 컬럼이 삭제되었습니다.")
                                        print(alias_df.head())
                                    else:
                                        print(f"{colum} 컬럼이 존재하지 않습니다.")

                                #suppression_column(alias_df)

                                def Suppression_Column_(alias_df):
                                    colum = input("어떤 컬럼을 삭제할 건지 적으세요\n>")
                                    if colum in alias_df.columns:
                                        for i in range(len(colum)):
                                                    alias_df.loc[alias_df(colum)] = None
                                    
                                        print(f"{colum} 컬럼이 삭제되었습니다.")
                                        print(alias_df.head())
                                    else:
                                        print(f"{colum} 컬럼이 존재하지 않습니다.")
                                    
                                Suppression_Column_(alias_df)
                                save_file(alias_df)
                                return

                            if Suppresion_Type in ['2', " 부분 삭제", "2. 부분 삭제"]:
                                print("1. 가명처리 - 1. 삭제기술 - 2. 부분 삭제를 선택하셨습니다.")
                                # 어떤 걸 삭제할건지, 어느 부분을 삭제 할건지, 어떤 모형으로 삭제할건지 입력받고 삭제
                                
                                # 부분 삭제
                                def partial_delete_column(alias_df):
                                    column_name = input("부분 삭제할 컬럼명을 입력하세요 > ").strip()
                                    masking_text = input("마스킹할 문자를 입력하세요 (예: ****) > ").strip()
                                    cut_index = int(input("몇 번째 문자까지 남기고 자를지 숫자를 입력하세요 (예: 4) > "))

                                    if column_name not in alias_df.columns:
                                        print(f"'{column_name}' 컬럼이 존재하지 않습니다.")
                                        return alias_df

                                    new_column_name = f"{column_name}_부분삭제"
                                    alias_df[new_column_name] = alias_df[column_name].astype(str).str.slice(0, cut_index) + masking_text
                                    print(f"'{new_column_name}' 컬럼이 생성되었습니다.")
                                    print(alias_df[[column_name, new_column_name]].head())

                                    return alias_df
                                
                                partial_delete_column(alias_df)
                                save_file(alias_df)
                                return

                            if Suppresion_Type in ['3', " 행 항목 삭제", "3. 행 항목 삭제"]:
                                print("1. 가명처리 - 1. 삭제 기술 - 3. 행 항목 삭제를 선택하셨습니다.")
                                # 어떤 행을 삭제 할건지 받고 삭제
                                
                                def row_delete_by_unique(alias_df):
                                    column_name = input("1회 등장하는 값을 삭제할 컬럼명을 입력하세요 > ").strip()

                                    if column_name not in alias_df.columns:
                                        print(f"'{column_name}' 컬럼이 존재하지 않습니다.")
                                        return alias_df

                                    # 삭제 전 행 개수
                                    before_count = len(alias_df)

                                    # 1번 등장하는 값 찾기
                                    value_counts = alias_df[column_name].value_counts()
                                    unique_values = value_counts[value_counts == 1].index

                                    print(f"\n1회 등장하는 값 목록:\n{list(unique_values)}")

                                    # 1번 등장하는 값을 가진 행 삭제
                                    alias_df = alias_df[~alias_df[column_name].isin(unique_values)]

                                    # 삭제 후 행 개수
                                    after_count = len(alias_df)
                                    deleted_rows = before_count - after_count

                                    print(f"\n삭제된 행 수: {deleted_rows}")

                                    return alias_df
                                row_delete_by_unique(alias_df)
                                save_file(alias_df)
                                return
                                
                            if Suppresion_Type in ['4', "로컬 삭제", "4. 로컬 삭제"]:
                                print("1. 가명처리 - 1. 삭제 기술 - 4. 로컬삭제를 선택하셨습니다.")
                                # 특이 정보를 해당 행 항목에서 삭제  

                                def local_delete_by_top_percent(alias_df):
                                    target_col = input("상위 1%를 기준으로 삼을 컬럼명을 입력하세요 > ").strip()
                                    if target_col not in alias_df.columns:
                                        print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                        return alias_df

                                    delete_col = input("삭제할 컬럼명을 입력하세요 > ").strip()
                                    if delete_col not in alias_df.columns:
                                        print(f"'{delete_col}' 컬럼이 존재하지 않습니다.")
                                        return alias_df

                                    # 삭제 전 정보 출력
                                    threshold_99 = alias_df[target_col].quantile(0.99)
                                    print(f"\n{target_col} 컬럼의 99% 분위수 (상위 1% 컷오프): {threshold_99}")

                                    top_1_percent_df = alias_df[alias_df[target_col] >= threshold_99]
                                    print(f"\n상위 1% 행 개수: {len(top_1_percent_df)}")
                                    print(top_1_percent_df[[target_col, delete_col]])

                                    # 값 삭제 (None 처리)
                                    alias_df.loc[alias_df[target_col] >= threshold_99, delete_col] = None

                                    # 결과 확인
                                    null_count = alias_df[delete_col].isnull().sum()
                                    print(f"\n삭제된 (None으로 변경된) '{delete_col}' 컬럼의 행 개수: {null_count}")
                                    print(alias_df[alias_df[delete_col].isnull()][[target_col, delete_col]])

                                    return alias_df
                                local_delete_by_top_percent(alias_df)
                                save_file(alias_df)
                                return

                            if Suppresion_Type in ['5', "마스킹", "5. 마스킹"]:
                                print("1. 가명처리 - 1. 삭제 기술 - 5. 마스킹을 선택하셨습니다.")
                                # # 어떤 걸 삭제할건지, 어느 부분을 삭제 할건지, 어떤 모형으로 삭제할건지 입력받고 삭제
                                
                                def masking_column(alias_df):
                                    target_col = input("마스킹할 컬럼명을 입력하세요 > ").strip()
                                    if target_col not in alias_df.columns:
                                        print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                        return alias_df

                                    new_col_name = input("새로 생성할 마스킹 컬럼명을 입력하세요 > ").strip()

                                    # 유저가 마스킹할 범위 지정 (앞 몇 글자 유지 / 뒤 몇 글자 유지)
                                    front_keep = int(input("앞에서 몇 글자를 유지할까요? (0 입력 가능) > ").strip())
                                    back_keep = int(input("뒤에서 몇 글자를 유지할까요? (0 입력 가능) > ").strip())
                                    masking_char = input("마스킹에 사용할 문자를 입력하세요 (예: *, # 등) > ").strip()
                                    if not masking_char:
                                        masking_char = '*'

                                    def mask_data(data):
                                        data = str(data)
                                        masked_len = len(data) - front_keep - back_keep
                                        if masked_len > 0:
                                            return data[:front_keep] + masking_char * masked_len + data[-back_keep:]
                                        else:
                                            # 데이터 길이가 너무 짧아서 마스킹할 부분이 없으면 그대로 반환
                                            return data

                                    alias_df[new_col_name] = alias_df[target_col].apply(mask_data)

                                    print(f"\n마스킹된 '{new_col_name}' 컬럼이 생성되었습니다.")
                                    print(alias_df[[target_col, new_col_name]].head())

                                    return alias_df
                                masking_column(alias_df)
                                save_file(alias_df)
                                return
                            
                            else:
                                print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")
                    
                    if Type_Of_Program in ['2', "통계 도구", "2. 통계 도구"]:
                        # TODO: Type_Of_Program in ['1', "통계도구", "2. 통계 도구", "통계도구"]가 가능하면 이게더 효율적
                        print("1. 가명처리 - 2. 통계 도구를 선택하셨습니다.")
                        
                        
                        def Statistical_Tools_(alias_df):
                            while True:
                                statistical_tools = input("0. 뒤로가기 or 1. 총계 처리 or 2. 부분 총계 중에 고르시오\n>")

                                if statistical_tools in ['0', '뒤로가기', '0. 뒤로가기']:
                                    print("프로그램 종료 또는 뒤로가기 선택됨.")
                                    return
                            
                                if statistical_tools in ['1',"총계 처리", "1. 총계 처리"]:
                                    print("1. 가명처리 - 2. 통계 도구 - 1. 총계 처리를 선택하셨습니다.")

                                    def Total_(alias_df):
                                        # 1. 평균값, 최소값, 최대값, 중앙값, 최빈값 계산
                                        total = input("어떤 컬럼을 총계 처리할건지 적으세요>")
                                        if total in alias_df.columns:
                                            mean_value = alias_df[total].mean()
                                            min_value = alias_df[total].min()
                                            max_value = alias_df[total].max()
                                            medium_value = alias_df[total].median()
                                            mode_value = alias_df[total].mode()[0] # 여러 최빈값중 첫 번째
                                            
                                            print("평균값: ", mean_value)
                                            print("최소값: ", min_value)
                                            print("최대값: ", max_value)
                                            print("중앙값: ", medium_value)
                                            print("최빈값: ", mode_value)
                                            
                                            # 컬럼의 빈도 계산 (groupby + size)
                                            dataframe_name = input("총계 처리의 데이터 프레임의 이름을 입력해 주세요>")

                                            mode_freq = (
                                                    alias_df.groupby(dataframe_name)
                                                    .size()
                                                    .reset_index(name='빈도')
                                                    .sort_values(by='빈도', ascending=False) # ORDER BY 빈도 DESC
                                            )
                                            
                                            print(mode_freq)

                                            # 2. 총계처리
                                            alias_df['{}_평균값'.format(dataframe_name)] = mean_value
                                            alias_df['{}_최소값'.format(dataframe_name)] = min_value
                                            alias_df['{}_최대값'.format(dataframe_name)] = max_value
                                            alias_df['{}_중앙값'.format(dataframe_name)] = medium_value
                                            alias_df['{}_최빈값'.format(dataframe_name)] = mode_value
                                            
                                            print(alias_df[[dataframe_name,
                                                            f'{dataframe_name}_평균값',
                                                            f'{dataframe_name}_최소값',
                                                            f'{dataframe_name}_최대값',
                                                            f'{dataframe_name}_최빈값',
                                                            f'{dataframe_name}_중앙값']].head(10))

                                        else:
                                            print(f"{total} 컬럼이 존재하지 않습니다.")   
                                    Total_(alias_df)
                                    save_file(alias_df)
                                    return
                                
                                if statistical_tools in ['2', "부분 총계", "2. 부분 총계"]:
                                    print("1. 가명처리 - 2. 통계 도구 - 2. 부분 총계를 선택하셨습니다.")
                                    
                                    def Partial_Statistics_(alias_df):
                                        partial_statistics = input("부분 통계를 낼 컬럼을 적으세요\n>")
                                        
                                        if partial_statistics in alias_df.columns:
                                            partial_column = input("부분 통게 대상 컬럼을 입력하세요\n>")
                                            alias_df[partial_column] = alias_df[partial_statistics].str.split().str[0]

                                            # 최빈값 계산 함수 (빈 경우 대비)
                                            def get_mode(series):
                                                mode = series.mode()
                                                return mode.iloc[0] if not mode.empty else np.nan
                                            
                                            # 1. 그룹별 통계 값 계산
                                            groups_columns_1, groups_columns_2 = input("그룹화 할 컬럼 2개를 적으세요\n>").split()
                                            groups_columns_1 = groups_columns_1.strip()
                                            groups_columns_2 = groups_columns_2.strip()

                                            if groups_columns_1 in alias_df.columns and groups_columns_2 in alias_df.columns:
                                                groups_stats = alias_df.groupby([partial_column, groups_columns_2])[groups_columns_1].agg([
                                                    ('그룹별_' + groups_columns_1 + '_평균값','mean'),
                                                    ('그룹별_' + groups_columns_1 + '_최소값', 'min'),
                                                    ('그룹별_' + groups_columns_1 + '_최대값', 'max'),
                                                    ('그룹별_' + groups_columns_1 + '_중앙값', 'median'),
                                                    ('그룹별_' + groups_columns_1 + '_최빈값', get_mode)
                                                ]).reset_index()

                                                # 2. 원본 alias_df에 merge (groups_columns_1, groups_columns_2 기준으로 join)
                                                alias_df = alias_df.merge(groups_stats, on = [partial_column, groups_columns_2], how='left')

                                                # 3. 그룹별 통계 확인
                                                new_reference_point = input("새로 만든 컬럼의 기준이 되는 수치를 적으세요\n>")
                                                reference_point_2 = input("두번째 컬럼의 기준이 되는 수치를 적으세요\n>")
                                                groups_stats_result = groups_stats[(groups_stats[groups_columns_2] == reference_point_2) & (groups_stats[partial_column] == new_reference_point)]

                                                subset = alias_df[
                                                    (alias_df[groups_columns_2] == reference_point_2) & 
                                                    (alias_df[partial_column] == new_reference_point)
                                                ][[
                                                    groups_columns_2, partial_column, groups_columns_1,
                                                    '그룹별_' + groups_columns_1 + '_평균값', '그룹별_' + groups_columns_1 + '_최소값',
                                                    '그룹별_' + groups_columns_1 + '_최대값', '그룹별_' + groups_columns_1 + '_최빈값', '그룹별_' + groups_columns_1 + '_중앙값'
                                                ]]
                                                print(subset)


                                            else:
                                                print(f"{groups_columns_1, groups_columns_2} 컬럼이 존재하지 않습니다.")
                                                return
                                    
                                        else:
                                            print(f"{partial_statistics} 컬럼이 존재하지 않습니다.")
                                    
                                    Partial_Statistics_(alias_df)
                                    save_file(alias_df)
                                    return
                                
                                else:
                                    print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")
                        
                        Statistical_Tools_(alias_df)

                    if Type_Of_Program in ['3', "일반화 기술", "3. 일반화 기술"]:
                        # 범주화 라운딩 구현
                        print("1. 가명처리 - 3. 일반화 기술을 선택하셨습니다.")
                        
                        def Generalization_(alias_df):
                            while True:
                                generalization_tools = input("0. 뒤로가기, 1. 라운딩, 2. 상하단코딩, 3. 로컬 일반화, 4. 범위방법, 5. 문자데이터 범주화 중에 고르시오\n>")

                                if generalization_tools in ['0', '뒤로가기', '0. 뒤로가기']:
                                    print("프로그램 종료 또는 뒤로가기 선택됨.")
                                    return
                                
                                if generalization_tools in ['1', '라운딩', '1. 라운딩']:
                                    print("1. 가명처리 - 3. 일반화 기술 - 1. 라운딩을 선택하셨습니다.")
                                    
                                    def rounding_columns(alias_df):
                                        target_col = input("라운딩할 컬럼명을 입력하세요 > ").strip()
                                        if target_col not in alias_df.columns:
                                            print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                            return
    
                                        try:
                                            rounding_unit = int(input("몇의 자리에서 반올림/올림/내림 할지 입력하세요 (예: 10, 100) > ").strip())
                                        except ValueError:
                                            print("잘못된 입력입니다. 숫자를 입력하세요.")
                                            return
    
                                        # 새 컬럼명 지정
                                        ceil_col = f"{target_col}_올림"
                                        floor_col = f"{target_col}_내림"
                                        round_col = f"{target_col}_반올림"

                                        # 라운딩 수행
                                        alias_df[ceil_col] = np.ceil(alias_df[target_col] / rounding_unit) * rounding_unit
                                        alias_df[floor_col] = np.floor(alias_df[target_col] / rounding_unit) * rounding_unit
                                        alias_df[round_col] = np.round(alias_df[target_col], -int(np.log10(rounding_unit)))

                                        print(f"\n'{ceil_col}', '{floor_col}', '{round_col}' 컬럼이 생성되었습니다.")
                                        print(alias_df[[target_col, ceil_col, floor_col, round_col]].head())

                                        return alias_df
                                    
                                    def random_round_columns(alias_df):
                                        target_col = input("랜덤 라운딩할 컬럼명을 입력하세요 > ").strip()
                                        if target_col not in alias_df.columns:
                                            print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                            return
    
                                        try:
                                            rounding_unit = int(input("몇의 자리에서 랜덤 올림/내림 할지 입력하세요 (예: 10, 100) > ").strip())
                                        except ValueError:
                                            print("잘못된 입력입니다. 숫자를 입력하세요.")
                                            return

                                        # 랜덤 라운딩 함수 정의
                                        def random_round(amount):
                                            floor_val = np.floor(amount / rounding_unit) * rounding_unit
                                            ceil_val = np.ceil(amount / rounding_unit) * rounding_unit
                                            return ceil_val if np.random.rand() < 0.5 else floor_val

                                        # 새 컬럼명 지정
                                        random_col = f"{target_col}_랜덤라운딩"
                                        alias_df[random_col] = alias_df[target_col].apply(random_round)

                                        print(f"\n'{random_col}' 컬럼이 생성되었습니다.")
                                        print(alias_df[[target_col, random_col]].head())

                                        return alias_df

                                    print("# 일반 라운딩(올림, 내림, 반올림)")
                                    rounding_columns(alias_df)
                                    random_round_columns(alias_df)
                                    save_file(alias_df)
                                    return
                                
                                if generalization_tools in ['2', '상하단코딩', '2. 상하단코딩']:
                                    print("1. 가명처리 - 3. 일반화 기술 - 2. 상하단코딩을 선택하셨습니다.")
                                    
                                    def Upper_Lower_Coding(alias_df):
                                        target_col = input("상하단 코딩할 컬럼명을 입력하세요\n> ")
    
                                        if target_col not in alias_df.columns:
                                            print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                            return

                                        try:
                                            lower_q = float(input("하단 분위수를 입력하세요 (예: 0.01=1%분위수) > ").strip())
                                            upper_q = float(input("상단 분위수를 입력하세요 (예: 0.99=99%분위수) > ").strip())
                                        except ValueError:
                                            print("잘못된 입력입니다. 숫자를 입력하세요.")
                                            return
    
                                        lower_bound = alias_df[target_col].quantile(lower_q)
                                        upper_bound = alias_df[target_col].quantile(upper_q)

                                        print(f"\n{target_col} 하단 분위수 ({lower_q}): {lower_bound:.2f}")
                                        print(f"{target_col} 상단 분위수 ({upper_q}): {upper_bound:.2f}")
    
                                        ulcolumn = f"{target_col}_상하단코딩"
                                        alias_df[ulcolumn] = alias_df[target_col].clip(lower=lower_bound, upper=upper_bound)

                                        # 결과 출력
                                        print(f"\n=== {target_col} 상하단 코딩 결과 (샘플) ===")
                                        print(alias_df[[target_col, ulcolumn]].head())
                                        print(alias_df[[target_col, ulcolumn]].tail())
    
                                        # 통계 비교 출력
                                        print(f"\n=== {target_col} 상하단 코딩 전 통계 ===")
                                        print(alias_df[target_col].describe())
    
                                        print(f"\n=== {target_col} 상하단 코딩 후 통계 ===")
                                        print(alias_df[ulcolumn].describe())
    
                                        return alias_df
                                    Upper_Lower_Coding(alias_df)
                                    save_file(alias_df)
                                    return
                                
                                if generalization_tools in ['3', '로컬 일반화', '3. 로컬 일반화']:
                                    print("1. 가명처리 - 3. 일반화 기술 - 3. 로컬 일반화을 선택하셨습니다.")

                                    def Local_Deletion(alias_df):
                                        target_col = input("상위 N%로 삭제할 기준 컬럼명을 입력하세요 > ")

                                        if target_col not in alias_df.columns:
                                            print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                            return

                                        # N설정
                                        try:
                                            upper_q = float(input("상위 몇 %를 기준으로 할지 입력하세요 (예: 0.99) > ").strip())
                                        except ValueError:
                                            print("잘못된 입력입니다. 숫자를 입력하세요.")
                                            return

                                        # N% 컷오프
                                        threshold = alias_df[target_col].quantile(upper_q)
                                        print(f"\n{upper_q * 100}% 분위수 (상위 {100 - upper_q * 100}% 컷오프): {threshold}")

                                        top_Npencent_df = alias_df[alias_df[target_col] >= threshold]
                                        print(f"\n상위 {100 - upper_q * 100}% 행 개수: {len(top_Npencent_df)}")
                                        print(top_Npencent_df)

                                        target_change_col = input("로컬 삭제할 컬럼명을 입력하세요 > ")
                                        if target_change_col not in alias_df.columns:
                                            print(f"'{target_change_col}' 컬럼이 존재하지 않습니다.")
                                            return alias_df

                                        replace_value = input("삭제할 대상 값을 입력하세요 > ")

                                        alias_df.loc[alias_df[target_col] >= threshold, target_change_col] = replace_value
                                        alias_df[alias_df[target_change_col] == replace_value]

                                        print(f"\n=== '{target_change_col}' 컬럼중에서 '{replace_value}' 값이 삭제된 결과 (상위 {100 - upper_q * 100}% 대상) ===")
                                        print(alias_df[alias_df[target_change_col] == replace_value])

                                        return alias_df
                                    Local_Deletion(alias_df)
                                    save_file(alias_df)
                                    return
                                
                                if generalization_tools in ['4', '범위방법', '4. 범위방법']:
                                    print("1. 가명처리 - 3. 일반화 기술 - 4. 범위방법을 선택하셨습니다.")

                                    def Range_Binning(alias_df):
                                        target_col = input("범주화할 컬럼명을 입력하세요 > ").strip()

                                        if target_col not in alias_df.columns:
                                            print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                            return
    
                                        try:
                                            bin_unit = int(input("몇 단위로 구간화할지 입력하세요 (예: 10) > ").strip())
                                        except ValueError:
                                            print("숫자를 입력해야 합니다.")
                                            return

                                        bins = range(0, int(alias_df[target_col].max()) + bin_unit, bin_unit)
                                        labels = [f'{i}대' for i in range(0, int(alias_df[target_col].max()), bin_unit)]

                                        alias_df[f'{target_col}_구간'] = pd.cut(alias_df[target_col], bins=bins, labels=labels, right=False)

                                        # 결과 출력
                                        print(f"\n=== '{target_col}' 컬럼의 구간화 결과 (샘플) ===")
                                        print(alias_df[[target_col, f'{target_col}_구간']].head())

                                        print(f"\n=== '{target_col}' 구간별 분포 ===")
                                        print(alias_df[f'{target_col}_구간'].value_counts().sort_index())

                                        return alias_df
                                    Range_Binning(alias_df)
                                    save_file(alias_df)
                                    return

                                if generalization_tools in ['5', '문자데이터 범주화', '5. 문자데이터 범주화']:
                                    print("1. 가명처리 - 3. 일반화 기술 - 5. 문자데이터 범주화을 선택하셨습니다.")

                                    def text_binning(alias_df):
                                        target_col = input("범주화할 컬럼명을 입력하세요 (예: 승차 Top1 행정동) > ")

                                        if target_col not in alias_df.columns:
                                            print(f"'{target_col}' 컬럼이 존재하지 않습니다.")
                                            return alias_df

                                        # 단어 추출 함수 (단어의 수 활용)

                                        def extract(words, word_range):
                                            parts = str(words).split()

                                            if len(parts) >= int(word_range):
                                                return " ".join(parts[:word_range])
                                            elif len(parts) == 1:
                                                return parts[0]
                                            return None  # 값이 NaN이거나 형식이 안 맞을 경우
                                        
                                        word_range = int(input("반영할 데이터의 단어수를 입력하세요>"))
                                        

                                        new_column = input("새로 만들 컬럼을 입력하세요\n>")
                                        alias_df[new_column] = alias_df[target_col].apply(lambda x: extract(x, word_range))

                                        # 결과 출력
                                        print(f"\n=== '{target_col}' → '{new_column}' 변환 결과 (샘플) ===")
                                        print(alias_df[[target_col, new_column]].head())

                                        # 시군구 빈도수 확인
                                        print(f"\n=== '{new_column}' 빈도수 ===")
                                        print(alias_df[new_column].value_counts().head(10))

                                        return alias_df
                                    text_binning(alias_df)
                                    save_file(alias_df)
                                    return

                                else:
                                    print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")
                        
                        Generalization_(alias_df) 
                        return
                        
                        
                else:
                    print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")

            Type_Of_Program_(alias_df)
                
            break

        if prossing in ['2', "가명정보 결합", "2. 가명정보 결합"]:
            print("2. 가명정보 결합을 선택했습니다.")
            # 가명정보 결합 - 결합키 생성, 전문기관 전송 파일 생성, 결합 전문 기관, 데이터 전문기관 구현해야함
            
            def Combining_Information_():
                while True:
                    combining_information = input("0. 뒤로가기, 1. 결합키 생성, 2. 전문기관 전송 파일 생성 중에 고르시오\n>")

                    if combining_information in ['0', '뒤로가기', '0. 뒤로가기']:
                        print("프로그램 종료 또는 뒤로가기 선택됨.")
                        return  
                    
                    if combining_information in ['1', '결합키 생성', '1. 결합키 생성']:
                        print("2. 가명정보 결합 - 1. 결합키 생성을 선택하셨습니다.")

                        def Creating_Combined_Key_():
                            while True:
                                creating_kombined_key = input("0. 뒤로가기, 1. 데이터 로드, 2. 결합키 함수 생성, 3. 결합키 생성, 4. 결합키 생성학목 삭제 중에 고르시오\n>")

                                if creating_kombined_key in ['0', '뒤로가기', '0. 뒤로가기']:
                                    print("프로그램 종료 또는 뒤로가기 선택됨.")
                                    return
                                
                                def Data_Path_():
                                    data_load_1_path = input("첫번째 데이터의 경로를 입력하세요\n>")
                                    data_load_1_df = pd.read_csv(data_load_1_path, encoding='utf-8')

                                    data_load_2_path = input("두번째 데이터의 경로를 입력하세요\n>")
                                    data_load_2_df = pd.read_csv(data_load_2_path, encoding='utf-8')
                                    return data_load_1_df, data_load_2_df
                                
                                if creating_kombined_key in ['1', '데이터 로드', '1. 데이터 로드']:
                                    print("2. 가명정보 결합 - 1. 결합키 생성 - 1. 데이터 로드를 선택하셨습니다.")

                                    Data_Path_()
                                    
                                    def Data_Load_(data_load_1_df, data_load_2_df):
                                        # 데이터 로드
                                        """ data_load_1_path = input("첫번째로 로드할 데이터의 경로를 입력하세요\n>")
                                        data_load_1_df = pd.read_csv(data_load_1_path, encoding='utf-8')

                                        data_load_2_path = input("두번째로 로드할 데이터의 경로를 입력하세요\n>")
                                        data_load_2_df = pd.read_csv(data_load_2_path, encoding='utf-8') """

                                        # 데이터 미리보기
                                        print(f"\n=== {data_load_1_df} 데이터 ===")
                                        print(len(data_load_1_df))
                                        print(data_load_1_df.head(3))

                                        print("\n")
                                        print("-"*30)

                                        print(f"\n=== {data_load_2_df} 데이터 ===")
                                        print(len(data_load_2_df))
                                        print(data_load_2_df.head(3))

                                        return
                                    
                                    Data_Load_()
                                    return
                                
                                if creating_kombined_key in ['2', '결합키 함수 생성', '2. 결합키 함수 생성']:
                                    print("2. 가명정보 결합 - 1. 결합키 생성 - 2. 결합키 함수 생성을 선택하셨습니다.")

                                    def Hash_Key_():

                                        hash_data_path = input("사용할 데이터의 경로를 입력하세요\n>")
                                        
                                        try:
                                            hash_data_df =  pd.read_csv(hash_data_path, encoding='utf-8')
                                            print("파일이 성공적으로 불러와졌습니다.")
                                        
        
                                        except Exception as e:
                                            print(f"파일을 불러오는 도중 오류 발생: {e}\n다시 시도하세요.\n")

                                        hash_data_cols = input("불러올 컬럼들을 입력하세요\n>").split(" ")                                        

                                        if not set(hash_data_cols).issubset(set(hash_data_df.columns)):
                                            print(f"'{hash_data_cols}' 컬럼이 존재하지 않습니다.")
                                            return
                                        
                                        fixed_salt = input("고정된 Salt값을 입력하세요\n>")
                                        print(f"사용할 고정 Salt: {fixed_salt}")
                                        """ hash_data_cols.append(fixed_salt)
                                        print(hash_data_cols) """                                        
                                        
                                        # 모든 결합키 생성 목록을 하나의 문자열로 결합
                                        for idx, row in hash_data_df.iterrows():
                                            hashed_info = [(col, row[col]) for col in hash_data_cols]
    
                                            data_to_hash = ''.join(str(row[col]) for col in hash_data_cols) + fixed_salt
                                            encoded_data = data_to_hash.encode('utf-8')
                                            hashed_value = hashlib.sha256(encoded_data).hexdigest()

                                            for i in range(len(hash_data_cols)):
                                                title = hashed_info[i][0]
                                                value = hashed_info[i][1]
                                                print(f"  {title}: {value}")

                                            print(f"  사용된 Salt: {fixed_salt}")
                                            print(f"해시 값: {hashed_value}")
                                            print("-"*30)
                                            return hashed_value

                                    

                                        # 새 컬럼 '해시함수' 추가
                                        hash_data_df['해시함수'] = hashed_value

                                        # 결과 확인
                                        print("\n=== 데이터프레임에 해시함수 컬럼 추가 결과 ===")
                                        print(hash_data_df.head())

                                        # 저장할지 물어보기 (선택 사항)
                                        save_path = input("\n결과를 저장할 파일 경로를 입력하세요 (예: result.csv):\n>")
                                        hash_data_df.to_csv(save_path, index=False, encoding='utf-8-sig')
                                        print(f"\n저장 완료: {save_path}")

                                        return
                                    Hash_Key_()
                                    return

                        Creating_Combined_Key_()


                        return
                    else:
                        print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")

            Combining_Information_()


            
            
            return

            
                
        
    else:
        print("잘못된 입력입니다. 띄어 스기 포함해서 다시 입력하세요.\n")



""" alias_df=alias_file()
prossing_(alias_df) """

def main():
#    alias_df = alias_file()
    while True:
        prossing_()
        restart = input("\n프로그램을 다시 실행하시겠습니까? (y/n): ")
        if restart.lower() != 'y':
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()

    
