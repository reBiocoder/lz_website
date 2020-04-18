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
          v-model="username"
          label="账号"
          lazy-rules
          :rules="[ val => val && val.length > 3 || '账号长度需要大于3']"
        />

        <q-input
          filled
          type="password"
          v-model="password"
          label="密码"
          lazy-rules
          :rules="[
          val => val !== null && val !== '' || '请输入密码',
          val => val.length >= 6   || '密码长度需要大于6位'
        ]"
        />
        <div>
          <q-btn label="登录" type="submit" color="primary"/>
          <q-btn label="重置" type="reset" color="primary" flat class="q-ml-sm"/>
        </div>
      </q-form>
      <router-link :to="{name: 'register'}">马上注册</router-link>
    </div>
    <div class="col-4"></div>
  </div>
</template>

<script>
  import http from "../../api/backStage"
  import {mapMutations, mapState} from 'vuex'
  import {real_name} from "../../store/mutations";

  export default {
    data() {
      return {
        username: null,
        password: null,
      }
    },
    methods: {
      ...mapMutations(process.env.APP_SCOPE_NAME, {
        "change_real_name": "real_name",
        "change_username": "username"
      }),
      onSubmit() {
        http.getLogin({"username": this.username, "password": this.password},
          (res) => {
          console.log(res)
            if (res.data.code === 'success') {
              this.change_real_name(res.data.data.real_name)
              this.change_username(res.data.data.username)
              this.$router.push({
                "name": "administrator",
              })
            } else if (res.data.code === 'login') {
              this.$q.notify({
                message: res.data.info
              })
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
