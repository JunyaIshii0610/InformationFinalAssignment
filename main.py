import os
import numpy as np
import matplotlib.pyplot as plt


# ========================================
# 情報取得後の行動確率を計算する関数
# ========================================
def calculate_after_probability(p0, pr, r):
    """
    p0 : 情報取得前に傘を持つ確率
    pr : 降水確率
    r  : 情報に対する信頼度
    """
    return p0 + r * (pr - p0)


# ========================================
# 情報の影響度を計算する関数
# ========================================
def calculate_information_impact(p0, p1):
    """
    p0 : 情報取得前に傘を持つ確率
    p1 : 情報取得後に傘を持つ確率
    """
    return abs(p1 - p0)


# 結果を保存するフォルダを作成
os.makedirs("results", exist_ok=True)


# ========================================
# 実験1：情報に対する信頼度を変化させる
# ========================================

# 固定値
p0 = 0.2
pr = 0.8

# 信頼度を0から1まで変化させる
reliabilities = np.linspace(0, 1, 101)

after_probabilities = []
information_impacts = []

for r in reliabilities:
    p1 = calculate_after_probability(p0, pr, r)
    impact = calculate_information_impact(p0, p1)

    after_probabilities.append(p1)
    information_impacts.append(impact)


# グラフを作成
plt.figure(figsize=(8, 5))

plt.plot(
    reliabilities,
    information_impacts,
    label="Information Impact"
)

plt.xlabel("Reliability r")
plt.ylabel("Information Impact")
plt.title("Experiment 1: Reliability and Information Impact")

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.grid(True)
plt.legend()

plt.tight_layout()

# グラフを保存
plt.savefig("results/experiment1.png", dpi=300)
plt.close()


# ========================================
# 実験2：降水確率を変化させる
# ========================================

# 固定値
p0 = 0.2
r = 0.7

# 降水確率を0から1まで変化させる
rain_probabilities = np.linspace(0, 1, 101)

after_probabilities = []
information_impacts = []

for pr in rain_probabilities:
    p1 = calculate_after_probability(p0, pr, r)
    impact = calculate_information_impact(p0, p1)

    after_probabilities.append(p1)
    information_impacts.append(impact)


# グラフを作成
plt.figure(figsize=(8, 5))

plt.plot(
    rain_probabilities,
    information_impacts,
    label="Information Impact"
)

plt.xlabel("Probability of Rain")
plt.ylabel("Information Impact")
plt.title("Experiment 2: Rain Probability and Information Impact")

plt.xlim(0, 1)
plt.ylim(0, 1)

plt.grid(True)
plt.legend()

plt.tight_layout()

# グラフを保存
plt.savefig("results/experiment2.png", dpi=300)
plt.close()


print("Experiments completed.")
print("results/experiment1.png was created.")
print("results/experiment2.png was created.")
