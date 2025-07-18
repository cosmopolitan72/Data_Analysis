import pandas as pd
import hashlib
import os

def load_csv(path_prompt):
    while True:
        path = input(f"{path_prompt} CSV 경로 입력: ").strip().strip('"').strip("'")
        try:
            df = pd.read_csv(path)
            print(f"✅ 파일 로드 성공! (행: {len(df)}, 열: {len(df.columns)})\n")
            return df
        except Exception as e:
            print(f"❌ 파일을 읽을 수 없습니다: {e}")
            continue

def get_column_choice(df, prompt_text):
    print(f"\n📋 '{prompt_text}'에 사용할 컬럼을 선택하세요:")
    for i, col in enumerate(df.columns):
        print(f"{i+1}. {col}")
    val = input(f"번호 또는 컬럼명 입력 (Enter 시 제외): ").strip()
    if val == "":
        return None
    elif val.isdigit() and 1 <= int(val) <= len(df.columns):
        return df.columns[int(val) - 1]
    elif val in df.columns:
        return val
    else:
        print("⚠️ 잘못된 입력입니다. 제외합니다.")
        return None

def generate_pseudonym_key(df, columns):
    def hash_row(row):
        values = [str(row[col]).strip() for col in columns if col in row and pd.notna(row[col])]
        if values:
            concat = ''.join(values)
            return hashlib.sha256(concat.encode()).hexdigest()
        else:
            return None
    return df.apply(hash_row, axis=1)

def main():
    print("📂 Step 1: CSV 파일 불러오기")
    mobility_df = load_csv("🛴 모빌리티 데이터")
    kpass_df = load_csv("🚌 K-패스 데이터")

    print("\n🔐 Step 2: 결합키로 사용할 컬럼 선택")
    print("※ Enter만 누르면 해당 항목은 제외됩니다.")

    print("\n🔸 모빌리티 데이터 컬럼 선택")
    name_col_mobility = get_column_choice(mobility_df, "이름")
    birth_col_mobility = get_column_choice(mobility_df, "생년월일")
    phone_col_mobility = get_column_choice(mobility_df, "전화번호")
    gender_col_mobility = get_column_choice(mobility_df, "성별")

    print("\n🔹 K-패스 데이터 컬럼 선택")
    name_col_kpass = get_column_choice(kpass_df, "이름")
    birth_col_kpass = get_column_choice(kpass_df, "생년월일")
    phone_col_kpass = get_column_choice(kpass_df, "전화번호")
    gender_col_kpass = get_column_choice(kpass_df, "성별")

    # 공통으로 존재하는 결합 컬럼만 추출
    join_cols_mobility = [col for col in [name_col_mobility, birth_col_mobility, phone_col_mobility, gender_col_mobility] if col]
    join_cols_kpass = [col for col in [name_col_kpass, birth_col_kpass, phone_col_kpass, gender_col_kpass] if col]

    if join_cols_mobility != join_cols_kpass:
        print("\n⚠️ [경고] 결합 대상 컬럼명이 두 데이터셋에서 서로 다릅니다.")
        print(f"모빌리티 컬럼: {join_cols_mobility}")
        print(f"K-패스 컬럼: {join_cols_kpass}")
        return

    print("\n🔗 Step 3: 가명 결합키 생성 중...")
    mobility_df['pseudonym_key'] = generate_pseudonym_key(mobility_df, join_cols_mobility)
    kpass_df['pseudonym_key'] = generate_pseudonym_key(kpass_df, join_cols_kpass)

    print("\n🔍 생성된 결합키 예시:")
    print("🛴 모빌리티:", mobility_df['pseudonym_key'].dropna().unique()[:5])
    print("🚌 K-패스:", kpass_df['pseudonym_key'].dropna().unique()[:5])

    print("\n📎 Step 4: 데이터 결합")
    merged_df = pd.merge(mobility_df, kpass_df, on='pseudonym_key', suffixes=('_mobility', '_kpass'))

    if merged_df.empty:
        print("❗ 결합 결과가 없습니다. 결합키를 다시 확인해주세요.")
    else:
        print(f"✅ 결합 완료! 결합된 행 수: {len(merged_df)}")
        print(merged_df.head(3))

        save = input("\n💾 결합된 데이터를 CSV로 저장하시겠습니까? (y/n): ").strip().lower()
        if save == 'y':
            save_path = input("저장할 파일 경로 (예: output.csv): ").strip().strip('"').strip("'")
            try:
                merged_df.to_csv(save_path, index=False)
                print(f"✅ 저장 완료: {save_path}")
            except Exception as e:
                print(f"❌ 저장 실패: {e}")

if __name__ == "__main__":
    main()
