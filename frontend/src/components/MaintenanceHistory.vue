<template>
  <div>
    <h2>Maintenance History</h2>
    <button @click="fetchMaintenances">Refresh</button>
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Machine ID</th>
          <th>Date</th>
          <th>Description</th>
          <th>Cost</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="m in maintenances" :key="m.id">
          <td>{{ m.id }}</td>
          <td>{{ m.machine_id }}</td>
          <td>{{ m.maintenance_date }}</td>
          <td>{{ m.description }}</td>
          <td>{{ m.cost }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'MaintenanceHistory',
  data() {
    return {
      maintenances: [],
    };
  },
  methods: {
    async fetchMaintenances() {
      const res = await axios.get('/api/maintenance');
      this.maintenances = res.data;
    },
  },
  mounted() {
    this.fetchMaintenances();
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
