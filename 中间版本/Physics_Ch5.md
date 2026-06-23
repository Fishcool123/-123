<!-- CHAPTER: 5 -->
# 第五章 静电场

## 5-1 电荷的量子化 电荷守恒定律 库仑定律

### 一、电荷的量子化

**核心概念/定义**
- **元电荷**：自然界中电荷的最小不可分割单元，即一个电子所带电量的绝对值。
- **电荷量子化**：宏观带电体所带电量只能取离散的、不连续的量值，且均为元电荷的整数倍。

**定理/定律/公式**
- 元电荷电量：
  $$e = 1.602 \times 10^{-19}\ \text{C}$$
- 任意带电体电量：
  $$q = ne \quad (n = \pm 1, \pm 2, \cdots)$$

---

### 二、电荷守恒定律

**核心概念/定义**
- 任何使物体带电的过程（摩擦、感应等）都只是正负电荷的分离或转移，并非电荷的创生或消灭。

**定理/定律/公式**
- 孤立系统中，正、负电荷的代数和在任何物理过程中始终保持不变。

---

### 三、库仑定律

**核心概念/定义**
- **库仑定律**：真空中两个静止点电荷之间的相互作用力，大小与电量乘积成正比，与距离平方成反比；方向沿两电荷连线。

**定理/定律/公式**
- 矢量表达式：
  $$\boldsymbol{F}_{21} = -\boldsymbol{F}_{12} = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2}\boldsymbol{e}_r$$
  （$\boldsymbol{e}_r$ 为由 $q_1$ 指向 $q_2$ 的单位矢量。同号电荷为斥力，异号为引力）
- **真空介电常量**：
  $$\varepsilon_0 \approx 8.85 \times 10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$$
  $$k = \frac{1}{4\pi\varepsilon_0} \approx 9.0 \times 10^9\ \text{N}\cdot\text{m}^2/\text{C}^2$$

**适用条件**
- 仅适用于**真空**、**静止**的**点电荷**。

---

## 5-2 电场强度

### 一、静电场

**核心概念/定义**
- 电荷在其周围空间激发**电场**。电场对放入其中的其他电荷产生力的作用。
- 电荷间相互作用通过电场传递：电荷 → 激发电场 → 作用于电荷。

### 二、电场强度

**核心概念/定义**
- **检验电荷 $q_0$**：电量足够小（不扰动原场）、线度足够小（可视为点电荷）的**正电荷**。
- **电场强度 $\boldsymbol{E}$**：描述电场力的性质的物理量。定义为检验电荷所受电场力与其电量的比值。

**定理/定律/公式**
- 定义式：
  $$\boldsymbol{E} = \frac{\boldsymbol{F}}{q_0}$$
- 单位：$\text{N/C}$ 或 $\text{V/m}$。
- 已知场强求点电荷受力：
  $$\boldsymbol{F} = q\boldsymbol{E}$$

### 三、点电荷的电场强度

**定理/定律/公式**
- 真空中点电荷 $Q$ 在距离 $r$ 处产生的场强：
  $$\boldsymbol{E} = \frac{1}{4\pi\varepsilon_0} \frac{Q}{r^2}\boldsymbol{e}_r$$
- $Q>0$ 时 $\boldsymbol{E}$ 沿矢径向外；$Q<0$ 时指向电荷。具有球对称性。

### 四、电场强度叠加原理

**核心概念/定义**
- 多个点电荷在某点产生的合场强，等于各电荷单独存在时在该点产生场强的**矢量和**。

**定理/定律/公式**
- 离散电荷系：
  $$\boldsymbol{E} = \sum_{i=1}^n \boldsymbol{E}_i$$
- **连续带电体**（积分法）：
  $$\boldsymbol{E} = \int d\boldsymbol{E} = \int \frac{1}{4\pi\varepsilon_0} \frac{dq}{r^2}\boldsymbol{e}_r$$
- 电荷密度：体密度 $\rho = \frac{dq}{dV}$，面密度 $\sigma = \frac{dq}{dS}$，线密度 $\lambda = \frac{dq}{dl}$。

### 五、电偶极子的电场强度

**核心概念/定义**
- **电偶极子**：距离很近的一对等量异号电荷 $+q$ 和 $-q$（间距 $l \ll$ 场点距离）。
- **电偶极矩**：$\boldsymbol{p} = q\boldsymbol{l}$，方向由 $-q$ 指向 $+q$。

**定理/定律/公式**
- 中垂线上距中心 $y$ 处（$y \gg l$）：
  $$\boldsymbol{E} = -\frac{1}{4\pi\varepsilon_0} \frac{\boldsymbol{p}}{y^3}$$
  （方向与 $\boldsymbol{p}$ 相反，大小与距离三次方成反比）
- **延长线上距中心 $x$ 处（$x \gg l$）**：
  $$E = \frac{1}{4\pi\varepsilon_0} \frac{2p}{x^3}$$
  （方向与 $\boldsymbol{p}$ 同向）

**典型解题套路（连续带电体场强计算）**
- **Step 1**：取电荷元 $dq$，写出 $d\boldsymbol{E}$ 的大小与方向。
- **Step 2**：建坐标系，利用对称性判定哪些分量积分后抵消为零。
- **Step 3**：统一积分变量（如用角度 $\theta$ 或坐标 $x$ 表示 $r$ 和 $dq$），对非零分量积分。
- **Step 4**：矢量合成求总场强。

### 六、电偶极子在外电场中的行为

**定理/定律/公式**
- **合力矩**（置于均匀外电场 $\boldsymbol{E}$ 中）：
  $$\boldsymbol{M} = \boldsymbol{p} \times \boldsymbol{E}$$
  大小：$M = pE\sin\theta$（$\theta$ 为 $\boldsymbol{p}$ 与 $\boldsymbol{E}$ 夹角）
- **电势能**：
  $$W_e = -\boldsymbol{p} \cdot \boldsymbol{E} = -pE\cos\theta$$

**物理意义**
- **力矩**：使电偶极矩 $\boldsymbol{p}$ 转向外场 $\boldsymbol{E}$ 方向。当 $\boldsymbol{p} \parallel \boldsymbol{E}$ 时力矩为零，为**稳定平衡态**。
- **电势能**：取向与场一致（$\theta=0$）时势能最低（$-pE$），反向（$\theta=\pi$）时势能最高（$+pE$）。外电场做功等于电势能减少量。

---

## 5-3 电场强度通量

### 一、电场线

**核心概念/定义**
- 假想曲线，切线方向表示 $\boldsymbol{E}$ 方向，线密度表示 $\boldsymbol{E}$ 大小。

**基本性质**
1. **有源性**：始于正电荷（或无穷远），止于负电荷（或无穷远）。
2. **无旋性**：永不闭合。
3. **不相交**：同一电场中任意两条电场线不相交。

### 二、电场强度通量

**核心概念/定义**
- 穿过某一曲面的电场线总数，反映电场"穿透"该面的净流量。

**定理/定律/公式**
- 均匀场，平面 $S$（法线与 $\boldsymbol{E}$ 夹角 $\theta$）：
  $$\Phi_e = \boldsymbol{E}\cdot\boldsymbol{S} = ES\cos\theta$$
- 非均匀场，任意曲面：
  $$\Phi_e = \int_S \boldsymbol{E}\cdot d\boldsymbol{S}$$
- **闭合曲面**（规定法线正方向由内向外）：
  $$\Phi_e = \oint_S \boldsymbol{E}\cdot d\boldsymbol{S}$$
  （外部电荷对闭合曲面总通量贡献为零）

---

## 5-4 高斯定理

### 一、高斯定理

**定理/定律/公式**
- 真空中静电场，通过任意闭合曲面（高斯面）的电通量等于面内包围电荷代数和除以 $\varepsilon_0$：
  $$\oint_S \boldsymbol{E}\cdot d\boldsymbol{S} = \frac{1}{\varepsilon_0} \sum_{(S\text{内})} q_i$$

**理解要点**
1. 等式左边 $\boldsymbol{E}$ 是**空间所有电荷**（含面外）产生的合场强。
2. 等式右边只与**面内净电荷**有关。
3. $\sum q_i > 0 \Rightarrow$ 净穿出；$\sum q_i < 0 \Rightarrow$ 净穿入。

### 二、高斯定理应用举例

**适用条件**
- 电荷分布具有高度对称性（球对称、柱对称、平面对称），使高斯面上 $\boldsymbol{E}$ 大小恒定且方向与法线平行/垂直。

**典型解题套路**
- **Step 1**：分析对称性，判断 $\boldsymbol{E}$ 方向。
- **Step 2**：选取高斯面，使面上部分区域 $\boldsymbol{E}\parallel d\boldsymbol{S}$ 且 $E$ 为常量，其余区域 $\boldsymbol{E}\perp d\boldsymbol{S}$。
- **Step 3**：计算 $\Phi_e = \oint \boldsymbol{E}\cdot d\boldsymbol{S}$ 与 $\sum q_{\text{内}}$。
- **Step 4**：代入定理求解 $E$。

### 三、常见静电场模型结论汇总

| 带电体模型 | 电场强度 $\boldsymbol{E}$ 分布 | 电势 $U$ 分布 (通常取无穷远为零) | 对称性与高斯面选择 |
|:---|:---|:---|:---|
| **无限长均匀带电直线**<br>(线密度 $\lambda$) | $E = \frac{\lambda}{2\pi\varepsilon_0 r}$<br>(径向，与 $r$ 成反比) | $U = U_0 - \frac{\lambda}{2\pi\varepsilon_0}\ln\frac{r}{r_0}$<br>(无穷远处发散，需选有限处 $r_0$ 为零势) | 柱对称<br>同轴圆柱面 |
| **无限大均匀带电平面**<br>(面密度 $\sigma$) | $E = \frac{\sigma}{2\varepsilon_0}$<br>(两侧均为匀强场，方向垂直板面) | $U = U_0 - \frac{\sigma}{2\varepsilon_0}x$<br>(随距离 $x$ 线性变化) | 平面对称<br>底面平行于带电平面的闭合圆柱面 |
| **均匀带电圆环轴线**<br>(半径 $R$, 总电量 $q$, 轴上距心 $x$) | $E = \frac{qx}{4\pi\varepsilon_0 (R^2+x^2)^{3/2}}$<br>(沿轴线，$x=0$ 处 $E=0$) | $U = \frac{q}{4\pi\varepsilon_0 \sqrt{R^2+x^2}}$ | 轴对称<br>(高斯法不适用，直接用叠加法/电势梯度) |
| **均匀带电球壳**<br>(半径 $R$, 总电量 $Q$) | 壳内 $E=0$；壳外 $E = \frac{Q}{4\pi\varepsilon_0 r^2}$ | 壳内等势 $U=\frac{Q}{4\pi\varepsilon_0 R}$；壳外 $U=\frac{Q}{4\pi\varepsilon_0 r}$ | 球对称<br>同心球面 |
| **均匀带电实心球体**<br>(半径 $R$, 总电量 $Q$) | 球内 $E = \frac{Qr}{4\pi\varepsilon_0 R^3}$ ($r<R$)<br>球外 $E = \frac{Q}{4\pi\varepsilon_0 r^2}$ ($r>R$) | 球内 $U = \frac{Q(3R^2-r^2)}{8\pi\varepsilon_0 R^3}$ ($r<R$)<br>球外 $U = \frac{Q}{4\pi\varepsilon_0 r}$ ($r>R$) | 球对称<br>同心球面 |

---

## 5-5 静电场的环路定理 电势能

### 一、静电场力所做的功

**核心概念/定义**
- 静电场力做功与路径无关，仅取决于始末位置。

**定理/定律/公式**
  $$W_{AB} = q_0 \int_A^B \boldsymbol{E}\cdot d\boldsymbol{l}$$

### 二、静电场的环路定理

**定理/定律/公式**
- 场强沿任意闭合路径的线积分（环流）恒为零：
  $$\oint_L \boldsymbol{E}\cdot d\boldsymbol{l} = 0$$

**物理意义**：静电场是**保守场**（无旋场）。

### 三、电势能

**核心概念/定义**
- 电荷在电场中某点具有的能量，属于电荷与电场系统共有。

**定理/定律/公式**
- 电势能变化与电场力做功：
  $$W_{AB} = W_{eA} - W_{eB} = -(W_{eB} - W_{eA})$$
- 某点电势能：等于将电荷从该点移至零势能点电场力所做的功：
  $$W_{eA} = q_0 \int_A^{\text{零势点}} \boldsymbol{E}\cdot d\boldsymbol{l}$$

---

## 5-6 电势

### 一、电势

**核心概念/定义**
- **电势 $U$**：描述电场能的性质的物理量。等于单位正电荷在该点的电势能。

**定理/定律/公式**
- 定义式（通常取无穷远为零势点）：
  $$U_P = \frac{W_{eP}}{q_0} = \int_P^{\infty} \boldsymbol{E}\cdot d\boldsymbol{l}$$
- **电势差（电压）**：
  $$U_{AB} = U_A - U_B = \int_A^B \boldsymbol{E}\cdot d\boldsymbol{l}$$
- 移动电荷 $q$ 电场力做功：
  $$W_{AB} = qU_{AB} = q(U_A - U_B)$$

**⚠️ 注意**：电荷分布在无限区域（如无限长带电直线）时，$\int^\infty \boldsymbol{E}\cdot d\boldsymbol{l}$ 发散，**不可取无穷远为零势点**，需选有限远处。

### 二、点电荷电场的电势

  $$U = \frac{q}{4\pi\varepsilon_0 r} \quad (\text{取无穷远为零势点})$$

### 三、电势的叠加原理

**核心概念/定义**
- 空间某点电势等于各电荷单独存在时在该点电势的**代数和**（标量叠加，比场强计算简便）。

**定理/定律/公式**
- 离散系：
  $$U_P = \sum_{i=1}^n \frac{q_i}{4\pi\varepsilon_0 r_i}$$
- **连续带电体**：
  $$U = \int dU = \int \frac{1}{4\pi\varepsilon_0} \frac{dq}{r}$$

**典型解题套路**
- **Step 1**：取 $dq$，写 $dU = \frac{dq}{4\pi\varepsilon_0 r}$。
- **Step 2**：确定积分限（带电体几何范围）。
- **Step 3**：直接标量积分求和。

---

## 5-7 电场强度与电势梯度

### 一、等势面

**核心概念/定义**
- 电势相等的点构成的曲面。

**性质**
1. 等势面与电场线**处处正交**。
2. 等势面越密集，场强越大。
3. 沿等势面移动电荷，电场力**不做功**。
4. 任意两等势面**不相交**。

### 二、电场强度与电势梯度

**核心概念/定义**
- 场强方向指向电势降低最快的方向，大小等于电势在该方向的空间变化率。

**定理/定律/公式**
- 沿任意方向 $l$ 的分量：
  $$E_l = -\frac{\partial U}{\partial l}$$
- 矢量形式（电势梯度的负值）：
  $$\boldsymbol{E} = -\nabla U = -\left( \frac{\partial U}{\partial x}\boldsymbol{i} + \frac{\partial U}{\partial y}\boldsymbol{j} + \frac{\partial U}{\partial z}\boldsymbol{k} \right)$$
- 一维/球对称简化：
  $$E = -\frac{dU}{dr}$$

**计算电势的两种常用方法总结**
1. **定义法**：已知 $\boldsymbol{E}(r)$ 分布 $\xrightarrow{\text{积分}}$ $U_P = \int_P^{\text{零势}} \boldsymbol{E}\cdot d\boldsymbol{l}$
2. **叠加法**：已知电荷分布 $\xrightarrow{\text{标量积分}}$ $U = \int \frac{dq}{4\pi\varepsilon_0 r}$

### 三、综合解题套路：带电粒子在静电场中的运动

**核心物理思想**
- 将电场力 $\boldsymbol{F} = q\boldsymbol{E}$ 代入质点动力学框架（牛顿第二定律或动能定理）。
- 通常忽略重力（除非题目明确说明或为带电微粒/液滴）。

#### 情形 1：直线加速/减速
- **适用场景**：初速度方向与电场线平行（或初速为零）。
- **解题套路**：
  - **Step 1**：判受力方向。$q>0$ 时 $\boldsymbol{F}\parallel\boldsymbol{E}$；$q<0$ 时 $\boldsymbol{F}\uparrow\downarrow\boldsymbol{E}$。
  - **Step 2**：首选**动能定理**（避免求时间）：
    $$qU_{AB} = \frac{1}{2}mv_B^2 - \frac{1}{2}mv_A^2$$
  - **Step 3**：若需求时间或位移过程，改用牛顿第二定律 $a = \frac{qE}{m}$ + 匀变速直线运动公式。

#### 情形 2：垂直偏转（类平抛运动）
- **适用场景**：带电粒子以初速 $v_0$ 垂直射入匀强电场（如平行板电容器）。
- **解题套路**：
  - **Step 1**：建立坐标系。$x$ 轴沿 $v_0$ 方向（匀速），$y$ 轴沿电场方向（匀加速）。
  - **Step 2**：分解运动学方程：
    $$x = v_0 t, \quad y = \frac{1}{2}at^2 = \frac{qE}{2m}t^2$$
  - **Step 3**：消去时间 $t$，得轨迹方程：
    $$y = \frac{qE}{2mv_0^2}x^2$$
  - **Step 4**：求偏转角 $\theta$：
    $$\tan\theta = \frac{v_y}{v_x} = \frac{at}{v_0} = \frac{qEl}{mv_0^2} = \frac{qUl}{mdv_0^2}$$
    （$l$ 为极板长度，$d$ 为极板间距，$U=Ed$）
  - **重要推论**：
    1. 速度偏转角 $\theta$ 与位移偏转角 $\alpha$ 满足：$\tan\theta = 2\tan\alpha$。
    2. 粒子射出电场后，速度反向延长线必交于水平位移的中点（$x = l/2$ 处）。

---