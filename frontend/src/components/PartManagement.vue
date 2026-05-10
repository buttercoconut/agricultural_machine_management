<template>
  <div>
    <h2>유지보수 기록</h2>
    <form @submit.prevent="addRecord">
      <label for="machineId">기계 ID</label>
      <input id="machineId" v-model="newRecord.machine_id" required />
      <label for="date">날짜</label>
      <input id="date" type="date" v-model="newRecord.date" required />
      <label for="description">설명</label>
      <textarea id="description" v-model="newRecord.description" required />
      <button type="submit">추가</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>기계 ID</th>
          <th>날짜</th>
          <th>설명</th>
        </tr>
      <thead>
      <tbody>
        <tr v-for="record in records" :key="record.id">
          <td>{{ record.id }}</td>
          <td>{{ record.machine_id }}</td>
          <td>{{ record.date }}</td>
          <td>{{ record.description }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const records = ref([]);
const newRecord = ref({ machine_id: '', date: '', description: '' });
const router = useRouter();

const fetchRecords = async () => {
  try {
    const response = await router.app.config.globalProperties.$axios.get('/maintenance_records');
    records.value = response.data;
  } catch (error) {
    console.error('Error fetching records:', error);
  }
};

const addRecord = async () => {
  try {
    await router.app.config.globalProperties.$axios.post('/maintenance_records', newRecord.value);
    newRecord.value = { machine_id: '', date: '', description: '' };
    fetchRecords();
  } catch (error) {
    console.error('Error adding record:', error);
  }
};

onMounted(() => {
  fetchRecords();
});
</script>

<style scoped>
form {
  margin-bottom: 20px;
}
label {
  display: block;
  margin-top: 10px;
}
input, textarea {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
}
button {
  margin-top: 10px;
  padding: 8px 12px;
}

/* Table styles */
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
