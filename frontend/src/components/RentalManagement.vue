<template>
  <div>
    <h2>임대 관리</h2>
    <form @submit.prevent="addRental">
      <label for="machineId">기계 ID</label>
      <input id="machineId" v-model="newRental.machine_id" required />
      <label for="startDate">시작일</label>
      <input id="startDate" type="date" v-model="newRental.start_date" required />
      <label for="endDate">종료일</label>
      <input id="endDate" type="date" v-model="newRental.end_date" required />
      <button type="submit">추가</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>ID</td>
          <th>기계 ID</td>
          <th>시작일</td>
          <th>종료일</td>
        </tr>
      <thead>
      <tbody>
        <tr v-for="rental in rentals" :key="rental.id">
          <td>{{ rental.id }}</td>
          <td>{{ rental.machine_id }}</td>
          <td>{{ rental.start_date }}</td>
          <td>{{ rental.end_date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const rentals = ref([]);
const newRental = ref({ machine_id: '', start_date: '', end_date: '' });
const router = useRouter();

const fetchRentals = async () => {
  try {
    const response = await router.app.config.globalProperties.$axios.get('/rental_records');
    rentals.value = response.data;
  } catch (error) {
    console.error('Error fetching rentals:', error);
  }
};

const addRental = async () => {
  try {
    await router.app.config.globalProperties.$axios.post('/rental_records', newRental.value);
    newRental.value = { machine_id: '', start_date: '', end_date: '' };
    fetchRentals();
  } catch (error) {
    console.error('Error adding rental:', error);
  }
};

onMounted(() => {
  fetchRentals();
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
}
th {
  background-color: #f2f2f2;
}
</style>
