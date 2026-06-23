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

<!-- CHAPTER: 1 -->
# 第一章 质点运动学

## 1-1 质点运动的描述

### 一、参考系 质点

**核心概念/定义**
- **质点**：当物体的大小和形状在所研究问题中可忽略不计时，把物体抽象为一个有质量的几何点。它是最简单、最理想的力学模型。
- **参考系**：描述物体运动时选作参考的物体。不特别指明时，默认以地球（地面）为参考系。
- **坐标系**：在参考系上建立的定量描述工具。常用类型：直角坐标系、极坐标系、**自然坐标系**、球坐标系、柱坐标系。

**适用条件/物理模型**
- 质点模型适用于物体线度远小于运动尺度，或只关心整体平动的问题。

---

### 二、位置矢量 运动方程 位移

**核心概念/定义**
- **位置矢量（位矢）$\boldsymbol{r}$**：由坐标原点指向质点所在位置的矢量。
- **运动方程**：位矢随时间变化的函数关系 $\boldsymbol{r} = \boldsymbol{r}(t)$。
- **轨迹方程**：从运动方程中消去时间 $t$，得到坐标之间的关系式，即质点运动的路径。
- **位移 $\Delta\boldsymbol{r}$**：从初位置指向末位置的有向线段，是矢量。

**定理/定律/公式**
- 直角坐标系下的位矢：
  $$\boldsymbol{r} = x\boldsymbol{i} + y\boldsymbol{j} + z\boldsymbol{k}$$
- 位矢大小：
  $$|\boldsymbol{r}| = r = \sqrt{x^2 + y^2 + z^2}$$
- 方向余弦：
  $$\cos\alpha = \frac{x}{r}, \quad \cos\beta = \frac{y}{r}, \quad \cos\gamma = \frac{z}{r}$$
- 运动方程分量式：
  $$\begin{cases} x = x(t) \\ y = y(t) \\ z = z(t) \end{cases}$$
- 位移公式：
  $$\Delta\boldsymbol{r} = \boldsymbol{r}_B - \boldsymbol{r}_A = \Delta x\,\boldsymbol{i} + \Delta y\,\boldsymbol{j} + \Delta z\,\boldsymbol{k}$$
- 位移大小：
  $$|\Delta\boldsymbol{r}| = \sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2} \neq |\boldsymbol{r}_B| - |\boldsymbol{r}_A|$$

**典型解题套路**
- **已知运动方程求位移**：代入 $t_1, t_2$ 分别求出 $\boldsymbol{r}_A, \boldsymbol{r}_B$，再计算 $\Delta\boldsymbol{r} = \boldsymbol{r}_B - \boldsymbol{r}_A$。

---

### 三、速度

**核心概念/定义**
- **平均速度 $\bar{\boldsymbol{v}}$**：位移与所用时间的比值，矢量。
- **瞬时速度 $\boldsymbol{v}$**：平均速度在 $\Delta t \to 0$ 时的极限，精确描述质点在某时刻的运动快慢和方向。
- **速率**：瞬时速度的大小，是标量。

**定理/定律/公式**
- 平均速度：
  $$\bar{\boldsymbol{v}} = \frac{\Delta\boldsymbol{r}}{\Delta t}$$
- 瞬时速度：
  $$\boldsymbol{v} = \lim_{\Delta t \to 0} \frac{\Delta\boldsymbol{r}}{\Delta t} = \frac{d\boldsymbol{r}}{dt}$$
- 直角坐标分量式：
  $$\boldsymbol{v} = v_x\boldsymbol{i} + v_y\boldsymbol{j} + v_z\boldsymbol{k} = \frac{dx}{dt}\boldsymbol{i} + \frac{dy}{dt}\boldsymbol{j} + \frac{dz}{dt}\boldsymbol{k}$$
- 速率：
  $$v = |\boldsymbol{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2} = \left|\frac{d\boldsymbol{r}}{dt}\right|$$

---

### 四、加速度

**核心概念/定义**
- **平均加速度 $\bar{\boldsymbol{a}}$**：速度增量 $\Delta\boldsymbol{v}$ 与所用时间 $\Delta t$ 的比值。
- **瞬时加速度 $\boldsymbol{a}$**：平均加速度在 $\Delta t \to 0$ 时的极限，描述速度大小和方向变化的快慢。

**定理/定律/公式**
- 平均加速度：
  $$\bar{\boldsymbol{a}} = \frac{\Delta\boldsymbol{v}}{\Delta t}$$
- 瞬时加速度：
  $$\boldsymbol{a} = \lim_{\Delta t \to 0} \frac{\Delta\boldsymbol{v}}{\Delta t} = \frac{d\boldsymbol{v}}{dt} = \frac{d^2\boldsymbol{r}}{dt^2}$$
- 直角坐标分量式：
  $$\boldsymbol{a} = a_x\boldsymbol{i} + a_y\boldsymbol{j} + a_z\boldsymbol{k} = \frac{dv_x}{dt}\boldsymbol{i} + \frac{dv_y}{dt}\boldsymbol{j} + \frac{dv_z}{dt}\boldsymbol{k}$$
- 加速度大小：
  $$a = |\boldsymbol{a}| = \sqrt{a_x^2 + a_y^2 + a_z^2}$$

**方向判定定理**
- 加速度与速度**同向** → 速率增大（加速）
- 加速度与速度**反向** → 速率减小（减速）
- 匀速直线运动 → 加速度为 $0$

**运动学的两类基本问题（解题套路）**

| 问题类型 | 已知条件 | 求解目标 | 核心方法 |
|:---|:---|:---|:---|
| **第一类（微分法）** | 运动方程 $\boldsymbol{r} = \boldsymbol{r}(t)$ | 求 $\boldsymbol{v}(t), \boldsymbol{a}(t)$ | 对 $t$ 求一阶导得速度，求二阶导得加速度 |
| **第二类（积分法）** | 加速度 $\boldsymbol{a}(t)$ + 初始条件 $\boldsymbol{v}_0, \boldsymbol{r}_0$ | 求 $\boldsymbol{v}(t), \boldsymbol{r}(t)$ | $\boldsymbol{v} = \boldsymbol{v}_0 + \int_{t_0}^{t}\boldsymbol{a}\,dt$，$\boldsymbol{r} = \boldsymbol{r}_0 + \int_{t_0}^{t}\boldsymbol{v}\,dt$ |

**典型解题套路（第二类问题的常见情形）**
- **Step 1**：明确加速度是 $t$、$v$ 还是 $x$ 的函数。
- **Step 2**：若 $a = a(t)$，直接积分：$v = v_0 + \int a(t)\,dt$。
- **Step 3**：若 $a = a(v)$，用分离变量法：$\frac{dv}{a(v)} = dt$，积分求解。
- **Step 4**：若 $a = a(x)$，用链式变换：$a = \frac{dv}{dt} = v\frac{dv}{dx}$，则 $\int_{v_0}^{v} v\,dv = \int_{x_0}^{x} a(x)\,dx$。
- **Step 5**：由 $v(t)$ 再积分得 $x(t)$。

---

## 1-2 圆周运动

### 一、平面极坐标

**核心概念/定义**
- 用径向距离 $r$ 和极角 $\theta$ 描述质点在平面内的位置。
- 适用于质点绕某固定点做曲线运动的场景。

### 二、圆周运动的角速度

**核心概念/定义**
- **角坐标 $\theta$**：代数量，规定逆时针方向为正。
- **平均角速度 $\bar{\omega}$**：$\bar{\omega} = \frac{\Delta\theta}{\Delta t}$
- **瞬时角速度 $\omega$**：
  $$\omega = \frac{d\theta}{dt}$$

### 三、圆周运动的切向加速度和法向加速度 角加速度

**核心概念/定义**
- **角加速度 $\beta$**（或 $\alpha$）：
  $$\beta = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$$
- **切向加速度 $a_\tau$**：描述速率**大小**的变化。
- **法向加速度 $a_n$**：描述速度**方向**的变化，始终指向圆心。

**定理/定律/公式**
- 自然坐标系下的加速度分解：
  $$\boldsymbol{a} = a_\tau\boldsymbol{e}_\tau + a_n\boldsymbol{e}_n$$
- 切向加速度：
  $$a_\tau = \frac{dv}{dt} = r\beta$$
- 法向加速度：
  $$a_n = \frac{v^2}{r} = r\omega^2$$
- 合加速度大小：
  $$a = \sqrt{a_\tau^2 + a_n^2} = \sqrt{\left(\frac{dv}{dt}\right)^2 + \left(\frac{v^2}{r}\right)^2} = r\sqrt{\beta^2 + \omega^4}$$
- 合加速度方向（与法向夹角）：
  $$\alpha = \arctan\frac{a_\tau}{a_n}$$

### 四、自然坐标系

**核心概念/定义**
- **切向单位矢量 $\boldsymbol{e}_\tau$**：沿质点所在点轨道的切线方向，指向运动方向。
- **法向单位矢量 $\boldsymbol{e}_n$**：垂直于切向，指向曲线凹侧（圆心方向）。
- 两个单位矢量的模均为 1，但方向随位置变化。

**速度表达**
$$\boldsymbol{v} = v\,\boldsymbol{e}_\tau$$

### 五、匀速率圆周运动和匀变速率圆周运动

**核心概念/定义**
- **匀角速圆周运动（匀速圆周运动）**：$\omega$ 为常量，$\beta = 0$。速率不变，只有法向加速度。
- **匀角加速圆周运动**：$\beta$ 为常量。

**定理/定律/公式**
- **匀角速圆周运动**：
  $$\theta = \theta_0 + \omega t$$
- **匀角加速圆周运动**（与匀变速直线运动公式类比）：
  $$\omega = \omega_0 + \beta t$$
  $$\theta = \theta_0 + \omega_0 t + \frac{1}{2}\beta t^2$$
  $$\omega^2 = \omega_0^2 + 2\beta(\theta - \theta_0)$$

**线量与角量关系汇总**
| 线量 | 角量 | 关系式 |
|:---|:---|:---|
| 弧长 $\Delta s$ | 角位移 $\Delta\theta$ | $\Delta s = r\Delta\theta$ |
| 速率 $v$ | 角速度 $\omega$ | $v = r\omega$ |
| 切向加速度 $a_\tau$ | 角加速度 $\beta$ | $a_\tau = r\beta$ |
| 法向加速度 $a_n$ | 角速度 $\omega$ | $a_n = r\omega^2$ |

---

## 1-3 相对运动

### 一、时间与空间

**核心概念/定义**
- **经典时空观（伽利略变换前提）**：在牛顿力学范围内，时间和空间的测量是**绝对的**，与参考系的选择无关。
- 即：$t = t'$，长度测量不随参考系改变。

### 二、相对运动

**核心概念/定义**
- 描述质点的运动依赖于参考系的选择。同一质点在不同参考系中，其位移、速度、加速度可能不同。

**定理/定律/公式（伽利略变换）**
- 设 $S$ 为静止参考系，$S'$ 为相对于 $S$ 运动的参考系：
  - **坐标变换**：
    $$\boldsymbol{r} = \boldsymbol{r}' + \boldsymbol{R}$$
  - **速度变换（伽利略速度合成定理）**：
    $$\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}$$
    （绝对速度 = 相对速度 + 牵连速度）
  - **加速度变换**：
    $$\boldsymbol{a} = \boldsymbol{a}' + \boldsymbol{a}_0$$
    （当 $S'$ 相对 $S$ 做匀速直线运动时，$\boldsymbol{a}_0 = 0$，则 $\boldsymbol{a} = \boldsymbol{a}'$）

**典型解题套路（相对运动问题）**
- **Step 1**：明确三个对象——质点（被观测物）、运动参考系（观测者）、静止参考系（地面）。
- **Step 2**：分别标出绝对速度 $\boldsymbol{v}$、相对速度 $\boldsymbol{v}'$、牵连速度 $\boldsymbol{u}$ 的方向和已知量。
- **Step 3**：建立直角坐标系，列矢量方程 $\boldsymbol{v} = \boldsymbol{v}' + \boldsymbol{u}$。
- **Step 4**：分解为 $x, y$ 分量，联立方程组求解未知量。
- **Step 5**：如求大小和方向，用 $v = \sqrt{v_x^2 + v_y^2}$，$\theta = \arctan\frac{v_y}{v_x}$。

---