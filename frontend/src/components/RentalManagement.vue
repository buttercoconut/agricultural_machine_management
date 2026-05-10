<template>
  <div>
    <h2>Rental Management</h2>
    <button @click="fetchRentals">Refresh</button>
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Machine ID</th>
          <th>Renter ID</th>
          <th>Start Date</th>
          <th>End Date</th>
          <th>Daily Rate</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="r in rentals" :key="r.id">
          <td>{{ r.id }}</td>
          <td>{{ r.machine_id }}</td>
          <td>{{ r.renter_id }}</td>
          <td>{{ r.start_date }}</td>
          <td>{{ r.end_date }}</td>
          <td>{{ r.daily_rate }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'RentalManagement',
  data() {
    return {
      rentals: [],
    };
  },
  methods: {
    async fetchRentals() {
      const res = await axios.get('/api/rental');
      this.rentals = res.data;
    },
  },
  mounted() {
    this.fetchRentals();
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
