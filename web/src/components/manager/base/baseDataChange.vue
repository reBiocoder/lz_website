<template>
  <div class="q-pa-md">
    <q-card>
      <q-tab-panel name="base_data" class="shadow-0">
        <div class="row">
          <div class="col-md-1 text-subtitle2" style="padding-top: 5px;">
            <q-icon name="keyboard_backspace"/>
            返回
          </div>
          <q-separator vertical inset/>
          <div class="col-md-3 text-primary text-h6">配置M744_RS13850</div>
        </div>
        <q-separator/>
        <!--修改表单---------------->
        <q-form
          @submit="onSubmit"
          @reset="onReset"
          class="q-gutter-md q-pt-md"
        >
          <q-input
            filled
            v-model="name"
            label="Your name *"
            hint="Name and surname"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Please type something']"
          />

          <q-input
            filled
            type="number"
            v-model="age"
            label="Your age *"
            lazy-rules
            :rules="[
          val => val !== null && val !== '' || 'Please type your age',
          val => val > 0 && val < 100 || 'Please type a real age'
        ]"
          />

          <q-toggle v-model="accept" label="I accept the license and terms"/>

          <div>
            <q-btn label="Submit" type="submit" color="primary"/>
            <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm"/>
          </div>
        </q-form>


      </q-tab-panel>
    </q-card>
  </div>
</template>

<script>
  export default {
    name: "baseDataChange",
    data() {
      return {
        name: null,
        age: null,

        accept: false
      }
    },

  }
</script>

<style scoped>

</style>
