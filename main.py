import numpy as np
import matplotlib.pyplot as plt


# ==================================================
# 情報取得後の行動確率を計算する関数
# ==================================================
def calculate_after_probability(p0, pr, r):
    """
    情報取得後に傘を持つ確率 P1 を計算する。

    Parameters
    ----------
    p0 : float
        情報取得前に傘を持つ確率
    pr : float
        天気予報で示された降水確率
    r : float
        情報に対する信頼度

    Returns
    -------
    float
        情報取得後に傘を持つ確率 P1
    """
    return p0 + r * (pr - p0)


# ==================================================
# 情報の影響度を計算する関数
# ==================================================
def calculate_information_impact(p0, p1):
    """
    情報取得前後の行動確率の差から
    情報の影響度を計算する。

    Parameters
    ----------
    p0 : float
        情報取得前に傘を持つ確率
    p1 : float
        情報取得後に傘を持つ確率

    Returns
    -------
    float
        情報の影響度
    """
    return abs(p1 - p0)


# ==================================================
# 実験1：情報に対する信頼度を変化させる
# ==================================================

# 固定値
p0 = 0.2
pr = 0.8

# 信頼度 r を 0 から 1 まで変化
reliabilities = np.linspace(0, 1, 101)

information_impacts_1 = []

# 各信頼度について情報の影響度を計算
for r in reliabilities:
    p1 = calculate_after_probability(p0, pr, r)
    impact = calculate_information_impact(p0, p1)

    information_impacts_1.append(impact)


# 実験1のグラフを作成
plt.figure(figsize=(8, 5))

plt.plot(
    reliabilities,
    information_impacts_1,
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

# README.md と同じディレクトリに保存
plt.savefig(
    "実験結果１.png",
    dpi=300,
    bbox_inches="tight"
)

# Google Colabなどでは画面にも表示
plt.show()
plt.close()


# ==================================================
# 実験2：降水確率を変化させる
# ==================================================

# 固定値
p0 = 0.2
r = 0.7

# 降水確率 PR を 0 から 1 まで変化
rain_probabilities = np.linspace(0, 1, 101)

information_impacts_2 = []

# 各降水確率について情報の影響度を計算
for pr in rain_probabilities:
    p1 = calculate_after_probability(p0, pr, r)
    impact = calculate_information_impact(p0, p1)

    information_impacts_2.append(impact)


# 実験2のグラフを作成
plt.figure(figsize=(8, 5))

plt.plot(
    rain_probabilities,
    information_impacts_2,
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

# README.md と同じディレクトリに保存
plt.savefig(
    "実験結果２.png",
    dpi=300,
    bbox_inches="tight"
)

# Google Colabなどでは画面にも表示
plt.show()
plt.close()


# ==================================================
# 実行完了メッセージ
# ==================================================

print("Experiments completed.")
print("実験結果１.png was created.")
print("実験結果２.png was created.")
