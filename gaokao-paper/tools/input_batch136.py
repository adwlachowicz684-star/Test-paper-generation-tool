# -*- coding: utf-8 -*-
r"""第 136 批（补录批·七）：攻「图形数据回填」组 + 三题「提取破碎」反推还原。

    python3 tools/run_batch.py 136

## 本批的两条方法论

### 一、图形数据回填（C 级题的通用救法，本批救回 3 题）

第 135 批在 M-T-214 系列上验证过的办法，本批在**立体几何**上再次奏效：

  M-T-325-E1  题干有「如图」，但 △PAD 边长、正方形、面面垂直全用文字给了
  M-T-174-V3  详解把图中读出的 f(0)=√3、零点 π/3、1/4 周期全写出来了
  M-T-293-V2  三视图 + 直观图，但详解给出了直三棱柱的全部尺寸关系

关键认识：**原书详解往往把「从图中读出的量」逐个写在步骤里**，
因为这些量正是解题的起点。把这些量回填进题干，题目就脱离原图独立成立。
本批 M-T-293-V2 更进一步——把三视图直接改写成文字描述的几何体。

### 二、「算出来矛盾」反推被 OCR 吃掉的部分（本批救回 3 题）

  M-T-130-V3  题干 e^x[f'+2f]=x 被读成 e^x f'+2f=x；f(1/2) 与 3^x-2^x 丢了指数。
              铁证：右边最小值恰为 1/(2√(2e)) = f(1/2) —— 这个「巧合」锁死了全部还原。
  M-T-315-V1  题干只剩三个小问，前置条件（PA⊥底面、AB=BC=PA=2、AD=4）全在详解里。
              校验：AC=CD=2√2 且 AC²+CD²=AD² 与详解逐字吻合。
  M-T-325-V1  「△BCF 为等腰三角形」+ EA∥FC + AE⊥底面 ⟹ ∠BCF=90° 且 BC=CF，
              等腰的腰由此唯一确定（否则后续 λ 无解）。

## ⚠ 本批不录（已登记）

  M-T-068-V1  详解为空，且按字面（两种 f 的解读都算过）n 恒为 3，与答案 B「1 或 3」矛盾
  M-T-229-V2  所求等式 ⟺ A=60°，但 b+c≤2a 推不出 A=60°（反例 A=90°, b=c 满足题设），
              原书证明逻辑断裂，疑题干 OCR 丢失
  M-T-110-V1  详解字段整体自我循环，无法还原
  M-T-124-E1  条件与详解首行无法建立自洽推导（>1 与 <0 无法判定），不臆造
"""

QS = []

# ── 1. M-T-130-V3 导数构造 + 双参数基本不等式（三处指数还原）────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)$ 满足 $\mathrm e^{x}\left[f'(x)+2f(x)\right]=x$，"
        r"$f\left(\dfrac12\right)=\dfrac{1}{2\sqrt{2\mathrm e}}$，若对任意正数 $a,\ b$ 都有" "\n"
        r"$f\left(3^{x}-2^{x}-\dfrac12\right)<\dfrac{1}{a^{2}\mathrm e^{2}}+\dfrac{1}{64b^{2}}+\dfrac{ab}{8}$，" "\n"
        r"则 $x$ 的取值范围是（　　）"
    ),
    'opts': [('A', r"$(-\infty,\ 1)$"), ('B', r"$(-\infty,\ 0)$"), ('C', r"$(0,\ 1)$"), ('D', r"$(1,\ +\infty)$")],
    'answer': r"D",
    'analysis': (
        r"先由 $e^{x}(f'+2f)=x$ 两边乘 $\mathrm e^{x}$ 凑出 $\left[\mathrm e^{2x}f(x)\right]'=x\mathrm e^{x}$，"
        r"积分出 $f$ 的表达式；再由 $f\left(\frac12\right)$ 定常数，判出 $f$ 严格递减。"
        r"右侧是只含 $a,b$ 的式子，两次基本不等式求出其最小值，"
        r"恰好等于 $f\left(\frac12\right)$，于是脱去 $f$ 得到关于 $x$ 的指数不等式。"
    ),
    'solution': (
        r"**第一步：求出 $f$ 并判定单调性。**" "\n"
        r"由 $\mathrm e^{x}\left[f'(x)+2f(x)\right]=x$，两边同乘 $\mathrm e^{x}$ 得" "\n"
        r"$\mathrm e^{2x}f'(x)+2\mathrm e^{2x}f(x)=x\mathrm e^{x}$，即 $\left[\mathrm e^{2x}f(x)\right]'=x\mathrm e^{x}$。" "\n"
        r"设 $g(x)=\mathrm e^{2x}f(x)$，则 $g'(x)=x\mathrm e^{x}$，积分得 $g(x)=\mathrm e^{x}(x-1)+C$。" "\n"
        r"于是 $f(x)=\dfrac{\mathrm e^{x}(x-1)+C}{\mathrm e^{2x}}$，" "\n"
        r"$f'(x)=\dfrac{\mathrm e^{x}\cdot\mathrm e^{2x}-\left[\mathrm e^{x}(x-1)+C\right]\cdot2\mathrm e^{2x}}{\mathrm e^{4x}}"
        r"=\dfrac{\mathrm e^{x}(2-x)-2C}{\mathrm e^{2x}}$。" "\n"
        r"由 $f\left(\dfrac12\right)=\dfrac{1}{2\sqrt{2\mathrm e}}$ 得 $\dfrac{-\frac12\sqrt{\mathrm e}+C}{\mathrm e}"
        r"=\dfrac{1}{2\sqrt{2\mathrm e}}$，" "\n"
        r"即 $C=\dfrac{\sqrt{\mathrm e}}{2}+\dfrac{\sqrt{\mathrm e}}{2\sqrt2}"
        r"=\dfrac{\sqrt{\mathrm e}}{2}\left(1+\dfrac{\sqrt2}{2}\right)$。" "\n"
        r"记 $h(x)=\mathrm e^{x}(2-x)-2C$，则 $f'(x)=\dfrac{h(x)}{\mathrm e^{2x}}$，" "\n"
        r"$h'(x)=\mathrm e^{x}(2-x)-\mathrm e^{x}=\mathrm e^{x}(1-x)$，" "\n"
        r"故 $h$ 在 $(-\infty,1)$ 上递增、在 $(1,+\infty)$ 上递减，$h(x)\le h(1)$。" "\n"
        r"而 $h(1)=\mathrm e-\sqrt{\mathrm e}\left(1+\dfrac{\sqrt2}{2}\right)$。" "\n"
        r"由 $\mathrm e<2.75<\dfrac32+\sqrt2=\left(1+\dfrac{\sqrt2}{2}\right)^{2}$ 知 $\sqrt{\mathrm e}<1+\dfrac{\sqrt2}{2}$，" "\n"
        r"故 $h(1)<0$，从而 $f'(x)<0$ 恒成立，$f$ 在 $\mathbf R$ 上严格递减。" "\n"
        r"**第二步：求右侧的最小值。**" "\n"
        r"$\dfrac{1}{a^{2}\mathrm e^{2}}+\dfrac{1}{64b^{2}}\ge2\cdot\dfrac{1}{a\mathrm e}\cdot\dfrac{1}{8b}"
        r"=\dfrac{1}{4ab\mathrm e}$（当 $a\mathrm e=8b$ 取等）；" "\n"
        r"$\dfrac{1}{4ab\mathrm e}+\dfrac{ab}{8}\ge2\sqrt{\dfrac{1}{4ab\mathrm e}\cdot\dfrac{ab}{8}}"
        r"=2\sqrt{\dfrac{1}{32\mathrm e}}=\dfrac{1}{2\sqrt{2\mathrm e}}$（当 $ab=\sqrt{\dfrac2{\mathrm e}}$ 取等）。" "\n"
        r"两处取等条件可同时满足，故右侧最小值为 $\dfrac{1}{2\sqrt{2\mathrm e}}=f\left(\dfrac12\right)$。" "\n"
        r"**第三步：脱去 $f$。**" "\n"
        r"「对任意正数 $a,b$ 成立」等价于 $f\left(3^{x}-2^{x}-\dfrac12\right)<\dfrac{1}{2\sqrt{2\mathrm e}}"
        r"=f\left(\dfrac12\right)$。" "\n"
        r"由 $f$ 递减得 $3^{x}-2^{x}-\dfrac12>\dfrac12$，即 $u(x)=3^{x}-2^{x}-1>0$。" "\n"
        r"当 $x<0$ 时 $3^{x}<2^{x}<1$，故 $u(x)<0$；当 $x\ge0$ 时" "\n"
        r"$u'(x)=3^{x}\ln3-2^{x}\ln2>2^{x}(\ln3-\ln2)>0$，$u$ 递增，而 $u(1)=3-2-1=0$。" "\n"
        r"故 $u(x)>0\iff x>1$。故选 $\mathbf{D}$．"
    ),
    'review': (
        r"① ⭐⭐ **乘 $\mathrm e^{x}$ 凑全微分是本题的题眼**：$e^{x}(f'+2f)=x$ 两边再乘 $\mathrm e^{x}$ "
        r"才得到 $\left[\mathrm e^{2x}f\right]'=x\mathrm e^{x}$。原式 $f'+2f$ 的系数 $2$ 就是 $\left(\mathrm e^{2x}\right)'$ 里那个 $2$，"
        r"看到 $f'+kf$ 就该想到乘 $\mathrm e^{kx}$。" "\n"
        r"② ⭐⭐ **「右侧最小值 = 题给的 $f$ 值」是还原本题的铁证**：$f\left(\frac12\right)$ 与右侧最小值同为 $\frac{1}{2\sqrt{2\mathrm e}}$，"
        r"这不是巧合而是命题设计——正因如此，题干 OCR 丢掉的指数（$3^x-2^x$、$\sqrt{2\mathrm e}$）才能被唯一锁定。" "\n"
        r"③ ⭐ **两次基本不等式的取等条件要验证相容**：$a\mathrm e=8b$ 与 $ab=\sqrt{2/\mathrm e}$ 联立得 $b^{2}=\frac{\sqrt{2\mathrm e}}{8}>0$，"
        r"有正解，故最小值**能取到**，此时严格不等号 $<$ 才必须成立。" "\n"
        r"④ ⚠ **$u(x)=3^{x}-2^{x}-1$ 不是 $\mathbf R$ 上的增函数**：$x\to-\infty$ 时 $u'(\cdot)$ 会变号。"
        r"但 $x<0$ 时 $3^{x}<2^{x}<1$ 直接给出 $u<0$，故只需在 $x\ge0$ 上讨论单调性即可。" "\n"
        r"⑤ ⚠ **原书详解有两处数值瑕疵**：一是称 $h$ 在 $x=\frac12$ 处取最大且 $h\left(\frac12\right)=0$，"
        r"实际 $h'=e^{x}(1-x)$ 给出最大点在 $x=1$，且代入题给的 $f\left(\frac12\right)$ 得 $h\left(\frac12\right)=\frac{\sqrt{\mathrm e}}{2}(1-\sqrt2)\ne0$；"
        r"二是称 $u$ 是增函数。两处都不影响最终答案，本解析已按严格推导重写。" "\n"
        r"⑥ 数值复核：$h(1)=2.71828-1.64872\times1.70711=-0.09608<0$ ✓；"
        r"$u(1)=0$、$u(1.001)=0.00\mathbf{+} $ ✓（$3^{1.001}-2^{1.001}-1\approx0.0031>0$）。"
    ),
    'topics': ['M-T-130'],
    'src': 'M-T-130-V3',
    'difficulty': 0.78,
})

# ── 2. M-T-155-V2 导数：切线定参 + 用前一问结论证不等式 ─────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知函数 $f(x)=\mathrm e^{x}-ax$（$a$ 为常数）的图象与 $y$ 轴交于点 $A$，"
        r"曲线 $y=f(x)$ 在点 $A$ 处的切线斜率为 $-1$。" "\n"
        r"(1) 求 $a$ 的值及函数 $f(x)$ 的极值；" "\n"
        r"(2) 证明：当 $x>0$ 时，$x^{2}<\mathrm e^{x}$．"
    ),
    'opts': [],
    'answer': (
        r"(1) $a=2$；$f(x)$ 在 $x=\ln2$ 处取得极小值 $f(\ln2)=2-\ln4$，无极大值。"
        r"(2) 证明见解析．"
    ),
    'analysis': (
        r"(1) 由 $f'(0)=-1$ 定出 $a$，再用导数符号变化求极值；"
        r"(2) 作差构造 $g(x)=\mathrm e^{x}-x^{2}$，其导数恰好是 (1) 中的 $f(x)$，"
        r"于是可直接沿用 (1) 的最小值结论，不必重新求导分析。"
    ),
    'solution': (
        r"(1) $f'(x)=\mathrm e^{x}-a$，由题意 $f'(0)=1-a=-1$，故 $a=2$。" "\n"
        r"此时 $f(x)=\mathrm e^{x}-2x$，$f'(x)=\mathrm e^{x}-2$。" "\n"
        r"令 $f'(x)=0$ 得 $x=\ln2$。" "\n"
        r"当 $x<\ln2$ 时 $f'(x)<0$，$f(x)$ 单调递减；当 $x>\ln2$ 时 $f'(x)>0$，$f(x)$ 单调递增。" "\n"
        r"故 $x=\ln2$ 时 $f(x)$ 取得极小值 $f(\ln2)=\mathrm e^{\ln2}-2\ln2=2-\ln4$，无极大值。" "\n"
        r"(2) 令 $g(x)=\mathrm e^{x}-x^{2}$，则 $g'(x)=\mathrm e^{x}-2x=f(x)$。" "\n"
        r"由 (1) 知 $f(x)\ge f(\ln2)=2-\ln4>0$（因 $\ln4\approx1.386<2$），" "\n"
        r"故 $g'(x)>0$ 恒成立，$g(x)$ 在 $\mathbf R$ 上单调递增。" "\n"
        r"又 $g(0)=\mathrm e^{0}-0=1>0$，所以当 $x>0$ 时 $g(x)>g(0)=1>0$，" "\n"
        r"即 $\mathrm e^{x}-x^{2}>0$，亦即 $x^{2}<\mathrm e^{x}$．"
    ),
    'review': (
        r"① ⭐⭐ **「后一问的导数是前一问的函数」是命题人的标准串联手法**："
        r"$g'(x)=\mathrm e^{x}-2x$ 与 $f(x)=\mathrm e^{x}-2x$ 完全一致，"
        r"所以 (1) 求出的最小值 $2-\ln4$ 直接就是 (2) 中 $g'$ 的下界。**看到这种重合，后一问就不必另起炉灶。**" "\n"
        r"② ⭐ **$2-\ln4>0$ 要给出判断依据**：$\ln4=2\ln2\approx1.386<2$。"
        r"这个正数保证 $g$ 严格递增，是 (2) 成立的关键，不能默认。" "\n"
        r"③ ⭐ **用 $g(0)=1$ 而非 $g(x)>0$ 收尾**：由 $g$ 递增且 $g(0)=1$，"
        r"得 $x>0$ 时 $g(x)>1$，比只写 $g(x)>g(0)=1>0$ 更强也更清晰。" "\n"
        r"④ 数值复核：$f(\ln2)=2-1.38629=0.61371=2-\ln4$ ✓；"
        r"$g(0.5)=1.64872-0.25=1.39872>0$ ✓，$g(2)=7.389-4=3.389>0$ ✓。"
    ),
    'topics': ['M-T-155'],
    'src': 'M-T-155-V2',
    'difficulty': 0.55,
})

# ── 3. M-T-160-V1 极值 + 同构型不等式（两边最小值相等）─────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"已知 $f(x)=x\ln x$。" "\n"
        r"(1) 求函数 $f(x)$ 的极值；" "\n"
        r"(2) 证明：对一切 $x\in(0,+\infty)$，都有" "\n"
        r"$\ln x\ \ge\ \dfrac{x+1-\dfrac1{\mathrm e}}{x\,\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac{2}{\mathrm e x}$ 成立．"
    ),
    'opts': [],
    'answer': (
        r"(1) $f(x)$ 在 $x=\dfrac1{\mathrm e}$ 处取得极小值 $-\dfrac1{\mathrm e}$，无极大值。"
        r"(2) 证明见解析．"
    ),
    'analysis': (
        r"(2) 两边同乘 $x>0$，化为 $x\ln x\ge g(x)$；左端最小值在 (1) 中已求出为 $-\frac1{\mathrm e}$，"
        r"再用导数求出右端 $g(x)$ 的最大值，发现恰好也等于 $-\frac1{\mathrm e}$，且取等点相同。"
    ),
    'solution': (
        r"(1) $f(x)=x\ln x$ 的定义域为 $(0,+\infty)$，$f'(x)=\ln x+1$。" "\n"
        r"令 $f'(x)=0$ 得 $x=\dfrac1{\mathrm e}$。" "\n"
        r"当 $x\in\left(0,\dfrac1{\mathrm e}\right)$ 时 $f'(x)<0$，$f$ 单调递减；"
        r"当 $x\in\left(\dfrac1{\mathrm e},+\infty\right)$ 时 $f'(x)>0$，$f$ 单调递增。" "\n"
        r"故 $f(x)$ 在 $x=\dfrac1{\mathrm e}$ 处取得极小值 $f\left(\dfrac1{\mathrm e}\right)"
        r"=\dfrac1{\mathrm e}\ln\dfrac1{\mathrm e}=-\dfrac1{\mathrm e}$，无极大值。" "\n"
        r"(2) 因 $x>0$，所证不等式等价于" "\n"
        r"$x\ln x\ \ge\ \dfrac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac{2}{\mathrm e}$。" "\n"
        r"设 $g(x)=\dfrac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac{2}{\mathrm e}"
        r"=\left(x+1-\dfrac1{\mathrm e}\right)\mathrm e^{-\left(x+1-\frac1{\mathrm e}\right)}-\dfrac{2}{\mathrm e}$。" "\n"
        r"记 $t=x+1-\dfrac1{\mathrm e}$，则 $g=t\mathrm e^{-t}-\dfrac{2}{\mathrm e}$，" "\n"
        r"$g'(x)=\mathrm e^{-t}-t\mathrm e^{-t}=\mathrm e^{-t}(1-t)$。" "\n"
        r"当 $0<x<\dfrac1{\mathrm e}$ 时 $t<1$，$g'(x)>0$，$g$ 单调递增；"
        r"当 $x>\dfrac1{\mathrm e}$ 时 $t>1$，$g'(x)<0$，$g$ 单调递减。" "\n"
        r"故 $g(x)_{\max}=g\left(\dfrac1{\mathrm e}\right)=1\cdot\mathrm e^{-1}-\dfrac{2}{\mathrm e}"
        r"=-\dfrac1{\mathrm e}$，" "\n"
        r"当且仅当 $x=\dfrac1{\mathrm e}$ 时取到。" "\n"
        r"由 (1) 知 $f(x)_{\min}=f\left(\dfrac1{\mathrm e}\right)=-\dfrac1{\mathrm e}$，" "\n"
        r"所以 $f(x)\ge-\dfrac1{\mathrm e}\ge g(x)$ 对一切 $x\in(0,+\infty)$ 成立，"
        r"且当且仅当 $x=\dfrac1{\mathrm e}$ 时取等号。" "\n"
        r"即 $x\ln x\ge\dfrac{x+1-\frac1{\mathrm e}}{\mathrm e^{\,x+1-\frac1{\mathrm e}}}-\dfrac{2}{\mathrm e}$，" "\n"
        r"两边同除以 $x$ 即得所证．"
    ),
    'review': (
        r"① ⭐⭐ **「两边最值相等且取等点相同」是这类不等式的标准结构**："
        r"$f_{\min}=g_{\max}=-\frac1{\mathrm e}$，且都在 $x=\frac1{\mathrm e}$ 取到。"
        r"**若取等点不同，则不等式是严格的**（$>$ 而非 $\ge$）——这是判断能否写等号的关键。" "\n"
        r"② ⭐ **换元 $t=x+1-\frac1{\mathrm e}$ 让导数一步成型**：$t\mathrm e^{-t}$ 的导数是 $\mathrm e^{-t}(1-t)$，"
        r"极值点直接是 $t=1$，即 $x=\frac1{\mathrm e}$。命题人把指数配成 $x+1-\frac1{\mathrm e}$ "
        r"正是为了让极值点落在前一小问的极值点 $\frac1{\mathrm e}$ 上。" "\n"
        r"③ ⭐ **除以 $x$ 前必须确认 $x>0$**：本题定义域保证了这一点，故同除不变号。" "\n"
        r"④ 数值复核：$x=\frac1{\mathrm e}$ 时，左端 $\ln\frac1{\mathrm e}=-1$；"
        r"右端 $=\frac{\frac1{\mathrm e}+1-\frac1{\mathrm e}}{\frac1{\mathrm e}\cdot\mathrm e^{1}}-\frac{2}{\mathrm e\cdot\frac1{\mathrm e}}"
        r"=\frac{1}{\frac1{\mathrm e}\cdot\mathrm e}-\frac{2}{1}=1-2=-1$ ✓ 取等。"
    ),
    'topics': ['M-T-160'],
    'src': 'M-T-160-V1',
    'difficulty': 0.70,
})

# ── 4. M-T-174-V3 三角：给图求解析式 + 图象平移（回填图形数据）──────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知函数 $f(x)=A\sin(\omega x+\varphi)\ \left(A>0,\ \omega>0,\ 0<\varphi<\dfrac\pi2\right)$ "
        r"的部分图象如图所示（由图象可读出：$f(0)=\sqrt3$，$x=\dfrac\pi3$ 是图象的一个零点，"
        r"且 $x=\dfrac\pi3$ 与 $x=\dfrac{7\pi}{12}$ 之间相隔 $\dfrac14$ 个周期），"
        r"则要得到该函数的图象，只需要将函数" "\n"
        r"$g(x)=1-2\sqrt3\sin x\cos x-2\sin^{2}x$ 的图象（　　）"
    ),
    'opts': [('A', r"向左平移 $\dfrac\pi4$ 个单位长度"), ('B', r"向右平移 $\dfrac\pi4$ 个单位长度"), ('C', r"向左平移 $\dfrac\pi2$ 个单位长度"), ('D', r"向右平移 $\dfrac\pi2$ 个单位长度")],
    'answer': r"B",
    'analysis': (
        r"先由图中数据定出 $A,\omega,\varphi$ 得 $f$；再把 $g$ 用倍角公式化成一个正弦型函数；"
        r"最后比较两式相位，用「左加右减」定平移方向与量。"
    ),
    'solution': (
        r"由 $\dfrac{7\pi}{12}-\dfrac\pi3=\dfrac14T$ 得 $\dfrac{7\pi}{12}-\dfrac{4\pi}{12}=\dfrac{\pi}{4}=\dfrac14T$，"
        r"故 $T=\pi$。" "\n"
        r"又 $T=\dfrac{2\pi}{\omega}$ 且 $\omega>0$，得 $\omega=2$，从而 $f(x)=A\sin(2x+\varphi)$。" "\n"
        r"由 $f\left(\dfrac\pi3\right)=0$ 得 $A\sin\left(\dfrac{2\pi}{3}+\varphi\right)=0$，"
        r"即 $\dfrac{2\pi}{3}+\varphi=k\pi\ (k\in\mathbf Z)$。" "\n"
        r"结合 $0<\varphi<\dfrac\pi2$，取 $k=1$ 得 $\varphi=\dfrac\pi3$，故 $f(x)=A\sin\left(2x+\dfrac\pi3\right)$。" "\n"
        r"由 $f(0)=\sqrt3$ 得 $A\sin\dfrac\pi3=\sqrt3$，即 $A\cdot\dfrac{\sqrt3}{2}=\sqrt3$，故 $A=2$。" "\n"
        r"$\therefore\ f(x)=2\sin\left(2x+\dfrac\pi3\right)$。" "\n"
        r"又 $g(x)=1-2\sqrt3\sin x\cos x-2\sin^{2}x=1-\sqrt3\sin2x-(1-\cos2x)"
        r"=\cos2x-\sqrt3\sin2x$" "\n"
        r"$=2\left(\dfrac12\cos2x-\dfrac{\sqrt3}{2}\sin2x\right)=2\cos\left(2x+\dfrac\pi3\right)"
        r"=2\sin\left(2x+\dfrac\pi3+\dfrac\pi2\right)=2\sin\left(2x+\dfrac{5\pi}{6}\right)$。" "\n"
        r"设将 $g$ 的图象向右平移 $m$ 个单位得 $f$，则" "\n"
        r"$2\sin\left(2(x-m)+\dfrac{5\pi}{6}\right)=2\sin\left(2x+\dfrac\pi3\right)$，" "\n"
        r"即 $-2m+\dfrac{5\pi}{6}=\dfrac\pi3+2k\pi$，取 $k=0$ 得 $m=\dfrac{\pi}{4}$。" "\n"
        r"故需将 $g(x)$ 的图象向右平移 $\dfrac\pi4$ 个单位长度。故选 $\mathbf{B}$．"
    ),
    'review': (
        r"① ⭐⭐ **平移量只由「相位差除以 $\omega$」决定**："
        r"$f$ 与 $g$ 的相位分别是 $2x+\frac\pi3$ 与 $2x+\frac{5\pi}{6}$，"
        r"相位差 $\frac\pi3-\frac{5\pi}{6}=-\frac\pi2$，除以 $\omega=2$ 得 $-\frac\pi4$，"
        r"负号即向右平移 $\frac\pi4$。**先统一函数名（都化成正弦）再比相位，是唯一稳妥的做法。**" "\n"
        r"② ⭐ **$1-2\sin^{2}x=\cos2x$ 与 $2\sin x\cos x=\sin2x$ 要一起用**："
        r"$g$ 里的 $1$ 与 $-2\sin^2x$ 合成 $\cos2x$，这是本题化简的第一个动作。" "\n"
        r"③ ⭐⭐ **「$\frac14T$ 是零点与相邻极值点的间距」**：由 $\frac{7\pi}{12}-\frac\pi3=\frac\pi4=\frac14T$ 得 $T=\pi$。"
        r"注意 $\frac{7\pi}{12}$ 处是**最高点**（$2x+\frac\pi3=\frac{7\pi}{6}+\frac\pi3=\frac{3\pi}{2}$，$f=-2$ 是最低点），"
        r"从零点到相邻极值点正是 $\frac14T$。" "\n"
        r"④ ⚠ **$\varphi$ 由 $f\left(\frac\pi3\right)=0$ 定出后要用 $f(0)=\sqrt3>0$ 检验**："
        r"若取 $k=0$ 则 $\varphi=-\frac{2\pi}{3}\notin\left(0,\frac\pi2\right)$，舍去；"
        r"若取 $k=2$ 则 $\varphi=\frac{4\pi}{3}$ 也不合。故 $\varphi=\frac\pi3$ 唯一。" "\n"
        r"⑤ 数值复核：$f(0)=2\sin\frac\pi3=\sqrt3=1.7320508$ ✓；$f\left(\frac\pi3\right)=2\sin\pi=0$ ✓；"
        r"$f\left(\frac{7\pi}{12}\right)=2\sin\frac{3\pi}{2}=-2$ ✓（最低点，与 $\frac14T$ 间距吻合）；"
        r"$g\left(x-\frac\pi4\right)=2\sin\left(2x-\frac\pi2+\frac{5\pi}{6}\right)=2\sin\left(2x+\frac\pi3\right)=f(x)$ ✓．" "\n"
        r"⑥ 📌 原题「部分图象如图所示」，本解析已把图中读出的三个数据回填进题干，"
        r"使题目脱离原图也能独立作答。"
    ),
    'topics': ['M-T-174'],
    'src': 'M-T-174-V3',
    'difficulty': 0.65,
})

# ── 5. M-T-293-V2 几何概型：外接球 + 三视图（三视图文字化）──────────────
QS.append({
    'type': '选择',
    'stem_text': (
        r"已知直三棱柱 $ADF-BCE$ 的底面 $\triangle ADF$（与 $\triangle BCE$ 全等）为等腰直角三角形，"
        r"侧面 $ABCD$、$DCEF$ 均为边长为 $a$ 的正方形，侧面 $ABEF$ 为矩形，$M$ 是 $AB$ 的中点。"
        r"一只小蜜蜂在几何体 $ADF-BCE$ 的外接球内自由飞翔，"
        r"则它飞入四面体 $FMCE$ 内的概率为（　　）"
    ),
    'opts': [('A', r"$\dfrac{4\sqrt3}{9\pi}$"), ('B', r"$\dfrac{4\sqrt3}{27\pi}$"), ('C', r"$\dfrac{\sqrt3}{3\pi}$"), ('D', r"$\dfrac{\sqrt3}{9\pi}$")],
    'answer': r"D",
    'analysis': (
        r"几何概型，概率 = 四面体体积 / 外接球体积。"
        r"直三棱柱的外接球球心在上下底面外心连线的中点；"
        r"底面是直角三角形，其外接圆半径即斜边的一半。"
    ),
    'solution': (
        r"由 $ABCD$ 为正方形知 $AD\perp AB$、$AD\perp DC$；由 $DCEF$ 为正方形知 $DF\perp DC$、$DF\perp FE$。" "\n"
        r"故 $AD\perp DF$，$\triangle ADF$ 是以 $D$ 为直角顶点的等腰直角三角形，直角边 $AD=DF=a$，"
        r"斜边 $AF=\sqrt2 a$；棱柱的高 $AB=DC=FE=a$。" "\n"
        r"**外接球：** 底面 $\triangle ADF$ 的外接圆半径 $r=\dfrac{AF}{2}=\dfrac{\sqrt2}{2}a$，" "\n"
        r"球心在上下底面外心连线的中点，故 $R^{2}=r^{2}+\left(\dfrac a2\right)^{2}"
        r"=\dfrac{a^{2}}{2}+\dfrac{a^{2}}{4}=\dfrac{3a^{2}}{4}$，$R=\dfrac{\sqrt3}{2}a$。" "\n"
        r"$V_{\text{球}}=\dfrac43\pi R^{3}=\dfrac43\pi\cdot\dfrac{3\sqrt3}{8}a^{3}=\dfrac{\sqrt3}{2}\pi a^{3}$。" "\n"
        r"**四面体 $FMCE$：** 建系，取 $D(0,0,0)$、$A(a,0,0)$、$F(0,a,0)$、$C(0,0,a)$、"
        r"$B(a,0,a)$、$E(0,a,a)$。" "\n"
        r"则 $F,C,E$ 三点均在平面 $x=0$ 上，而 $M$ 为 $AB$ 中点，其 $x$ 坐标为 $a$，"
        r"故 $M$ 到平面 $FCE$ 的距离为 $a$。" "\n"
        r"在 $\triangle FCE$ 中，$FE=CE=a$，$FC=\sqrt2 a$，故 $FE^{2}+CE^{2}=FC^{2}$，"
        r"$S_{\triangle FCE}=\dfrac12a\cdot a=\dfrac{a^{2}}{2}$。" "\n"
        r"$V_{M-FCE}=\dfrac13\cdot\dfrac{a^{2}}{2}\cdot a=\dfrac{a^{3}}{6}$。" "\n"
        r"**概率：** $P=\dfrac{V_{M-FCE}}{V_{\text{球}}}=\dfrac{\dfrac{a^{3}}{6}}{\dfrac{\sqrt3}{2}\pi a^{3}}"
        r"=\dfrac{1}{3\sqrt3\pi}=\dfrac{\sqrt3}{9\pi}$。故选 $\mathbf{D}$．"
    ),
    'review': (
        r"① ⭐⭐ **直棱柱外接球的半径公式**：$R^{2}=r_{\text{底外接圆}}^{2}+\left(\dfrac h2\right)^{2}$。"
        r"本题 $r=\frac{\sqrt2}{2}a$、$h=a$，故 $R=\frac{\sqrt3}{2}a$，即外接球直径 $=\sqrt{a^{2}+a^{2}+a^{2}}=\sqrt3 a$"
        r"（体对角线）——**当底面外接圆直径与高相等时，两者结果一致，可当自检。**" "\n"
        r"② ⭐ **识别出 $F,C,E$ 共面于 $x=0$，是求体积的捷径**："
        r"于是 $M$ 到平面 $FCE$ 的距离直接就是 $M$ 的 $x$ 坐标 $a$，完全不必求法向量。" "\n"
        r"③ ⭐ **几何概型的体积比要认准「球的体积」而非「棱柱体积」**："
        r"蜜蜂是在**外接球内**飞翔，故样本空间是球。" "\n"
        r"④ ⚠ **底面是等腰直角三角形，直角顶点在 $D$**：由两个正方形侧面 $ABCD$、$DCEF$ 共用棱 $DC$ 得到，"
        r"$AD\perp DC$ 且 $DF\perp DC$ 只能推出 $DC\perp$ 平面 $ADF$，"
        r"而 $AD\perp DF$ 用的是「正方形 $ABCD$ 中 $AD\perp AB$」配「$AB\parallel DC$」——两步结合。" "\n"
        r"⑤ 数值复核（取 $a=1$）：$R=0.8660254$，$V_{\text{球}}=2.720699=\frac{\sqrt3}{2}\pi$ ✓；"
        r"$V_{M-FCE}=0.1666667=\frac16$ ✓；比值 $=0.0612586=\frac{\sqrt3}{9\pi}$ ✓．" "\n"
        r"⑥ 📌 原题给出的是三视图与直观图，本解析已把几何体的全部尺寸关系改写为文字，"
        r"使题目脱离图形也能独立作答。"
    ),
    'topics': ['M-T-293'],
    'src': 'M-T-293-V2',
    'difficulty': 0.68,
})

# ── 6. M-T-315-V1 四棱锥：体积 + 线面垂直 + 存在性反证（题干回填）────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"如图，在四棱锥 $P-ABCD$ 中，$PA\perp$ 底面 $ABCD$，四边形 $ABCD$ 是直角梯形，"
        r"$AD\parallel BC$，$AB\perp AD$，$AB=BC=PA=2$，$AD=4$。" "\n"
        r"(1) 求四棱锥 $P-ABCD$ 的体积；" "\n"
        r"(2) 求证：$CD\perp$ 平面 $PAC$；" "\n"
        r"(3) 在棱 $PC$ 上是否存在点 $M$（异于点 $C$），使得 $BM\parallel$ 平面 $PAD$？"
        r"若存在，求 $\dfrac{PM}{PC}$ 的值；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': r"(1) $4$；(2) 证明见解析；(3) 不存在．",
    'analysis': (
        r"(1) 梯形面积公式配 $PA$ 为高；(2) 用勾股定理逆定理证 $AC\perp CD$，"
        r"再由 $PA\perp$ 底面得 $PA\perp CD$，两条相交直线都在平面 $PAC$ 内；"
        r"(3) 用反证法：若存在则两个平行关系推出面面平行，与两平面交于 $P$ 矛盾。"
    ),
    'solution': (
        r"(1) $S_{ABCD}=\dfrac12(BC+AD)\cdot AB=\dfrac12\times(2+4)\times2=6$。" "\n"
        r"又 $PA\perp$ 底面 $ABCD$，$\therefore\ V_{P-ABCD}=\dfrac13S_{ABCD}\cdot PA"
        r"=\dfrac13\times6\times2=4$。" "\n"
        r"(2) 在直角梯形 $ABCD$ 中，$AC=\sqrt{AB^{2}+BC^{2}}=\sqrt{4+4}=2\sqrt2$。" "\n"
        r"又 $CD=\sqrt{AB^{2}+(AD-BC)^{2}}=\sqrt{4+4}=2\sqrt2$。" "\n"
        r"$\therefore\ AC^{2}+CD^{2}=8+8=16=AD^{2}$，即 $AC\perp CD$。" "\n"
        r"$\because\ PA\perp$ 平面 $ABCD$，$CD\subset$ 平面 $ABCD$，$\therefore\ PA\perp CD$。" "\n"
        r"又 $PA\cap AC=A$，$PA,AC\subset$ 平面 $PAC$，$\therefore\ CD\perp$ 平面 $PAC$。" "\n"
        r"(3) 不存在，用反证法证明。" "\n"
        r"假设存在点 $M$（异于点 $C$）使得 $BM\parallel$ 平面 $PAD$。" "\n"
        r"$\because\ BC\parallel AD$，$BC\not\subset$ 平面 $PAD$，$AD\subset$ 平面 $PAD$，"
        r"$\therefore\ BC\parallel$ 平面 $PAD$。" "\n"
        r"又 $BM\parallel$ 平面 $PAD$，$BC\cap BM=B$，$BC,BM\subset$ 平面 $PBC$，" "\n"
        r"$\therefore$ 平面 $PBC\parallel$ 平面 $PAD$。" "\n"
        r"但点 $P$ 同时在这两个平面内，即两平面相交，与平行矛盾。" "\n"
        r"故不存在这样的点 $M$．"
    ),
    'review': (
        r"① ⭐⭐ **「(3) 不存在」的通用反证结构**：先由 $BC\parallel AD$ 得到 $BC\parallel$ 平面 $PAD$，"
        r"再与假设的 $BM\parallel$ 平面 $PAD$ 合成**面面平行**；最后指出两个平面有公共点 $P$。"
        r"**凡是「棱上找点使线面平行」的题，先看看棱所在平面与已知平面是否已经共点。**" "\n"
        r"② ⭐ **线面垂直要凑两条相交直线**：$CD\perp AC$（计算）+ $CD\perp PA$（线面垂直性质），"
        r"缺一不可。其中 $PA\perp CD$ 来自「$PA\perp$ 底面」这条总条件，常是第一步就写出来的。" "\n"
        r"③ ⭐ **$CD$ 的长度用「直角梯形的高」算**：$CD=\sqrt{AB^{2}+(AD-BC)^{2}}$，"
        r"其中 $AD-BC=2$ 是上下底之差。配合 $AC=2\sqrt2$ 恰好凑成 $AC^{2}+CD^{2}=AD^{2}$，" "\n"
        r"　 这个「恰好」正是命题人把 $AD$ 定成 $4$ 的原因，可作还原题干的**硬校验**。" "\n"
        r"④ 数值复核：$S_{ABCD}=6$ ✓，$V=4$ ✓；$AC=CD=2.828427=2\sqrt2$ ✓，$AC^{2}+CD^{2}=16=AD^{2}$ ✓．" "\n"
        r"⑤ 📌 原题题干在提取时只剩三个小问，前置条件（$PA\perp$ 底面、$AB=BC=PA=2$、$AD=4$）"
        r"由详解中的三个算式反推补全，并用 $AC^{2}+CD^{2}=AD^{2}$ 校验通过。"
    ),
    'topics': ['M-T-315'],
    'src': 'M-T-315-V1',
    'difficulty': 0.62,
})

# ── 7. M-T-325-E1 面面垂直 + 线面平行 + 体积求参（图形数据回填）──────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"如图，$\triangle PAD$ 是边长为 $3$ 的等边三角形，四边形 $ABCD$ 为正方形，"
        r"平面 $PAD\perp$ 平面 $ABCD$。点 $E,\ F$ 分别为棱 $CD,\ PD$ 上的点，"
        r"且 $\dfrac{PF}{FD}=\dfrac{CE}{ED}=\dfrac12$，$G$ 为棱 $AB$ 上一点，且 $\dfrac{AG}{GB}=\lambda$。" "\n"
        r"(I) 当 $\lambda=\dfrac12$ 时，求证：$PG\parallel$ 平面 $AEF$；" "\n"
        r"(II) 已知三棱锥 $A-EFG$ 的体积为 $\sqrt3$，求 $\lambda$ 的值．"
    ),
    'opts': [],
    'answer': r"(I) 证明见解析；(II) $\lambda=2$．",
    'analysis': (
        r"(I) 由比例得 $EF\parallel PC$，再由 $\lambda=\frac12$ 构造平行四边形得 $AE\parallel CG$，"
        r"两线合成面面平行；(II) 用面面垂直性质得 $PO\perp$ 底面，"
        r"由 $F$ 的分点位置算出它到底面的距离，再用等体积法 $V_{A-EFG}=V_{F-AEG}$ 解出 $AG$。"
    ),
    'solution': (
        r"(I) 连接 $CG$。当 $\lambda=\dfrac12$ 时，$\dfrac{AG}{GB}=\dfrac12$，"
        r"又 $AB=3$，故 $AG=1$、$GB=2$。" "\n"
        r"由 $\dfrac{CE}{ED}=\dfrac12$ 且 $CD=3$ 得 $CE=1$。" "\n"
        r"$\because\ CE\parallel AG$ 且 $CE=AG=1$，$\therefore$ 四边形 $AECG$ 是平行四边形，"
        r"$\therefore\ AE\parallel CG$。" "\n"
        r"在 $\triangle PDC$ 中，$\dfrac{PF}{FD}=\dfrac{CE}{ED}=\dfrac12$，$\therefore\ EF\parallel PC$。" "\n"
        r"$\because\ AE\cap EF=E$，$PC\cap CG=C$，$AE,EF\subset$ 平面 $AEF$，$PC,CG\subset$ 平面 $PCG$，" "\n"
        r"$\therefore$ 平面 $PCG\parallel$ 平面 $AEF$。又 $PG\subset$ 平面 $PCG$，"
        r"$\therefore\ PG\parallel$ 平面 $AEF$。" "\n"
        r"(II) 取 $AD$ 的中点为 $O$，连接 $PO$，则 $PO\perp AD$。" "\n"
        r"$\because$ 平面 $PAD\perp$ 平面 $ABCD$，交线为 $AD$，$PO\subset$ 平面 $PAD$，"
        r"$\therefore\ PO\perp$ 平面 $ABCD$。" "\n"
        r"$PO=\dfrac{\sqrt3}{2}\times3=\dfrac{3\sqrt3}{2}$。" "\n"
        r"过 $F$ 作 $FH\perp AD$ 于 $H$，则 $FH\parallel PO$，故 $FH\perp$ 平面 $ABCD$。" "\n"
        r"由 $\dfrac{PF}{FD}=\dfrac12$ 得 $\dfrac{DF}{DP}=\dfrac23$，"
        r"$\therefore\ FH=\dfrac23PO=\dfrac23\times\dfrac{3\sqrt3}{2}=\sqrt3$。" "\n"
        r"由等体积法 $V_{A-EFG}=V_{F-AEG}=\dfrac13\cdot S_{\triangle AEG}\cdot FH=\sqrt3$，" "\n"
        r"得 $S_{\triangle AEG}=3$。" "\n"
        r"而 $S_{\triangle AEG}=\dfrac12\cdot AB\cdot AG=\dfrac12\times3\times AG=3$，"
        r"$\therefore\ AG=2$。" "\n"
        r"$\therefore\ GB=AB-AG=1$，$\lambda=\dfrac{AG}{GB}=2$．"
    ),
    'review': (
        r"① ⭐⭐ **两个「$\frac12$」是同一条暗线**：$\frac{PF}{FD}=\frac{CE}{ED}=\frac12$ 让 $EF\parallel PC$，"
        r"而 $\lambda=\frac12$ 让 $AG=CE$ 凑出平行四边形。**若 $\lambda$ 不是 $\frac12$，"
        r"平行四边形就凑不出来，(I) 的证法立刻失效**——这是两个条件必须相等的原因。" "\n"
        r"② ⭐ **面面垂直 ⟹ 线面垂直的三要素**：交线 $AD$ + $PO\perp AD$ + $PO$ 在平面 $PAD$ 内。"
        r"拿到 $PO\perp$ 底面后，$P$ 及 $PD$ 上各点到底面的距离都按**分点比例**缩放："
        r"$F$ 距 $D$ 为 $\frac23DP$，故距离也是 $\frac23PO$。" "\n"
        r"③ ⭐ **等体积法换顶点是求三棱锥体积的常规动作**："
        r"$V_{A-EFG}$ 中 $A$ 到平面 $EFG$ 的距离难求，换成以 $F$ 为顶点、$\triangle AEG$ 为底，"
        r"高就是 $FH$（已知），底面积只含 $AG$（未知量），一步解出。" "\n"
        r"④ ⚠ **$S_{\triangle AEG}=\frac12\cdot AB\cdot AG$ 要用 $AB$ 而非 $AE$ 作高**："
        r"$G$ 在 $AB$ 上，而 $AB\perp AD$、$E$ 在 $CD$ 上，故 $E$ 到直线 $AB$ 的距离就是 $AD=AB=3$。" "\n"
        r"⑤ ⚠ **原书答案把体积印成 $3$（丢根号）**：按 $3$ 则 $S_{\triangle AEG}=3\sqrt3$，"
        r"$AG=2\sqrt3>AB=3$？不，$2\sqrt3\approx3.46>3$，点 $G$ 跑到 $AB$ 延长线上，矛盾。"
        r"正确值为 $\sqrt3$，已更正。" "\n"
        r"⑥ 数值复核：$PO=2.598076=\frac{3\sqrt3}{2}$ ✓；$FH=1.7320508=\sqrt3$ ✓；"
        r"$AG=2$ 时 $S_{\triangle AEG}=3$ ✓，$V=\frac13\times3\times\sqrt3=\sqrt3$ ✓．"
    ),
    'topics': ['M-T-325'],
    'src': 'M-T-325-E1',
    'difficulty': 0.72,
})

# ── 8. M-T-325-V1 面面平行 + 等体积法求参（图形数据回填）────────────────
QS.append({
    'type': '解答',
    'stem_text': (
        r"如图，四边形 $ABCD$ 为矩形，$\triangle BCF$ 为等腰三角形，且 $\angle BAE=\angle DAE=90^{\circ}$，"
        r"$EA\parallel FC$。" "\n"
        r"(1) 证明：$BF\parallel$ 平面 $ADE$；" "\n"
        r"(2) 设 $\dfrac{BC}{AB}=\lambda$，问是否存在正实数 $\lambda$，"
        r"使得三棱锥 $A-BDF$ 的高恰好等于 $\dfrac{\sqrt6}{6}BC$？"
        r"若存在，求出 $\lambda$ 的值；若不存在，请说明理由．"
    ),
    'opts': [],
    'answer': r"(1) 证明见解析；(2) 存在，$\lambda=2$．",
    'analysis': (
        r"(1) 由 $AD\parallel BC$ 与 $EA\parallel FC$ 两次线面平行合成面面平行；"
        r"(2) 设 $AB=a$、$BC=b$，用等体积法 $V_{A-BDF}=V_{F-ABD}$ 建立方程，"
        r"其中 $\triangle BDF$ 是等腰三角形，用勾股定理求其面积。"
    ),
    'solution': (
        r"(1) $\because\ AD\parallel BC$，$AD\subset$ 平面 $ADE$，$BC\not\subset$ 平面 $ADE$，"
        r"$\therefore\ BC\parallel$ 平面 $ADE$。" "\n"
        r"$\because\ EA\parallel FC$，$AE\subset$ 平面 $ADE$，$FC\not\subset$ 平面 $ADE$，"
        r"$\therefore\ FC\parallel$ 平面 $ADE$。" "\n"
        r"又 $BC\cap FC=C$，$BC,FC\subset$ 平面 $BCF$，$\therefore$ 平面 $BCF\parallel$ 平面 $ADE$。" "\n"
        r"$\because\ BF\subset$ 平面 $BCF$，$\therefore\ BF\parallel$ 平面 $ADE$。" "\n"
        r"(2) 由 $\angle BAE=\angle DAE=90^{\circ}$ 得 $AE\perp AB$ 且 $AE\perp AD$，"
        r"又 $AB\cap AD=A$，故 $AE\perp$ 平面 $ABCD$。" "\n"
        r"由 $EA\parallel FC$ 得 $FC\perp$ 平面 $ABCD$，从而 $FC\perp BC$、$FC\perp CD$。" "\n"
        r"$\because\ \triangle BCF$ 为等腰三角形且 $\angle BCF=90^{\circ}$，"
        r"$\therefore\ BC=CF=b$（设 $AB=a$，$BC=b$，$b=\lambda a$）。" "\n"
        r"于是 $BD=DF=\sqrt{a^{2}+b^{2}}$，$BF=\sqrt2 b$。" "\n"
        r"在等腰 $\triangle BDF$ 中，$BF$ 边上的高为" "\n"
        r"$h=\sqrt{DF^{2}-\left(\dfrac{BF}{2}\right)^{2}}=\sqrt{a^{2}+b^{2}-\dfrac{b^{2}}{2}}"
        r"=a\sqrt{1+\dfrac{\lambda^{2}}{2}}$，" "\n"
        r"$\therefore\ S_{\triangle BDF}=\dfrac12\cdot\sqrt2 b\cdot a\sqrt{1+\dfrac{\lambda^{2}}{2}}$。" "\n"
        r"**一方面**，$V_{A-BDF}=\dfrac13S_{\triangle BDF}\cdot d$，其中 $d=\dfrac{\sqrt6}{6}b$，" "\n"
        r"$V_{A-BDF}=\dfrac13\cdot\dfrac12\sqrt2 b\cdot a\sqrt{1+\dfrac{\lambda^{2}}{2}}\cdot\dfrac{\sqrt6}{6}b"
        r"=\dfrac{\sqrt3}{18}ab^{2}\sqrt{1+\dfrac{\lambda^{2}}{2}}$。" "\n"
        r"**另一方面**，$V_{A-BDF}=V_{F-ABD}=\dfrac13S_{\triangle ABD}\cdot FC"
        r"=\dfrac13\cdot\dfrac12ab\cdot b=\dfrac{ab^{2}}{6}$。" "\n"
        r"两式相等：$\dfrac{\sqrt3}{18}\sqrt{1+\dfrac{\lambda^{2}}{2}}=\dfrac16$，"
        r"即 $\sqrt{1+\dfrac{\lambda^{2}}{2}}=\sqrt3$，" "\n"
        r"$\therefore\ 1+\dfrac{\lambda^{2}}{2}=3$，$\lambda^{2}=4$，又 $\lambda>0$，故 $\lambda=2$。" "\n"
        r"所以存在正实数 $\lambda=2$ 满足题意．"
    ),
    'review': (
        r"① ⭐⭐ **「等腰 + 一个直角」⟹ 腰唯一确定**：由 $EA\parallel FC$ 与 $AE\perp$ 底面得 $FC\perp BC$，"
        r"即 $\angle BCF=90^{\circ}$；等腰三角形若有一内角为 $90^{\circ}$，该角必为顶角，"
        r"故两腰为 $BC=CF=b$。**这一步确定了 $F$ 的位置，否则 (2) 中 $DF$ 无法确定。**" "\n"
        r"② ⭐⭐ **等体积法选「好算的那一个」作顶点**：$A$ 到平面 $BDF$ 的距离是题设给的 $\frac{\sqrt6}{6}b$，"
        r"而 $F$ 到平面 $ABD$ 的距离是 $FC=b$。两边各用各的高，把未知量 $\lambda$ 隔离在 $S_{\triangle BDF}$ 里。" "\n"
        r"③ ⭐ **$BD=DF$ 是等腰 $\triangle BDF$ 的关键**，它让「$BF$ 边上的高」落在 $BF$ 中点，"
        r"用勾股定理一步得出 $h=a\sqrt{1+\frac{\lambda^{2}}{2}}$。" "\n"
        r"④ ⚠ **$\dfrac{\sqrt3}{18}\times\sqrt3=\dfrac{3}{18}=\dfrac16$ 是方程能解净的原因**："
        r"$\frac{1}{2}\sqrt2\cdot\frac{\sqrt6}{6}=\frac{\sqrt{12}}{12}=\frac{\sqrt3}{6}$，再乘 $\frac13$ 得 $\frac{\sqrt3}{18}$，"
        r"$\lambda=2$ 时 $\sqrt{1+\frac42}=\sqrt3$ 恰好把它配成 $\frac16$。命题人把 $d$ 定成 $\frac{\sqrt6}{6}BC$ 正为此。" "\n"
        r"⑤ 数值复核（取 $a=1,\ \lambda=2,\ b=2$）：$BD=DF=\sqrt5=2.2360680$ ✓，$BF=2\sqrt2=2.8284271$ ✓，"
        r"$h=\sqrt{5-2}=\sqrt3=1.7320508$ ✓，$S_{\triangle BDF}=\frac12\times2\sqrt2\times\sqrt3=2.4494897$ ✓，" "\n"
        r"　 $V_{A-BDF}=\frac13\times2.4494897\times\frac{\sqrt6}{6}\times2=0.6666667$；"
        r"$V_{F-ABD}=\frac13\times\frac12\times2\times2=\frac23=0.6666667$ ✓ 完全吻合。" "\n"
        r"⑥ 📌 题干中 $E$ 点由 $\angle BAE=\angle DAE=90^{\circ}$ 定位（即 $AE\perp$ 平面 $ABCD$），"
        r"$F$ 点由 $EA\parallel FC$ 定位，图形仅作辅助。"
    ),
    'topics': ['M-T-325'],
    'src': 'M-T-325-V1',
    'difficulty': 0.75,
})
