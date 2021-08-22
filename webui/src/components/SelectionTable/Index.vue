<template>
  <el-table
    v-loading="loading"
    ref="table"
    :max-height="maxHeight"
    :data="currentRowData"
    :stripe="true"
    :row-style="{'height':'35px'}"
    :cell-style="{padding:'0px'}"
    :header-row-style="{height:'40px'}"
    :header-cell-style="{padding:'0px'}"
    style="width: 100%;"
    highlight-current-row
    @select="pinSelect"
    @row-click="handleRowClick"
    @selection-change="handleSelectionChange"
  >
    <slot name="selection">
      <el-table-column type="selection" min-width="5%"/>
    </slot>
    <slot/>
  </el-table>
</template>

<script>
export default {
  name: 'SelectionTable',
  props: {
    loading: {
      type: Boolean,
      default: false,
      required: true
    },
    data: {
      type: Array,
      default: () => [],
      required: true
    },
    selectRow: {
      type: Object,
      default: () => {
      },
      required: true
    },
    selectRows: {
      type: Array,
      default: () => [],
      required: true
    },
    maxHeight: {
      type: Number,
      default: undefined
    }
  },
  data() {
    return {
      pinOrigin: -1,
      pin: false
    }
  },
  computed: {
    currentRowData: {
      get() {
        this.addIndex(this.data)
        return this.data
      }
    },
    currentRow: {
      get() {
        return this.selectRow
      },
      set(val) {
        this.$emit('update:selectRow', val)
      }
    },
    currentRows: {
      get() {
        return this.selectRows
      },
      set(val) {
        this.$emit('update:selectRows', val)
      }
    }
  },
  mounted() {
    window.addEventListener('keydown', code => { // 这个是获取键盘按住事件
      if (code.keyCode === 16 && code.shiftKey) { // 判断是否按住shift键，是就把pin赋值为true
        this.pin = true
      }
    })
    window.addEventListener('keyup', code => { // 这个是获取键盘松开事件
      if (code.keyCode === 16) { // 判断是否松开shift键，是就把pin赋值为false
        this.pin = false
      }
    })
  },
  methods: {
    addIndex(data) {
      data.forEach((item, index) => {
        item.index = index
      })
    },
    handleRowClick(row, column, event) {
      this.$refs['table'].clearSelection()
      this.$refs['table'].toggleRowSelection(row)
      this.currentRow = row
    },
    handleSelectionChange(selection) {
      this.currentRows = this.$refs['table'].selection
      this.currentRow = this.$refs['table'].selection.length === 1 ? this.$refs['table'].selection[0] : {}
    },
    pinSelect(item, index) {
      const data = this.$refs['table'].tableData // 获取所以数据
      const origin = this.pinOrigin // 起点数 从-1开始
      const endIdx = index.index // 终点数
      if (this.pin && item.includes(data[origin])) { // 判断按住
        const sum = Math.abs(origin - endIdx) + 1 // 这里记录终点
        const min = Math.min(origin, endIdx) // 这里记录起点
        let i = 0
        while (i < sum) {
          const index = min + i
          this.$refs['table'].toggleRowSelection(data[index], true) // 通过ref打点调用toggleRowSelection方法，第二个必须为true
          i++
        }
      } else {
        this.pinOrigin = index.index // 没按住记录起点
      }
    }
  }
}
</script>

<style scoped>

</style>
