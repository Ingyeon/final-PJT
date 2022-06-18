import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from '../src/store/index'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

// fontAwesome
import { library } from "@fortawesome/fontawesome-svg-core"
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"
import { faHatWizard } from '@fortawesome/free-solid-svg-icons'

import {fas} from '@fortawesome/free-solid-svg-icons'
import {far} from '@fortawesome/free-regular-svg-icons'

library.add(faHatWizard, fas, far)
Vue.component('font-awesome-icon', FontAwesomeIcon)

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
