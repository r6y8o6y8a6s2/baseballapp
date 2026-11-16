import math
import streamlit as st

st.title("⚾ プロ野球・打率計算アプリ")
st.write("打数と安打数を入力すると、自動で打率を計算します。")

# 入力フォーム
at_bats = st.number_input("打数 (at bat) を入力してください", min_value=0, value=30)
hits = st.number_input("安打数 (hits) を入力してください", min_value=0, value=10)

# 【追加】目標打率の入力欄
target_avg = st.number_input(
    "目標打率を入力してください (例: 0.300)",
    min_value=0.000,
    max_value=1.000,
    value=0.300,
    format="%.3f",
)

if at_bats > 0:
  # 現在の打率計算
  batting_avg = hits / at_bats
  st.write(f"### 現在の打率: {batting_avg:.3f}")

  # 【追加】目標達成に必要な安打数の逆算ロジック
  required_hits = math.ceil(target_avg * at_bats)

  if batting_avg >= target_avg:
    st.success("🎉 すでに目標の打率を達成しています！お見事です！")
  else:
    needed = required_hits - hits
    st.info(
        f"🎯 目標の打率 ({target_avg:.3f}) まであと **{needed} 本**"
        " のヒットが必要です！"
    )
else:
  st.warning("打数を1以上にしてください。")
            st.write("🎉 素晴らしい！3割打者（クリーンナップ級）です！")
        elif avg >= 0.250:
            st.write("👍 ナイスバッティング！レギュラー級の成績です！")
        else:
            st.write("💪 もっと練習してレギュラーを奪い返そう！")
