<!-- 
  Reference: https://element-plus.gitee.io/
             https://www.bilibili.com/video/BV14P4y1L7i8?spm_id_from=333.999.0.0
-->
<template>
  <div
    class="position-relative scene"
    ref="scene"
    v-loading.fullscreen.lock='loading'
    element-loading-text="模型下载中（大约需要5s）..."
  >
    <div v-bind:style='style1' v-show="showMessage">
      <el-row v-bind:style='style2' justify="space-between">
        <div>详细信息</div>
        <el-button v-on:Click='closeHint'>关闭</el-button>
      </el-row>
      <el-descriptions class="margin-top" :column="3" :size="size" border>
        <el-descriptions-item>
          <template #label><div class="cell-item">建筑名称</div></template>
          {{message[index].name}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">长</div></template>
          {{message[index].length}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">宽</div></template>
          {{message[index].width}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">高</div></template>
          {{message[index].height}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">体积</div></template>
          {{message[index].volume}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">窗户面积</div></template>
          {{message[index].windowArea}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">窗户数目</div></template>
          {{message[index].windowNumber}}
        </el-descriptions-item>
        <el-descriptions-item>
          <template #label><div class="cell-item">楼层数目</div></template>
          {{message[index].layerNumber}}
        </el-descriptions-item>
      </el-descriptions>
    </div>
  </div>
</template>

<script>
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';
import {
  EffectComposer,
  RenderPass,
  EffectPass,
  BloomEffect,
} from 'postprocessing';
import { h } from 'vue';

export default {
  name: 'Scene',

  data: () => ({
    loading: true,
    publicPath: import.meta.env.BASE_URL,
    progress: 0,
    showMessage: false,
    part: 0,
    index: 0, //如果要应用不同模型用这个作为索引，索引值为0，1，2
    isWhiteMesh: true,
    url: null,
    list: [
      [
        {name: "东北亚学院", url: "./three/dongbeiya"},
        {name: "体育馆北馆", url: "./three/gym_north"},
        {name: "体育馆南馆", url: "./three/gym_south"}
      ],
      [
        {name: "东北亚学院", url: "./three/dongbeiya"},
        {name: "体育馆北馆", url: "./three/gym_north"},
        {name: "体育馆南馆", url: "./three/gym_south"}
      ],
      [
        {name: "东北亚学院", url: "./three/dongbeiya_neus"},
        {name: "体育馆北馆", url: "./three/gym_north_neus"},
        {name: "体育馆南馆", url: "./three/gym_south_neus"}
      ],
    ],
    message: [{
        name: '东北亚学院',
        length: '90.21',
        width: '24.10',
        height: '28.10',
        volume: '24958.36',
        windowArea: '548.4',
        windowNumber: '204',
        layerNumber: '3/5/6',
      },
      {
        name: '体育馆北馆',
        length: '83.88',
        width: '50.39',
        height: '28.28',
        volume: '77142.45',
        windowArea: '1402.5',
        windowNumber: '113',
        layerNumber: '5',
      },
      {
        name: '体育馆南馆',
        length: '68.94',
        width: '83.88',
        height: '28.10',
        volume: '59844.31',
        windowArea: '1016.8',
        windowNumber: '95',
        layerNumber: '3',
      },
    ],
    style1: {
      position: 'fixed',
      bottom: '0',
      right: '0',
      width: '400px',
      border: '1px solid #aaaaaa',
      padding: '10px',
      background: '#ffffff',
    },
    style2: {
      padding: '5px'
    },
  }),

  mounted() {
    if (this.$route.params) {
      this.part = this.$route.params.part;
      this.index = this.$route.params.index;
      this.url = this.list[this.part][this.index].url;
    } else {
      this.$route.push('/index');
    }
    if (this.part == 0) {
      this.isWhiteMesh = false;
    }
    console.log(this.part, this.index, this.url);

    window.addEventListener('resize', this.onCanvasResize, false);
    this.init();
    window.addEventListener('click', this.onClick, false);
  },

  unmounted() {
    window.removeEventListener('resize', this.onCanvasResize);
    window.removeEventListener('click', this.onClick);
  },

  methods: {
    init() {
      // Scene
      this.scene = new THREE.Scene();
      this.scene.background = new THREE.Color(0x000000); // 背景设为黑色

      // Renderer
      this.renderer = new THREE.WebGLRenderer({
        antialias: true
      });
      // this.renderer.setSize(this.$refs.scene.clientWidth, this.$refs.scene.clientHeight);
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.renderer.toneMapping = THREE.ReinhardToneMapping;
      this.renderer.toneMappingExposure = 3;
      this.renderer.shadowMap.enabled = true;
      // this.renderer.setClearColor(0xffffff, 1);
      this.$refs.scene.appendChild(this.renderer.domElement);

      // Camera
      // const aspect = this.$refs.scene.clientWidth / this.$refs.scene.clientHeight;
      const aspect = window.innerWidth / window.innerHeight;
      this.camera = new THREE.PerspectiveCamera(60, aspect, 0.01, 1000);
      // this.camera.position.set(0, 3, 5);
      this.camera.position.set(0, 5, 8);

      // Camera Controls
      this.controls = new OrbitControls(
        this.camera,
        this.renderer.domElement
      );
      // this.controls.addEventListener('change', this.renderer);
      this.controls.update();

      // Light
      if (this.isWhiteMesh) {
        // this.hemiLight = new THREE.HemisphereLight(0xffeeb1, 0x080820, 2);
        this.hemiLight = new THREE.HemisphereLight(0xaaaaaa, 0x222222, 2);
        this.hemiLight.position.set(0, 10, 0);
        this.scene.add(this.hemiLight);
      } else {
        var ambient = new THREE.AmbientLight(0xffffff);
        this.scene.add(ambient);
      }

      // this.spotLight = new THREE.SpotLight(0xffa95c, 4);
      // this.spotLight.castShadow = true;
      // this.spotLight.shadow.bias = -0.0001;
      // this.spotLight.shadow.mapSize.width = 10000;
      // this.spotLight.shadow.mapSize.height = 10000;
      // this.scene.add(this.spotLight);

      // Post Processing
      this.composer = new EffectComposer(this.renderer);
      this.composer.addPass(
        new RenderPass(this.scene, this.camera)
      );

      const effectPass = new EffectPass(
        this.camera,
        new BloomEffect({
          intensity: 3,
          luminanceThreshold: 0.8,
          width: 100,
          height: 100,
        })
      );
      this.composer.addPass(effectPass);

      // Loading Manager
      const manager = new THREE.LoadingManager();
      manager.onProgress = (url, itemsLoaded, itemsTotal) => {
        this.progress = (itemsLoaded / itemsTotal) * 100;
        if ((itemsLoaded / itemsTotal) * 100 === 100) {
          this.loading = false;
          setTimeout(() => {
            this.flag = true;
          }, 1000);
        }
      };

      const loader = new PLYLoader(manager);
      // loader.load(`${this.publicPath}/${this.url.slice(2)}.ply`, (result) => {
      loader.load(`${this.url.slice(2)}.ply`, (result) => {
        // const model = result.scene.children[0];

        result.computeVertexNormals();
        if (this.isWhiteMesh) {
          console.log('white')
          var material = new THREE.MeshStandardMaterial({
            color: 0xffffff,
            flatShading: true
          });
        } else {
          const texture = new THREE.TextureLoader().load(`${this.url}.png`);
          var material = new THREE.MeshStandardMaterial({
            map: texture
          });
        }

        const model = new THREE.Mesh(result, material);
        model.scale.set(1, 1, 1);

        var axis1 = new THREE.Vector3(1, 0, 0);  // 向量axis
        var axis2 = new THREE.Vector3(0, 1, 0);  // 向量axis
        var axis3 = new THREE.Vector3(0, 0, 1);  // 向量axis
        if (this.part == 0 && this.index == 0) {
          model.scale.set(1.5, 1.5, 1.5);
          model.rotateOnAxis(axis1, Math.PI * 1.8);
          model.rotateOnAxis(axis2, Math.PI);
          model.rotateOnAxis(axis3, Math.PI);
        } else if (this.part == 0 && this.index == 1) {
          model.scale.set(1.3, 1.3, 1.3);
          model.rotateOnAxis(axis1, Math.PI * 1);
          model.rotateOnAxis(axis2, Math.PI * 1.2);
          model.rotateOnAxis(axis3, Math.PI * 0.1);
        } else if (this.part == 0 && this.index == 2) {
          model.scale.set(1.3, 1.3, 1.3);
          model.rotateOnAxis(axis1, Math.PI * 1);
          model.rotateOnAxis(axis2, Math.PI * 1.2);
          model.rotateOnAxis(axis3, Math.PI * 0.17);
        } else if (this.part == 1 && this.index == 0) {
          model.scale.set(1.5, 1.5, 1.5);
          model.rotateOnAxis(axis1, Math.PI * 1.8);
          model.rotateOnAxis(axis2, Math.PI);
          model.rotateOnAxis(axis3, Math.PI);
        } else if (this.part == 1 && this.index == 1) {
          model.scale.set(1.3, 1.3, 1.3);
          model.rotateOnAxis(axis1, Math.PI * 1);
          model.rotateOnAxis(axis2, Math.PI * 1.2);
          model.rotateOnAxis(axis3, Math.PI * 0.1);
        } else if (this.part == 1 && this.index == 2) {
          model.scale.set(1.3, 1.3, 1.3);
          model.rotateOnAxis(axis1, Math.PI * 1);
          model.rotateOnAxis(axis2, Math.PI * 1.2);
          model.rotateOnAxis(axis3, Math.PI * 0.17);
        } else if (this.part == 2 && this.index == 0) {
          model.scale.set(1.5, 1.5, 1.5);
          model.rotateOnAxis(axis1, Math.PI * 1.8);
          model.rotateOnAxis(axis2, Math.PI * 1.3);
          model.rotateOnAxis(axis3, Math.PI * 1.2);
        } else if (this.part == 2 && this.index == 1) {
          model.scale.set(1.3, 1.3, 1.3);
          model.rotateOnAxis(axis1, Math.PI * 1);
          model.rotateOnAxis(axis2, Math.PI * 1.2);
          model.rotateOnAxis(axis3, Math.PI * 0.1);
        } else if (this.part == 2 && this.index == 2) {
          model.scale.set(1.3, 1.3, 1.3);
          model.rotateOnAxis(axis1, Math.PI * 1.1);
          model.rotateOnAxis(axis2, Math.PI * 16);
          model.rotateOnAxis(axis3, Math.PI * 0);
        } 

        model.traverse((n) => {
          if (n.isMesh) {
            n.castShadow = false;
            n.receiveShadow = true;
            // n.receiveShadow = false;
            if (n.material.map) n.material.map.anisotropy = 100;
          }
        });
        this.scene.add(model);
        this.animate();
      });

    },
    closeHint() {
      this.showMessage = false;
    },
    onClick(event) {
      if (!this.showMessage) {
        // 获取 raycaster 和所有模型相交的数组，其中的元素按照距离排序，越近的越靠前
        var intersects = this.getIntersects(event);

        // 获取选中最近的 Mesh 对象
        if (intersects.length != 0 && intersects[0].object instanceof THREE.Mesh && !this.showMessage && this.isWhiteMesh) {
          this.showMessage = true;
          this.selectObject = intersects[0].object;
        } else {
          console.log("未选中 Mesh!");
        }
      }
    },
    getIntersects(event) {
      event.preventDefault();

      // 声明 raycaster 和 mouse 变量
      var raycaster = new THREE.Raycaster();
      var mouse = new THREE.Vector2();

      // 通过鼠标点击位置,计算出 raycaster 所需点的位置,以屏幕为中心点,范围 -1 到 1
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;

      //通过鼠标点击的位置(二维坐标)和当前相机的矩阵计算出射线位置
      raycaster.setFromCamera(mouse, this.camera);

      // 获取与射线相交的对象数组，其中的元素按照距离排序，越近的越靠前
      var intersects = raycaster.intersectObjects(this.scene.children);

      //返回选中的对象
      return intersects;
    },
    // 更新div的位置
    renderDiv(object) {
      // 获取窗口的一半高度和宽度
      var halfWidth = window.innerWidth / 2;
      var halfHeight = window.innerHeight / 2;

      // 逆转相机求出二维坐标
      var vector = object.position.clone().project(this.camera);

      // 修改 div 的位置
      console.log('hit!');
    },

    animate() {
      if (this.selectObject != undefined && this.selectObject != null) {
        this.renderDiv(this.selectObject);
        this.selectObject = null;
      }
      requestAnimationFrame(this.animate);
      this.controls.update();
      // this.spotLight.position.set(
      //   this.camera.position.x + 5,
      //   this.camera.position.y + 5,
      //   this.camera.position.z - 5,
      // )
      // this.renderer.render(this.scene, this.camera);
      this.composer.render();
    },
    onCanvasResize() {
      this.camera.aspect = window.innerWidth / window.innerHeight;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(
        window.innerWidth,
        window.innerHeight
      );
      this.composer.setSize(
        window.innerWidth,
        window.innerHeight
      );
    },
  },
}
</script>

<style scoped>
  .scene {
    width: 70%;
    height: 0;
    padding-bottom: 39.375%;
  }

  .w-20 {
    width: 20%;
  }

  .h-small {
    height: 10px;
  }

  @media (max-width: 992px) {
    .scene {
      width: 100%;
      height: 0;
      padding-bottom: 56.25%;
    }
  }
</style>