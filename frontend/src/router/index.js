import { createRouter, createWebHistory } from 'vue-router';
import AgriculturalMachineList from '../components/AgriculturalMachineList.vue';
import MaintenanceHistory from '../components/MaintenanceHistory.vue';
import PartManagement from '../components/PartManagement.vue';
import RentalManagement from '../components/RentalManagement.vue';

const routes = [
  { path: '/', redirect: '/machines' },
  { path: '/machines', component: AgriculturalMachineList },
  { path: '/maintenance', component: MaintenanceHistory },
  { path: '/parts', component: PartManagement },
  { path: '/rentals', component: RentalManagement },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
