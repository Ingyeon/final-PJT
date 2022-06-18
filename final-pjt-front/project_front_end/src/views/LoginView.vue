<template>
  <div class="mx-auto my-3 p-3 border border-1 rounded" style="max-width:400px;">

    <h2>Login</h2>
    <AccountErrorList v-if="authError" style="display: none"></AccountErrorList>
    <div style="max-width: 400px;" class="">
      <b-form @submit.prevent="login(credentials)">
        <b-form-group id="username" label="Username:" label-for="username" >
          <b-form-input id="username" v-model="credentials.username" type="text" placeholder="Enter Username" required />
        </b-form-group>

        <b-form-group id="password" label="Password:" label-for="password">
          <b-form-input id="password" v-model="credentials.password" placeholder="Enter Password" type="password" required />
        </b-form-group>

        <b-button type="submit" variant="primary" class="mt-3">로그인</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style>
  label {
    text-align: start;
  }
</style>
