---
puppeteer:
  format: "A4"          # 纸张规格：A4 / Letter / Legal / A3 / Tabloid / A0~A10
  scale: 0.9           # 整体缩放：<1 缩小字体，>1 放大；0.78 ≈ 把 12pt 变 9pt
  landscape: false       # true=横向（宽表格、公式多列时推荐），false=纵向
  printBackground: true # 是否打印代码块/表格的背景色，true 保留样式
  displayHeaderFooter: true
  headerTemplate: |     # 页眉 HTML，| 表示多行字符串
    <div style="font-size:9px; color:#888; text-align:center; width:100%; border-bottom:1px solid #ddd; padding-bottom:4px;">
      物理学（第七版）上册 · 公式速查表
    </div>
  footerTemplate: |     # 页脚 HTML
    <div style="font-size:9px; color:#888; text-align:center; width:100%; border-top:1px solid #ddd; padding-top:4px;">
      <span class="pageNumber"></span> / <span class="totalPages"></span>
    </div>
  margin:               # 页面四周边距
    top: "1.2cm"
    bottom: "1.2cm"
    left: "1.2cm"
    right: "1.2cm"
---

# 《物理学（第七版）上册》公式速查表

> 精简版 · 8章核心公式 · 适合考前快速翻阅

---

## 常用物理常量

| 符号 | 名称 | 数值 |
|:---|:---|:---|
| $g$ | 重力加速度 | $9.8\ \text{m/s}^2$ |
| $G$ | 引力常量 | $6.67 \times 10^{-11}\ \text{N}\cdot\text{m}^2/\text{kg}^2$ |
| $e$ | 元电荷 | $1.602 \times 10^{-19}\ \text{C}$ |
| $\varepsilon_0$ | 真空介电常量 | $8.85 \times 10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$ |
| $k = \frac{1}{4\pi\varepsilon_0}$ | 库仑常数 | $9.0 \times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$ |
| $\mu_0$ | 真空磁导率 | $4\pi \times 10^{-7}\ \text{N/A}^2$ |

---

## 第1章 质点运动学

### 位矢、速度、加速度
$$\boldsymbol{r} = x\boldsymbol{i} + y\boldsymbol{j} + z\boldsymbol{k},\quad r = \sqrt{x^2+y^2+z^2}$$
$$\boldsymbol{v} = \frac{d\boldsymbol{r}}{dt},\quad \boldsymbol{a} = \frac{d\boldsymbol{v}}{dt} = \frac{d^2\boldsymbol{r}}{dt^2}$$
$$\Delta\boldsymbol{r} = \boldsymbol{r}_B - \boldsymbol{r}_A,\quad |\Delta\boldsymbol{r}| \neq |\boldsymbol{r}_B| - |\boldsymbol{r}_A|$$

### 两类基本问题
| 类型 | 已知 → 求 | 方法 |
|:---|:---|:---|
| 第一类（微分） | $\boldsymbol{r}(t)$ → $\boldsymbol{v},\boldsymbol{a}$ | 求导 |
| 第二类（积分） | $\boldsymbol{a}$ + 初条件 → $\boldsymbol{v},\boldsymbol{r}$ | $\boldsymbol{v}=\boldsymbol{v}_0+\int\!\boldsymbol{a}\,dt$，$\boldsymbol{r}=\boldsymbol{r}_0+\int\!\boldsymbol{v}\,dt$ |
| 换元技巧 | $a=a(x)$ | $a = v\frac{dv}{dx}$ → $\int v\,dv = \int a(x)\,dx$ |

### 圆周运动
$$\omega = \frac{d\theta}{dt},\quad \beta = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$$
$$\boldsymbol{a} = a_\tau\boldsymbol{e}_\tau + a_n\boldsymbol{e}_n$$
$$a_\tau = \frac{dv}{dt} = r\beta,\quad a_n = \frac{v^2}{r} = r\omega^2,\quad a = \sqrt{a_\tau^2 + a_n^2}$$

### 线角关系
$$s = r\theta,\quad v = r\omega,\quad a_\tau = r\beta,\quad a_n = r\omega^2$$

### 匀变速率圆周运动（$\beta =$ 常量）
$$\omega = \omega_0 + \beta t,\quad \theta = \theta_0 + \omega_0 t + \tfrac{1}{2}\beta t^2,\quad \omega^2 = \omega_0^2 + 2\beta(\theta-\theta_0)$$

### 抛体运动
平抛（$v_0$ 水平）：$x = v_0 t,\; y = \frac{1}{2}gt^2,\;$ 轨迹 $y = \dfrac{g}{2v_0^2}x^2$
斜抛（$v_0$ 与水平夹角 $\theta$）：
$v_x = v_0\cos\theta,\; v_y = v_0\sin\theta - gt$
射程 $R = \dfrac{v_0^2\sin 2\theta}{g}$，射高 $H = \dfrac{v_0^2\sin^2\theta}{2g}$，飞行时间 $T = \dfrac{2v_0\sin\theta}{g}$

### 相对运动（伽利略变换）
$$\boldsymbol{v}_{\text{绝}} = \boldsymbol{v}_{\text{相}} + \boldsymbol{v}_{\text{牵}}$$
$$\boldsymbol{a}_{\text{绝}} = \boldsymbol{a}_{\text{相}} + \boldsymbol{a}_{\text{牵}}$$

---

## 第2章 牛顿运动定律

### 三大定律
1. **惯性定律**：$\sum\boldsymbol{F}=0 \Rightarrow$ 静止或匀速直线运动
2. **核心方程**：$\boldsymbol{F} = \frac{d\boldsymbol{p}}{dt} = m\boldsymbol{a}$（$m$ 恒定）
3. **作用-反作用**：$\boldsymbol{F}_{12} = -\boldsymbol{F}_{21}$

### 常见力
| 力 | 公式 | 方向 |
|:---|:---|:---|
| 万有引力 | $F = G\frac{m_1 m_2}{r^2}$ | 沿连线，吸引 |
| 重力 | $P = mg$ | 竖直向下 |
| 弹簧弹力（胡克定律） | $F = -kx$ | 指向平衡位置 |
| 最大静摩擦力 | $f_{s\max} = \mu_s N$ | 与相对运动趋势反向 |
| 滑动摩擦力 | $f_k = \mu_k N$ | 与相对运动反向 |

### 非惯性系 *
$$\boldsymbol{F}_i = -m\boldsymbol{a}_0 \quad \text{（平动惯性力）}$$
离心惯性力：$F_e = m\omega^2 r$；科里奥利力：$\boldsymbol{F}_c = -2m\boldsymbol{\omega}\times\boldsymbol{v}'$

### 解题通用步骤
1. 选对象 → 2. 受力分析（重力→弹力→摩擦力） → 3. 列 $\sum\boldsymbol{F}=m\boldsymbol{a}$ → 4. 分解求解

---

## 第3章 动量守恒定律和能量守恒定律

### 动量定理
$$\boldsymbol{I} = \int_{t_1}^{t_2}\boldsymbol{F}\,dt = \boldsymbol{p}_2 - \boldsymbol{p}_1 = m\boldsymbol{v}_2 - m\boldsymbol{v}_1$$

### 动量守恒定律
$$\sum\boldsymbol{F}_{\text{外}} = 0 \;\Longrightarrow\; \sum\boldsymbol{p} = \text{恒矢量}$$
（若某方向合外力为零，则该方向分量守恒）

### 变质量问题（火箭）*
$$m\frac{d\boldsymbol{v}}{dt} = \boldsymbol{F}_{\text{外}} + \frac{dm}{dt}(\boldsymbol{u} - \boldsymbol{v})$$
火箭速度公式（不计外力）：$v - v_0 = u\ln\frac{m_0}{m}$

### 功与动能定理
$$W = \int_A^B \boldsymbol{F}\cdot d\boldsymbol{r},\quad P = \frac{dW}{dt} = \boldsymbol{F}\cdot\boldsymbol{v}$$
$$W_{\text{合}} = E_{kB} - E_{kA} = \tfrac{1}{2}mv_B^2 - \tfrac{1}{2}mv_A^2$$

### 势能
| 类型 | 表达式 | 零势点 |
|:---|:---|:---|
| 重力势能 | $E_p = mgh$ | 任意（地面） |
| 弹性势能 | $E_p = \frac{1}{2}kx^2$ | 平衡位置 |
| 万有引力势能 | $E_p = -G\frac{Mm}{r}$ | 无穷远 |

保守力做功：$W_{\text{保}} = -\Delta E_p$；保守力与势能关系：$F = -\dfrac{dE_p}{dr}$

### 功能原理与机械能守恒
$$W_{\text{外}} + W_{\text{非保内}} = E_1 - E_0 = \Delta E$$
$$W_{\text{外}} = 0,\; W_{\text{非保内}} = 0 \;\Longrightarrow\; E_k + E_p = \text{常量}$$

### 碰撞
| 类型 | $e$ | 动量 | 动能 | 特征 |
|:---|:---|:---|:---|:---|
| 完全弹性 | $1$ | 守恒 | 守恒 | 无能量损失 |
| 完全非弹性 | $0$ | 守恒 | 不守恒（最大损失） | 碰后共速 |
| 非弹性 | $0<e<1$ | 守恒 | 不守恒 | — |

恢复系数：$e = \dfrac{v_2 - v_1}{v_{10} - v_{20}}$

弹性碰撞通式：$v_1 = \frac{(m_1-m_2)v_{10} + 2m_2 v_{20}}{m_1+m_2},\; v_2 = \frac{(m_2-m_1)v_{20} + 2m_1 v_{10}}{m_1+m_2}$
特例（$m_1=m_2,\;v_{20}=0$）：碰后**交换速度**（$v_1=0,\;v_2=v_{10}$）
完全非弹性碰撞：$v = \frac{m_1 v_{10} + m_2 v_{20}}{m_1+m_2},\; \Delta E_k = \frac{m_1 m_2(v_{10}-v_{20})^2}{2(m_1+m_2)}$

### 质心与柯尼希定理
$$\boldsymbol{r}_C = \frac{\sum m_i\boldsymbol{r}_i}{M},\quad \sum\boldsymbol{F}_{\text{外}} = M\boldsymbol{a}_C$$
$$E_k = \tfrac{1}{2}Mv_C^2 + E_{k(\text{内})}$$

---

## 第4章 刚体转动和流体运动

### 转动运动学
$$\omega = \frac{d\theta}{dt},\quad \beta = \frac{d\omega}{dt},\quad v = r\omega,\quad a_\tau = r\beta,\quad a_n = r\omega^2$$

### 转动定律
$$M = J\beta \quad\text{（类比 } F = ma\text{）}$$

### 常见转动惯量
| 刚体 | 转轴 | $J$ |
|:---|:---|:---|
| 细圆环/圆筒 | 过中心⊥环面 | $mR^2$ |
| 圆盘/圆柱 | 过中心⊥盘面 | $\frac{1}{2}mR^2$ |
| 细杆 | 过中心⊥杆 | $\frac{1}{12}mL^2$ |
| 细杆 | 过一端⊥杆 | $\frac{1}{3}mL^2$ |
| 实心球 | 过球心 | $\frac{2}{5}mR^2$ |
| 薄球壳 | 过球心 | $\frac{2}{3}mR^2$ |

**平行轴定理**：$J = J_C + md^2$

### 角动量定理与守恒
$$\boldsymbol{L} = \boldsymbol{r} \times \boldsymbol{p} = \boldsymbol{r} \times m\boldsymbol{v},\quad L_{\text{刚体}} = J\omega$$
$$\int M\,dt = L_2 - L_1 = J\omega_2 - J\omega_1$$
$$\sum M_{\text{外}} = 0 \;\Longrightarrow\; L = J\omega = \text{常量}$$

### 转动动能与功
$$E_k = \tfrac{1}{2}J\omega^2,\quad W = \int M\,d\theta = \tfrac{1}{2}J\omega_2^2 - \tfrac{1}{2}J\omega_1^2$$
$$P = M\omega$$

### 刚体平面平行运动（纯滚动）*
条件：$v_C = R\omega,\; a_C = R\beta$
动能：$E_k = \frac{1}{2}Mv_C^2 + \frac{1}{2}J_C\omega^2$
斜面纯滚质心加速度：$a_C = \dfrac{g\sin\theta}{1 + J_C/(MR^2)}$
| 刚体 | $J_C$ | $a_C$ |
|:---|:---|:---|
| 圆环/薄圆筒 | $MR^2$ | $\frac{1}{2}g\sin\theta$ |
| 圆盘/圆柱 | $\frac{1}{2}MR^2$ | $\frac{2}{3}g\sin\theta$ |
| 球体 | $\frac{2}{5}MR^2$ | $\frac{5}{7}g\sin\theta$ |
| 球壳 | $\frac{2}{3}MR^2$ | $\frac{3}{5}g\sin\theta$ |

### 流体 *
连续性方程（不可压缩）：$S_1 v_1 = S_2 v_2$
伯努利方程：$p + \frac{1}{2}\rho v^2 + \rho gh = \text{常量}$

---

## 第5章 静电场

### 库仑定律
$$\boldsymbol{F} = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r^2}\boldsymbol{e}_r,\quad k = \frac{1}{4\pi\varepsilon_0} \approx 9.0\times 10^9$$

### 电场强度
定义：$\boldsymbol{E} = \boldsymbol{F}/q_0$
点电荷：$\boldsymbol{E} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}\boldsymbol{e}_r$
叠加原理：$\boldsymbol{E} = \sum\boldsymbol{E}_i,\quad \boldsymbol{E} = \int d\boldsymbol{E}$
电偶极矩：$\boldsymbol{p} = q\boldsymbol{l}$
电偶极子场强（$x \gg l$）：
- 中垂线上：$\boldsymbol{E} = -\dfrac{1}{4\pi\varepsilon_0}\dfrac{\boldsymbol{p}}{y^3}$
- 延长线上：$E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{x^3}$

### 高斯定理
$$\oint_S \boldsymbol{E}\cdot d\boldsymbol{S} = \frac{1}{\varepsilon_0}\sum_{(S\text{内})} q_i$$

### 常见场强分布
| 模型 | 场强 $E$ |
|:---|:---|
| 无限长均匀带电直线（线密度 $\lambda$） | $\dfrac{\lambda}{2\pi\varepsilon_0 r}$ |
| 无限大均匀带电平面（面密度 $\sigma$） | $\dfrac{\sigma}{2\varepsilon_0}$（匀强） |
| 均匀带电球壳($R$) 壳内/壳外 | $0$ / $\dfrac{Q}{4\pi\varepsilon_0 r^2}$ |
| 均匀带电球体($R$) 体内/体外 | $\dfrac{Qr}{4\pi\varepsilon_0 R^3}$ / $\dfrac{Q}{4\pi\varepsilon_0 r^2}$ |
| 带电圆环轴线（距心 $x$） | $\dfrac{qx}{4\pi\varepsilon_0(R^2+x^2)^{3/2}}$ |

### 环路定理与电势
$$\oint \boldsymbol{E}\cdot d\boldsymbol{l} = 0 \quad \text{（静电场是保守场）}$$
$$U_P = \int_P^{\infty} \boldsymbol{E}\cdot d\boldsymbol{l},\quad U_{AB} = U_A - U_B = \int_A^B \boldsymbol{E}\cdot d\boldsymbol{l}$$
点电荷电势：$U = \dfrac{q}{4\pi\varepsilon_0 r}$；叠加：$U = \sum\dfrac{q_i}{4\pi\varepsilon_0 r_i} = \int\dfrac{dq}{4\pi\varepsilon_0 r}$
电场力做功：$W_{AB} = qU_{AB}$

### 场强与电势梯度
$$\boldsymbol{E} = -\nabla U,\quad E_l = -\frac{\partial U}{\partial l},\quad E = -\frac{dU}{dr}$$

### 电偶极子在外场中 *
力矩：$\boldsymbol{M} = \boldsymbol{p} \times \boldsymbol{E}$；势能：$W_e = -\boldsymbol{p}\cdot\boldsymbol{E}$

---

## 第6章 静电场中的导体与电介质

### 导体静电平衡
条件：$E_{\text{内}}=0$，$\boldsymbol{E}_{\text{表面}}\perp$ 表面，导体为等势体
表面场强：$E = \sigma/\varepsilon_0$（垂直表面）；电荷分布于表面；尖端曲率大 → $\sigma$ 大 → 尖端放电

### 电介质
$$E = E_0/\varepsilon_r,\quad \varepsilon = \varepsilon_r\varepsilon_0$$
表面极化电荷：$\sigma' = (1 - 1/\varepsilon_r)\sigma_0$

### 电位移矢量与有介质高斯定理
$$\boldsymbol{D} = \varepsilon\boldsymbol{E} = \varepsilon_r\varepsilon_0\boldsymbol{E}$$
$$\oint_S \boldsymbol{D}\cdot d\boldsymbol{S} = \sum q_{i(\text{自由})}$$

### 电容
定义：$C = Q/U$
平行板：$C = \dfrac{\varepsilon_0\varepsilon_r S}{d}$
球形：$C = 4\pi\varepsilon_0\varepsilon_r\dfrac{R_A R_B}{R_B - R_A}$
圆柱形：$C = \dfrac{2\pi\varepsilon_0\varepsilon_r L}{\ln(R_B/R_A)}$

串并联：$C_{\text{并}} = \sum C_i,\quad \dfrac{1}{C_{\text{串}}} = \sum\dfrac{1}{C_i}$

### 静电场能量
电容器储能：$W_e = \dfrac{Q^2}{2C} = \dfrac{1}{2}CU^2 = \dfrac{1}{2}QU$
能量密度：$w_e = \dfrac{1}{2}\varepsilon E^2 = \dfrac{1}{2}\boldsymbol{D}\cdot\boldsymbol{E}$
总能量：$W_e = \displaystyle\int_V \dfrac{1}{2}\varepsilon E^2\,dV$

### RC电路暂态过程 *
时间常数：$\tau = RC$
充电：$q(t) = C\mathcal{E}\!\left(1 - e^{-t/\tau}\right),\; I(t) = \dfrac{\mathcal{E}}{R}e^{-t/\tau}$
放电：$q(t) = Q_0 e^{-t/\tau},\; I(t) = -\dfrac{Q_0}{\tau}e^{-t/\tau}$
通用三要素：$f(t) = f(\infty) + [f(0) - f(\infty)]e^{-t/\tau}$

---

## 第7章 恒定磁场

### 电流与电流密度
$$I = \frac{dq}{dt},\quad j = \frac{dI}{dS_\perp},\quad I = \int_S \boldsymbol{j}\cdot d\boldsymbol{S}$$

### 电动势
$$\mathcal{E} = \int_{-}^{+} \boldsymbol{E}_k \cdot d\boldsymbol{l}$$

### 磁感应强度
方向：小磁针 N 极指向；大小：$B = f_{\max}/(qv)$
运动电荷受力（洛伦兹力）：$\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B}$

### 毕奥-萨伐尔定律
$$d\boldsymbol{B} = \frac{\mu_0}{4\pi}\frac{I d\boldsymbol{l}\times\boldsymbol{e}_r}{r^2},\quad \boldsymbol{B} = \int_L d\boldsymbol{B}$$

### 必考磁场公式
| 模型 | $B$ |
|:---|:---|
| 无限长直导线（距 $a$） | $\dfrac{\mu_0 I}{2\pi a}$ |
| 半无限长直导线端点对面 | $\dfrac{\mu_0 I}{4\pi a}$ |
| 圆形电流圆心 | $\dfrac{\mu_0 I}{2R}$ |
| 圆形电流轴线上（距心 $x$） | $\dfrac{\mu_0 I R^2}{2(R^2+x^2)^{3/2}}$ |
| 直导线延长线上 | $0$ |
| 无限长直螺线管内部 | $\mu_0 n I$（匀强） |
| 螺绕环内部 | $\dfrac{\mu_0 N I}{2\pi r}$ |
| 有限长直导线通式 | $\dfrac{\mu_0 I}{4\pi a}(\cos\theta_1 - \cos\theta_2)$ |

### 磁场的高斯定理
$$\oint_S \boldsymbol{B}\cdot d\boldsymbol{S} = 0 \quad \text{（磁场无源）}$$

### 安培环路定理
$$\oint_L \boldsymbol{B}\cdot d\boldsymbol{l} = \mu_0 \sum_{(L\text{内})} I_i$$

**同轴电缆 $B$ 分布**（内筒半径 $R_1$，外筒 $R_2$，电流 $I$）
| 区域 | $B$ |
|:---|:---|
| 内筒内 $r<R_1$ | $\dfrac{\mu_0 I r}{2\pi R_1^2}$ |
| 筒间 $R_1<r<R_2$ | $\dfrac{\mu_0 I}{2\pi r}$ |
| 外部 $r>R_2$ | $0$ |

### 带电粒子在磁场中运动
$$\boldsymbol{F} = q\boldsymbol{v}\times\boldsymbol{B} \quad \text{（永不做功）}$$
$\boldsymbol{v}\perp\boldsymbol{B}$：$R = \dfrac{mv}{qB},\; T = \dfrac{2\pi m}{qB}$（$T$ 与 $v$ 无关）
$\boldsymbol{v}$ 与 $\boldsymbol{B}$ 成 $\theta$：$R = \dfrac{mv\sin\theta}{qB},\;$ 螺距 $d = \dfrac{2\pi m v\cos\theta}{qB}$
速度选择器：$v = E/B$

### 安培力
$$d\boldsymbol{F} = I d\boldsymbol{l}\times\boldsymbol{B},\quad \boldsymbol{F} = \int_L I d\boldsymbol{l}\times\boldsymbol{B}$$
匀强磁场中弯曲导线受力 = 起点到终点直导线受力

### 磁力矩
磁矩：$\boldsymbol{m} = NIS\boldsymbol{e}_n$；力矩：$\boldsymbol{M} = \boldsymbol{m}\times\boldsymbol{B}$；大小：$M = mB\sin\theta$
磁力做功：$W = I\Delta\Phi_m$

### 霍尔效应
$$U_H = \frac{IB}{nqd} = R_H\frac{IB}{d},\quad R_H = \frac{1}{nq}$$

### 磁介质
$$\boldsymbol{H} = \frac{\boldsymbol{B}}{\mu} = \frac{\boldsymbol{B}}{\mu_r\mu_0},\quad \oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = \sum I_0$$
分类：顺磁质($\mu_r\!>\!1$)、抗磁质($\mu_r\!<\!1$)、铁磁质($\mu_r\!\gg\!1$)

---

## 第8章 电磁感应 电磁场

### 法拉第电磁感应定律
$$\varepsilon_i = -\frac{d\Phi_m}{dt},\quad \varepsilon_i = -N\frac{d\Phi_m}{dt}\;\text{（$N$ 匝）}$$
楞次定律：感应电流的磁场**阻碍**原磁通变化（**增反减同**）
感应电荷量：$q = \dfrac{|\Delta\Phi_m|}{R}$（与变化快慢无关！）

### 动生电动势
$$\varepsilon_{\text{动}} = \int_L (\boldsymbol{v}\times\boldsymbol{B})\cdot d\boldsymbol{l},\quad \varepsilon = Blv \;\text{（直导线⊥切割匀强场）}$$
方向：右手定则（磁感线穿手心，拇指→$\boldsymbol{v}$，四指→高电势）

### 感生电动势与感生电场
$$\varepsilon_{\text{感}} = \oint_L \boldsymbol{E}_k\cdot d\boldsymbol{l} = -\int_S \frac{\partial\boldsymbol{B}}{\partial t}\cdot d\boldsymbol{S}$$
感生电场是**非保守场**（涡旋电场，有旋无源）

轴对称变化磁场中：$r<R$：$E_k = \frac{r}{2}\frac{\partial B}{\partial t}$；$r>R$：$E_k = \frac{R^2}{2r}\frac{\partial B}{\partial t}$

### 自感与互感
自感：$\Psi_m = LI,\; \varepsilon_L = -L\dfrac{dI}{dt},\;$ 长直螺线管 $L = \mu_0 n^2 V$
互感：$\Psi_{m21} = MI_1,\; \varepsilon_{21} = -M\dfrac{dI_1}{dt}$

### RL电路暂态过程 *
时间常数：$\tau = L/R$
接通（电流增长）：$I(t) = \dfrac{\mathcal{E}}{R}\!\left(1 - e^{-t/\tau}\right)$
短接（电流衰减）：$I(t) = I_0\,e^{-t/\tau}$
通用三要素：$I(t) = I(\infty) + [I(0) - I(\infty)]e^{-t/\tau}$

### 磁场能量
线圈储能：$W_m = \frac{1}{2}LI^2$
能量密度：$w_m = \dfrac{B^2}{2\mu} = \dfrac{1}{2}\mu H^2 = \dfrac{1}{2}BH$
总能量：$W_m = \displaystyle\int_V \dfrac{B^2}{2\mu}\,dV$

### 位移电流与麦克斯韦方程组
位移电流密度：$\boldsymbol{j}_d = \dfrac{\partial\boldsymbol{D}}{\partial t}$；位移电流：$I_d = \dfrac{d\Phi_D}{dt}$
全电流安培环路定理：$\displaystyle\oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = I_c + \int_S \frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$

| 方程 | 积分形式 | 意义 |
|:---|:---|:---|
| 电场高斯 | $\oint_S \boldsymbol{D}\cdot d\boldsymbol{S} = \sum q$ | 电场有源 |
| 法拉第 | $\oint_L \boldsymbol{E}\cdot d\boldsymbol{l} = -\int_S \frac{\partial\boldsymbol{B}}{\partial t}\cdot d\boldsymbol{S}$ | 变磁场生电场 |
| 磁场高斯 | $\oint_S \boldsymbol{B}\cdot d\boldsymbol{S} = 0$ | 磁场无源 |
| 全电流安培 | $\oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = I_c + \int_S \frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$ | 电流+变电场生磁场 |

电磁波速：$c = \dfrac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3\times 10^8\ \text{m/s}$

---

## 附录：力学/电磁学公式类比速记

| 力学平动 | 力学转动 | 电磁学 |
|:---|:---|:---|
| $m$（质量） | $J$（转动惯量） | — |
| $\boldsymbol{F}$（力） | $M$（力矩） | $q,\;I$（源） |
| $\boldsymbol{a}$（加速度） | $\beta$（角加速度） | — |
| $\boldsymbol{v}$（速度） | $\omega$（角速度） | $I$（电流） |
| $\boldsymbol{p}=m\boldsymbol{v}$（动量） | $\boldsymbol{L}=J\boldsymbol{\omega}$（角动量） | — |
| $\boldsymbol{F}=m\boldsymbol{a}$ | $M=J\beta$ | — |
| $E_k=\frac{1}{2}mv^2$ | $E_k=\frac{1}{2}J\omega^2$ | $W_e=\frac{1}{2}CU^2,\;W_m=\frac{1}{2}LI^2$ |
| $\int\boldsymbol{F}dt=\Delta\boldsymbol{p}$ | $\int M dt=\Delta L$ | — |
| $W=\int\boldsymbol{F}\cdot d\boldsymbol{r}$ | $W=\int M d\theta$ | — |
| 动量守恒（$\sum\boldsymbol{F}_{\text{外}}=0$） | 角动量守恒（$\sum M_{\text{外}}=0$） | 电荷守恒 |
| 机械能守恒（仅保守力） | 机械能守恒（仅保守力） | 能量守恒 |
