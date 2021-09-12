<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="标题">
        <el-input v-model="form.title" />
      </el-form-item>
      <el-form-item label="类别">
        <el-select v-model="form.categories" multiple placeholder="请选择" style="width: 100%;">
          <el-option
            v-for="item in categoryOptions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
      </el-form-item>
      <!--      <el-form-item label="活动时间">-->
      <!--        <el-col :span="11">-->
      <!--          <el-date-picker v-model="form.date1" type="date" placeholder="选择日期" style="width: 100%;" />-->
      <!--        </el-col>-->
      <!--        <el-col class="line" :span="2">-</el-col>-->
      <!--        <el-col :span="11">-->
      <!--          <el-time-picker v-model="form.date2" placeholder="选择时间" style="width: 100%;" />-->
      <!--        </el-col>-->
      <!--      </el-form-item>-->

      <!--      <el-form-item label="活动性质">-->
      <!--        <el-checkbox-group v-model="form.type">-->
      <!--          <el-checkbox label="美食/餐厅线上活动" name="type" />-->
      <!--          <el-checkbox label="地推活动" name="type" />-->
      <!--          <el-checkbox label="线下主题活动" name="type" />-->
      <!--          <el-checkbox label="单纯品牌曝光" name="type" />-->
      <!--        </el-checkbox-group>-->
      <!--      </el-form-item>-->
      <!--      <el-form-item label="特殊资源">-->
      <!--        <el-radio-group v-model="form.resource">-->
      <!--          <el-radio label="线上品牌商赞助" />-->
      <!--          <el-radio label="线下场地免费" />-->
      <!--        </el-radio-group>-->
      <!--      </el-form-item>-->
      <el-form-item label="简介">
        <el-input v-model="form.description" type="textarea" />
      </el-form-item>
      <el-form-item label="主体">
        <mavon-editor
          ref="md"
          v-model="form.content"
          :toolbars="toolbars"
          @change="handleMarkdownChange"
          @save="handleEditorSave"
          @imgAdd="imgAdd"
          @imgDel="imgDel"
        />
      </el-form-item>
      <el-form-item label="发布">
        <el-switch v-model="form.is_published" />
      </el-form-item>
      <el-form-item label="评论">
        <el-switch v-model="form.can_comment" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'Create',
  data() {
    return {
      form: {
        title: '',
        delivery: false,
        type: [],
        resource: '',
        desc: '',
        categories: [],
        can_comment: true,
        is_published: true,
        description: ''
      },
      categoryOptions: [{
        value: '选项1',
        label: '黄金糕'
      }, {
        value: '选项2',
        label: '双皮奶'
      }, {
        value: '选项3',
        label: '蚵仔煎'
      }, {
        value: '选项4',
        label: '龙须面'
      }, {
        value: '选项5',
        label: '北京烤鸭'
      }],
      toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        // imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: true, // 全屏编辑
        readmodel: true, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: true, // 帮助
        /* 1.3.5 */
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        // save: false, // 保存（触发events中的save事件）
        /* 1.4.2 */
        navigation: true, // 导航目录
        /* 2.1.8 */
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true // 预览
      }
    }
  },
  methods: {
    onSubmit() {
      console.log('submit!')
    },
    handleEditorSave(value, render) {
    },
    handleMarkdownChange(value, render) {
    },
    imgAdd(filename, imgfile) {
      const data = new FormData()
      data.append('file', imgfile)
      // uploadAttachment(data).then(res => {
      //   const data = res.data
      //   this.$refs.md.$img2Url(filename, data.url)
      // }).catch(() => {
      //
      // })
    },
    imgDel(filename) {
      // const file_url = filename[0]
      // deleteAttachment({ 'url': file_url }).then(res => {
      // }).catch((err) => {
      //   console.log(err)
      // })
    }
  }
}
</script>

<style scoped>

</style>
