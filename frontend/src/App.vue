<template>
  <v-app>
    <Navbar>
    </Navbar>
    <v-content class="mb-12">
      <router-view />
    </v-content>
    <v-spacer></v-spacer>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar'
export default {
  name: 'App',

  components: {
    Navbar
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
