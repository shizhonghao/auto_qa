<template>
  <div>
    <el-row>
      <el-col :span="12" :offset="6">
        一共获得{{ info }}个查询结果
        <el-table
          :data="answerList"
          style="width: 100%">
          <el-table-column
            fixed
            prop="answer"
            lable="答案"
            width="500">
          </el-table-column>
          <el-table-column
            prop="percentage"
            lable="相似度"
            width="200">
            <template slot-scope="scope">
              <el-progress type="circle" :percentage="scope.row.percentage"></el-progress>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <el-row>
      <el-button type="primary" @click="goback" plain> 返回 </el-button>
    </el-row>
  </div>
</template>


<script>
  import ElCol from "element-ui/packages/col/src/col";
  import ElRow from "element-ui/packages/row/src/row";
  export default {
    components: {
      ElRow,
      ElCol},
    name: 'view',
    data(){
        return {
            info:'this is view page',
            answerList:[{answer:'test',percentage:90},{answer:'test2',percentage:80},{answer:'test3',percentage:55}]
        }
    },
    methods:{
        goback(){
            //this.$message.error('goback')
            this.$router.push( '/')
        }

    },
    created(){
        this.answerList = JSON.parse(sessionStorage.getItem("answer")) //storage只能存储字符串的数据，对于JS中常用的数组或对象却不能直接存储。
        this.info = sessionStorage.getItem("cnt")
        //this.$message.error('test:' + this.answerList[1]["answer"])
    }
  }
</script>
