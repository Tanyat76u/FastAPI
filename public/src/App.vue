<template>
  <div id="app">
    <auth-component v-if="!isAuth" @handleAuth="handleAuth"/>
    <div v-else>
      <p>Вы авторизованы</p>
    </div>
  </div>
</template>

<script>
import AuthComponent from './components/AuthComponent.vue'

export default {
  name: 'App',
  components: {
    AuthComponent
  },
  data() {
    return {
      isAuth: false
  };
},
  methods: {
    handleAuth() {
      this.isAuth = true;
  }
}
}
</script>

<style>
</style>
