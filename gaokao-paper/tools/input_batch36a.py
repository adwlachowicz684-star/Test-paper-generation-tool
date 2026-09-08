# -*- coding: utf-8 -*-
r"""第36批：解三角形 · 「扩展线」型（4题）

来源：2024高中数学热点题型归纳完整解析版.pdf p168（PDF 页 167）

## 选题

`pick_batch.py --n 14` → p168（M-T-205），4 题全在一页，A 级。
专题「4-3 正余弦定理与解三角形小题归类 · 题型一 图形5：扩展线」。

## ★ 选项用字符坐标还原（根号是矢量绘制，提取必丢）

| 题 | 还原 |
|---|---|
| V1 | A 分子`1`(x=66.5)`3`(x=71)/分母`2`(x=65.5)→$\frac{\sqrt{13}}2$；C `3`+`1`→$\sqrt3+1$；D `2``3`→$2\sqrt3$ |
| V2 | A→$2\sqrt3$；B→$\sqrt3$；C 分子`3`/分母`2`→$\frac{\sqrt3}2$；D 分子`3`/分母`4`→$\frac{\sqrt3}4$ |

## 四题验算

| 题 | 结果 | 答案 |
|---|---|---|
| E1 | $\sqrt3\sin\alpha=\cos\alpha$→$\alpha=30^\circ$ | **C** |
| V1 | $|AD|^2=2\sqrt3\sin2B+4$→$\max=\sqrt3+1$ | **C** |
| V2 | $y^2=\frac49[(m-1)^2+3]$，$m=1$→$S=\frac{\sqrt3}2$ | **C** |
| V3 | 构造 $AD=BD=2$、$AC=8$ | **D** |

## ⚠ 两处原书提取失真

- **E1**：详解「$3\sin\alpha=\cos\alpha$」实为 $\sqrt3\sin\alpha=\cos\alpha$
  （若按 $3$ 则 $\alpha\approx18.4^\circ$，四选项无一符合 —— 反证必是 $\sqrt3$）
- **V3**：$\sin C=\frac{3\sqrt7}{32}$、$\sin\angle CAD=\frac{3\sqrt7}8$ 均被提取成 `3 7 32` 样式
"""

T205_E1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$D$ 是边 $BC$ 上的一点，$\angle C=40^\circ$，"
        r"$\angle CAD=60^\circ$，$BD=AC$，则 $\angle DBA=$（　　）"
    ),
    'opts': [
        ('A', r"$20^\circ$"), ('B', r"$25^\circ$"),
        ('C', r"$30^\circ$"), ('D', r"$35^\circ$"),
    ],
    'answer': 'C',
    'analysis': (
        r"$\triangle ADC$ 中得 $\angle ADC=80^\circ$，由正弦定理 $AD:AC=\sin40^\circ:\sin80^\circ$；"
        r"再在 $\triangle ABD$ 中用正弦定理，配合二倍角与两角和公式解出 $\alpha$。"
    ),
    'solution': (
        r"**第一步：$\triangle ADC$ 中求角**" "\n"
        r"$\angle C=40^\circ$、$\angle CAD=60^\circ$，故 $\angle ADC=180^\circ-40^\circ-60^\circ=80^\circ$．" "\n"
        r"正弦定理：$\dfrac{AD}{\sin C}=\dfrac{AC}{\sin\angle ADC}$，即 $AD:AC=\sin40^\circ:\sin80^\circ$．" "\n"
        r"设 $AD=k\sin40^\circ$、$AC=k\sin80^\circ$（$k>0$），由 $BD=AC$ 得 $BD=k\sin80^\circ$．" "\n"
        r"**第二步：$\triangle ABD$ 中列方程**" "\n"
        r"设 $\angle DBA=\alpha$（$0<\alpha<90^\circ$）．"
        r"$\angle ADB=180^\circ-80^\circ=100^\circ$，故 $\angle BAD=80^\circ-\alpha$．" "\n"
        r"正弦定理：$\dfrac{AD}{\sin\alpha}=\dfrac{BD}{\sin(80^\circ-\alpha)}$，" "\n"
        r"即 $\dfrac{\sin40^\circ}{\sin\alpha}=\dfrac{\sin80^\circ}{\sin(80^\circ-\alpha)}$．" "\n"
        r"**第三步：化简**" "\n"
        r"$\sin80^\circ=2\sin40^\circ\cos40^\circ$；"
        r"$\sin(80^\circ-\alpha)=\sin[90^\circ-(10^\circ+\alpha)]=\cos(10^\circ+\alpha)$：" "\n"
        r"$\cos(10^\circ+\alpha)=2\cos40^\circ\sin\alpha$．" "\n"
        r"左 $=\cos10^\circ\cos\alpha-\sin10^\circ\sin\alpha$；" "\n"
        r"右 $=2\cos(30^\circ+10^\circ)\sin\alpha=(\sqrt3\cos10^\circ-\sin10^\circ)\sin\alpha$．" "\n"
        r"$\Rightarrow\sqrt3\cos10^\circ\sin\alpha-\sin10^\circ\sin\alpha"
        r"=\cos10^\circ\cos\alpha-\sin10^\circ\sin\alpha$" "\n"
        r"$\Rightarrow\sqrt3\cos10^\circ\sin\alpha=\cos10^\circ\cos\alpha"
        r"\Rightarrow\sqrt3\sin\alpha=\cos\alpha$．" "\n"
        r"**第四步**：$\tan\alpha=\dfrac1{\sqrt3}$，又 $0<\alpha<90^\circ$，故 $\alpha=30^\circ$．选 C．"
    ),
    'review': (
        r"★ 题干、选项、详解完整 ✓。" "\n"
        r"**⚠ 详解提取失真**：原文「即 $3\cos10^\circ\sin\alpha-\sin10^\circ\sin\alpha"
        r"=\cos10^\circ\cos\alpha-\sin10^\circ\sin\alpha$，即 $3\sin\alpha=\cos\alpha$」"
        r"两处 $3$ 实为 $\sqrt3$（根号丢失）。" "\n"
        r"**反证**：若按字面 $3\sin\alpha=\cos\alpha$ 则 $\alpha=\arctan\frac13\approx18.4^\circ$，"
        r"**四个选项无一符合** —— 必是 $\sqrt3$。" "\n"
        r"**独立验算**（$\alpha=30^\circ$ 反查）：" "\n"
        r"$\frac{AD}{\sin\alpha}=\frac{k\sin40^\circ}{\sin30^\circ}=\frac{0.6428k}{0.5}=1.2856k$；" "\n"
        r"$\frac{BD}{\sin(80^\circ-30^\circ)}=\frac{k\sin80^\circ}{\sin50^\circ}=\frac{0.9848k}{0.7660}=1.2856k$ ✓ "
        r"**两式相等，正弦定理成立**" "\n"
        r"**答案 C 正确** ✓" "\n"
        r"**⭐ 套路**：「扩展线」型用一条线段串起两个三角形，**各用一次正弦定理再联立**。"
    ),
    'difficulty': 0.88,
    'topics': ['M-T-205'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-205-E1',
}

T205_V1 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$\angle BAC=60^\circ$，$BC=3$，"
        r"且有 $\vec{CD}=2\vec{DB}$，则线段 $AD$ 长的最大值为（　　）"
    ),
    'opts': [
        ('A', r"$\dfrac{\sqrt{13}}2$"), ('B', r"$2$"),
        ('C', r"$\sqrt3+1$"), ('D', r"$2\sqrt3$"),
    ],
    'answer': 'C',
    'analysis': (
        r"由 $\vec{CD}=2\vec{DB}$ 得 $BD=\frac13BC$；把 $\vec{AD}$ 用 $\vec{AB}$、$\vec{AC}$ 表示后平方，"
        r"再用正弦定理化为关于 $B$ 的三角函数求最值。"
    ),
    'solution': (
        r"**第一步：向量表示**" "\n"
        r"由 $\vec{CD}=2\vec{DB}$ 知 $D$ 在线段 $BC$ 上，$BD=\dfrac13BC$、$DC=\dfrac23BC$．" "\n"
        r"$\vec{AD}=\vec{AB}+\dfrac13\vec{BC}=\vec{AB}+\dfrac13(\vec{AC}-\vec{AB})"
        r"=\dfrac23\vec{AB}+\dfrac13\vec{AC}$，即 $3\vec{AD}=2\vec{AB}+\vec{AC}$．" "\n"
        r"**第二步：平方**" "\n"
        r"$9|AD|^{2}=4c^{2}+b^{2}+4bc\cos A=4c^{2}+b^{2}+2bc$（$A=60^\circ$）．" "\n"
        r"**第三步：化为三角函数**" "\n"
        r"$\dfrac a{\sin A}=\dfrac3{\sin60^\circ}=2\sqrt3$，故 $b=2\sqrt3\sin B$、$c=2\sqrt3\sin C$，$B+C=120^\circ$．" "\n"
        r"代入 $C=120^\circ-B$ 化简：$9|AD|^{2}=18\sqrt3\sin2B+36$，即 $|AD|^{2}=2\sqrt3\sin2B+4$．" "\n"
        r"**第四步：求最值**" "\n"
        r"$0<B<120^\circ$ → $0<2B<240^\circ$；当 $2B=90^\circ$（$B=45^\circ$）时 $\sin2B=1$ 最大．" "\n"
        r"$|AD|^{2}_{\max}=2\sqrt3+4=(\sqrt3+1)^{2}$，故 $|AD|_{\max}=\sqrt3+1$．选 C．"
    ),
    'review': (
        r"★ 由详解「$3\vec{AD}=2\vec{AB}+\vec{AC}$，所以 "
        r"$9|AD|^{2}=b^{2}+4c^{2}+4\vec{AB}\cdot\vec{AC}=b^{2}+4c^{2}+2bc$…"
        r"得出 $|AD|^{2}=2\sqrt3\sin2B+4$，∵$0<B<\frac{2\pi}3$，则 $0<2B<\frac{4\pi}3$，"
        r"当 $2B=\frac\pi2$ 即 $B=\frac\pi4$ 时 $|AD|$ 取最大值，"
        r"即 $|AD|_{\max}=\sqrt{4+2\sqrt3}=\sqrt3+1$」还原。" "\n"
        r"**选项用字符坐标确认**（PDF 页 167，y≈546/556）："
        r"A 分子`1`(x=66.5)`3`(x=71.0)/分母`2`(x=65.5)→$\frac{\sqrt{13}}2$；"
        r"B `2`(x=115.6)→$2$；C `3`(x=176.8)`+``1`(x=194.9)→$\sqrt3+1$；"
        r"D `2`(x=227.4)`3`(x=237.4)→$2\sqrt3$。" "\n"
        r"（四选项 $1.803<2<2.732<3.464$ 递增，作为「最大值」合理 ✓；"
        r"D 超过实际最大值，是典型干扰项）" "\n"
        r"**独立验算**（$B=45^\circ$ 数值对拍）：" "\n"
        r"$C=75^\circ$；$b=2\sqrt3\sin45^\circ=2.4495$；$c=2\sqrt3\sin75^\circ=3.3461$" "\n"
        r"$9|AD|^2=4c^2+b^2+2bc=44.785+6.0+16.393=67.178$ → $|AD|^2=7.4642$" "\n"
        r"公式值：$2\sqrt3\sin90^\circ+4=3.4641+4=7.4641$ ✓✓ **完全吻合**" "\n"
        r"$|AD|=\sqrt{7.4641}=2.7320=\sqrt3+1$ ✓ **答案 C 正确**" "\n"
        r"（校验 $(\sqrt3+1)^2=4+2\sqrt3=7.4641$ ✓）"
    ),
    'difficulty': 0.93,
    'topics': ['M-T-205'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-205-V1',
}

T205_V2 = {
    'type': '选择',
    'stem_text': (
        r"如图，$D$ 为 $\triangle ABC$ 的边 $AC$ 上一点，$|AD|=2|DC|$，"
        r"$\angle ABC=60^\circ$，$|\vec{AB}|+2|\vec{BC}|=4$，"
        r"当 $|\vec{BD}|$ 取最小值时，$\triangle ABC$ 的面积为（　　）"
    ),
    'opts': [
        ('A', r"$2\sqrt3$"), ('B', r"$\sqrt3$"),
        ('C', r"$\dfrac{\sqrt3}2$"), ('D', r"$\dfrac{\sqrt3}4$"),
    ],
    'answer': 'C',
    'analysis': (
        r"设 $CD=x$、$BD=y$、$BC=m$，先由 ∠ABC 的余弦定理得 $9x^{2}=7m^{2}-20m+16$；"
        r"再由 $\cos\angle ADB=-\cos\angle BDC$ 得 $y^{2}$ 的二次式，配方求最小值点。"
    ),
    'solution': (
        r"**设元**：$CD=x$、$BD=y$、$BC=m$，则 $AD=2x$、$AC=3x$；"
        r"由 $|AB|+2|BC|=4$ 得 $AB=4-2m$．" "\n"
        r"**第一步：$\triangle ABC$ 中余弦定理**" "\n"
        r"$\cos B=\dfrac{(4-2m)^{2}+m^{2}-9x^{2}}{2m(4-2m)}=\dfrac12$" "\n"
        r"$\Rightarrow m(4-2m)=(4-2m)^{2}+m^{2}-9x^{2}$" "\n"
        r"$\Rightarrow4m-2m^{2}=16-16m+5m^{2}-9x^{2}$" "\n"
        r"$\Rightarrow9x^{2}=7m^{2}-20m+16$　①" "\n"
        r"**第二步：互补角余弦**" "\n"
        r"$\angle ADB+\angle BDC=\pi$，故 $\cos\angle ADB=-\cos\angle BDC$．" "\n"
        r"$\dfrac{4x^{2}+y^{2}-(4-2m)^{2}}{4xy}=-\dfrac{x^{2}+y^{2}-m^{2}}{2xy}$" "\n"
        r"$\Rightarrow4x^{2}+y^{2}-(4-2m)^{2}=-2x^{2}-2y^{2}+2m^{2}$" "\n"
        r"$\Rightarrow3y^{2}=-6x^{2}+2m^{2}+(4-2m)^{2}$" "\n"
        r"$\Rightarrow y^{2}=-2x^{2}+2m^{2}-\dfrac{16}3m+\dfrac{16}3$　②" "\n"
        r"**第三步：代入①配方**" "\n"
        r"$y^{2}=\dfrac{-14m^{2}+40m-32+18m^{2}-48m+48}9=\dfrac{4m^{2}-8m+16}9"
        r"=\dfrac49\bigl[(m-1)^{2}+3\bigr]$．" "\n"
        r"**第四步**：$m=1$ 时 $y^{2}$ 最小，此时 $BC=1$、$AB=2$．" "\n"
        r"$S=\dfrac12\times2\times1\times\dfrac{\sqrt3}2=\dfrac{\sqrt3}2$．选 C．"
    ),
    'review': (
        r"★ 由详解「设 $CD=x$、$BD=y$、$BC=m$，则 $AD=2x$、$AB=4-2m$，…"
        r"由余弦定理可得 $9x^{2}=7m^{2}-20m+16$；"
        r"又∵$\angle ADB+\angle BDC=\pi$，∴$\cos\angle ADB=-\cos\angle BDC$，…"
        r"当 $m=1$ 时 $y^{2}$ 有最小值，此时 $BC=1$、$AB=2$，"
        r"所以 $S_{\triangle ABC}=\frac12\times2\times1\times\sin60^\circ$…故选 C」还原。" "\n"
        r"**选项字符坐标确认**（PDF 页 167，y≈247~257 右栏）："
        r"A `2`(x=335.0)`3`(x=344.9)→$2\sqrt3$；B `3`(x=396.5)→$\sqrt3$；"
        r"C 分子`3`(x=454.4)/分母`2`(x=451.3)→$\frac{\sqrt3}2$；"
        r"D 分子`3`(x=510.4)/分母`4`(x=507.4)→$\frac{\sqrt3}4$。" "\n"
        r"（$3.464,1.732,0.866,0.433$ 成等比，面积类选项的典型设计 ✓）" "\n"
        r"**独立验算**：" "\n"
        r"① $(4-2m)^2+m^2=16-16m+5m^2$ ✓ → $9x^2=16-16m+5m^2-4m+2m^2=7m^2-20m+16$ ✓" "\n"
        r"② 代入后 $\frac{4m^2-8m+16}{9}=\frac49[(m-1)^2+3]$ ✓" "\n"
        r"$m=1$：$y^2=\frac43$、$x^2=\frac{7-20+16}9=\frac13$ ✓" "\n"
        r"③ $S=\frac12\cdot2\cdot1\cdot\frac{\sqrt3}2=\frac{\sqrt3}2\approx0.866$ ✓ **答案 C 正确**" "\n"
        r"**⭐ 提速**：不必真求 $x$、$y$，配成关于 $m$ 的二次式找到最小值点，回代算面积即可。"
    ),
    'difficulty': 0.94,
    'topics': ['M-T-205'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-205-V2',
}

T205_V3 = {
    'type': '选择',
    'stem_text': (
        r"在 $\triangle ABC$ 中，$A>B$，$BC=10$，$\sin C=\dfrac{3\sqrt7}{32}$，"
        r"$\cos(A-B)=\dfrac18$．若点 $P$ 是 $\triangle ABC$ 所在平面内任意一点，"
        r"则 $|\vec{PA}|-|\vec{PC}|$ 的取值范围是（　　）"
    ),
    'opts': [
        ('A', r"$[-5,5]$"), ('B', r"$[-6,6]$"),
        ('C', r"$[-7,7]$"), ('D', r"$[-8,8]$"),
    ],
    'answer': 'D',
    'analysis': (
        r"由三角形不等式 $\bigl||PA|-|PC|\bigr|\le|AC|$，只需求 $AC$．"
        r"在 $BC$ 上取 $D$ 使 $\angle BAD=B$，则 $AD=BD$ 且 $\angle CAD=A-B$。"
    ),
    'solution': (
        r"**第一步：转化为边长**" "\n"
        r"对任意 $P$，$\bigl||PA|-|PC|\bigr|\le|AC|$，等号可取到"
        r"（$P$ 在直线 $AC$ 上、位于 $A$ 或 $C$ 外侧时）．故只需求 $|AC|$．" "\n"
        r"**第二步：构造 $D$**" "\n"
        r"因 $A>B$，可在 $BC$ 上取 $D$ 使 $\angle BAD=B$．" "\n"
        r"$\triangle ABD$ 中 $\angle BAD=\angle ABD=B$，故 $AD=BD$．设 $AD=BD=x$，则 $CD=10-x$．" "\n"
        r"此时 $\angle CAD=A-B$，故 $\cos\angle CAD=\dfrac18$、"
        r"$\sin\angle CAD=\sqrt{1-\dfrac1{64}}=\dfrac{3\sqrt7}8$．" "\n"
        r"**第三步：正弦定理**" "\n"
        r"$\dfrac{CD}{\sin\angle CAD}=\dfrac{AD}{\sin C}"
        r"\Rightarrow\dfrac{10-x}{3\sqrt7/8}=\dfrac{x}{3\sqrt7/32}$" "\n"
        r"$\Rightarrow8(10-x)=32x\Rightarrow x=2$．故 $AD=2$、$CD=8$．" "\n"
        r"**第四步：余弦定理求 $AC$**" "\n"
        r"$\dfrac{4+AC^{2}-64}{4AC}=\dfrac18\Rightarrow8(AC^{2}-60)=4AC$" "\n"
        r"$\Rightarrow2AC^{2}-AC-120=0\Rightarrow(2AC+15)(AC-8)=0\Rightarrow AC=8$．" "\n"
        r"**结论**：$|\vec{PA}|-|\vec{PC}|\in[-8,8]$．选 D．"
    ),
    'review': (
        r"★ 题干、选项、答案完整 ✓。由详解「由于 $A>B$，设 $D$ 是 $BC$ 上一点…"
        r"由 $\cos(A-B)=\frac18$ 得 $\cos\angle CAD=\frac18$…"
        r"设 $BD=x$，$AD=x$、$CD=10-x$，$\sin\angle CAD=\frac{3\sqrt7}8$、$\sin C=\frac{3\sqrt7}{32}$，"
        r"由正弦定理…解得 $x=2$，所以 $AD=2$、$CD=8$。"
        r"在 $\triangle ADC$ 中由余弦定理…化简得 $2AC^{2}-AC-120=0$…得 $AC=8$。"
        r"$|\vec{PA}|-|\vec{PC}|$ 表示点 $P$ 到 $A,C$ 的距离之差，"
        r"所以 $\bigl||PA|-|PC|\bigr|\le|CA|=8$，所以 $-8\le|PA|-|PC|\le8$」还原。" "\n"
        r"**⚠ 提取失真**：题干 $\sin C=\frac{3\sqrt7}{32}$ 与详解 $\sin\angle CAD=\frac{3\sqrt7}8$ "
        r"都被提取成 `3 7 32` 样式，根号丢失。" "\n"
        r"**独立验算**：" "\n"
        r"① $8(10-x)=32x$ → $x=2$ ✓；$CD=8$ ✓；$2AC^2-AC-120=0$ → $AC=8$ ✓" "\n"
        r"② **角度链条闭合**：$\angle ADB=180^\circ-2B$ → $\angle ADC=2B$；"
        r"$\triangle ADC$ 内角和 $(A-B)+2B+C=180^\circ$ → $A+B+C=180^\circ$ ✓ **恒等**" "\n"
        r"③ 数值：$B=\frac12\arcsin\frac{3\sqrt7}8=41.41^\circ$；$A-B=82.82^\circ$ → $A=124.23^\circ$；"
        r"$C=180-124.23-41.41=14.36^\circ$" "\n"
        r"$\sin C=\sin14.36^\circ=0.2480=\frac{3\sqrt7}{32}=\frac{7.9373}{32}=0.2480$ ✓✓ **完全吻合**" "\n"
        r"**答案 D 正确** ✓" "\n"
        r"**⭐ 构造的巧思**：取 $\angle BAD=B$ 使 $\triangle ABD$ 等腰（$AD=BD$），"
        r"同时 $\angle CAD=A-B$ 正好接上已知 $\cos(A-B)=\frac18$ —— "
        r"**一个构造同时解决两件事**，这是本题关键。"
    ),
    'difficulty': 0.95,
    'topics': ['M-T-205'],
    'src': '2024高中数学热点题型归纳完整解析版.pdf · M-T-205-V3',
}

QS = [T205_E1, T205_V1, T205_V2, T205_V3]
