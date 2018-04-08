<template>
  <div id="admin">
    {{msg}}
    <router-view></router-view>
  </div>
</template>

<script>
  //import answer from './admin_components/answer.vue'
  export default {
    name: 'admin',
    data () {
      return {
        msg: 'I am admin',
        question_list: []
      }
    },
    created(){
      //this.$message.error("in admin"),
      this.axios.get('/login')
          .then((response) => {
            //this.$message.success("response get:" + JSON.stringify(response.data.question_list))
            this.question_list = response.data.question_list
            sessionStorage.setItem('Q_list', JSON.stringify(response.data.question_list))
            }
          )
      this.$router.push('/login')
       /* this.$ajax.get('/login')
          .then((response) => {

            }
          )*/
    }
  }
</script>

<style>
  #admin {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
