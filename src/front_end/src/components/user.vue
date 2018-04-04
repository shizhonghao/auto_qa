<template>
  <div>
    <el-row>
      <el-col :span="12" :offset="6">
        <div style="margin-top: 15px;">
          <el-input placeholder="请输入内容" v-model="question" class="input-with-select">
            <el-select v-model="select" slot="prepend" placeholder="请选择">
              <el-option label="餐厅名" value="1"></el-option>
              <el-option label="订单号" value="2"></el-option>
              <el-option label="用户电话" value="3"></el-option>
            </el-select>
            <el-button slot="append"  @click="query" icon="el-icon-search"></el-button>
          </el-input>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import ElRow from "element-ui/packages/row/src/row";
  import ElCol from "element-ui/packages/col/src/col";
export default {
  components: {
    ElCol,
    ElRow},
  name: 'main',
  data () {
    return {
      question:''
    }
  },
  methods:{
      query(){
        if(this.question==''){
            this.$message.error('请输入要查询的问题')
        }else{
            this.$ajax({
              method:'get',
              url:encodeURI('http://localhost:5000/query?question='.concat(this.question))
            })
              .then((response) => {
                //this.$message.error('type:' + response.data.cnt)
                sessionStorage.setItem('answer',JSON.stringify(response.data.answer))
                sessionStorage.setItem('cnt',response.data.cnt)
                this.$router.push('/view')
              })
              .catch((error) => {
                console.log(error)
                })
          //this.$message.error('/query?question='.concat(this.question))
        }
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
