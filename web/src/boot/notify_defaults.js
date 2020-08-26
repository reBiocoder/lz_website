import {Notify} from 'quasar'

Notify.setDefaults({
  icon: 'warning',
  color: 'red-5',
  textColor: 'white',
  position: 'top',
  timeout: 2500,
  actions: [{icon: 'close', color: 'white'}]
})
