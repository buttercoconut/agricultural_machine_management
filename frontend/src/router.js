import { createRouter, createWebHistory } from 'vue-router';
import AgriculturalMachineList from './components/AgriculturalMachineList.vue';
import MaintenanceHistory from './components/MaintenanceHistory.vue';
import PartInventory from './components/PartInventory.vue';
import RentalManagement from './components/RentalManagement.vue';
import UserManagement from './components/UserManagement.vue';

const routes = [
  { path: '/machines', component: AgriculturalMachineList },
  { path: '/maintenances', component: MaintenanceHistory },
  { path: '/parts', component: PartInventory },
  { path: '/rentals', component: RentalManagement },
  { path: '/users', component: UserManagement },
  { path: '/', redirect: '/machines' },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
