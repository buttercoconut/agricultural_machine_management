<template>
  <div class="container">
    <h1>농업기계 관리 시스템</h1>
    <nav class="nav">
      <router-link to="/machines">기계 목록</router-link>
      <router-link to="/maintenance">유지보수</router-link>
      <router-link to="/parts">부품 관리</router-link>
      <router-link to="/rentals">임대 관리</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
// No additional logic needed for the root component
</script>

<style scoped>
.container {
  padding: 20px;
}
.nav {
  margin-bottom: 20px;
}
.nav a {
  margin-right: 15px;
  text-decoration: none;
  color: #42b983;
}
.nav a.router-link-exact-active {
  font-weight: bold;
}
</style>
