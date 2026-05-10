<template>
  <div>
    <h2>농업기계 목록</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>모델명</th>
          <th>제조사</th>
          <th>구매일자</th>
          <th>시운전 시간</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="machine in machines" :key="machine.id">
          <td>{{ machine.id }}</td>
          <td>{{ machine.model_name }}</td>
          <td>{{ machine.manufacturer }}</td>
          <td>{{ machine.purchase_date }}</td>
          <td>{{ machine.test_run_hours }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const machines = ref([]);
const router = useRouter();

const fetchMachines = async () => {
  try {
    const response = await router.app.config.globalProperties.$axios.get('/agricultural_machines');
    machines.value = response.data;
  } catch (error) {
    console.error('Error fetching machines:', error);
  }
};

onMounted(() => {
  fetchMachines();
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
