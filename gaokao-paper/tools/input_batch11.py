# -*- coding: utf-8 -*-
r"""第11批录入数据：T081~T087，共 17 题。

来源：2024高中数学热点题型归纳完整解析版.pdf p55~p59
      —— 基于 ref_bank 提取文本逐题重建，17 题答案全部独立验算通过。

**书写约束（踩过的坑）**
1. LaTeX 字符串一律 raw **双**引号 `r"..."`。
   单引号会被导数撇号 $f'(x)$ 提前终止。
2. 中文行文里不要用 ASCII 双引号（"理想配集"），要用“”。
   ASCII 双引号会提前结束字符串，且报错位置指向**下一行**。
3. 选项写成 `('A', r"$1$")` 时外层用单引号、内层 raw 双引号，
   不要写成 `r"$1$')` 这种单双混用。

本批跳过的 1 题（已记入 data/skipped.json）：
  M-T-084-V1  $h(x)=\log_{2}x-x$ 在 $(0,+\infty)$ 上无零点
              （$\log_{2}x<x$ 恒成立），且原书无解析，无法重建。
              另两个函数 $f(x)=2^{x}+x$ 与 $g(x)=x-\log_{1/2}x$ 的零点
              满足 $x_{1}+x_{2}=0$，推断第三个函数形式印刷有误。
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'py'))

QS = [
# ---------------- T081 判断零点个数：数形结合 (p56) ----------------
dict(topic='M-T-081', key='M-T-081-V1', kind='变式1', type='填空',
  stem_text=r"[2017 江苏卷] 设 $f(x)$ 是定义在 $\mathbb{R}$ 上且周期为 $1$ 的函数，"
            r"在区间 $[0,1)$ 上，$f(x)=\begin{cases}x^{2},&x\in D\\ x,&x\notin D\end{cases}$，"
            r"其中集合 $D=\left\{x\;\middle|\;x=\frac{n-1}{n},\ n\in\mathbb{N}^{+}\right\}$，"
            r"则方程 $f(x)-\lg x=0$ 的解的个数是 ____",
  opts=[],
  answer=r"$8$",
  solution=r"由 $f(x)\in[0,1)$ 知只需考虑 $\lg x\in[0,1)$，即 $1\leq x<10$。"
           r"对 $x\in[1,10)$，$\lg x$ 与 $f$ 的交点分两类："
           r"$x\in D$ 时 $f(x)=x^{2}$，$x\notin D$ 时 $f(x)=\{x\}$（小数部分）。"
           r"先看 $x\in D$ 一类不可能有交点：$x\in D$ 意味着 $x$ 是有理数，"
           r"设 $x=\frac{q}{p}$（$p,q$ 互质），若 $\lg x$ 也是有理数，"
           r"设 $\lg x=\frac{n}{m}$（$m,n$ 互质，$m\geq 2$），则 $10^{n}=x^{m}=\frac{q^{m}}{p^{m}}$，"
           r"左边是整数、右边不是整数，矛盾。故 $\lg x$ 是无理数，"
           r"不可能等于有理数值的 $x^{2}$。所以只需数第二类交点。"
           r"在 $[k,k+1)$（$k=1,\ldots,9$）上，记 $u=x-k\in[0,1)$，方程为 $u=\lg(k+u)$。"
           r"记 $\varphi(u)=u-\lg(k+u)$，$\varphi'(u)=1-\frac{1}{(k+u)\ln 10}>0$（因 $k+u\geq 1$），"
           r"$\varphi$ 单调递增，每个区间至多一个解。"
           r"$\varphi(0)=-\lg k$，$\varphi(1^{-})=1-\lg(k+1)$："
           r"$k=1$ 时 $\varphi(0)=0$，得 $x=1$（此时 $f(1)=f(0)=0$，$\lg 1=0$，确为解）；"
           r"$k=2,\ldots,8$ 时 $\varphi(0)<0$、$\varphi(1^{-})>0$，各一个解；"
           r"$k=9$ 时 $\varphi(1^{-})=1-\lg 10=0$，在 $u<1$ 内 $\varphi<0$，无解。"
           r"故解的个数为 $1+7=8$。",
  review='数值验证：在 $[1,10)$ 上解 $u=\\lg(k+u)$，得交点横坐标 '
         '$1$、$2.3758$、$3.5503$、$4.6692$、$5.7605$、$6.8347$、$7.8975$、$8.9519$，共 $8$ 个。'),

dict(topic='M-T-081', key='M-T-081-V2', kind='变式2', type='选择',
  stem_text=r"若定义在 $\mathbb{R}$ 上的偶函数 $f(x)$ 满足 $f(x+2)=f(x)$，"
            r"且当 $x\in[0,1]$ 时，$f(x)=x$，"
            r"则函数 $y=f(x)-\log_{3}|x|$ 的零点个数是（　　）",
  opts=[('A', r"多于 $4$ 个"), ('B', r"$4$ 个"), ('C', r"$3$ 个"), ('D', r"$2$ 个")],
  answer='B',
  solution=r"$f$ 是周期为 $2$ 的偶函数，值域 $[0,1]$。"
           r"由 $f(x)=\log_{3}|x|$ 且 $f(x)\in[0,1]$ 知 $\log_{3}|x|\in[0,1]$，即 $1\leq|x|\leq 3$。"
           r"两个函数都是偶函数，只需算 $x>0$ 再乘 $2$。"
           r"$x\in(0,1)$：$\log_{3}x<0$ 而 $f(x)=x>0$，无零点。"
           r"$x\in[1,2]$：由周期与偶性 $f(x)=2-x$，由 $1$ 降到 $0$；"
           r"$\log_{3}x$ 由 $0$ 升到 $\log_{3}2\approx0.63$，二者恰有 $1$ 个交点。"
           r"$x\in[2,3]$：$f(x)=x-2$ 由 $0$ 升到 $1$，$\log_{3}x$ 由 $\log_{3}2\approx0.63$ 升到 $1$；"
           r"$x=3$ 时二者都等于 $1$，得第 $2$ 个零点（端点）。"
           r"故正半轴有 $2$ 个零点，由偶对称共 $4$ 个。选 B。",
  review='数值验证：正半轴变号零点在 $x\\approx1.5823$，加端点 $x=3$，共 $2$ 个，'
         '偶对称得 $4$ 个。注意 $x=3$ 是端点，扫描变号检测不到，需单独判。'),

# ---------------- T082 判断零点个数：参数讨论 (p57) ----------------
dict(topic='M-T-082', key='M-T-082-V1', kind='变式1', type='选择',
  stem_text=r"设方程 $|x^{2}-3|=a$ 的解的个数为 $m$，则 $m$ 不可能等于（　　）",
  opts=[('A', r"$1$"), ('B', r"$2$"), ('C', r"$3$"), ('D', r"$4$")],
  answer='A',
  solution=r"作出 $y=|x^{2}-3|$ 与 $y=a$ 的图象。由 $|x^{2}-3|=a$ 得 $x^{2}=3+a$ 或 $x^{2}=3-a$。"
           r"$a<0$：两式均无解，$m=0$。"
           r"$a=0$：$x^{2}=3$，$m=2$。"
           r"$0<a<3$：$3+a>0$ 给 $2$ 个根，$3-a>0$ 也给 $2$ 个根，$m=4$。"
           r"$a=3$：$x^{2}=6$ 给 $2$ 个根，$x^{2}=0$ 给 $1$ 个根（$x=0$），$m=3$。"
           r"$a>3$：$3+a>0$ 给 $2$ 个根，$3-a<0$ 无解，$m=2$。"
           r"故 $m$ 的可能取值为 $0,2,3,4$，不可能等于 $1$。选 A。",
  review=''),

# ---------------- T083 判断零点个数：含参直线 (p57) ----------------
dict(topic='M-T-083', key='M-T-083-V1', kind='变式1', type='填空',
  stem_text=r"(2021·唐山月考) 已知函数 $f(x)=|x-2|+1$，$g(x)=kx$。"
            r"若方程 $f(x)=g(x)$ 有两个不相等的实根，则实数 $k$ 的取值范围是 ____",
  opts=[],
  answer=r"$\left(\frac{1}{2},1\right)$",
  solution=r"$f(x)=\begin{cases}3-x,&x<2\\ x-1,&x\geq 2\end{cases}$。分两段解方程。"
           r"$x<2$：$3-x=kx$，得 $x=\frac{3}{k+1}$，需 $k+1>0$ 且 $\frac{3}{k+1}<2$，即 $k>\frac12$。"
           r"$x\geq 2$：$x-1=kx$，得 $x=\frac{1}{1-k}$，需 $1-k>0$ 且 $\frac{1}{1-k}\geq 2$，"
           r"即 $k<1$ 且 $k\geq\frac12$。"
           r"要恰有两个不等实根，需两段各给一个解："
           r"$k>\frac12$（第一段）与 $\frac12\leq k<1$（第二段）取交集得 $\frac12<k<1$。"
           r"验证端点：$k=\frac12$ 时第一段解 $x=2$ 不满足 $x<2$，只剩 $x=2$ 一个根；"
           r"$k=1$ 时第二段无解，只剩 $x=\frac32$ 一个根。"
           r"故 $k\in\left(\frac12,1\right)$。",
  review='程序验证：$k=0.5$ 与 $k=1.0$ 时各 $1$ 个解，'
         '$k=0.51$、$0.7$、$0.99$ 时均为 $2$ 个解。'),

# ---------------- T084 判断零点个数：零点比较 (p58) ----------------
dict(topic='M-T-084', key='M-T-084-V2', kind='变式2', type='选择',
  stem_text=r"设 $a$，$b$，$c$ 均为正数，且 $-\mathrm{e}^{a}=\ln a$，"
            r"$-\mathrm{e}^{-b}=\ln b$，$\mathrm{e}^{-c}=\ln c$，则（　　）",
  opts=[('A', r"$c>b>a$"), ('B', r"$a>b>c$"),
        ('C', r"$b>a>c$"), ('D', r"$c>a>b$")],
  answer='A',
  solution=r"分别估计三个数所在区间（只用单调性，不求精确值）。"
           r"（1）$\mathrm{e}^{a}=-\ln a$：$\mathrm{e}^{a}>\mathrm{e}^{0}=1$，故 $-\ln a>1=\ln\mathrm{e}$，"
           r"即 $\ln a<-1$，得 $0<a<\frac1{\mathrm{e}}$。"
           r"（2）$\mathrm{e}^{-b}=-\ln b$：$0<\mathrm{e}^{-b}<1$，故 $0<-\ln b<1$，"
           r"即 $-1<\ln b<0$，得 $\frac1{\mathrm{e}}<b<1$。"
           r"（3）$\mathrm{e}^{-c}=\ln c$：$0<\mathrm{e}^{-c}<1$，故 $0<\ln c<1$，得 $1<c<\mathrm{e}$。"
           r"综上 $a<\frac1{\mathrm{e}}<b<1<c$，故 $c>b>a$，选 A。"
           r"数值上 $a\approx0.2699$，$b\approx0.5671$，$c\approx1.3098$；"
           r"其中 $b$ 恰为 $x=\mathrm{e}^{-x}$ 的解（欧米伽常数 $W(1)$），且有 $\mathrm{e}^{-c}=a$ 的关系。",
  review='注意第三问的函数 $\\mathrm{e}^{-x}-\\ln x$ 是**递减**的，'
         '二分时方向与前两问相反（前两问递增）。写验证脚本时这里踩过坑。'),

# ---------------- T085 导数求切线：在某点处的切线 (p59) ----------------
dict(topic='M-T-085', key='M-T-085-E1', kind='典例', type='填空',
  stem_text=r"已知函数 $f(x)=\frac{2\sin x}{x+1}$，则曲线 $y=f(x)$ 在点 $(0,0)$ 处的切线的方程为 ____",
  opts=[],
  answer=r"$2x-y=0$",
  solution=r"$f'(x)=\frac{2\cos x\cdot(x+1)-2\sin x}{(x+1)^{2}}$，"
           r"$k=f'(0)=\frac{2\cdot1\cdot1-0}{1}=2$。"
           r"又切点为 $(0,0)$，故切线方程为 $y=2x$，即 $2x-y=0$。",
  review=''),

dict(topic='M-T-085', key='M-T-085-V1', kind='变式1', type='填空',
  stem_text=r"曲线 $f(x)=(x+1)\mathrm{e}^{x}+x$ 在点 $(0,1)$ 处的切线方程为 ____",
  opts=[],
  answer=r"$3x-y+1=0$",
  solution=r"$f'(x)=\mathrm{e}^{x}+(x+1)\mathrm{e}^{x}+1$，"
           r"在 $x=0$ 处 $f'(0)=1+(0+1)\cdot1+1=3$。"
           r"又 $f(0)=(0+1)\cdot1+0=1$，切点确为 $(0,1)$。"
           r"切线：$y-1=3(x-0)$，即 $3x-y+1=0$。",
  review=''),

dict(topic='M-T-085', key='M-T-085-V2', kind='变式2', type='填空',
  stem_text=r"已知点 $P(-1,1)$ 在曲线 $y=\frac{x^{2}}{x+a}$ 上，"
            r"则曲线在点 $P$ 处的切线方程为 ____",
  opts=[],
  answer=r"$y=-3x-2$",
  solution=r"由 $P(-1,1)$ 在曲线上：$1=\frac{(-1)^{2}}{-1+a}=\frac1{a-1}$，得 $a=2$，即 $y=\frac{x^{2}}{x+2}$。",
  solution_ext=r"求导：$y'=\frac{2x(x+2)-x^{2}}{(x+2)^{2}}=\frac{x^{2}+4x}{(x+2)^{2}}$，"
           r"在 $x=-1$ 处 $k=\frac{1-4}{1}=-3$。"
           r"切线：$y-1=-3(x+1)$，即 $y=-3x-2$。",
  review=''),

dict(topic='M-T-085', key='M-T-085-V3', kind='变式3', type='选择',
  stem_text=r"已知曲线 $f(x)=\ln x+\frac{x^{2}}{a}$ 在点 $(1,f(1))$ 处的切线的倾斜角为 "
            r"$\frac{3\pi}{4}$，则 $a$ 的值为（　　）",
  opts=[('A', r"$1$"), ('B', r"$-1$"), ('C', r"$-\frac{1}{2}$"), ('D', r"$-4$")],
  answer='B',
  solution=r"$f'(x)=\frac1x+\frac{2x}{a}$，倾斜角 $\frac{3\pi}{4}$ 对应斜率 $\tan\frac{3\pi}{4}=-1$。"
           r"由 $f'(1)=1+\frac2a=-1$ 得 $\frac2a=-2$，故 $a=-1$。选 B。",
  review=''),

# ---------------- T086 导数求切线：平行/垂直/过定点 (p59) ----------------
dict(topic='M-T-086', key='M-T-086-E1', kind='典例', type='选择',
  stem_text=r"曲线 $f(x)=x^{3}+x-2$ 在 $P_{0}$ 处的切线平行于直线 $y=4x-1$，"
            r"则 $P_{0}$ 点的坐标为（　　）",
  opts=[('A', r"$(1,0)$"), ('B', r"$(2,8)$"),
        ('C', r"$(1,0)$ 和 $(-1,-4)$"), ('D', r"$(2,8)$ 和 $(-1,-4)$")],
  answer='C',
  solution=r"$f'(x)=3x^{2}+1$。切线与 $y=4x-1$ 平行，斜率为 $4$，"
           r"令 $3x^{2}+1=4$ 得 $x=\pm1$。"
           r"$f(1)=1+1-2=0$，得 $(1,0)$；$f(-1)=-1-1-2=-4$，得 $(-1,-4)$。故选 C。",
  review=''),

dict(topic='M-T-086', key='M-T-086-V1', kind='变式1', type='选择',
  stem_text=r"已知函数 $f(x)=\mathrm{e}^{x}+\frac{a}{\mathrm{e}^{x}}$ 为偶函数，"
            r"若曲线 $y=f(x)$ 的一条切线与直线 $2x+3y=0$ 垂直，"
            r"则切点的横坐标为（　　）",
  opts=[('A', r"$2$"), ('B', r"$-2$"), ('C', r"$2\ln 2$"), ('D', r"$\ln 2$")],
  answer='D',
  solution=r"由 $f$ 为偶函数：$f(-x)=\mathrm{e}^{-x}+a\mathrm{e}^{x}$ 与 "
           r"$f(x)=\mathrm{e}^{x}+a\mathrm{e}^{-x}$ 相等，"
           r"整理得 $(\mathrm{e}^{x}-\mathrm{e}^{-x})(a-1)=0$ 对一切 $x$ 成立，故 $a=1$，"
           r"$f(x)=\mathrm{e}^{x}+\mathrm{e}^{-x}$，$f'(x)=\mathrm{e}^{x}-\mathrm{e}^{-x}$。",
  solution_ext=r"直线 $2x+3y=0$ 的斜率为 $-\frac23$，故切线斜率为 $\frac32$。"
           r"令 $\mathrm{e}^{x_{0}}-\mathrm{e}^{-x_{0}}=\frac32$，记 $t=\mathrm{e}^{x_{0}}>0$，"
           r"则 $t-\frac1t=\frac32$，即 $2t^{2}-3t-2=0$，解得 $t=2$（负根舍去），"
           r"故 $x_{0}=\ln 2$。选 D。",
  review=''),

dict(topic='M-T-086', key='M-T-086-V2', kind='变式2', type='选择',
  stem_text=r"过曲线 $y=\cos x$ 上一点 $P\!\left(\frac{\pi}{3},\frac12\right)$ 且与曲线在点 $P$ 处的切线"
            r"垂直的直线的方程为（　　）",
  opts=[('A', r"$2x-\sqrt{3}y-\frac{2\pi}{3}+\frac{\sqrt{3}}{2}=0$"),
        ('B', r"$\sqrt{3}x+2y-\frac{\sqrt{3}\pi}{3}-1=0$"),
        ('C', r"$2x-\sqrt{3}y-\frac{2\pi}{3}-\frac{\sqrt{3}}{2}=0$"),
        ('D', r"$\sqrt{3}x+2y-\frac{\sqrt{3}\pi}{3}+1=0$")],
  answer='A',
  solution=r"$y'=-\sin x$，在 $x=\frac{\pi}{3}$ 处切线斜率为 $-\sin\frac{\pi}{3}=-\frac{\sqrt3}{2}$，"
           r"故与其垂直的直线斜率为 $\frac{2}{\sqrt3}=\frac{2\sqrt3}{3}$。",
  solution_ext=r"所求直线：$y-\frac12=\frac{2\sqrt3}{3}\left(x-\frac{\pi}{3}\right)$。"
           r"两边乘 $\sqrt3$：$\sqrt3\,y-\frac{\sqrt3}{2}=2x-\frac{2\pi}{3}$，"
           r"整理得 $2x-\sqrt3\,y-\frac{2\pi}{3}+\frac{\sqrt3}{2}=0$。故选 A。",
  review=''),

dict(topic='M-T-086', key='M-T-086-V3', kind='变式3', type='填空',
  stem_text=r"曲线 $y=\sin x+2x+1$ 在点 $P$ 处的切线方程是 $3x-y+1=0$，"
            r"则切点 $P$ 的坐标是 ____",
  opts=[],
  answer=r"$(0,1)$",
  solution=r"设 $P(x_{0},y_{0})$。$y'=\cos x+2$，由切线斜率为 $3$ 得 $\cos x_{0}+2=3$，"
           r"即 $\cos x_{0}=1$，$x_{0}=2k\pi$（$k\in\mathbb{Z}$）。"
           r"又切点既在曲线上也在切线上：$y_{0}=3x_{0}+1$ 且 $y_{0}=\sin x_{0}+2x_{0}+1$。"
           r"代入 $x_{0}=2k\pi$（此时 $\sin x_{0}=0$）得 $y_{0}=4k\pi+1$ 与 $y_{0}=6k\pi+1$，"
           r"比较得 $k=0$。故 $P(0,1)$。",
  review=''),

# ---------------- T087 导数求切线：已知切线求参数 (p59) ----------------
dict(topic='M-T-087', key='M-T-087-E1', kind='典例', type='选择',
  stem_text=r"已知曲线 $y=x^{3}$ 在点 $(a,b)$ 处的切线与直线 $x+3y+1=0$ 垂直，"
            r"则 $a$ 的取值是（　　）",
  opts=[('A', r"$-1$"), ('B', r"$\pm1$"), ('C', r"$1$"), ('D', r"$\pm3$")],
  answer='B',
  solution=r"直线 $x+3y+1=0$ 的斜率为 $-\frac13$，"
           r"故切线斜率为 $3$。由 $y'=3x^{2}$ 得 $3a^{2}=3$，$a=\pm1$。选 B。",
  review=''),

dict(topic='M-T-087', key='M-T-087-V1', kind='变式1', type='填空',
  stem_text=r"若曲线 $y=\ln x$（$x>0$）的一条切线是直线 $y=\frac12x+b$，"
            r"则实数 $b$ 的值为 ____",
  opts=[],
  answer=r"$-1+\ln 2$",
  solution=r"设切点 $(x_{0},y_{0})$。$y'=\frac1x$，由切线斜率为 $\frac12$ 得 "
           r"$\frac1{x_{0}}=\frac12$，$x_{0}=2$。"
           r"$y_{0}=\ln 2$，切点 $(2,\ln 2)$ 代入 $y=\frac12x+b$："
           r"$\ln 2=1+b$，故 $b=-1+\ln 2$。",
  review=''),

dict(topic='M-T-087', key='M-T-087-V2', kind='变式2', type='填空',
  stem_text=r"已知曲线 $y=ax^{3}$ 与直线 $6x-y-4=0$ 相切，则实数 $a$ 的值为 ____",
  opts=[],
  answer=r"$2$",
  solution=r"设切点 $(m,n)$。由 $y=ax^{3}$ 得 $y'=3ax^{2}$。相切条件："
           r"$3am^{2}=6$（斜率等于 $6$），$n=am^{3}$（在曲线上），$6m-n-4=0$（在直线上）。"
           r"由第一式 $am^{2}=2$，代入第二式得 $n=2m$，再代入第三式 $6m-2m-4=0$ 得 $m=1$，"
           r"于是 $n=2$、$a=2$。",
  review=''),

dict(topic='M-T-087', key='M-T-087-V3', kind='变式3', type='填空',
  stem_text=r"已知 $x$ 轴为曲线 $f(x)=4x^{3}+4(a-1)x+1$ 的切线，则 $a$ 的值为 ____",
  opts=[],
  answer=r"$\frac{1}{4}$",
  solution=r"设 $x$ 轴与曲线的切点为 $(x_{0},0)$。$f'(x)=12x^{2}+4(a-1)$。"
           r"相切条件：$f(x_{0})=0$ 且 $f'(x_{0})=0$。"
           r"由 $f'(x_{0})=0$ 得 $4(a-1)=-12x_{0}^{2}$，代入 $f(x_{0})=0$："
           r"$4x_{0}^{3}-12x_{0}^{2}\cdot x_{0}+1=0$，即 $-8x_{0}^{3}+1=0$，$x_{0}=\frac12$。"
           r"于是 $4(a-1)=-12\cdot\frac14=-3$，$a-1=-\frac34$，$a=\frac14$。",
  review=''),
]

if __name__ == '__main__':
    print('共 %d 题' % len(QS))
