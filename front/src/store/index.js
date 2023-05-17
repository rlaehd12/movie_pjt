import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins:[
    createPersistedState(),
  ],
  state: {
    token:null,
  },
  getters: {
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name:'HomeView'})  // store/index,js $ router 접근 불가 ->import 해야됨
    },
    DELETE_TOKEN(state){
      state.token = null
    }
  },
  actions: {
    login(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method:'post',
        url:`${API_URL}/accounts/login/`,
        data:{
          username, password
        }
      })
      .then((res)=>{
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    logout(context, payload){
      axios({
        method:'post',
        url:`${API_URL}/accounts/logout/`,
        headers:{
          Authorization: `Token ${payload}`
        }
      })
      .then((res)=>{
        console.log(res);
        context.commit('DELETE_TOKEN')
      })
      .catch((err)=>{
        console.log(err);
      })
    },
    signUp(context, payload){
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method:'post',
        url:`${API_URL}/accounts/signup/`,
        data: {
          username: username,
          password1: password1,
          password2: password2,
        }
      })
      .then((res)=>{
        console.log(res);
        context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err)=>{
        console.log(err);
      })
    },
  },
  modules: {
  }
})
