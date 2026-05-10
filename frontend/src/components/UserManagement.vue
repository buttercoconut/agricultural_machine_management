<template>
  <div>
    <h2>User Management</h2>
    <button @click="fetchUsers">Refresh</button>
    <table border="1" cellpadding="5" cellspacing="0">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Phone</th>
          <th>Email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="u in users" :key="u.id">
          <td>{{ u.id }}</td>
          <td>{{ u.name }}</td>
          <td>{{ u.phone }}</td>
          <td>{{ u.email }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'UserManagement',
  data() {
    return {
      users: [],
    };
  },
  methods: {
    async fetchUsers() {
      const res = await axios.get('/api/user');
      this.users = res.data;
    },
  },
  mounted() {
    this.fetchUsers();
  },
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>
