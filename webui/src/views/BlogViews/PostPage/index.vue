<template>
  <div>
    <b-modal v-if="curerntReplayComment" v-model="showReplyModal" title="回复" @close="handleReplyModalCancel">
      <template v-slot:modal-title>
        回复：<span>{{ curerntReplayComment.author }}</span>
      </template>
      <p v-if="curerntReplayComment.body.length > 50">{{ curerntReplayComment.body.slice(0, 60) }} ...</p>
      <p v-else>{{ curerntReplayComment.body }}</p>
      <div class="d-block">
        <b-form @submit="handleReplyModalOk" @reset="handleReplyModalCancel">
          <div v-if="!isLogin">
            <b-form-group
              id="input-group-1"
              label="你的名字:"
              label-for="input-1"
            >
              <b-form-input
                id="input-1"
                v-model="replyForm.author"
                required
              />
            </b-form-group>
            <b-form-group
              id="input-group-2"
              label="电子邮箱:"
              label-for="input-2"
            >
              <b-form-input
                id="input-2"
                v-model="replyForm.email"
                type="email"
                required
              />
            </b-form-group>
          </div>
          <b-form-group id="input-group-3" label="评论:" label-for="input-3">
            <b-form-textarea
              id="input-3"
              v-model="replyForm.body"
              required
              style="height: 100px;"
            />
          </b-form-group>
          <b-button type="submit" size="sm" variant="outline-secondary">
            提交
          </b-button>
          <b-button style="margin-left: 10px;" type="reset" size="sm" variant="outline-danger">
            取消
          </b-button>
        </b-form>
      </div>
      <template v-slot:modal-footer="{ ok, cancel, hide }">
        <div />
      </template>
    </b-modal>
    <div v-if="postData" class="row">
      <div class="col-md-9">
        <div id="main">
          <div class="post">
            <p class="date">{{ postData.timestamp }}</p>
            <h1 class="post-title">
              <a href="#">
                {{ postData.title }}
              </a>
            </h1>
            <div class="posted">
              <span>类别：</span>
              <b-badge v-for="category in postData.categories" :key="category.name" style="margin-right: 10px;" variant="info">{{ category.name }}</b-badge>
            </div>
            <div class="post_desc">
              {{ postData.description }}
            </div>
            <div class="post_body">
              <mavon-editor
                ref="md"
                :ishljs="true"
                :editable="false"
                :toolbars-flag="false"
                :navigation="true"
                :box-shadow="false"
                style="border: none; z-index: 2000;"
                v-html="postData.body_html"
              />
            </div>
          </div>
          <div class="comment">
            <h5 style="text-align: right;">
              <span>{{ postData.comments.length }} 个评论</span>
            </h5>
            <ul>
              <li v-for="(item, index) in postData.comments" :key="index">
                <div class="comment-body">
                  <div style="padding-top: 10px;" class="d-flex flex-row">
                    <b-badge variant="secondary">#{{ index+1 }}</b-badge>
                    <b-badge variant="info" style="margin: 0 4px;">{{ item.author }}</b-badge>
                    <span>{{ item.timestamp }}</span>
                  </div>
                  <div style="overflow: auto;">
                    <p>{{ item.body }}</p>
                  </div>
                  <div class="can-reply d-flex flex-row-reverse">
                    <button type="button" size="sm" variant="outline-secondary" @click="handleShowReply(item)">回复</button>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          <h5>留下你的评论</h5>
          <b-form @submit="handleReplyOk">
            <div v-if="!isLogin">
              <b-form-group id="input-group-1" label="你的名字:" label-for="input-1">
                <b-form-input
                  id="input-1"
                  v-model="replyForm.author"
                  required
                />
              </b-form-group>
              <b-form-group
                id="input-group-2"
                label="电子邮箱:"
                label-for="input-2"
              >
                <b-form-input
                  id="input-2"
                  v-model="replyForm.email"
                  type="email"
                  required
                />
              </b-form-group>
            </div>

            <b-form-group
              id="input-group-3"
              label="评论:"
              label-for="input-3"
            >
              <b-form-textarea
                id="input-3"
                v-model="replyForm.body"
                required
                style="height: 150px;"
              />
            </b-form-group>
            <b-button type="submit" variant="outline-secondary">提交</b-button>
          </b-form>
        </div>
      </div>
      <div class="col-md-3 category-sidebar-bg">
        <category-sidebar />
      </div>
    </div>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import CategorySidebar from '@/components/CategorySidebar'
import { getPostPublished } from '@/api/post'
import { createCommentAnonymous, createComment } from '@/api/comment'

export default {
  name: 'PostPageIndex',
  components: { CategorySidebar },
  data() {
    return {
      loading: false,
      postId: undefined,
      postData: undefined,
      commentData: [],
      showReplyModal: false,
      replyForm: {
        author: undefined,
        email: undefined,
        body: undefined
      },
      curerntReplayComment: undefined
    }
  },
  computed: {
    isLogin() {
      if (this.$store.getters.token === '' || this.$store.getters.token === undefined) {
        return false
      }
      return true
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      this.loading = true
      const postId = this.$route.query.postId
      getPostPublished(postId).then(res => {
        this.postData = res.data
        this.postId = postId
        this.loading = false
        console.log(this.postData)
      })
    },
    handleShowReply(item) {
      this.curerntReplayComment = item
      this.showReplyModal = true
    },
    handleReplyModalOk(evt) {
      evt.preventDefault()
      this.loading = true
      const data = {
        post_id: this.postId,
        body: this.replyForm.body,
        replied_id: this.curerntReplayComment.id
      }
      this.submitData(data).then(res => {
        this.$message({
          type: 'success',
          message: '评论成功'
        })
        this.reset()
        this.getData()
      })
    },
    handleReplyModalCancel() {
      this.reset()
    },
    submitData(data) {
      return new Promise((resolve, reject) => {
        if (this.isLogin) {
          createComment(data).then(res => {
            return resolve(res)
          }).catch(err => {
            return reject(err)
          })
        } else {
          data['author'] = this.replyForm.author
          data['email'] = this.replyForm.email
          createCommentAnonymous(data).then(res => {
            return resolve(res)
          }).catch(err => {
            return reject(err)
          })
        }
      })
    },
    handleReplyOk(evt) {
      evt.preventDefault()
      this.loading = true
      const data = {
        post_id: this.postId,
        body: this.replyForm.body
      }
      this.submitData(data).then(res => {
        this.$message({
          type: 'success',
          message: '评论成功'
        })
        this.reset()
        this.getData()
      })
    },
    reset() {
      this.replyForm = {
        author: undefined,
        email: undefined,
        body: undefined
      }
      this.curerntReplayComment = undefined
      this.showReplyModal = false
    }
  }
}
</script>

<style scoped>
    #main {
    padding: 10px 10px 10px 10px;
  }

  #main .date {
    padding: 2px 8px;
    margin: 5px 0px 0px 0px;
    border: 1px solid #ccc;
    font-size: 100%;
    color: #666;
    float: right;
    display: inline;
    position: relative;
    top: 4px;
  }
  #main h1 {
    font-size: 170%;
    font-weight: normal;
    line-height: 140%;
    padding-bottom: 5px;
    margin-top: 20px;
  }

  #main p {
    font-size: 120%;
    line-height: 150%;
    margin-bottom: 20px;
  }
  #main .post {
    margin-bottom: 20px;
    /*border-bottom: 1px solid #ccc;*/
  }
  #main h1.post-title a {
    color: #666;
    cursor:pointer;
    text-decoration:none;
  }
  #main h1.post-title a:hover {
    color: black;
  }
  #main .posted {
    font-size: 100%;
    font-weight: normal;
    padding-bottom: 4px;
    margin-bottom: 16px;
    border-bottom: 1px solid #ccc;
  }

  .category-sidebar-bg {
    background-color: #f0f0f0;
    margin-top: 10px;
    height: 100%;
    padding-bottom: 16px;
    padding-top: 16px;
  }

  #main .comment {
    padding: 4px 4px 8px 4px;
    /*border-top: 1px solid #ddd;*/
    font-size: 80%;
  }
  #main .comment ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
  }
  #main .comment ul li {
    padding: 8px;
  }
  #main .comment ul li:nth-child(odd) {
    background-color: #eee;
    border-bottom: 1px solid #ddd;
  }
  #main .comment ul li div.comment-thumbnail {
    width: 60px;
    position: absolute;
  }
  #main .comment ul li div.comment-body {
    /*margin-left: 70px;*/
    overflow: auto;
  }

  .v-note-wrapper{ z-index:1 !important; }
</style>
