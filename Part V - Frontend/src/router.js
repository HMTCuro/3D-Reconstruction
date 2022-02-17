import { createRouter, createWebHistory } from 'vue-router';
import Index from './views/Index.vue';
import Scene from './components/Scene.vue';

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
    meta: { title: 'SDU 3D-Viewer' },
  },
  {
    path: '/scene',
    name: 'Scene',
    component: Scene,
    meta: { title: 'SDU 3D-Viewer' },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router;
