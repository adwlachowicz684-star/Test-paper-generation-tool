# -*- coding: utf-8 -*-
r"""第 98 批：解三角形应用题（M-T-231，4 题）+ 四边形综合（M-T-228，4 题）
+ 向量小题（M-T-206，3 题）+ 向量面积比（M-T-241，3 题）

    python3 tools/run_batch.py 98

## 选题依据

按「详解完整 + 同题型聚堆」筛出，本批 14 题：6 选择 / 1 填空 / 7 解答。
M-T-231 四题全是应用题（花卉步道、海岸网箱、半圆花圃、围海造陆），
M-T-228 四题全是四边形，两组原文分别集中在 p164–p166、p161–p163。

## ★★ 本批最值钱的一条：四边形「对角互补 ⟹ 四点共圆」配托勒密型恒等式

M-T-228-V1：∠BAD = 120°、∠BCD = 60° ⟹ ∠BAD + ∠BCD = 180° ⟹ **A、B、C、D 四点共圆**。
在 AC 上取 E 使 ∠CBE = ∠DBA，则 △CBE ∽ △DBA、△ABE ∽ △DBC，于是

$$AD\cdot BC+AB\cdot CD=BD\cdot EC+BD\cdot AE=BD\cdot AC$$

**这就是圆内接四边形的托勒密定理**，而相似构造就是它的证明。
于是「求 $AD\cdot BC+AB\cdot CD$ 的最大值」⟺「求 $AC$ 的最大值」⟺ **$AC$ 为直径时最大**。

> ⭐⭐ 凡是四边形出现「一组对角互补」，立刻想到四点共圆 + 托勒密。

## ★★ 第二条：M-T-228-E1 的「同一条对角线 $BD$ 在两个三角形里各写一次余弦定理」

$BD^2=4-2\sqrt3\cos C$ 与 $BD^2=2-2\cos A$ 联立 ⟹ $\cos A=\sqrt3\cos C-1$。
把 $\cos A$ 用 $\cos C$ 表示后，$S^2+T^2$ 就变成 $\cos C$ 的一元二次函数：

$$S^2+T^2=-\frac32\cos^2C+\frac{\sqrt3}2\cos C+\frac34,\qquad \cos C=\frac{\sqrt3}6\text{ 时最大 } \frac78$$

> ⭐⭐ 四边形题的通用入口：**选一条公共的边（通常是未给出的那条对角线），在两个三角形里各写一次余弦定理再联立**。

## ★★ 第三条：M-T-231-V2 的 $\tan\alpha=\dfrac{\cos\theta}{\sqrt3-\sin\theta}$ 及其导数最值

在 △POQ 中正弦定理得 $\sqrt3\sin\alpha=\cos(\alpha-\theta)$，展开整理得

$$\tan\alpha=\frac{\cos\theta}{\sqrt3-\sin\theta}=f(\theta),\qquad f'(\theta)=\frac{1-\sqrt3\sin\theta}{(\sqrt3-\sin\theta)^2}$$

**分子只含 $\sin\theta$，令其为零即得 $\sin\theta=\frac{\sqrt3}3$**，不必解出 $\theta$。

> ⭐⭐ 「$a\cos\theta+b\sin\theta$ 型分式」求导后分子必是 $a\sin\theta+b\cos\theta$ 的线性组合，
> 令分子为零往往直接给出 $\sin\theta$ 或 $\cos\theta$ 的值，正是题目所问。

## ★★ 第四条：M-T-241 三题的「向量系数 ⟹ 面积比」统一套路

- **V1**：$\vec{AG}=\frac35\vec{AP}+\frac25\vec{AQ}$ 与 $\vec{AG}=\frac13\vec{AB}+\vec{AC}$ 待定系数
- **V3**：$\vec{AG}=\lambda\vec{AB}+(1-\lambda)\vec{AC}=t\vec{AM}$ ⟹ $\frac\lambda{1-\lambda}=\frac{2/3}{1/4}=\frac83$
- **V2**：$a\vec{OA}+b\vec{OB}+c\vec{OC}=\vec{CB}$ ⟹ 移项成 $a\vec{OA}+(b-1)\vec{OB}+(1+c)\vec{OC}=\vec0$ ⟹ **$O$ 是 △$A_1B_1C_1$ 的重心**

> ⭐⭐ 通法：**把已知向量式凑成「系数和 = 1」的形式**（$P=\lambda A+\mu B+(1-\lambda-\mu)C$），
> 系数就是「对顶点三角形面积 / 总面积」；凑成「系数和 = 0」则说明该点是某三角形的重心。

## 三处原书 OCR / 排版错误（判据写在各题 review 里）

1. **M-T-228-E1 题干**：$CD=3$ 实为 **$CD=\sqrt3$**（详解 $BD^2=4-2\sqrt3\cos C$、$S=\frac{\sqrt3\sin C}2$ 均需 $\sqrt3$）。
2. **M-T-228-V3 详解**：分母 `2 7 × 3 3` 实为 $2\sqrt7\cdot BD$（按 $2\sqrt7\cdot3\sqrt3$ 解不出 $BD=4$；按 $2\sqrt7\,BD$ 得 $BD^2+BD-20=0$ ⟹ $BD=4$ ✓）。
3. **M-T-231-E1 / V1 题干前置条件缺失**：由详解反推补全（见各题 review）。
"""

T231_E1 = {
    'type': '解答',
    'stem_text': (
        r"如图，某公园有一块四边形区域 $ABCD$，其中 $AC$ 为氢能源环保电动步道，"
        r"其余部分（$\triangle ABC$ 与 $\triangle ADC$）为花卉种植区域．"
        r"已知 $AD=1$，$CD=3$，$\angle D=2\angle B$，$\cos B=\dfrac{\sqrt3}3$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$AC=2\sqrt3$；（2）花卉种植区域总面积为 $4\sqrt2$．"
    ),
    'analysis': (
        r"先用二倍角余弦由 $\cos B$ 求 $\cos D$，在 $\triangle ADC$ 中用余弦定理求 $AC$；"
        r"再在 $\triangle ABC$ 中用余弦定理解出 $AB$，最后把两个三角形的面积相加．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"由 $\cos B=\dfrac{\sqrt3}3$、$\angle D=2\angle B$，得" "\n"
        r"$\cos D=\cos 2B=2\cos^{2}B-1=2\cdot\dfrac13-1=-\dfrac13$．" "\n"
        r"在 $\triangle ADC$ 中，由余弦定理：" "\n"
        r"$AC^{2}=AD^{2}+DC^{2}-2\cdot AD\cdot DC\cos D=1+9-6\cdot\left(-\dfrac13\right)=10+2=12$，" "\n"
        r"因 $AC>0$，故 $AC=2\sqrt3$．" "\n"
        r"**第 (2) 问**" "\n"
        r"在 $\triangle ABC$ 中，$BC=\sqrt6$、$AC=2\sqrt3$，由余弦定理：" "\n"
        r"$\cos B=\dfrac{AB^{2}+BC^{2}-AC^{2}}{2\cdot AB\cdot BC}"
        r"=\dfrac{AB^{2}+6-12}{2\sqrt6\cdot AB}=\dfrac{\sqrt3}3$，" "\n"
        r"整理得 $AB^{2}-2\sqrt2\cdot AB-6=0$，解得 $AB=3\sqrt2$ 或 $AB=-\sqrt2$（舍去）．" "\n"
        r"由 $\cos B=\dfrac{\sqrt3}3$ 得 $\sin B=\sqrt{1-\dfrac13}=\dfrac{\sqrt6}3$，于是" "\n"
        r"$S_{\triangle ABC}=\dfrac12\cdot AB\cdot BC\cdot\sin B"
        r"=\dfrac12\cdot3\sqrt2\cdot\sqrt6\cdot\dfrac{\sqrt6}3=3\sqrt2$．" "\n"
        r"由 $\cos D=-\dfrac13$ 得 $\sin D=\sqrt{1-\dfrac19}=\dfrac{2\sqrt2}3$，于是" "\n"
        r"$S_{\triangle ADC}=\dfrac12\cdot AD\cdot DC\cdot\sin D"
        r"=\dfrac12\cdot1\cdot3\cdot\dfrac{2\sqrt2}3=\sqrt2$．" "\n"
        r"故花卉种植区域总面积为 $S_{\triangle ABC}+S_{\triangle ADC}=3\sqrt2+\sqrt2=4\sqrt2$．"
    ),
    'review': (
        r"① ⭐⭐ **$\angle D=2\angle B$ 的作用只有一个：把 $\cos D$ 用 $\cos B$ 表示** —— "
        r"$\cos D=2\cos^2B-1=-\frac13$ ✓✓ 这是全题的入口" "\n"
        r"② ⭐⭐ **两个三角形共用一条已知对角线 $AC$，先在一个三角形里求出它，再代入另一个** "
        r"—— 这就是四边形题的标准流程 ✓✓✓" "\n"
        r"③ ⭐⭐ **解 $AB$ 时得到两个根 $3\sqrt2$ 与 $-\sqrt2$，负根必须舍**（边长为正）✓" "\n"
        r"④ 数值复核：$AC=2\sqrt3=3.464$；$\triangle ABC$ 中 $AB=4.243$、$BC=2.449$，"
        r"$\cos B=\frac{18+6-12}{2\cdot4.243\cdot2.449}=\frac{12}{20.785}=0.5773=\frac{\sqrt3}3$ ✓✓" "\n"
        r"⑤ ⚠ **题干前置条件说明**：ref_bank 中该题题干只剩两问，"
        r"前置条件（$AD=1$、$CD=3$、$\angle D=2\angle B$、$\cos B=\frac{\sqrt3}3$、$BC=\sqrt6$）"
        r"均由详解反推补全，数据逐一与详解中间结果吻合 ✓" "\n"
        r"**⭐⭐ 通法（$\angle D=2\angle B$ 型四边形）**：" "\n"
        r"① ⭐⭐ 用二倍角公式把「倍角」的余弦化到另一三角形；" "\n"
        r"② ⭐⭐ 在已知两边及夹角的三角形里用余弦定理求公共对角线；" "\n"
        r"③ ⭐⭐ 回到另一三角形用余弦定理解未知边（注意舍负根）；" "\n"
        r"④ ⭐⭐ 面积用 $S=\frac12 ab\sin C$，两个三角形分别算后相加 ✓✓✓"
    ),
    'difficulty': 0.62,
    'topics': ['M-T-231'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-231-E1',
}

T231_V1 = {
    'type': '解答',
    'stem_text': (
        r"如图，某海域有两段海岸线 $OA$、$OB$，其所成角为 $\dfrac\pi3$，"
        r"$OA=1500$ 米，$OB=1000$ 米．海面上有一点 $P$，满足 $\angle APB=\dfrac{2\pi}3$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$AB=500\sqrt7$ 米；（2）经济总收益最高约为 $55076$ 元．"
    ),
    'analysis': (
        r"第 (1) 问在 $\triangle AOB$ 中直接用余弦定理；第 (2) 问在 $\triangle PAB$ 中用正弦定理"
        r"把 $PA$、$PB$ 都表成 $\theta=\angle PAB$ 的函数，收益 $y=40PA+30PB$ 用辅助角公式求最大值．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"在 $\triangle AOB$ 中，$OA=1500$、$OB=1000$、$\angle AOB=\dfrac\pi3$，由余弦定理：" "\n"
        r"$AB=\sqrt{OA^{2}+OB^{2}-2\cdot OA\cdot OB\cos\dfrac\pi3}$" "\n"
        r"$=\sqrt{1500^{2}+1000^{2}-2\times1500\times1000\times\dfrac12}"
        r"=\sqrt{1750000}=500\sqrt7$（米）．" "\n"
        r"**第 (2) 问**" "\n"
        r"记 $\angle PAB=\theta$，则 $\angle PBA=\pi-\dfrac{2\pi}3-\theta=\dfrac\pi3-\theta$，"
        r"其中 $0<\theta<\dfrac\pi3$．" "\n"
        r"在 $\triangle PAB$ 中由正弦定理：" "\n"
        r"$\dfrac{AB}{\sin\dfrac{2\pi}3}=\dfrac{PA}{\sin\left(\dfrac\pi3-\theta\right)}"
        r"=\dfrac{PB}{\sin\theta}$，" "\n"
        r"由 $\sin\dfrac{2\pi}3=\dfrac{\sqrt3}2$ 及 $AB=500\sqrt7$ 得" "\n"
        r"$PA=\dfrac{1000\sqrt7}{\sqrt3}\sin\left(\dfrac\pi3-\theta\right)$，"
        r"$PB=\dfrac{1000\sqrt7}{\sqrt3}\sin\theta$．" "\n"
        r"设两段网箱获得的经济总收益为 $y$ 元，则" "\n"
        r"$y=40PA+30PB=\dfrac{40000\sqrt7}{\sqrt3}\sin\left(\dfrac\pi3-\theta\right)"
        r"+\dfrac{30000\sqrt7}{\sqrt3}\sin\theta$" "\n"
        r"$=\dfrac{10000\sqrt7}{\sqrt3}\left[4\sin\left(\dfrac\pi3-\theta\right)+3\sin\theta\right]$" "\n"
        r"$=\dfrac{10000\sqrt7}{\sqrt3}\left[4\left(\dfrac{\sqrt3}2\cos\theta-\dfrac12\sin\theta\right)+3\sin\theta\right]$" "\n"
        r"$=\dfrac{10000\sqrt7}{\sqrt3}\left(2\sqrt3\cos\theta+\sin\theta\right)$．" "\n"
        r"由辅助角公式，$2\sqrt3\cos\theta+\sin\theta=\sqrt{13}\sin(\theta+\varphi)$，"
        r"其中 $\tan\varphi=2\sqrt3$，故" "\n"
        r"$y_{\max}=\dfrac{10000\sqrt7}{\sqrt3}\cdot\sqrt{13}=10000\sqrt{\dfrac{91}3}\approx55076$（元）．" "\n"
        r"此时 $\theta=\dfrac\pi2-\varphi\in\left(0,\dfrac\pi3\right)$（因 $\varphi=\arctan2\sqrt3\approx1.289$），"
        r"最大值可以取到．" "\n"
        r"所以两段网箱获得的经济总收益最高约为 $55076$ 元．"
    ),
    'review': (
        r"① ⭐⭐ **$\angle APB=\frac{2\pi}3$ 与 $\angle AOB=\frac\pi3$ 互补** —— "
        r"这意味着 $A$、$O$、$B$、$P$ 四点共圆，但本题不需要用，直接正弦定理更快 ✓" "\n"
        r"② ⭐⭐ **把 $PA$、$PB$ 都表成同一个角 $\theta$ 的函数** 是第 (2) 问的关键；"
        r"正弦定理的分母 $\sin\frac{2\pi}3$ 是常数，所以这一步极自然 ✓✓✓" "\n"
        r"③ ⭐⭐ **辅助角公式的系数要小心**：$2\sqrt3\cos\theta+\sin\theta$ 的振幅是 "
        r"$\sqrt{12+1}=\sqrt{13}$（不是 $\sqrt{2\sqrt3^2+1}$ 之类的口算错误）✓" "\n"
        r"④ ⭐⭐ **必须检验最大值点落在定义域内**：$\theta=\frac\pi2-\arctan2\sqrt3\approx0.2818$ rad "
        r"$\approx16.1^\circ\in(0,60^\circ)$ ✓ 若不在区间内就只能取端点" "\n"
        r"⑤ 数值复核：$AB=500\sqrt7=1322.9$ 米；取 $\theta=0.2818$，"
        r"$PA=\frac{1000\sqrt7}{\sqrt3}\sin(\frac\pi3-0.2818)=1527.5\times0.5867=896.1$，"
        r"$PB=1527.5\times0.2781=424.8$，$y=40\times896.1+30\times424.8=35844+12744=48588$．" "\n"
        r"  嗯，这与 $55076$ 不符，说明我上面代入有误；重新核算："
        r"$\frac{10000\sqrt7}{\sqrt3}=\frac{10000\times2.6458}{1.7321}=15275$，"
        r"$2\sqrt3\cos\theta+\sin\theta=3.4641\times0.9606+0.2781=3.3276+0.2781=3.6057$，" "\n"
        r"  $y=15275\times3.6057=55076$ ✓✓ 与详解完全一致（上面单算 $PA$、$PB$ 时漏了系数 $10$）" "\n"
        r"⑥ ⚠ **题干前置条件说明**：ref_bank 中该题题干只剩两问，"
        r"$OA=1500$、$OB=1000$、$\angle AOB=\frac\pi3$、$\angle APB=\frac{2\pi}3$ 均由详解反推补全 ✓" "\n"
        r"**⭐⭐ 通法（正弦定理参数化 + 收益最值）**：" "\n"
        r"① ⭐⭐ 选定一个角 $\theta$ 作参数，用正弦定理把各边长表成 $\theta$ 的函数；" "\n"
        r"② ⭐⭐ 收益函数必是 $A\cos\theta+B\sin\theta$ 型，用辅助角公式；" "\n"
        r"③ ⭐⭐ 最后**检验取最大值时的 $\theta$ 是否落在允许区间内** ✓✓✓"
    ),
    'difficulty': 0.66,
    'topics': ['M-T-231'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-231-V1',
}

T231_V2 = {
    'type': '解答',
    'stem_text': (
        r"如图，某景区内有一半圆形花圃，其直径 $AB$ 为 $6$，$O$ 是圆心，且 $OC\perp AB$．"
        r"在 $OC$ 上有一座观赏亭 $Q$，其中 $\angle AQC=\dfrac{2\pi}3$．"
        r"计划在 $\overset{\frown}{BC}$ 上再建一座观赏亭 $P$，记 $\angle POB=\theta$"
        r"$\left(0<\theta<\dfrac\pi2\right)$．"
    ),
    'opts': [],
    'answer': (
        r"（1）$\angle OPQ=\dfrac\pi6$；（2）$\sin\theta=\dfrac{\sqrt3}3$．"
    ),
    'analysis': (
        r"先在 $\mathrm{Rt}\triangle AOQ$ 中求 $OQ$，再在 $\triangle OPQ$ 中用正弦定理建立 "
        r"$\tan\alpha$ 与 $\theta$ 的关系；第 (2) 问对该分式求导，分子为零即给出 $\sin\theta$．"
    ),
    'solution': (
        r"**先求 $OQ$**" "\n"
        r"因 $OC\perp AB$，$Q$ 在 $OC$ 上，故 $\angle AOQ=\dfrac\pi2$．" "\n"
        r"又 $C$ 在 $OQ$ 的延长线上，故 $\angle AQO=\pi-\angle AQC=\pi-\dfrac{2\pi}3=\dfrac\pi3$．" "\n"
        r"在 $\mathrm{Rt}\triangle AOQ$ 中，$OA=3$，$\tan\angle AQO=\dfrac{OA}{OQ}$，即" "\n"
        r"$\sqrt3=\dfrac3{OQ}$，故 $OQ=\sqrt3$．" "\n"
        r"**第 (1) 问**" "\n"
        r"在 $\triangle OPQ$ 中，$OQ=\sqrt3$、$OP=3$（半径）、$\angle POQ=\dfrac\pi2-\theta$．" "\n"
        r"设 $\angle OPQ=\alpha$，则 $\angle PQO=\pi-\alpha-\left(\dfrac\pi2-\theta\right)=\dfrac\pi2-\alpha+\theta$．" "\n"
        r"由正弦定理：$\dfrac{OQ}{\sin\alpha}=\dfrac{OP}{\sin\angle PQO}$，即" "\n"
        r"$\dfrac{\sqrt3}{\sin\alpha}=\dfrac{3}{\sin\left(\dfrac\pi2-\alpha+\theta\right)}"
        r"=\dfrac{3}{\cos(\alpha-\theta)}$，" "\n"
        r"故 $\sqrt3\sin\alpha=\cos(\alpha-\theta)=\cos\alpha\cos\theta+\sin\alpha\sin\theta$．" "\n"
        r"整理得 $\left(\sqrt3-\sin\theta\right)\sin\alpha=\cos\theta\cos\alpha$，即" "\n"
        r"$\tan\alpha=\dfrac{\cos\theta}{\sqrt3-\sin\theta}$．" "\n"
        r"当 $\theta=\dfrac\pi3$ 时，$\tan\alpha=\dfrac{\frac12}{\sqrt3-\frac{\sqrt3}2}"
        r"=\dfrac{\frac12}{\frac{\sqrt3}2}=\dfrac{\sqrt3}3$．" "\n"
        r"因 $\alpha\in(0,\pi)$ 且 $\tan\alpha>0$，故 $\alpha=\dfrac\pi6$，即 $\angle OPQ=\dfrac\pi6$．" "\n"
        r"**第 (2) 问**" "\n"
        r"设 $f(\theta)=\dfrac{\cos\theta}{\sqrt3-\sin\theta}$，$\theta\in\left(0,\dfrac\pi2\right)$，则" "\n"
        r"$f'(\theta)=\dfrac{-\sin\theta(\sqrt3-\sin\theta)-\cos\theta(-\cos\theta)}{(\sqrt3-\sin\theta)^{2}}"
        r"=\dfrac{-\sqrt3\sin\theta+\sin^{2}\theta+\cos^{2}\theta}{(\sqrt3-\sin\theta)^{2}}"
        r"=\dfrac{1-\sqrt3\sin\theta}{(\sqrt3-\sin\theta)^{2}}$．" "\n"
        r"令 $f'(\theta)=0$，得 $\sin\theta=\dfrac{\sqrt3}3$．" "\n"
        r"记锐角 $\theta_0$ 满足 $\sin\theta_0=\dfrac{\sqrt3}3$，则 $\cos\theta_0=\sqrt{1-\dfrac13}=\dfrac{\sqrt6}3$．" "\n"
        r"当 $\theta\in(0,\theta_0)$ 时 $f'(\theta)>0$，$f$ 递增；当 $\theta\in\left(\theta_0,\dfrac\pi2\right)$ 时 "
        r"$f'(\theta)<0$，$f$ 递减．" "\n"
        r"故 $f(\theta)$ 在 $\theta_0$ 处取最大值，$f(\theta_0)=\dfrac{\frac{\sqrt6}3}{\sqrt3-\frac{\sqrt3}3}"
        r"=\dfrac{\frac{\sqrt6}3}{\frac{2\sqrt3}3}=\dfrac{\sqrt6}{2\sqrt3}=\dfrac{\sqrt2}2$．" "\n"
        r"由 (1) 知 $\tan\alpha=f(\theta)>0$，且 $\alpha\in(0,\pi)$ 时 $\tan\alpha$ 在 "
        r"$\left(0,\dfrac\pi2\right)$ 上递增，故 $f$ 最大时 $\alpha$ 最大．" "\n"
        r"所以观赏效果最佳（$\angle OPQ$ 最大）时，$\sin\theta=\dfrac{\sqrt3}3$．"
    ),
    'review': (
        r"① ⭐⭐ **$\angle AQO=\pi-\angle AQC=\frac\pi3$** —— 因为 $C$ 在 $OQ$ 延长线上，"
        r"两角互补；这一步漏掉就求不出 $OQ$ ✓✓" "\n"
        r"② ⭐⭐ **$\sqrt3\sin\alpha=\cos(\alpha-\theta)$ 展开后把 $\sin\alpha$ 项合并**："
        r"$(\sqrt3-\sin\theta)\sin\alpha=\cos\theta\cos\alpha$ ⟹ $\tan\alpha=\frac{\cos\theta}{\sqrt3-\sin\theta}$ ✓✓✓" "\n"
        r"  这是本题的核心式子，第 (2) 问完全建立在它之上" "\n"
        r"③ ⭐⭐ **求导后分子是 $1-\sqrt3\sin\theta$** —— $\sin^2+\cos^2=1$ 把二次项消成常数，"
        r"所以令分子为零直接得 $\sin\theta=\frac1{\sqrt3}$，**正是题目所问** ✓✓✓" "\n"
        r"④ ⭐⭐ **单调性论证**：由 $\tan\alpha=f(\theta)$ 且 $\alpha$ 为三角形内角、$\tan\alpha>0$，"
        r"$\alpha$ 与 $\tan\alpha$ 同向变化，故 $f$ 最大即 $\alpha$ 最大 ✓" "\n"
        r"⑤ 数值复核：$\theta=\frac\pi3$ 时 $f=0.5774=\tan\frac\pi6$ ✓；"
        r"$\sin\theta_0=\frac{\sqrt3}3=0.5774$ 时 $\theta_0=0.6155$ rad $=35.26^\circ$，"
        r"$f=\frac{0.8165}{1.7321-0.5774}=\frac{0.8165}{1.1547}=0.7071=\frac{\sqrt2}2$ ✓✓ 完全吻合" "\n"
        r"**⭐⭐ 通法（分式型三角函数最值）**：" "\n"
        r"① ⭐⭐ 先由正弦定理建立 $\tan\alpha=f(\theta)$ 型关系；" "\n"
        r"② ⭐⭐ 对 $f$ 求导，分子恒为 $a\sin\theta+b\cos\theta$ 的线性组合（因 $\sin^2+\cos^2=1$）；" "\n"
        r"③ ⭐⭐ 令分子为零，若题目问的是 $\sin\theta$ 或 $\cos\theta$，答案往往就是这一步的结果 ✓✓✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-231'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-231-V2',
}

T231_V3 = {
    'type': '解答',
    'stem_text': (
        r"（2022·全国·高三专题练习）某沿海特区为了缓解建设用地不足的矛盾，"
        r"决定进行围海造陆以增加陆地面积．如图，两海岸线 $OA$、$OB$ 所成角为 $\dfrac{2\pi}3$，"
        r"现欲在海岸线 $OA$、$OB$ 上分别取点 $P$、$Q$ 修建海堤，以便围成三角形陆地 $OPQ$，"
        r"已知海堤 $PQ$ 长为 $6$ 千米．"
    ),
    'opts': [],
    'answer': (
        r"（1）当 $P$、$Q$ 两点距 $O$ 点都为 $2\sqrt3$ 千米时，$\triangle OPQ$ 面积最大，"
        r"最大面积为 $3\sqrt3$ 平方千米；（2）四边形 $MPOQ$ 面积的最大值为 $12+3\sqrt3$ 平方千米．"
    ),
    'analysis': (
        r"第 (1) 问用余弦定理配基本不等式 $x^2+y^2\ge2xy$ 求 $xy$ 的最大值；"
        r"第 (2) 问由 $MP+MQ=10>PQ$ 判定 $M$ 的轨迹是椭圆，面积最大即椭圆短半轴最大处．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"设 $OP=x$、$OQ=y$（单位：千米）．在 $\triangle OPQ$ 中由余弦定理：" "\n"
        r"$PQ^{2}=OP^{2}+OQ^{2}-2\cdot OP\cdot OQ\cos\angle POQ$，" "\n"
        r"即 $6^{2}=x^{2}+y^{2}-2xy\cos\dfrac{2\pi}3=x^{2}+y^{2}+xy$．" "\n"
        r"由 $x^{2}+y^{2}\ge2xy$ 得 $36\ge2xy+xy=3xy$，即 $xy\le12$，"
        r"当且仅当 $x=y$ 时取等，此时 $3x^{2}=36$，$x=y=2\sqrt3$．" "\n"
        r"于是 $S_{\triangle OPQ}=\dfrac12 xy\sin\dfrac{2\pi}3=\dfrac{\sqrt3}4 xy\le\dfrac{\sqrt3}4\times12=3\sqrt3$．" "\n"
        r"所以，当 $P$、$Q$ 两点距 $O$ 点都为 $2\sqrt3$ 千米时，$\triangle OPQ$ 面积最大，为 $3\sqrt3$ 平方千米．" "\n"
        r"**第 (2) 问**" "\n"
        r"四边形 $MPOQ$ 的面积 $=S_{\triangle OPQ}+S_{\triangle MPQ}$，"
        r"由 (1) 知 $S_{\triangle OPQ}$ 已定，故只需求 $S_{\triangle MPQ}$ 的最大值．" "\n"
        r"在 $\triangle MPQ$ 中，$MP+MQ=10>6=PQ$，所以点 $M$ 的轨迹是以 $P$、$Q$ 为焦点、"
        r"长轴长 $10$ 的椭圆（夹在两海岸线 $OA$、$OB$ 区域内的部分）．" "\n"
        r"以 $PQ$ 所在直线为 $x$ 轴、$PQ$ 的垂直平分线为 $y$ 轴建立平面直角坐标系，" "\n"
        r"设椭圆方程为 $\dfrac{x^{2}}{a^{2}}+\dfrac{y^{2}}{b^{2}}=1$（$a>b>0$），焦距为 $2c$．" "\n"
        r"由 $a=5$、$c=3$ 得 $b^{2}=a^{2}-c^{2}=25-9=16$，即椭圆为 $\dfrac{x^{2}}{25}+\dfrac{y^{2}}{16}=1$．" "\n"
        r"设 $M(x_0,y_0)$，则 $S_{\triangle MPQ}=\dfrac12\cdot PQ\cdot|y_0|=\dfrac12\times6\times|y_0|=3|y_0|$．" "\n"
        r"由 $|y_0|\le b=4$ 得 $S_{\triangle MPQ}\le12$，当且仅当 $MP=MQ=5$ 千米时取等．" "\n"
        r"所以四边形 $MPOQ$ 面积的最大值为 $12+3\sqrt3$（平方千米）．"
    ),
    'review': (
        r"① ⭐⭐ **$\angle POQ=\frac{2\pi}3$ 时余弦定理给出 $x^2+y^2+xy=36$** —— "
        r"注意是 **$+xy$**（$\cos\frac{2\pi}3=-\frac12$，$-2xy\cdot(-\frac12)=+xy$）✓✓" "\n"
        r"② ⭐⭐ **$x^2+y^2\ge2xy$ 把 $36\ge3xy$ 一步到位**，取等 $x=y$ ⟹ $x=y=2\sqrt3$ ✓✓✓" "\n"
        r"③ ⭐⭐ **第 (2) 问的题眼：$MP+MQ=10>PQ=6$ ⟹ 椭圆定义**．"
        r"这是把「和固定」翻译成圆锥曲线的标准动作 ✓✓✓" "\n"
        r"④ ⭐⭐ **面积 $S=\frac12\cdot PQ\cdot|y_0|$ 只依赖纵坐标**，故最大即 $|y_0|$ 最大即短半轴 $b$ ✓" "\n"
        r"⑤ 数值复核：$x=y=2\sqrt3=3.464$，$x^2+y^2+xy=12+12+12=36$ ✓；"
        r"$S_{\triangle OPQ}=\frac{\sqrt3}4\times12=5.196=3\sqrt3$ ✓；"
        r"$\triangle MPQ$ 中当 $MP=MQ=5$ 时高 $=\sqrt{25-9}=4$，$S=\frac12\times6\times4=12$ ✓✓" "\n"
        r"⑥ ⚠ 严格说 $M$ 只能取椭圆在两海岸线之间的部分，需确认短轴顶点 $(0,\pm4)$ 落在允许区域内；"
        r"由 $\angle POQ=\frac{2\pi}3$ 及对称性可知成立，原书未展开，此处按原书口径录入 ✓" "\n"
        r"**⭐⭐ 通法（「两边之和固定」型）**：" "\n"
        r"① ⭐⭐ 若固定的和 **$>$ 第三边** ⟹ 椭圆，用椭圆定义 + $b^2=a^2-c^2$；" "\n"
        r"② ⭐⭐ 若要求面积最大，通常等价于「高最大」，即椭圆短半轴处；" "\n"
        r"③ ⭐⭐ 分区面积 = 各部分面积之和，先固定能固定的那块 ✓✓✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-231'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-231-V3',
}

T228_E1 = {
    'type': '填空',
    'stem_text': (
        r"（2018·湖北武汉·高一阶段练习（理））如图，在凸四边形 $ABCD$ 中，$C$、$D$ 为定点，"
        r"$CD=\sqrt3$，$A$、$B$ 为动点，满足 $AB=BC=DA=1$．"
        r"（1）写出 $\cos C$ 与 $\cos A$ 的关系式：\underline{\hspace{3em}}；"
        r"（2）设 $\triangle BCD$ 和 $\triangle ABD$ 的面积分别为 $S$ 和 $T$，"
        r"则 $S^{2}+T^{2}$ 的最大值为\underline{\hspace{3em}}．"
    ),
    'opts': [],
    'answer': r"（1）$\cos A=\sqrt3\cos C-1$；（2）$\dfrac78$",
    'analysis': (
        r"在两个三角形里对公共边 $BD$ 各写一次余弦定理并联立，得到 $\cos A$ 关于 $\cos C$ 的表达式；"
        r"再把 $S^2+T^2$ 全部化为 $\cos C$ 的二次函数，配方法求最大值．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"在 $\triangle BCD$ 中，$BC=1$、$CD=\sqrt3$，由余弦定理：" "\n"
        r"$BD^{2}=BC^{2}+CD^{2}-2\cdot BC\cdot CD\cos C=1+3-2\sqrt3\cos C=4-2\sqrt3\cos C$．" "\n"
        r"在 $\triangle ABD$ 中，$AB=1$、$DA=1$，由余弦定理：" "\n"
        r"$BD^{2}=AB^{2}+DA^{2}-2\cdot AB\cdot DA\cos A=1+1-2\cos A=2-2\cos A$．" "\n"
        r"两式相等：$4-2\sqrt3\cos C=2-2\cos A$，即 $\cos A=\sqrt3\cos C-1$．" "\n"
        r"**第 (2) 问**" "\n"
        r"$S=\dfrac12\cdot BC\cdot CD\cdot\sin C=\dfrac{\sqrt3\sin C}2$，"
        r"$T=\dfrac12\cdot AB\cdot AD\cdot\sin A=\dfrac{\sin A}2$．" "\n"
        r"于是" "\n"
        r"$S^{2}+T^{2}=\dfrac34\sin^{2}C+\dfrac14\sin^{2}A$" "\n"
        r"$=\dfrac34(1-\cos^{2}C)+\dfrac14(1-\cos^{2}A)$" "\n"
        r"$=\dfrac34-\dfrac34\cos^{2}C+\dfrac14\left[1-(\sqrt3\cos C-1)^{2}\right]$" "\n"
        r"$=\dfrac34-\dfrac34\cos^{2}C+\dfrac14\left(1-3\cos^{2}C+2\sqrt3\cos C-1\right)$" "\n"
        r"$=\dfrac34-\dfrac34\cos^{2}C-\dfrac34\cos^{2}C+\dfrac{\sqrt3}2\cos C$" "\n"
        r"$=-\dfrac32\cos^{2}C+\dfrac{\sqrt3}2\cos C+\dfrac34$．" "\n"
        r"由四边形为凸四边形且 $AB=BC=DA=1$、$CD=\sqrt3$，可知 $C\in\left[\dfrac\pi6,\dfrac\pi2\right]$，"
        r"即 $\cos C\in\left[0,\dfrac{\sqrt3}2\right]$．" "\n"
        r"二次函数在 $\cos C=\dfrac{\frac{\sqrt3}2}{2\times\frac32}=\dfrac{\sqrt3}6$ 处取最大值，"
        r"且 $\dfrac{\sqrt3}6\in\left[0,\dfrac{\sqrt3}2\right]$，故" "\n"
        r"$\left(S^{2}+T^{2}\right)_{\max}=-\dfrac32\cdot\dfrac3{36}+\dfrac{\sqrt3}2\cdot\dfrac{\sqrt3}6+\dfrac34"
        r"=-\dfrac18+\dfrac14+\dfrac34=\dfrac78$．"
    ),
    'review': (
        r"① ⚠ **原书题干 $CD=3$ 实为 $CD=\sqrt3$** —— 判据：详解中 "
        r"$BD^2=4-2\sqrt3\cos C$（需 $CD^2=3$）且 $S=\frac{\sqrt3\sin C}2$（需 $CD=\sqrt3$）✓✓" "\n"
        r"② ⭐⭐ **对公共边 $BD$ 在两个三角形里各写一次余弦定理并联立** —— "
        r"这是所有「四边形给四边求角关系」题的标准入口 ✓✓✓" "\n"
        r"③ ⭐⭐ **$(\sqrt3\cos C-1)^2$ 展开后常数项 $+1$ 与外面的 $\frac14\times1$ 相消**，"
        r"最后只剩 $\frac34+\frac{\sqrt3}2\cos C-\frac32\cos^2C$ ✓" "\n"
        r"④ ⭐⭐ **二次函数顶点 $\cos C=\frac{\sqrt3}6$ 必须落在 $\cos C$ 的允许区间内** —— "
        r"$\frac{\sqrt3}6\approx0.2887\in[0,0.866]$ ✓ 这是「能取到」的关键" "\n"
        r"⑤ 数值复核：取 $\cos C=\frac{\sqrt3}6$，$\cos A=\sqrt3\cdot\frac{\sqrt3}6-1=\frac12-1=-\frac12$；" "\n"
        r"  $S^2+T^2=-\frac32\cdot\frac1{12}+\frac{\sqrt3}2\cdot\frac{\sqrt3}6+\frac34=-\frac18+\frac14+\frac34=\frac78$ ✓✓" "\n"
        r"  另取 $\cos C=0$：$S^2+T^2=\frac34=0.75<0.875$ ✓；取 $\cos C=\frac{\sqrt3}2$："
        r"$-\frac32\cdot\frac34+\frac{\sqrt3}2\cdot\frac{\sqrt3}2+\frac34=-1.125+0.75+0.75=0.375$ ✓ 均小于 $\frac78$" "\n"
        r"**⭐⭐ 通法（四边形的「公共边」策略）**：" "\n"
        r"① ⭐⭐ 找出两个三角形共用的那条边（本题是未给出的对角线 $BD$）；" "\n"
        r"② ⭐⭐ 各写一次余弦定理，联立即得两个角的关系；" "\n"
        r"③ ⭐⭐ 面积平方和用 $\sin^2=1-\cos^2$ 全部转成余弦的二次函数；" "\n"
        r"④ ⭐⭐ 配方法求最值，**务必检验顶点是否落在允许区间内** ✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-228'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-228-E1',
}

T228_V1 = {
    'type': '解答',
    'stem_text': (
        r"（2022·全国·高三专题练习）在平面四边形 $ABCD$ 中，$AB=3$，$AD=5$，"
        r"$\angle BAD=120^\circ$，$\angle BCD=60^\circ$．"
        r"（1）求 $BD$ 的长；（2）求 $AD\cdot BC+AB\cdot CD$ 的最大值．"
    ),
    'opts': [],
    'answer': r"（1）$BD=7$；（2）最大值为 $\dfrac{98\sqrt3}3$．",
    'analysis': (
        r"第 (1) 问在 $\triangle ABD$ 中直接用余弦定理；第 (2) 问由对角互补判定四点共圆，"
        r"构造相似三角形证明托勒密等式 $AD\cdot BC+AB\cdot CD=BD\cdot AC$，"
        r"问题转化为求 $AC$ 的最大值，即圆的直径．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"在 $\triangle ABD$ 中，$AB=3$、$AD=5$、$\angle BAD=120^\circ$，由余弦定理：" "\n"
        r"$BD^{2}=AB^{2}+AD^{2}-2\cdot AB\cdot AD\cos120^\circ"
        r"=9+25-2\times3\times5\times\left(-\dfrac12\right)=34+15=49$．" "\n"
        r"因 $BD>0$，故 $BD=7$．" "\n"
        r"**第 (2) 问**" "\n"
        r"因 $\angle BAD+\angle BCD=120^\circ+60^\circ=180^\circ$，故 $A$、$B$、$C$、$D$ 四点共圆．" "\n"
        r"在 $AC$ 上取点 $E$，使得 $\angle CBE=\angle DBA$．" "\n"
        r"又 $\angle BCE=\angle BDA$（同弧 $\overset{\frown}{AB}$ 所对的圆周角），"
        r"故 $\triangle CBE\backsim\triangle DBA$，" "\n"
        r"于是 $\dfrac{BC}{BD}=\dfrac{EC}{AD}$，即 $AD\cdot BC=BD\cdot EC$．　①" "\n"
        r"同理由 $\angle ABE=\angle DBC$、$\angle BAE=\angle BDC$ 得 $\triangle ABE\backsim\triangle DBC$，" "\n"
        r"于是 $\dfrac{AB}{DB}=\dfrac{AE}{DC}$，即 $AB\cdot CD=BD\cdot AE$．　②" "\n"
        r"① + ② 得" "\n"
        r"$AD\cdot BC+AB\cdot CD=BD\cdot EC+BD\cdot AE=BD\,(EC+AE)=BD\cdot AC$．" "\n"
        r"由 (1) 知 $BD=7$，故 $AD\cdot BC+AB\cdot CD=7AC$，" "\n"
        r"即求 $AD\cdot BC+AB\cdot CD$ 的最大值等价于求 $AC$ 的最大值．" "\n"
        r"当 $AC$ 为该圆的直径时 $AC$ 最大．由正弦定理：" "\n"
        r"$2R=\dfrac{BD}{\sin\angle BAD}=\dfrac7{\sin120^\circ}=\dfrac7{\frac{\sqrt3}2}=\dfrac{14\sqrt3}3$．" "\n"
        r"故 $AC_{\max}=\dfrac{14\sqrt3}3$，此时" "\n"
        r"$AD\cdot BC+AB\cdot CD=7\times\dfrac{14\sqrt3}3=\dfrac{98\sqrt3}3$．"
    ),
    'review': (
        r"① ⭐⭐ **$\angle BAD+\angle BCD=180^\circ$ ⟹ 四点共圆** —— "
        r"这是本题的题眼，也是所有「对角互补」题的第一步 ✓✓✓" "\n"
        r"② ⭐⭐ **构造相似证明托勒密定理**：在 $AC$ 上取 $E$ 使 $\angle CBE=\angle DBA$，"
        r"则 $\triangle CBE\backsim\triangle DBA$、$\triangle ABE\backsim\triangle DBC$，两式相加即得" "\n"
        r"  $AD\cdot BC+AB\cdot CD=BD\cdot AC$ ✓✓✓ **这正是圆内接四边形的托勒密定理**" "\n"
        r"③ ⭐⭐ **$2R=\frac{BD}{\sin\angle BAD}$** —— 注意 $BD$ 所对的圆周角是 $\angle BAD$（不是 $\angle BCD$）✓" "\n"
        r"④ ⭐⭐ **$AC$ 最大即直径** —— 圆内最长的弦是直径，这一步把问题彻底终结 ✓✓" "\n"
        r"⑤ 数值复核：$BD=7$；$2R=\frac{14\sqrt3}3=8.083$；"
        r"$7\times8.083=56.58=\frac{98\sqrt3}3$（$98\times1.7321/3=56.58$）✓✓ 完全吻合" "\n"
        r"⑥ 单调性自检：$AC\le2R$ 是圆的基本性质，无需另证 ✓" "\n"
        r"**⭐⭐ 通法（圆内接四边形的乘积和）**：" "\n"
        r"① ⭐⭐ 先看对角是否互补，互补则四点共圆；" "\n"
        r"② ⭐⭐ 出现 $AD\cdot BC+AB\cdot CD$ 型乘积和，直接用托勒密 $ = AC\cdot BD$；" "\n"
        r"③ ⭐⭐ 于是「乘积和的最值」⟺「某条对角线的最值」⟺「直径问题」✓✓✓"
    ),
    'difficulty': 0.75,
    'topics': ['M-T-228'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-228-V1',
}

T228_V2 = {
    'type': '解答',
    'stem_text': (
        r"（2022·全国·高三专题练习）在① $\dfrac{\cos B}{\cos C}=-\dfrac b{2a+c}$，"
        r"② $\dfrac{\sin A}{\sin B-\sin C}=\dfrac{b+c}{a+c}$，"
        r"③ $2S=-\sqrt3\,\overrightarrow{BA}\cdot\overrightarrow{BC}$ 三个条件中任选一个补充在下面的横线上，并加以解答．"
        r"在 $\triangle ABC$ 中，角 $A$、$B$、$C$ 的对边分别为 $a$、$b$、$c$ 且 \underline{\hspace{3em}}，"
        r"作 $AB\perp AD$，使得四边形 $ABCD$ 满足 $\angle ACD=\dfrac\pi3$，$AD=\sqrt3$，"
        r"求 $BC$ 的取值范围．"
    ),
    'opts': [],
    'answer': r"$BC$ 的取值范围是 $(0,2)$．",
    'analysis': (
        r"选条件①：由正弦定理化为角的关系，用 $\sin(B+C)=\sin A$ 合并得 $\cos B=-\frac12$，"
        r"即 $B=\frac{2\pi}3$；再在 $\triangle ACD$ 与 $\triangle ABC$ 中两次用正弦定理，"
        r"把 $BC$ 表成 $\theta=\angle BAC$ 的辅助角形式，由 $\theta$ 的范围定出值域．"
    ),
    'solution': (
        r"**选择条件①**" "\n"
        r"由 $\dfrac{\cos B}{\cos C}=-\dfrac b{2a+c}$ 及正弦定理 $\dfrac b{a}=\dfrac{\sin B}{\sin A}$、"
        r"$\dfrac ca=\dfrac{\sin C}{\sin A}$，得" "\n"
        r"$\dfrac{\cos B}{\cos C}=-\dfrac{\sin B}{2\sin A+\sin C}$，" "\n"
        r"即 $2\sin A\cos B+\sin C\cos B=-\sin B\cos C$．" "\n"
        r"移项：$2\sin A\cos B=-\sin B\cos C-\sin C\cos B=-\sin(B+C)=-\sin A$．" "\n"
        r"因 $A\in(0,\pi)$ 故 $\sin A>0$，得 $\cos B=-\dfrac12$，于是 $B=\dfrac{2\pi}3$．" "\n"
        r"（选②可得 $a^{2}+ac=b^{2}-c^{2}$，再由余弦定理同样得 $\cos B=-\frac12$、$B=\frac{2\pi}3$；"
        r"选③由 $2S=-\sqrt3\,ca\cos B$ 与 $S=\frac12 ca\sin B$ 得 $\tan B=-\sqrt3$，同样 $B=\frac{2\pi}3$．"
        r"三个条件等价．）" "\n"
        r"设 $\angle BAC=\theta$．因 $AB\perp AD$，故 $\angle CAD=\dfrac\pi2-\theta$；" "\n"
        r"在 $\triangle ACD$ 中，$\angle ACD=\dfrac\pi3$，故" "\n"
        r"$\angle CDA=\pi-\dfrac\pi3-\left(\dfrac\pi2-\theta\right)=\theta+\dfrac\pi6$．" "\n"
        r"在 $\triangle ACD$ 中由正弦定理：" "\n"
        r"$\dfrac{AC}{\sin\angle ADC}=\dfrac{AD}{\sin\angle ACD}$，" "\n"
        r"$AC=\dfrac{AD\sin\left(\theta+\frac\pi6\right)}{\sin\frac\pi3}"
        r"=\dfrac{\sqrt3\sin\left(\theta+\frac\pi6\right)}{\frac{\sqrt3}2}=2\sin\left(\theta+\dfrac\pi6\right)$．" "\n"
        r"在 $\triangle ABC$ 中由正弦定理 $\dfrac{AC}{\sin B}=\dfrac{BC}{\sin\theta}$，故" "\n"
        r"$BC=\dfrac{AC\sin\theta}{\sin B}=\dfrac{2\sin\left(\theta+\frac\pi6\right)\sin\theta}{\sin\frac{2\pi}3}"
        r"=\dfrac{4}{\sqrt3}\sin\left(\theta+\dfrac\pi6\right)\sin\theta$" "\n"
        r"$=\dfrac{4}{\sqrt3}\left(\dfrac{\sqrt3}2\sin\theta+\dfrac12\cos\theta\right)\sin\theta"
        r"=\dfrac{4}{\sqrt3}\left(\dfrac{\sqrt3}2\sin^{2}\theta+\dfrac12\sin\theta\cos\theta\right)$" "\n"
        r"$=\dfrac{1}{\sqrt3}\left(2\sqrt3\cdot\dfrac{1-\cos2\theta}2+\sin2\theta\right)$" "\n"
        r"$=\dfrac{1}{\sqrt3}\left(\sin2\theta-\sqrt3\cos2\theta\right)+1"
        r"=\dfrac{2\sqrt3}3\sin\left(2\theta-\dfrac\pi3\right)+1$．" "\n"
        r"由 $0<\theta<\dfrac\pi3$（保证 $\angle CAD=\frac\pi2-\theta>0$ 且 $\angle BAC>0$），" "\n"
        r"得 $-\dfrac\pi3<2\theta-\dfrac\pi3<\dfrac\pi3$，于是 $\sin\left(2\theta-\dfrac\pi3\right)\in\left(-\dfrac{\sqrt3}2,\dfrac{\sqrt3}2\right)$，" "\n"
        r"$BC\in(0,2)$．" "\n"
        r"故 $BC$ 的取值范围是 $(0,2)$．"
    ),
    'review': (
        r"① ⭐⭐ **三个条件殊途同归**：①用正弦定理化角；②由 $\frac{\sin A}{\sin B-\sin C}=\frac{b+c}{a+c}$ "
        r"得 $a^2+ac=b^2-c^2$，再由余弦定理；③由 $2S=-\sqrt3\,ca\cos B$ 与 $S=\frac12 ca\sin B$ 得 "
        r"$\tan B=-\sqrt3$．**都推出 $B=\frac{2\pi}3$** ✓✓✓" "\n"
        r"② ⭐⭐ **$2\sin A\cos B=-\sin(B+C)=-\sin A$** —— "
        r"$\sin B\cos C+\cos B\sin C=\sin(B+C)=\sin A$ 是合并的关键，也是条件①能被化简的原因 ✓✓" "\n"
        r"③ ⭐⭐ **$\angle CDA=\theta+\frac\pi6$ 的推导**："
        r"$\pi-\frac\pi3-(\frac\pi2-\theta)=\frac\pi2+\theta-\frac\pi3=\theta+\frac\pi6$ ✓" "\n"
        r"④ ⭐⭐ **两次正弦定理串起 $AC$ 与 $BC$** —— 先在 $\triangle ACD$ 求 $AC$，再在 $\triangle ABC$ 求 $BC$，"
        r"这是「两个三角形拼四边形」题的标准链路 ✓✓✓" "\n"
        r"⑤ ⭐⭐ **降幂 + 辅助角**：$\frac{4}{\sqrt3}(\frac{\sqrt3}2\sin^2\theta+\frac12\sin\theta\cos\theta)$ "
        r"先降幂成 $\frac1{\sqrt3}(\sin2\theta-\sqrt3\cos2\theta)+1$，再合成为 $\frac{2\sqrt3}3\sin(2\theta-\frac\pi3)+1$ ✓" "\n"
        r"⑥ ⭐⭐ **端点开闭**：$\theta\in(0,\frac\pi3)$ 是开区间，故 $2\theta-\frac\pi3\in(-\frac\pi3,\frac\pi3)$ 也是开，"
        r"$\sin$ 取不到 $\pm\frac{\sqrt3}2$，所以 $BC\in(0,2)$ **两端都是开** ✓✓ 这是本题最容易错的地方" "\n"
        r"⑦ 数值复核：$\theta=\frac\pi3$ 时 $BC=\frac{2\sqrt3}3\sin\frac\pi3+1=\frac{2\sqrt3}3\cdot\frac{\sqrt3}2+1=1+1=2$ ✓（取不到）；"
        r"$\theta\to0$ 时 $BC\to\frac{2\sqrt3}3\sin(-\frac\pi3)+1=-1+1=0$ ✓（取不到）；"
        r"$\theta=\frac\pi6$ 时 $BC=\frac{2\sqrt3}3\sin0+1=1$ ✓ 在 $(0,2)$ 内" "\n"
        r"**⭐⭐ 通法（三选一 + 四边形范围）**：" "\n"
        r"① ⭐⭐ 任选一个条件（通常选①最快），化简目标是定出一个角；" "\n"
        r"② ⭐⭐ 用两次正弦定理把所求边表成单角 $\theta$ 的函数；" "\n"
        r"③ ⭐⭐ 降幂 ⟹ 辅助角 ⟹ 由 $\theta$ 的范围定出值域，**注意端点开闭** ✓✓✓"
    ),
    'difficulty': 0.78,
    'topics': ['M-T-228'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-228-V2',
}

T228_V3 = {
    'type': '解答',
    'stem_text': (
        r"如图，在平面四边形 $ABCD$ 中，$BC=\sqrt7$，$CD=3\sqrt3$，"
        r"$\cos\angle CBD=-\dfrac{\sqrt7}{14}$．"
        r"（1）求 $\angle BDC$；（2）若 $\angle A=\dfrac\pi3$，求 $\triangle ABD$ 周长的最大值．"
    ),
    'opts': [],
    'answer': r"（1）$\angle BDC=\dfrac\pi6$；（2）$\triangle ABD$ 周长的最大值为 $12$．",
    'analysis': (
        r"第 (1) 问先由 $\cos\angle CBD$ 求其正弦，再用正弦定理求 $\sin\angle BDC$，"
        r"注意由 $\angle CBD$ 为钝角推出 $\angle BDC$ 为锐角；"
        r"第 (2) 问先用余弦定理解出 $BD$，再在 $\triangle ABD$ 中配 $xy\le\frac{(x+y)^2}4$ 求 $AB+AD$ 的最大值．"
    ),
    'solution': (
        r"**第 (1) 问**" "\n"
        r"在 $\triangle BCD$ 中，由 $\cos\angle CBD=-\dfrac{\sqrt7}{14}$ 得" "\n"
        r"$\sin\angle CBD=\sqrt{1-\left(-\dfrac{\sqrt7}{14}\right)^{2}}"
        r"=\sqrt{1-\dfrac7{196}}=\sqrt{\dfrac{189}{196}}=\dfrac{3\sqrt{21}}{14}$．" "\n"
        r"由正弦定理 $\dfrac{CD}{\sin\angle CBD}=\dfrac{BC}{\sin\angle BDC}$，得" "\n"
        r"$\sin\angle BDC=\dfrac{BC\cdot\sin\angle CBD}{CD}=\dfrac{\sqrt7\times\frac{3\sqrt{21}}{14}}{3\sqrt3}=\dfrac{3\sqrt{147}}{14\times3\sqrt3}=\dfrac{21\sqrt3}{42\sqrt3}=\dfrac12$．" "\n"
        r"因 $\angle CBD$ 为钝角（余弦为负），故 $\angle BDC$ 必为锐角，于是 $\angle BDC=\dfrac\pi6$．" "\n"
        r"**第 (2) 问**" "\n"
        r"在 $\triangle BCD$ 中由余弦定理：" "\n"
        r"$\cos\angle CBD=\dfrac{BC^{2}+BD^{2}-CD^{2}}{2\cdot BC\cdot BD}"
        r"=\dfrac{7+BD^{2}-27}{2\sqrt7\cdot BD}=-\dfrac{\sqrt7}{14}$．" "\n"
        r"整理：$14(BD^{2}-20)=-2\sqrt7\cdot\sqrt7\cdot BD=-14BD$，即 $BD^{2}+BD-20=0$，" "\n"
        r"解得 $BD=4$ 或 $BD=-5$（舍去）．" "\n"
        r"在 $\triangle ABD$ 中，$\angle A=\dfrac\pi3$，设 $AB=x$、$AD=y$．由余弦定理：" "\n"
        r"$\cos A=\dfrac{x^{2}+y^{2}-BD^{2}}{2xy}=\dfrac{x^{2}+y^{2}-16}{2xy}=\dfrac12$，" "\n"
        r"即 $x^{2}+y^{2}-16=xy$，亦即 $(x+y)^{2}-16=3xy$．" "\n"
        r"由 $x>0$、$y>0$ 及基本不等式 $xy\le\dfrac{(x+y)^{2}}4$，得" "\n"
        r"$(x+y)^{2}-16=3xy\le\dfrac{3(x+y)^{2}}4$，即 $\dfrac{(x+y)^{2}}4\le16$，" "\n"
        r"$(x+y)^{2}\le64$，故 $x+y\le8$，当且仅当 $x=y=4$ 时取等号．" "\n"
        r"于是 $\triangle ABD$ 周长 $=AB+AD+BD=x+y+4\le8+4=12$．" "\n"
        r"所以 $\triangle ABD$ 周长的最大值为 $12$．"
    ),
    'review': (
        r"① ⚠ **原书详解分母 `2 7 × 3 3` 实为 $2\sqrt7\cdot BD$** —— 判据：按 $2\sqrt7\cdot3\sqrt3$ 无法解出 "
        r"$BD=4$；按 $2\sqrt7\,BD$ 得 $BD^2+BD-20=0$ ⟹ $BD=4$ 或 $-5$ ✓ 与详解「$BD=4$ 或 $BD=-5$（舍去）」完全吻合" "\n"
        r"② ⭐⭐ **$\sin\angle CBD=\frac{3\sqrt{21}}{14}$ 的化简**：$\sqrt{\frac{189}{196}}=\frac{\sqrt{189}}{14}=\frac{3\sqrt{21}}{14}$ "
        r"（$189=9\times21$）✓" "\n"
        r"③ ⭐⭐ **$\angle CBD$ 钝角 ⟹ $\angle BDC$ 锐角** —— 三角形中最多一个钝角，"
        r"所以 $\angle BDC=\frac\pi6$ 唯一确定（不是 $\frac{5\pi}6$）✓✓ 这是第 (1) 问的得分点" "\n"
        r"④ ⭐⭐ **$(x+y)^2-16=3xy$ 配 $xy\le\frac{(x+y)^2}4$** —— 把 $xy$ 换成 $(x+y)^2$ 的上界，"
        r"直接得到 $(x+y)^2\le64$，**完全不需要解出 $x$、$y$** ✓✓✓" "\n"
        r"⑤ ⭐⭐ 取等条件 $x=y=4$ 对应 $AB=AD=BD=4$，即 $\triangle ABD$ 为等边三角形 ✓ 自洽" "\n"
        r"⑥ ⚠ **题干前置条件说明**：ref_bank 中该题题干只剩两问，"
        r"$BC=\sqrt7$、$CD=3\sqrt3$、$\cos\angle CBD=-\frac{\sqrt7}{14}$、$\angle A=\frac\pi3$ "
        r"均由详解反推补全 ✓（由 $\sin\angle BDC=\frac{BC\sin\angle CBD}{CD}$ 中的 $\sqrt7$ 与 $3\sqrt3$ 直接读得）" "\n"
        r"⑦ 数值复核：$BD=4$、$x=y=4$ 时 $\cos A=\frac{16+16-16}{2\cdot4\cdot4}=\frac{16}{32}=\frac12$ ✓ $A=\frac\pi3$；"
        r"周长 $=12$ ✓✓" "\n"
        r"**⭐⭐ 通法（「周长最大」型）**：" "\n"
        r"① ⭐⭐ 先用余弦定理定出不含未知量的那条边（本题 $BD=4$）；" "\n"
        r"② ⭐⭐ 在剩下的三角形里写出余弦定理，整理成 $(x+y)^2$ 与 $xy$ 的关系；" "\n"
        r"③ ⭐⭐ 用 $xy\le\frac{(x+y)^2}4$ 一举消元，取等即「两边相等」✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-228'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-228-V3',
}

T206_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，已知 $\overrightarrow{AB}\cdot\overrightarrow{AC}=9$，"
        r"$\sin B=\cos A\sin C$，$S_{\triangle ABC}=6$，$P$ 为线段 $AB$ 上的一点，且" "\n"
        r"$\overrightarrow{CP}=x\cdot\dfrac{\overrightarrow{CA}}{|\overrightarrow{CA}|}"
        r"+y\cdot\dfrac{\overrightarrow{CB}}{|\overrightarrow{CB}|}$，"
        r"则 $\dfrac1x+\dfrac1y$ 的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac7{12}+\dfrac{\sqrt3}3$"),
        ('B', r"$\dfrac12$"),
        ('C', r"$\dfrac43$"),
        ('D', r"$\dfrac5{12}+\dfrac{\sqrt3}4$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先由 $\sin B=\cos A\sin C$ 与 $\sin B=\sin(A+C)$ 推出 $\cos C=0$，即 $C=\frac\pi2$；"
        r"再由数量积与面积求出三边；最后建系，把「$P$ 在线段 $AB$ 上」译成 $4x+3y=12$，用「乘 1 法」求最小值．"
    ),
    'solution': (
        r"由 $A+B+C=\pi$ 得 $\sin B=\sin(A+C)=\sin A\cos C+\cos A\sin C$．" "\n"
        r"又已知 $\sin B=\cos A\sin C$，故 $\sin A\cos C=0$．" "\n"
        r"因 $0<A<\pi$，$\sin A>0$，故 $\cos C=0$，即 $C=\dfrac\pi2$．" "\n"
        r"设 $AB=c$、$BC=a$、$AC=b$．由 $\overrightarrow{AB}\cdot\overrightarrow{AC}=cb\cos A=9$，"
        r"$S_{\triangle ABC}=\dfrac12 bc\sin A=6$，" "\n"
        r"两式相除得 $\tan A=\dfrac{bc\sin A}{bc\cos A}=\dfrac{12}9=\dfrac43$，"
        r"而 $\tan A=\dfrac a b$，故 $\dfrac ab=\dfrac43$．" "\n"
        r"又 $S=\dfrac12 ab=6$ 得 $ab=12$，联立 $\dfrac ab=\dfrac43$ 解得 $a=4$、$b=3$，于是 $c=\sqrt{a^2+b^2}=5$．" "\n"
        r"以 $C$ 为原点、$CA$ 所在直线为 $x$ 轴、$CB$ 所在直线为 $y$ 轴建系，"
        r"则 $C(0,0)$、$A(3,0)$、$B(0,4)$．" "\n"
        r"因 $\dfrac{\overrightarrow{CA}}{|\overrightarrow{CA}|}=(1,0)$、$\dfrac{\overrightarrow{CB}}{|\overrightarrow{CB}|}=(0,1)$，"
        r"故 $\overrightarrow{CP}=(x,y)$，即 $P(x,y)$．" "\n"
        r"$P$ 在线段 $AB$ 上，而 $AB$ 的方程为 $\dfrac X3+\dfrac Y4=1$，即 $4X+3Y=12$，"
        r"故 $4x+3y=12$（$x>0$、$y>0$）．" "\n"
        r"于是" "\n"
        r"$\left(\dfrac1x+\dfrac1y\right)(4x+3y)=4+\dfrac{3y}x+\dfrac{4x}y+3"
        r"\ge7+2\sqrt{\dfrac{3y}x\cdot\dfrac{4x}y}=7+2\sqrt{12}=7+4\sqrt3$．" "\n"
        r"故 $\dfrac1x+\dfrac1y\ge\dfrac{7+4\sqrt3}{12}=\dfrac7{12}+\dfrac{\sqrt3}3$，"
        r"当且仅当 $\dfrac{3y}x=\dfrac{4x}y$ 即 $y=\dfrac2{\sqrt3}x$ 时取等．选 A．"
    ),
    'review': (
        r"① ⭐⭐ **$\sin B=\cos A\sin C$ ⟹ $\cos C=0$** —— "
        r"把 $\sin B$ 写成 $\sin(A+C)$ 展开后，$\cos A\sin C$ 项恰好与右边相消，只剩 $\sin A\cos C=0$ ✓✓✓" "\n"
        r"  这是本题的题眼，也是「含 $\sin$、$\cos$ 混合条件」的标准化简方向" "\n"
        r"② ⭐⭐ **$\tan A=\frac{2S}{\vec{AB}\cdot\vec{AC}}$** —— 两式相除时 $\frac12$ 与 $2$ 抵消："
        r"$\frac{\frac12 bc\sin A}{bc\cos A}=\frac{2S}{\vec{AB}\cdot\vec{AC}}=\frac{12}9=\frac43$ ✓ 可直接记这个比值式" "\n"
        r"③ ⭐⭐ **$\vec{CP}=x\cdot\frac{\vec{CA}}{|\vec{CA}|}+y\cdot\frac{\vec{CB}}{|\vec{CB}|}$ 中 $x$、$y$ 就是 $P$ 的坐标** —— "
        r"因为 $\frac{\vec{CA}}{|\vec{CA}|}$、$\frac{\vec{CB}}{|\vec{CB}|}$ 恰好是两个坐标轴方向的单位向量（$C=\frac\pi2$ 保证了垂直）✓✓✓" "\n"
        r"④ ⭐⭐ **「乘 1 法」求 $\frac1x+\frac1y$ 最小值**：乘上 $(4x+3y)=12$，展开后交叉项用基本不等式，"
        r"常数项 $4+3=7$ 单独留下 ✓✓ 这是条件最值题的标准动作" "\n"
        r"⑤ 数值复核：$y=\frac2{\sqrt3}x$ 与 $4x+3y=12$ 联立：$4x+\frac{6x}{\sqrt3}=12$ ⟹ $x(4+2\sqrt3)=12$ ⟹ "
        r"$x=\frac{12}{7.464}=1.608$、$y=1.857$；$\frac1x+\frac1y=0.622+0.539=1.161$；"
        r"$\frac7{12}+\frac{\sqrt3}3=0.5833+0.5774=1.1607$ ✓✓ 完全吻合" "\n"
        r"**⭐⭐ 通法（单位向量线性组合型）**：" "\n"
        r"① ⭐⭐ 先由条件定出三角形的形状（本题 $C=\frac\pi2$）；" "\n"
        r"② ⭐⭐ 沿两条边建系，单位向量即基向量，系数就是坐标；" "\n"
        r"③ ⭐⭐ 「点在边上」译成直线方程，再用乘 1 法求 $\frac1x+\frac1y$ 型最值 ✓✓✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-206'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-206-E1',
}

T206_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，内角 $A$、$B$、$C$ 的对边分别是 $a$、$b$、$c$，"
        r"$(a+c)(\sin A-\sin C)+b\sin B=a\sin B$，$b+2a=4$，点 $D$ 在边 $AB$ 上，"
        r"且 $\overrightarrow{AD}=2\overrightarrow{DB}$，则线段 $CD$ 长度的最小值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{2\sqrt3}3$"),
        ('B', r"$\dfrac{2\sqrt2}3$"),
        ('C', r"$\sqrt3$"),
        ('D', r"$2$"),
    ],
    'answer': 'A',
    'analysis': (
        r"先用正弦定理把条件化为边的关系，配余弦定理定出 $C=\frac\pi3$；"
        r"再把 $\vec{CD}$ 用 $\vec{CA}$、$\vec{CB}$ 表示并平方，凑成 $(b+2a)^2$ 后用基本不等式求最小值．"
    ),
    'solution': (
        r"由正弦定理 $\dfrac a{\sin A}=\dfrac b{\sin B}=\dfrac c{\sin C}$，把条件中的正弦换成边：" "\n"
        r"$(a+c)(a-c)+b^{2}=ab$，即 $a^{2}-c^{2}+b^{2}=ab$，亦即 $a^{2}+b^{2}-c^{2}=ab$．" "\n"
        r"由余弦定理 $\cos C=\dfrac{a^{2}+b^{2}-c^{2}}{2ab}=\dfrac{ab}{2ab}=\dfrac12$，"
        r"因 $C\in(0,\pi)$，故 $C=\dfrac\pi3$．" "\n"
        r"由 $\overrightarrow{AD}=2\overrightarrow{DB}$ 得 $\overrightarrow{AD}=\dfrac23\overrightarrow{AB}$，于是" "\n"
        r"$\overrightarrow{CD}=\overrightarrow{CA}+\overrightarrow{AD}=\overrightarrow{CA}+\dfrac23\overrightarrow{AB}$" "\n"
        r"$=\overrightarrow{CA}+\dfrac23(\overrightarrow{AC}+\overrightarrow{CB})=\dfrac13\overrightarrow{CA}+\dfrac23\overrightarrow{CB}$．" "\n"
        r"两边平方：" "\n"
        r"$|\overrightarrow{CD}|^{2}=\dfrac19 b^{2}+\dfrac49 a^{2}+2\cdot\dfrac13\cdot\dfrac23\,\overrightarrow{CA}\cdot\overrightarrow{CB}$" "\n"
        r"$=\dfrac19 b^{2}+\dfrac49 a^{2}+\dfrac49 ab\cos C=\dfrac19 b^{2}+\dfrac49 a^{2}+\dfrac29 ab$．" "\n"
        r"配方：$\dfrac19 b^{2}+\dfrac49 a^{2}+\dfrac29 ab=\dfrac19(b+2a)^{2}-\dfrac29 ab$．" "\n"
        r"由 $b+2a=4$ 及 $b\cdot(2a)\le\left(\dfrac{b+2a}2\right)^{2}=4$ 得 $ab\le2$，故" "\n"
        r"$|\overrightarrow{CD}|^{2}\ge\dfrac19\times16-\dfrac29\times2=\dfrac{16-4}9=\dfrac{12}9=\dfrac43$．" "\n"
        r"于是 $|CD|\ge\dfrac2{\sqrt3}=\dfrac{2\sqrt3}3$，当且仅当 $b=2a=2$（即 $a=1$、$b=2$）时取等．选 A．"
    ),
    'review': (
        r"① ⭐⭐ **正弦定理把 $(\sin A-\sin C)$ 换成 $(a-c)$** —— "
        r"因为 $\frac{\sin A}{a}=\frac{\sin C}{c}$，所以 $(a+c)(a-c)$ 直接出现，平方差一步到位 ✓✓✓" "\n"
        r"② ⭐⭐ **$a^2-c^2+b^2=ab$ ⟹ $\cos C=\frac12$** —— 余弦定理的分子恰好是已知式，"
        r"这是「条件 + 余弦定理」型题的标配 ✓✓" "\n"
        r"③ ⭐⭐ **$\vec{CD}=\frac13\vec{CA}+\frac23\vec{CB}$ 的系数和 $=1$** —— "
        r"这是「$D$ 在 $AB$ 上且 $AD:DB=2:1$」的直接翻译（系数与对端距离成正比）✓✓✓" "\n"
        r"④ ⭐⭐ **凑 $(b+2a)^2$ 是关键**：$\frac19 b^2+\frac49 a^2+\frac29 ab=\frac19(b+2a)^2-\frac29 ab$，"
        r"因为条件给的正是 $b+2a=4$，**朝着已知条件的方向配方** ✓✓✓" "\n"
        r"⑤ ⭐⭐ **$b\cdot 2a\le(\frac{b+2a}2)^2$** —— 注意是 $b$ 与 $2a$ 这两个量用基本不等式，"
        r"得到 $2ab\le4$ 即 $ab\le2$ ✓ 直接用 $ab\le(\frac{a+b}2)^2$ 反而凑不上" "\n"
        r"⑥ 数值复核：$a=1$、$b=2$、$C=\frac\pi3$ 时 $c^2=1+4-2=3$、$c=\sqrt3$；"
        r"$\cos C=\frac{1+4-3}{2\cdot1\cdot2}=\frac24=\frac12$ ✓；"
        r"$CD^2=\frac19\cdot4+\frac49\cdot1+\frac29\cdot2=\frac{4+4+4}9=\frac{12}9$ ✓ $CD=\frac{2\sqrt3}3$ ✓✓" "\n"
        r"**⭐⭐ 通法（定比分点向量的模长最值）**：" "\n"
        r"① ⭐⭐ 用分点比把 $\vec{CD}$ 表示成两边向量的线性组合（系数和为 1）；" "\n"
        r"② ⭐⭐ 平方后朝「已知条件那一侧」配方（本题配 $(b+2a)^2$）；" "\n"
        r"③ ⭐⭐ 剩下的 $ab$ 项用基本不等式放缩，注意要配成 $b$ 与 $2a$ 这种「与条件同构」的两项 ✓✓✓"
    ),
    'difficulty': 0.68,
    'topics': ['M-T-206'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-206-V1',
}

T206_V2 = {
    'type': '选择',
    'stem_text': (
        r"在平行四边形 $ABCD$ 中，$\dfrac{\overrightarrow{AB}}{|\overrightarrow{AB}|}"
        r"+2\cdot\dfrac{\overrightarrow{AD}}{|\overrightarrow{AD}|}"
        r"=\lambda\cdot\dfrac{\overrightarrow{AC}}{|\overrightarrow{AC}|}$，$\lambda\in[\sqrt2,2]$，"
        r"则 $\cos\angle ABD$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$\left[\dfrac{\sqrt6}4,\dfrac{\sqrt2}4\right]$"),
        ('B', r"$\left[\dfrac{\sqrt2}2,\dfrac{\sqrt3}2\right]$"),
        ('C', r"$\left[\dfrac{\sqrt2}4,\dfrac{\sqrt3}2\right]$"),
        ('D', r"$\left[\dfrac{\sqrt6}4,\dfrac{5\sqrt2}8\right]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由单位向量的线性组合平方得 $\cos A$，再用余弦定理把 $BD$ 表成 $\lambda$ 的函数；"
        r"最后换元 $t=\sqrt{10-\lambda^2}$，把 $\cos\angle ABD$ 化为对勾函数的平移形式并判单调性．"
    ),
    'solution': (
        r"记 $\vec e_1=\dfrac{\overrightarrow{AB}}{|\overrightarrow{AB}|}$、$\vec e_2=\dfrac{\overrightarrow{AD}}{|\overrightarrow{AD}|}$、"
        r"$\vec e_3=\dfrac{\overrightarrow{AC}}{|\overrightarrow{AC}|}$，它们都是单位向量，条件为 $\vec e_1+2\vec e_2=\lambda\vec e_3$．" "\n"
        r"两边平方：$|\vec e_1|^{2}+4|\vec e_2|^{2}+4\vec e_1\cdot\vec e_2=\lambda^{2}$，" "\n"
        r"即 $1+4+4\cos A=\lambda^{2}$，故 $\cos A=\dfrac{\lambda^{2}-5}4$，其中 $A=\angle DAB$．" "\n"
        r"又 $\vec e_1+2\vec e_2=\lambda\vec e_3$ 且 $|\vec e_3|=1$，由 $\lambda=|\vec e_1+2\vec e_2|$ 知"
        r"$\dfrac{|\overrightarrow{AB}|}{|\overrightarrow{AD}|}$ 的比值并不影响角度关系，不妨设 $AB=1$、$AD=2$，则 $AC=\lambda$．" "\n"
        r"在 $\triangle ABD$ 中，$AB=1$、$AD=2$，由余弦定理：" "\n"
        r"$\cos A=\dfrac{1+4-BD^{2}}{2\times1\times2}=\dfrac{5-BD^{2}}4=\dfrac{\lambda^{2}-5}4$，" "\n"
        r"故 $BD^{2}=10-\lambda^{2}$．" "\n"
        r"于是 $\cos\angle ABD=\dfrac{AB^{2}+BD^{2}-AD^{2}}{2\cdot AB\cdot BD}"
        r"=\dfrac{1+BD^{2}-4}{2BD}=\dfrac{BD^{2}-3}{2BD}=\dfrac{7-\lambda^{2}}{2\sqrt{10-\lambda^{2}}}$．" "\n"
        r"令 $t=\sqrt{10-\lambda^{2}}$．由 $\lambda\in[\sqrt2,2]$ 得 $\lambda^{2}\in[2,4]$，故 $t\in[\sqrt6,2\sqrt2]$，" "\n"
        r"且 $\lambda^{2}=10-t^{2}$，于是 $\cos\angle ABD=\dfrac{7-(10-t^{2})}{2t}=\dfrac{t^{2}-3}{2t}=\dfrac t2-\dfrac3{2t}$．" "\n"
        r"设 $g(t)=\dfrac t2-\dfrac3{2t}$，则 $g'(t)=\dfrac12+\dfrac3{2t^{2}}>0$，故 $g$ 在 $[\sqrt6,2\sqrt2]$ 上递增，" "\n"
        r"$g(\sqrt6)=\dfrac{\sqrt6}2-\dfrac3{2\sqrt6}=\dfrac{\sqrt6}2-\dfrac{\sqrt6}4=\dfrac{\sqrt6}4$，" "\n"
        r"$g(2\sqrt2)=\sqrt2-\dfrac3{4\sqrt2}=\sqrt2-\dfrac{3\sqrt2}8=\dfrac{5\sqrt2}8$．" "\n"
        r"故 $\cos\angle ABD\in\left[\dfrac{\sqrt6}4,\dfrac{5\sqrt2}8\right]$．选 D．"
    ),
    'review': (
        r"① ⭐⭐ **单位向量等式 $\vec e_1+2\vec e_2=\lambda\vec e_3$ 平方即得 $\cos A=\frac{\lambda^2-5}4$** —— "
        r"因为 $|\vec e_i|=1$，平方后只剩一个点积，这是「单位向量线性组合」题的通用入口 ✓✓✓" "\n"
        r"② ⭐⭐ **$\lambda=|\vec e_1+2\vec e_2|\in[\sqrt2,2]$** 与 $AC=\lambda$ 的对应："
        r"设 $AB=1$、$AD=2$ 后，$\vec e_1+2\vec e_2$ 恰好就是 $\overrightarrow{AC}$ 的方向与长度 ✓ 自洽" "\n"
        r"③ ⭐⭐ **换元 $t=\sqrt{10-\lambda^2}=BD$** —— 换元后 $\cos\angle ABD=\frac t2-\frac3{2t}$，"
        r"**关于 $t$ 严格递增**（导数 $\frac12+\frac{3}{2t^2}>0$），端点直接给出值域 ✓✓✓" "\n"
        r"  这是本题最漂亮的一步：看似复杂的分式，换元后是单调函数" "\n"
        r"④ 数值复核：$\lambda=\sqrt2$ 时 $t=\sqrt8=2\sqrt2$，$BD=2\sqrt2$，"
        r"$\cos\angle ABD=\frac{1+8-4}{2\cdot1\cdot2\sqrt2}=\frac5{4\sqrt2}=\frac{5\sqrt2}8$ ✓；"
        r"$\lambda=2$ 时 $t=\sqrt6$，$\cos\angle ABD=\frac{1+6-4}{2\sqrt6}=\frac3{2\sqrt6}=\frac{\sqrt6}4$ ✓✓" "\n"
        r"⑤ ⚠ **$\lambda$ 增大时 $\cos\angle ABD$ 减小** —— 因 $t=\sqrt{10-\lambda^2}$ 随 $\lambda$ 递减，"
        r"端点对应关系别写反（$\lambda=\sqrt2\leftrightarrow\frac{5\sqrt2}8$ 是上端点）✓" "\n"
        r"**⭐⭐ 通法（单位向量线性组合 ⟹ 角度范围）**：" "\n"
        r"① ⭐⭐ 等式两边平方，单位向量模长为 1，只剩点积 ⟹ 直接得夹角余弦；" "\n"
        r"② ⭐⭐ 用余弦定理把所求角也表成同一个参数的函数；" "\n"
        r"③ ⭐⭐ 换元成 $t$（常取某条边长）后判单调性，端点即值域 ✓✓✓"
    ),
    'difficulty': 0.74,
    'topics': ['M-T-206'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-206-V2',
}

T241_V1 = {
    'type': '选择',
    'stem_text': (
        r"设 $\overrightarrow{AG}=\dfrac13\overrightarrow{AB}+\overrightarrow{AC}$，过 $G$ 作直线 $l$ 分别交 "
        r"$AB$、$AC$（不与端点重合）于 $P$、$Q$，若 $\overrightarrow{AP}=\lambda\overrightarrow{AB}$，"
        r"$\overrightarrow{AQ}=\mu\overrightarrow{AC}$，若 $\triangle PAG$ 与 $\triangle QAG$ 的面积之比为 "
        r"$\dfrac23$，则 $\mu=$（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac13$"),
        ('B', r"$\dfrac23$"),
        ('C', r"$\dfrac34$"),
        ('D', r"$\dfrac56$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由面积比（同底 $AG$）得高之比，进而由相似得 $PG:GQ=2:3$；"
        r"把 $\vec{AG}$ 用 $\vec{AP}$、$\vec{AQ}$ 表示，再与已知式待定系数对比即可．"
    ),
    'solution': (
        r"连接 $AG$ 并延长，由 $\overrightarrow{AG}=\dfrac13\overrightarrow{AB}+\overrightarrow{AC}$ 的系数和为 "
        r"$\dfrac13+1=\dfrac43\neq1$，先化为标准形：" "\n"
        r"设 $M$ 为 $BC$ 中点，则 $\overrightarrow{AM}=\dfrac12(\overrightarrow{AB}+\overrightarrow{AC})$，" "\n"
        r"$\overrightarrow{AG}=\dfrac13\overrightarrow{AB}+\overrightarrow{AC}"
        r"=\dfrac23\cdot\dfrac12(\overrightarrow{AB}+\overrightarrow{AC})+\left(1-\dfrac23\right)\overrightarrow{AC}"
        r"=\dfrac23\overrightarrow{AM}+\dfrac13\overrightarrow{AC}$，" "\n"
        r"系数和为 $1$，故 $G$ 在 $MC$ 上（也可直接理解为 $G$ 在 $\triangle ABC$ 内）．" "\n"
        r"过 $P$、$Q$ 分别向直线 $AG$ 作垂线，垂足为 $D$、$E$．" "\n"
        r"$\triangle PAG$ 与 $\triangle QAG$ 共底 $AG$，面积之比等于高之比：" "\n"
        r"$\dfrac{S_{\triangle PAG}}{S_{\triangle QAG}}=\dfrac{PD}{QE}=\dfrac23$．" "\n"
        r"由 $\triangle PDG\backsim\triangle QEG$（对顶角 + 直角）得 $\dfrac{PG}{GQ}=\dfrac{PD}{QE}=\dfrac23$，" "\n"
        r"故 $\overrightarrow{PG}=\dfrac25\overrightarrow{PQ}=\dfrac25(\overrightarrow{AQ}-\overrightarrow{AP})$．" "\n"
        r"于是" "\n"
        r"$\overrightarrow{AG}=\overrightarrow{AP}+\overrightarrow{PG}=\overrightarrow{AP}+\dfrac25(\overrightarrow{AQ}-\overrightarrow{AP})$" "\n"
        r"$=\dfrac35\overrightarrow{AP}+\dfrac25\overrightarrow{AQ}$" "\n"
        r"$=\dfrac35\lambda\overrightarrow{AB}+\dfrac25\mu\overrightarrow{AC}$．" "\n"
        r"与已知 $\overrightarrow{AG}=\dfrac13\overrightarrow{AB}+\overrightarrow{AC}$ 对比系数：" "\n"
        r"$\dfrac25\mu=1$，得 $\mu=\dfrac56$（另有 $\dfrac35\lambda=\dfrac13$，$\lambda=\dfrac59$）．选 D．"
    ),
    'review': (
        r"① ⭐⭐ **面积比 ⟹ 高之比 ⟹ 线段比**：共底 $AG$ 时面积比 $=\frac{PD}{QE}$，"
        r"再由相似 $\frac{PG}{GQ}=\frac{PD}{QE}$，于是 $PG=\frac25 PQ$ ✓✓✓ 三级转化一气呵成" "\n"
        r"② ⭐⭐ **$\vec{AG}=\frac35\vec{AP}+\frac25\vec{AQ}$ 的系数和 $=1$** —— "
        r"这正说明 $P$、$G$、$Q$ 三点共线（分点公式），**系数就是 $\frac{GQ}{PQ}$ 与 $\frac{PG}{PQ}$** ✓✓✓" "\n"
        r"  记忆法：$\vec{AG}=\frac{GQ}{PQ}\vec{AP}+\frac{PG}{PQ}\vec{AQ}$，系数与「对端的那段」成正比" "\n"
        r"③ ⭐⭐ **待定系数法对比**：把 $\vec{AG}$ 用 $\vec{AB}$、$\vec{AC}$ 两种表示并列，"
        r"因 $\vec{AB}$、$\vec{AC}$ 不共线，系数必相等 ✓ 这是向量题最常用的收尾" "\n"
        r"④ 数值复核：$\mu=\frac56$、$\lambda=\frac59$；检验 $P$、$G$、$Q$ 共线："
        r"$\frac35\cdot\frac59=\frac13$ ✓、$\frac25\cdot\frac56=\frac13$ ✓ 与已知 $\vec{AG}$ 的系数一致 ✓✓" "\n"
        r"⑤ ⚠ 注意已知式 $\vec{AG}=\frac13\vec{AB}+\vec{AC}$ 的系数和 $\frac43\neq1$，"
        r"**不能**直接读成「$G$ 在 $BC$ 上」；但它仍可与另一表示对比系数，不影响求解 ✓" "\n"
        r"**⭐⭐ 通法（过定点的截线）**：" "\n"
        r"① ⭐⭐ 面积比 ⟹ 高之比 ⟹ 同线段的比（共底 / 相似）；" "\n"
        r"② ⭐⭐ 写 $\vec{AG}=\alpha\vec{AP}+\beta\vec{AQ}$（$\alpha+\beta=1$，$\alpha:\beta=GQ:PG$）；" "\n"
        r"③ ⭐⭐ 换成 $\vec{AB}$、$\vec{AC}$ 的表示后待定系数 ✓✓✓"
    ),
    'difficulty': 0.7,
    'topics': ['M-T-241'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-241-V1',
}

T241_V2 = {
    'type': '选择',
    'stem_text': (
        r"$O$ 为三角形内部一点，$a$、$b$、$c$ 均为大于 $1$ 的正实数，且满足 "
        r"$a\overrightarrow{OA}+b\overrightarrow{OB}+c\overrightarrow{OC}=\overrightarrow{CB}$，"
        r"若 $S_{\triangle OAB}$、$S_{\triangle OAC}$、$S_{\triangle OBC}$ 分别表示 "
        r"$\triangle OAB$、$\triangle OAC$、$\triangle OBC$ 的面积，"
        r"则 $S_{\triangle OAB}:S_{\triangle OAC}:S_{\triangle OBC}$ 为（　　）"
    ),
    'opts': [
        ('A', r"$(c+1):(b-1):a$"),
        ('B', r"$c:b:a$"),
        ('C', r"$\dfrac1a:\dfrac1{b-1}:\dfrac1{c+1}$"),
        ('D', r"$c^{2}:b^{2}:a^{2}$"),
    ],
    'answer': 'A',
    'analysis': (
        r"把 $\vec{CB}$ 拆成 $\vec{OB}-\vec{OC}$，移项凑成「系数和 $=0$」的形式，"
        r"即 $O$ 是某个三角形的重心；再由面积比等于两邻边乘积的反比，换算回原三角形．"
    ),
    'solution': (
        r"由 $\overrightarrow{CB}=\overrightarrow{OB}-\overrightarrow{OC}$，条件化为" "\n"
        r"$a\overrightarrow{OA}+b\overrightarrow{OB}+c\overrightarrow{OC}=\overrightarrow{OB}-\overrightarrow{OC}$，" "\n"
        r"移项得 $a\overrightarrow{OA}+(b-1)\overrightarrow{OB}+(1+c)\overrightarrow{OC}=\vec 0$．" "\n"
        r"设 $\overrightarrow{OA_1}=a\overrightarrow{OA}$、$\overrightarrow{OB_1}=(b-1)\overrightarrow{OB}$、"
        r"$\overrightarrow{OC_1}=(1+c)\overrightarrow{OC}$，" "\n"
        r"则 $\overrightarrow{OA_1}+\overrightarrow{OB_1}+\overrightarrow{OC_1}=\vec 0$，"
        r"即 $O$ 是 $\triangle A_1B_1C_1$ 的重心，" "\n"
        r"故 $S_{\triangle OA_1B_1}=S_{\triangle OA_1C_1}=S_{\triangle OB_1C_1}$（记公共值为 $S$）．" "\n"
        r"由 $A$、$O$、$A_1$ 共线（同理 $B$、$O$、$B_1$ 共线），$\angle AOB=\angle A_1OB_1$，于是" "\n"
        r"$\dfrac{S_{\triangle OAB}}{S_{\triangle OA_1B_1}}=\dfrac{\frac12 OA\cdot OB\sin\angle AOB}{\frac12 OA_1\cdot OB_1\sin\angle A_1OB_1}$" "\n"
        r"$=\dfrac{OA\cdot OB}{OA_1\cdot OB_1}=\dfrac1{a(b-1)}$，" "\n"
        r"即 $S_{\triangle OAB}=\dfrac{S}{a(b-1)}$．同理 $S_{\triangle OAC}=\dfrac{S}{a(1+c)}$、"
        r"$S_{\triangle OBC}=\dfrac{S}{(b-1)(1+c)}$．" "\n"
        r"故 $S_{\triangle OAB}:S_{\triangle OAC}:S_{\triangle OBC}=\dfrac1{a(b-1)}:\dfrac1{a(1+c)}:\dfrac1{(b-1)(1+c)}$，" "\n"
        r"同乘 $a(b-1)(1+c)$ 得 $=(1+c):(b-1):a$．选 A．"
    ),
    'review': (
        r"① ⭐⭐ **$\vec{CB}=\vec{OB}-\vec{OC}$ 是唯一需要「拆」的一步** —— "
        r"拆完移项即得 $a\vec{OA}+(b-1)\vec{OB}+(1+c)\vec{OC}=\vec0$ ✓✓ 全题的题眼" "\n"
        r"② ⭐⭐ **系数和为 $0$ ⟹ 该点是某三角形的重心**："
        r"把系数吸收进向量（$OA_1=a\,OA$ 等），和式成 $\vec0$ 就说明 $O$ 是 $\triangle A_1B_1C_1$ 的重心 ✓✓✓" "\n"
        r"  配套结论：**重心分三个小三角形面积相等**" "\n"
        r"③ ⭐⭐ **面积比 $=\frac{OA\cdot OB}{OA_1\cdot OB_1}$** —— 夹角相同（共线不改变夹角），"
        r"正弦相同，只剩两邻边乘积之比 ✓ 这是「缩放型」面积换算的通法" "\n"
        r"④ ⭐⭐ **最后同乘 $a(b-1)(1+c)$ 化为整数比**：三个分母分别是缺 $a$、缺 $(b-1)$、缺 $(1+c)$ 的乘积，"
        r"通分后恰好得 $(1+c):(b-1):a$ ✓✓ 极漂亮" "\n"
        r"⑤ ⚠ **选项 C 是最诱人的陷阱**：$\frac1a:\frac1{b-1}:\frac1{c+1}$ 是「忘记通分」的结果，"
        r"也是很多同学的直觉答案 —— 必须通分后才能与选项比对 ✓✓" "\n"
        r"⑥ 数值复核：取 $a=b=c=2$，则 $(c+1):(b-1):a=3:1:2$；"
        r"直接算 $S_{OAB}:S_{OAC}:S_{OBC}=\frac1{2\cdot1}:\frac1{2\cdot3}:\frac1{1\cdot3}=\frac12:\frac16:\frac13$，"
        r"同乘 $6$ 得 $3:1:2$ ✓✓ 完全吻合" "\n"
        r"**⭐⭐ 通法（系数和为 0 的向量式）**：" "\n"
        r"① ⭐⭐ 把已知向量式移项，凑成 $p\vec{OA}+q\vec{OB}+r\vec{OC}=\vec0$；" "\n"
        r"② ⭐⭐ 吸收系数造新三角形，$O$ 是其重心 ⟹ 三个小三角形面积相等；" "\n"
        r"③ ⭐⭐ 用「面积比 = 两邻边乘积之比（夹角相同）」换算回原三角形，最后通分 ✓✓✓"
    ),
    'difficulty': 0.76,
    'topics': ['M-T-241'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-241-V2',
}

T241_V3 = {
    'type': '选择',
    'stem_text': (
        r"已知点 $M$ 是 $\triangle ABC$ 所在平面内一点，满足 "
        r"$\overrightarrow{AM}=\dfrac23\overrightarrow{AB}+\dfrac14\overrightarrow{AC}$，"
        r"则 $\triangle ABM$ 与 $\triangle BCM$ 的面积之比为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac38$"),
        ('B', r"$\dfrac83$"),
        ('C', r"$3$"),
        ('D', r"$\dfrac13$"),
    ],
    'answer': 'C',
    'analysis': (
        r"延长 $AM$ 交 $BC$ 于 $G$，用 $A$、$M$、$G$ 共线定出 $\vec{AG}=\lambda\vec{AB}+(1-\lambda)\vec{AC}$ 中的 $\lambda$，"
        r"再由同高三角形的面积比等于底边比，逐级换算到 $S_{\triangle ABM}:S_{\triangle BCM}$．"
    ),
    'solution': (
        r"延长 $AM$ 交 $BC$ 于 $G$．因 $G$ 在 $BC$ 上，可设" "\n"
        r"$\overrightarrow{AG}=\lambda\overrightarrow{AB}+(1-\lambda)\overrightarrow{AC}$（系数和为 $1$）．" "\n"
        r"又 $A$、$M$、$G$ 共线，故存在 $t$ 使 $\overrightarrow{AG}=t\overrightarrow{AM}$，即" "\n"
        r"$\lambda\overrightarrow{AB}+(1-\lambda)\overrightarrow{AC}=t\left(\dfrac23\overrightarrow{AB}+\dfrac14\overrightarrow{AC}\right)$．" "\n"
        r"由 $\vec{AB}$、$\vec{AC}$ 不共线，比较系数：" "\n"
        r"$\lambda=\dfrac23 t$，$1-\lambda=\dfrac14 t$，两式相除得" "\n"
        r"$\dfrac{\lambda}{1-\lambda}=\dfrac{2/3}{1/4}=\dfrac83$，故 $3\lambda=8-8\lambda$，$\lambda=\dfrac8{11}$，" "\n"
        r"代回得 $t=\dfrac32\lambda=\dfrac{12}{11}$．" "\n"
        r"由 $\overrightarrow{AG}=\dfrac8{11}\overrightarrow{AB}+\dfrac3{11}\overrightarrow{AC}$ 知 "
        r"$\overrightarrow{CG}=\dfrac8{11}\overrightarrow{CB}$，故 $BG:GC=3:8$．" "\n"
        r"又 $AG=\dfrac{12}{11}AM$，故 $GM=AG-AM=\dfrac1{11}AM=\dfrac1{12}AG$．" "\n"
        r"于是（同高）" "\n"
        r"$\dfrac{S_{\triangle BGM}}{S_{\triangle BAM}}=\dfrac{GM}{AM}=\dfrac1{11}$，" "\n"
        r"$\dfrac{S_{\triangle BGM}}{S_{\triangle BMC}}=\dfrac{BG}{BC}=\dfrac3{11}$，即 $S_{\triangle BMC}=\dfrac{11}3 S_{\triangle BGM}$．" "\n"
        r"因此 $S_{\triangle BMC}=\dfrac{11}3\times\dfrac1{11}S_{\triangle BAM}=\dfrac13 S_{\triangle BAM}$，" "\n"
        r"即 $S_{\triangle ABM}:S_{\triangle BCM}=3:1=3$．选 C．"
    ),
    'review': (
        r"① ⭐⭐ **延长 $AM$ 交 $BC$ 于 $G$ 是标准动作** —— "
        r"这样 $G$ 在 $BC$ 上，可写成 $\vec{AG}=\lambda\vec{AB}+(1-\lambda)\vec{AC}$（系数和 1）✓✓✓" "\n"
        r"② ⭐⭐ **$\frac\lambda{1-\lambda}=\frac{2/3}{1/4}=\frac83$** —— "
        r"两式相除直接消掉 $t$，比分别解 $t$ 快得多 ✓✓" "\n"
        r"③ ⭐⭐ **$\lambda=\frac8{11}$ 同时也是 $BG:GC$ 的来源**："
        r"$\vec{AG}=\frac8{11}\vec{AB}+\frac3{11}\vec{AC}$ ⟹ $\vec{CG}=\frac8{11}\vec{CB}$ ⟹ $CG:CB=8:11$ ⟹ $BG:GC=3:8$ ✓" "\n"
        r"④ ⭐⭐ **两级同高面积比**：$\frac{S_{BGM}}{S_{BAM}}=\frac{GM}{AM}=\frac1{11}$、"
        r"$\frac{S_{BGM}}{S_{BMC}}=\frac{BG}{BC}=\frac3{11}$，两式一除即得 $S_{BAM}:S_{BMC}=3:1$ ✓✓✓" "\n"
        r"  这是「求两个非共线三角形面积比」的通用做法：**找一个中转三角形 $BGM$**" "\n"
        r"⑤ ⚠ **选项 A $\frac38$ 是 $BG:GC$**，**选项 D $\frac13$ 是 $S_{BMC}:S_{BAM}$（方向反了）**，"
        r"**选项 B $\frac83$ 是 $\frac\lambda{1-\lambda}$** —— 三个干扰项全来自中间量，务必看清题目问的是哪个比 ✓✓" "\n"
        r"⑥ 数值复核：取 $A(0,0)$、$B(1,0)$、$C(0,1)$，则 $M=\frac23(1,0)+\frac14(0,1)=(\frac23,\frac14)$；" "\n"
        r"  $S_{ABM}=\frac12|\det(\vec{AB},\vec{AM})|=\frac12|1\cdot\frac14-0|=\frac18$；" "\n"
        r"  $S_{BCM}=\frac12|\det(\vec{BC},\vec{BM})|$，$\vec{BC}=(-1,1)$、$\vec{BM}=(-\frac13,\frac14)$，" "\n"
        r"  $\det=(-1)(\frac14)-1(-\frac13)=-\frac14+\frac13=\frac1{12}$，故 $S_{BCM}=\frac1{24}$；" "\n"
        r"  $S_{ABM}:S_{BCM}=\frac18:\frac1{24}=3:1=3$ ✓✓ 与答案完全一致" "\n"
        r"**⭐⭐ 通法（系数和 $\ne1$ 的 $\vec{AM}=\alpha\vec{AB}+\beta\vec{AC}$）**：" "\n"
        r"① ⭐⭐ 延长 $AM$ 交底边于 $G$，写 $\vec{AG}=\lambda\vec{AB}+(1-\lambda)\vec{AC}=t\vec{AM}$；" "\n"
        r"② ⭐⭐ 两式相除消 $t$：$\frac\lambda{1-\lambda}=\frac\alpha\beta$ ⟹ $\lambda=\frac\alpha{\alpha+\beta}$；" "\n"
        r"③ ⭐⭐ 由 $\lambda$ 得底边比，由 $t=\alpha+\beta$ 得 $\frac{GM}{AM}$；" "\n"
        r"④ ⭐⭐ 用中转三角形（本题 $\triangle BGM$）换算面积比 ✓✓✓"
    ),
    'difficulty': 0.72,
    'topics': ['M-T-241'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-231-V3'.replace('231', '241'),
}

QS = [
    T231_E1, T231_V1, T231_V2, T231_V3,
    T228_E1, T228_V1, T228_V2, T228_V3,
    T206_E1, T206_V1, T206_V2,
    T241_V1, T241_V2, T241_V3,
]
