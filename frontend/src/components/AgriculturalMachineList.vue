<template>
  <div>
    <h2>Agricultural Machine List</h2>
    <button @click="fetchMachines">Refresh</button>
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Type</th>
          <th>Status</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="m in machines" :key="m.id">
          <td>{{ m.id }}</td>
          <td>{{ m.name }}</td>
          <td>{{ m.type }}</td>
          <td>{{ m.status }}</td>
          <td>{{ m.location }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'AgriculturalMachineList',
  data() {
    return {
      machines: [],
    };
  },
  methods: {
    async fetchMachines() {
      const res = await axios.get('/api/agricultural_machine');
      this.machines = res.data;
    },
  },
  mounted() {
    this.fetchMachines();
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
