<template>
  <div>
    <h2>Part Inventory</h2>
    <button @click="fetchParts">Refresh</button>
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Quantity</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in parts" :key="p.id">
          <td>{{ p.id }}</td>
          <td>{{ p.name }}</td>
          <td>{{ p.quantity }}</td>
          <td>{{ p.location }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'PartInventory',
  data() {
    return {
      parts: [],
    };
  },
  methods: {
    async fetchParts() {
      const res = await axios.get('/api/part');
      this.parts = res.data;
    },
  },
  mounted() {
    this.fetchParts();
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
