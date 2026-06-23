# 《物理学（第七版）上册》期末复习资料

<!-- METADATA -->
| 属性 | 内容 |
|:---|:---|
| **书名** | 物理学 |
| **版本** | 第七版 上册（参考马文蔚系列教材） |
| **适用对象** | 高等学校理工科非物理类专业本科生 |
| **文档用途** | 期末复习资料，提炼核心概念、公式、定理及解题套路，严格遵循考试范围 |
| **内容来源** | 共享知识库中的 PPT、PDF、教案等教学资料 |

---

<!-- CHAPTER: 8 -->
# 第八章 电磁感应 电磁场

## 8-1 电磁感应定律

### 一、电磁感应现象

**核心概念/定义**
- **电磁感应**：当穿过闭合回路的磁通量发生变化时，回路中产生感应电流的现象。
- 产生感应电流的三种典型方式：
  1. 磁体与闭合回路做相对运动。
  2. 回路所处磁场由变化的电流激发（如互感实验）。
  3. 闭合回路的一部分导体在磁场中做切割磁感线运动。

---

### 二、电磁感应定律

**核心概念/定义**
- 无论磁通量变化是什么原因引起的，回路中产生的感应电动势 $\varepsilon_i$ 的大小与穿过回路的磁通量对时间的变化率成正比。

**定理/定律/公式**
- 单匝线圈：
  $$\varepsilon_i = -\frac{d\Phi_m}{dt}$$
- $N$ 匝密绕线圈（磁通链 $\Psi_m = N\Phi_m$）：
  $$\varepsilon_i = -N\frac{d\Phi_m}{dt} = -\frac{d\Psi_m}{dt}$$

**⚠️ 注意**
- 公式中的负号体现了**楞次定律**，表示感应电动势总是反抗磁通量的变化。
- 实际计算大小时常取绝对值 $|\varepsilon_i| = N \left| \frac{d\Phi_m}{dt} \right|$，方向单独用楞次定律判断。

### 三、楞次定律

**核心概念/定义**
- 闭合回路中感应电流的方向，总是使得它所激发的磁场来**阻碍**引起感应电流的磁通量的变化（口诀：**增反减同**）。

**🔑 典型解题套路（判定感应电流方向）**
- **Step 1 定原场**：确定穿过回路的原磁场 $\boldsymbol{B}$ 的方向。
- **Step 2 判增减**：判断穿过回路的磁通量 $\Phi_m$ 是增加还是减少。
- **Step 3 定感应场**：若 $\Phi_m$ 增加，感应磁场 $\boldsymbol{B}'$ 与 $\boldsymbol{B}$ **反向**；若 $\Phi_m$ 减少，$\boldsymbol{B}'$ 与 $\boldsymbol{B}$ **同向**。
- **Step 4 右手螺旋**：右手拇指指向 $\boldsymbol{B}'$ 方向，弯曲四指即为感应电流方向。

### 四、感应电流与感应电荷

**定理/定律/公式**
- 感应电流：
  $$I_i = \frac{\varepsilon_i}{R} = -\frac{1}{R} \frac{d\Phi_m}{dt}$$
- 时间 $\Delta t = t_2 - t_1$ 内通过回路的感应电荷量：
  $$q = \int_{t_1}^{t_2} I_i\,dt = -\frac{1}{R} \int_{\Phi_{m1}}^{\Phi_{m2}} d\Phi_m = \frac{1}{R}(\Phi_{m1} - \Phi_{m2}) = \frac{|\Delta\Phi_m|}{R}$$

**物理意义与解题套路**
- **核心结论**：感应电荷量 $q$ 仅与磁通量的**变化量** $\Delta\Phi_m$ 有关，与磁通量变化的快慢（即时间 $\Delta t$）无关。
- **典型应用**：在已知回路电阻 $R$ 和测量到的电荷量 $q$ 时，可反推磁通量的变化量或磁场强度 $B$。

---

## 8-2 动生电动势和感生电动势

### 一、动生电动势

**核心概念/定义**
- 导体在恒定磁场中运动时，导体内的自由电荷受洛伦兹力作用而产生定向移动，从而在导体两端产生的电动势。
- 非静电性场强：$\boldsymbol{E}_k = \boldsymbol{v} \times \boldsymbol{B}$

**定理/定律/公式**
- 动生电动势的一般表达式：
  $$\varepsilon_{\text{动}} = \int_L (\boldsymbol{v} \times \boldsymbol{B}) \cdot d\boldsymbol{l}$$
- 直导线垂直切割匀强磁场：
  $$\varepsilon = Blv$$

**🔑 直导线平动切割秒杀技巧（右手定则）**
- 伸开右手，让磁感线垂直穿入手心，拇指指向导体运动方向 $\boldsymbol{v}$，四指所指方向即为动生电动势方向（即高电势端）。

**🔑 典型解题套路（非均匀磁场中的动生电动势）**
- **Step 1**：在导体上取长度元 $d\boldsymbol{l}$，判断该处 $\boldsymbol{B}$ 的大小和方向。
- **Step 2**：写出微元电动势 $d\varepsilon = (\boldsymbol{v} \times \boldsymbol{B}) \cdot d\boldsymbol{l} = Bv\cos\theta\,dl$。
- **Step 3**：沿导体长度积分 $\varepsilon = \int d\varepsilon$，注意正负号（积分结果正负代表与 $d\boldsymbol{l}$ 方向相同或相反）。

---

### 二、感生电动势

**核心概念/定义**
- **感生电场（涡旋电场）$\boldsymbol{E}_k$**：由变化的磁场激发的电场。即使空间中没有导体，感生电场依然存在。
- **感生电动势**：感生电场对静止导体回路中电荷做功产生的电动势。

**定理/定律/公式**
- 感生电动势与感生电场的关系：
  $$\varepsilon_{\text{感}} = \oint_L \boldsymbol{E}_k \cdot d\boldsymbol{l} = -\int_S \frac{\partial\boldsymbol{B}}{\partial t} \cdot d\boldsymbol{S}$$
  （$S$ 为以闭合回路 $L$ 为边界的任意曲面）

#### 感生电场与静电场的对比

| 性质 | 静电场 $\boldsymbol{E}$ | 感生电场 $\boldsymbol{E}_k$ |
|:---|:---|:---|
| **激发源** | 静止电荷 | 变化的磁场 $\frac{\partial\boldsymbol{B}}{\partial t}$ |
| **场线特征** | 有头有尾（起止于电荷） | 无头无尾的闭合曲线（涡旋状） |
| **有源性** | 有源场（$\oint_S \boldsymbol{E}\cdot d\boldsymbol{S} = \frac{q}{\varepsilon_0}$） | 无源场（$\oint_S \boldsymbol{E}_k\cdot d\boldsymbol{S} = 0$） |
| **保守性** | 保守场（$\oint \boldsymbol{E}\cdot d\boldsymbol{l} = 0$） | 非保守场（$\oint \boldsymbol{E}_k\cdot d\boldsymbol{l} = \varepsilon_{\text{感}} \neq 0$） |

**🔑 典型解题套路（轴对称变化磁场求感生电场）**
- **Step 1**：分析磁场变化 $\frac{\partial B}{\partial t}$ 的对称性。若磁场局限在半径 $R$ 内且均匀变化，感生电场线为同心圆。
- **Step 2**：选取圆形环路（半径 $r$）。计算环流 $\oint \boldsymbol{E}_k \cdot d\boldsymbol{l} = E_k \cdot 2\pi r$。
- **Step 3**：计算磁通变化率 $\left|\frac{d\Phi_m}{dt}\right| = \int \frac{\partial B}{\partial t} dS$。
  - 若 $r < R$（管内）：$E_k \cdot 2\pi r = \frac{\partial B}{\partial t} \cdot \pi r^2 \Rightarrow E_k = \frac{r}{2} \frac{\partial B}{\partial t}$
  - 若 $r > R$（管外）：$E_k \cdot 2\pi r = \frac{\partial B}{\partial t} \cdot \pi R^2 \Rightarrow E_k = \frac{R^2}{2r} \frac{\partial B}{\partial t}$
- **Step 4 方向判定（楞次定律）**：若 $\frac{\partial B}{\partial t} > 0$（原磁场增强），$\boldsymbol{E}_k$ 激发的感应磁场与原磁场 $\boldsymbol{B}$ **反向**；若 $\frac{\partial B}{\partial t} < 0$（原磁场减弱），则**同向**。最后用**右手螺旋定则**判定 $\boldsymbol{E}_k$ 的环绕方向。

---

## 8-3 自感和互感

### 一、自感电动势 自感

**核心概念/定义**
- **自感现象**：线圈自身电流变化引起自身磁通量变化，从而产生自感电动势的现象。
- **自感系数 $L$**：描述线圈自身电磁惯性大小的物理量，仅与线圈形状、尺寸、匝数及介质有关。

**定理/定律/公式**
- 磁通链与电流关系：
  $$\Psi_m = LI \Rightarrow L = \frac{\Psi_m}{I}$$
- 自感电动势：
  $$\varepsilon_L = -\frac{d\Psi_m}{dt} = -L\frac{dI}{dt}$$
  （负号表示自感电动势阻碍电流的变化：电流增加时反向，电流减小时同向）
- **长直螺线管自感**（$n$ 为单位长度匝数，$V$ 为体积）：
  $$L = \mu_0 n^2 V = \mu_0 \frac{N^2}{l} S$$

**🔑 典型解题套路（计算自感 $L$）**
- **Step 1**：假设线圈通有电流 $I$。
- **Step 2**：求电流 $I$ 产生的磁感应强度 $\boldsymbol{B}$ 分布。
- **Step 3**：求穿过单匝线圈的磁通 $\Phi_m = \int \boldsymbol{B} \cdot d\boldsymbol{S}$。
- **Step 4**：求磁通链 $\Psi_m = N\Phi_m$。
- **Step 5**：代入定义式 $L = \frac{\Psi_m}{I}$（结果中 $I$ 必被消去）。

---

### 二、互感电动势 互感

**核心概念/定义**
- **互感现象**：一个回路中的电流变化在邻近回路中激发感应电动势的现象。
- **互感系数 $M$**：表征两回路磁耦合强弱的物理量，$M_{12} = M_{21} = M$。

**定理/定律/公式**
- 磁通与电流关系：$\Phi_{m21} = MI_1$
- 互感电动势：
  $$\varepsilon_{21} = -M\frac{dI_1}{dt}$$
- 单位：亨利（H），$1\ \text{H} = 1\ \text{Wb/A}$。

**🔑 典型解题套路（计算互感 $M$）**
- **Step 1**：假设线圈 1 通有电流 $I_1$。
- **Step 2**：求 $I_1$ 产生的磁场 $\boldsymbol{B}_1$ 分布。
- **Step 3**：求 $\boldsymbol{B}_1$ 穿过线圈 2 的单匝磁通 $\Phi_{21}$。
- **Step 4**：求磁通链 $\Psi_{21} = N_2\Phi_{21}$。
- **Step 5**：代入定义式 $M = \frac{\Psi_{21}}{I_1}$。

---

## 8-5 磁场的能量 磁场能量密度

### 一、自感线圈储存的能量

**定理/定律/公式**
- 建立电流 $I$ 过程中，电源克服自感电动势所做的功转化为磁场能量：
  $$W_m = \int_0^I \mathcal{E} i\,dt = \int_0^I L i\,di = \frac{1}{2}LI^2$$

---

### 二、磁场的能量 磁场能量密度

**核心概念/定义**
- 磁场能量储存在磁场占据的空间中，与磁感应强度的平方成正比。

**定理/定律/公式**
- 磁场能量密度（单位体积内的磁场能量）：
  $$w_m = \frac{B^2}{2\mu} = \frac{1}{2}\mu H^2 = \frac{1}{2}BH$$
- 有限空间内的总磁场能量：
  $$W_m = \int_V w_m\,dV = \int_V \frac{1}{2}BH\,dV$$
  （适用于非均匀磁场，需对全场空间积分）

**🔑 磁场能量计算套路**
- **已知 $L$ 和 $I$**：直接用 $W_m = \frac{1}{2}LI^2$。
- **已知场分布 $B(r)$**：
  1. 写出能量密度 $w_m = \frac{B^2}{2\mu}$。
  2. 选取体积元 $dV$（如球壳 $4\pi r^2 dr$，圆柱壳 $2\pi rl\,dr$）。
  3. 积分 $W_m = \int w_m dV$，积分范围覆盖所有存在磁场的空间。

---

## 8-6 位移电流 电磁场基本方程的积分形式

### 一、位移电流 全电流安培环路定理

**核心概念/定义**
- 安培环路定理在非稳恒电流（如电容器充放电）中出现矛盾。麦克斯韦提出：**变化的电场等效于一种电流**，称为位移电流。
- 位移电流密度 $\boldsymbol{j}_d$ 和位移电流 $I_d$：
  $$\boldsymbol{j}_d = \frac{\partial\boldsymbol{D}}{\partial t}, \quad I_d = \frac{d\Phi_D}{dt} = \int_S \frac{\partial\boldsymbol{D}}{\partial t} \cdot d\boldsymbol{S}$$
  （$\boldsymbol{D}$ 为电位移矢量，$\Phi_D$ 为电位移通量）

**定理/定律/公式**
- **全电流安培环路定理**：传导电流与位移电流共同激发磁场。
  $$\oint_L \boldsymbol{H} \cdot d\boldsymbol{l} = I_c + I_d = I_c + \int_S \frac{\partial\boldsymbol{D}}{\partial t} \cdot d\boldsymbol{S}$$
  （$I_c$ 为穿过环路所围曲面的传导电流）

**⚠️ 注意**
- 位移电流与传导电流在激发磁场方面等效，但位移电流**不产生焦耳热**。

---

### 二、电磁场 麦克斯韦电磁场方程的积分形式

**核心概念/定义**
- 麦克斯韦将静电场、恒定磁场规律推广至时变电磁场，总结出四个基本方程，统一描述电磁场行为。

#### 麦克斯韦方程组（积分形式）

| 方程 | 积分形式 | 物理意义 |
|:---|:---|:---|
| **电场高斯定理** | $\displaystyle\oint_S \boldsymbol{D}\cdot d\boldsymbol{S} = \sum q_i$ | 电荷是电场的源（电场有源） |
| **法拉第电磁感应定律** | $\displaystyle\oint_L \boldsymbol{E}\cdot d\boldsymbol{l} = -\int_S \frac{\partial\boldsymbol{B}}{\partial t}\cdot d\boldsymbol{S}$ | 变化的磁场产生涡旋电场（电场有旋） |
| **磁场高斯定理** | $\displaystyle\oint_S \boldsymbol{B}\cdot d\boldsymbol{S} = 0$ | 磁感线闭合，无磁单极（磁场无源） |
| **全电流安培环路定理** | $\displaystyle\oint_L \boldsymbol{H}\cdot d\boldsymbol{l} = I_c + \int_S \frac{\partial\boldsymbol{D}}{\partial t}\cdot d\boldsymbol{S}$ | 传导电流和变化的电场产生磁场（磁场有旋） |

**⚠️ 核心结论**
- 变化的电场和磁场相互激发，形成统一的**电磁场**，并以波的形式在空间传播（电磁波）。
- 电磁波在真空中的传播速度：
  $$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3 \times 10^8\ \text{m/s}$$

---

### 🔹 综合解题套路汇总（应试核武器）

#### 套路 1：法拉第电磁感应定律应用
- **Step 1**：选定回路正方向与法线方向（右手螺旋关系）。
- **Step 2**：计算磁通量 $\Phi_m = \int \boldsymbol{B}\cdot d\boldsymbol{S}$，注意 $\boldsymbol{B}$ 可能随空间或时间变化。
- **Step 3**：求导得电动势大小 $\varepsilon_i = \left|\frac{d\Phi_m}{dt}\right|$。
- **Step 4**：用楞次定律或公式负号判定方向。

#### 套路 2：动生与感生电动势的区分与计算
- **动生**：导体动、磁场稳。核心是 $\boldsymbol{v} \times \boldsymbol{B}$，积分路径沿**导体**。
- **感生**：导体静、磁场变。核心是 $\frac{\partial\boldsymbol{B}}{\partial t}$，积分路径为**闭合回路**，利用对称性选环路。
- **混合情况**：若两者同时存在，总电动势 $\varepsilon = \varepsilon_{\text{动}} + \varepsilon_{\text{感}}$，矢量叠加。

#### 套路 3：自感系数 $L$ 计算
- **Step 1**：设电流 $I$ → **Step 2**：求 $\boldsymbol{B}$ → **Step 3**：求 $\Phi_m$ → **Step 4**：求 $\Psi_m = N\Phi_m$ → **Step 5**：$L = \Psi_m/I$。

#### 套路 4：磁场能量计算
- **线圈模型**：$W_m = \frac{1}{2}LI^2$。
- **场分布模型**：$W_m = \int_V \frac{B^2}{2\mu} dV$，选合适的体积元积分。

---