<template>
  <div class="manage-post">
    <el-page-header content="创建文章" @back="goBack"/>
    <el-form ref="form" :model="form" label-width="80px" style="margin-top: 20px">
      <el-row>
        <el-col :span="24">
          <el-form-item label="标题">
            <el-input v-model="form.name" clearable />
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="分类">
            <el-select v-model="form.category_id" placeholder="请选择" clearable >
              <el-option
                v-for="item in categoryOptions"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="发布">
            <el-radio-group v-model="form.is_publish" style="margin-top: 6px">
              <el-radio v-for="dict in boolOptions" :key="dict.value" :label="dict.value">{{ dict.label }}</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="可以评论">
            <el-radio-group v-model="form.can_comment" style="margin-top: 6px">
              <el-radio v-for="dict in boolOptions" :key="dict.value" :label="dict.value">{{ dict.label }}</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
        <mavon-editor
          v-model="form.content"
          @change="handleMarkdownChange"
          @save="handleEditorSave"
          @imgAdd="imgAdd"
          @imgDel="imgDel"
        />
      </el-form-item>
      <el-form-item>
        <el-button style="margin-top:5px;" type="primary" icon="el-icon-document">
          提交
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'ManagePost',
  data() {
    return {
      form: {
        title: undefined,
        is_publish: true,
        can_comment: true,
        category_id: undefined,
        content: '',
        summary: ''
      },
      categoryOptions: [],
      boolOptions: [
        { label: '是', value: true },
        { label: '否', value: false }
      ]
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    },
    handleEditorSave(value, render) {
      console.log(value)
      console.log(render)
    },
    handleMarkdownChange(value, render) {
    },
    imgAdd(filename, imgfile) {
      console.log(filename)
      console.log(imgfile)
    },
    imgDel(filename) {

    }
  }
}
</script>

<style scoped>

</style>
