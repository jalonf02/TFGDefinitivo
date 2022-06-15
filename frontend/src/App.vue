<template>
  <v-app>
    <Navbar>
    </Navbar>
<<<<<<< HEAD
      <router-view />
=======
    <v-content class="mb-12">
      <router-view />
    </v-content>
>>>>>>> fc92d65fbf4f8f79471ebd3b2e43a3911cdbfb2c
    <v-spacer></v-spacer>
  </v-app>
</template>

<script>
import Navbar from './components/Navbar'
export default {
  name: 'App',
<<<<<<< HEAD
=======

>>>>>>> fc92d65fbf4f8f79471ebd3b2e43a3911cdbfb2c
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
