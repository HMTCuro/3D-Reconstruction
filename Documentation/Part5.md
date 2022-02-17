# Part V 网站开发

## 网站结构

- 首页（导航页）
  - 点云（使用Potree渲染）
    - 东北亚学院
    - 体育馆北馆
    - 体育馆南馆
  - 带有窗户识别结果的点云（使用Potree渲染，Part 2 结果）
    - 东北亚学院
    - 体育馆北馆
    - 体育馆南馆
  - 带有语义分割结果的点云（使用Potree渲染，Part 3 结果） 
    - 东北亚学院
    - 体育馆北馆
    - 体育馆南馆
  - 表面重建、纹理贴图结果（使用Three.js渲染）
    - 东北亚学院
    - 体育馆北馆
    - 体育馆南馆
  - 白模（使用Three.js渲染）
    - 东北亚学院
    - 体育馆北馆
    - 体育馆南馆
  - 白模（使用Three.js渲染，Neus生成）
    - 东北亚学院
    - 体育馆北馆
    - 体育馆南馆



## 网站技术

- 前端框架：[Vue3](https://v3.cn.vuejs.org/)

- 前端开发与构建：[Vite](https://cn.vitejs.dev/)

- 路由：[Vue Router](https://router.vuejs.org/)

- 前端组件库：[Element Plus](https://element-plus.gitee.io/zh-CN/)

- 渲染工具：[Potree](https://potree.github.io/index.html)（渲染较大点云）、[Three.js](https://threejs.org/)（渲染白模等较小模型）

- 后期处理：[Postprocessing](https://github.com/vanruesc/postprocessing)



## 参考链接

- https://element-plus.gitee.io/zh-CN/component/button.html
- https://www.bilibili.com/video/BV14P4y1L7i8?spm_id_from=333.999.0.0

