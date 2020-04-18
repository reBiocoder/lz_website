<template>

  <div class="row">
    <div class="col-4">
    </div>
    <div class="q-pa-md col-4">
      <q-form
        @submit="onSubmit"
        @reset="onReset"
        class="q-gutter-md"
      >
        <q-input
          type="text"
          filled
          v-model="real_name"
          label="真实姓名"
          lazy-rules
          :rules="[ val => val && val.length <= 3 || '姓名长度小于3']"
        />
        <q-input
          type="text"
          filled
          v-model="username"
          label="您的账号"
          lazy-rules
          :rules="[ val => val && val.length > 3 || '账号长度需要大于3']"
        />

        <q-input
          filled
          type="password"
          v-model="password"
          label="您的密码"
          lazy-rules
          :rules="[
          val => val !== null && val !== '' || '请输入密码',
          val => val.length >= 6   || '密码长度需要大于6位'
        ]"
        />
        <q-input
          filled
          type="password"
          v-model="once_password"
          label="再次验证密码"
          lazy-rules
          :rules="[
          val => val === this.password || '两次密码不一致'
        ]"
        />
        <div>
          <q-btn label="Submit" type="submit" color="primary"/>
          <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm"/>
        </div>
      </q-form>
      <router-link :to="{name: 'login'}">马上登录</router-link>
    </div>
    <div class="col-4"></div>
  </div>
</template>

<script>
  import http from "../../api/backStage";

  export default {
    name: 'register',
    data() {
      return {
        real_name: null,
        username: null,
        password: null,
        once_password: null
      }
    },

    methods: {
      onSubmit() {
        http.getRegister({
            "real_name": this.real_name,
            "username": this.username,
            "password": this.password,
          },
          (res) => {
            if (res.data.code === 'success') {
              this.$router.push({name: "login"})
            } else {
              this.$q.notify({
                message: res.data.info
              })
            }
          })
      },

      onReset() {
        this.username = null
        this.password = null
      }
    }
  }
</script>
