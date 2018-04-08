<template>
  <div>
    {{info}}
    <el-card class="box-card">
      <!-- Navigate Row  -->
      <div v-for="(item,index) in Q_list">
        <el-row>
          <el-col :span="10">
            {{item.question}}
          </el-col>
          <el-col :span="10">
            <el-input v-model="item.answer" placeholder="请输入回答"></el-input>
          </el-col>
          <el-col :span="4">
            <el-button type="primary" @click="submit(index)" plain> 返回 </el-button>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data(){
      return {
        info:'以下是回答列表',
        Q_list: []
      }
    },
    methods:{
        submit(index){
            this.axios.patch('/answer',{"question":this.Q_list[index].question,"answer":this.Q_list[index].answer})
              .then((response) => {
                if(response.data.Success){
                  this.$message.success('提交成功!' + index);
//                  var index = Q_list.indexOf(index)
                  if (index > -1) {
                    this.Q_list.splice(index,1)
                  }


                }
                else{
                  this.$message.error("提交失败")
                }
                }
              )
        }
    },
    created(){
      this.Q_list = JSON.parse(sessionStorage.getItem('Q_list'))
      //this.$router.push('/admin')
      //this.$message.error("list is:" + JSON.stringify(this.QA_list))
      //this.$message.error('test:' + this.answerList[1]["answer"])
    }
  }
</script>
