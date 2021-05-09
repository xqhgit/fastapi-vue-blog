<template>
  <div class="row">
    <div class="col-md-8">
      <div id="main">
        <div class="post">
          <p class="date">January 11 2021</p>
          <h1 class="post-title">
            <a href="/post?learn-socket-io-with-python-and-javascript-in-90-minutes">Learn Socket.IO with Python and JavaScript in 90 Minutes!</a>
          </h1>
          <div class="posted">
            由
            <span class="badge badge-danger"><a href="#">Demo</a></span>
            发布
            <span class="badge badge-info"><a href="#">Python</a></span>
            <span class="badge badge-info"><a href="#">JavaScript</a></span>
          </div>
          <div class="post_body">
            <p>
              This is the list of chapters, each with a link to the code for each part of the tutorial:
              This is the list of chapters, each with a link to the code for each part of the tutorial:
              This is the list of chapters, each with a link to the code for each part of the tutorial:
              This is the list of chapters, each with a link to the code for each part of the tutorial:
              This is the list of chapters, each with a link to the code for each part of the tutorial:
            </p>
          </div>
        </div>
        <h4 style="text-align: right;">
          <a>4 个评论</a>
        </h4>
        <div class="comment">
          <ul>
            <li>
              <div class="comment-thumbnail">
                <img src="https://gravatar.com/avatar/411824f056e647134ef0313d04b07ff2?s=60&d=identicon" alt="">
              </div>
              <div class="comment-body">
                <p>
                  <b-badge variant="secondary">#1</b-badge>
                  <b-badge variant="info">demo</b-badge>
                  <span>said</span>
                  <span>2020-12-25T23:42:02Z</span>
                </p>
                <div style="overflow: auto;">
                  <!--<pre>-->
                  <p>Hello World</p>
                  <p>Do you plan to make a paid guide/tutorial on this topic?  If not,do you have any resources that you'd recommend for a beginner, besides your videos?</p>
                  <p>Hello World</p>
                  <!--</pre>-->
                </div>
              </div>
            </li>
            <li>
              <div class="comment-thumbnail">
                <img src="https://gravatar.com/avatar/5d519db99877719f9b497f6bb1edf3c2?s=60&d=identicon" alt="">
              </div>
              <div class="comment-body">
                <p>
                  <b-badge variant="secondary">#2</b-badge>
                  <b-badge variant="danger">admin</b-badge>
                  <span>said</span>
                  <span>2020-12-25T23:42:02Z</span>
                </p>
                <div style="overflow: auto;">
                  <p>@drs: Yes. I don't have a release date yet, but I'm working on a longer React tutorial.</p>
                </div>
              </div>
            </li>
          </ul>
        </div>
        <h3>留下你的评论</h3>
        <b-form>
          <b-form-group id="input-group-1" label="你的名字:" label-for="input-1">
            <b-form-input
              id="input-1"
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
              type="email"
              required
            />
          </b-form-group>
          <b-form-group
            id="input-group-3"
            label="评论:"
            label-for="input-3"
          >
            <b-form-textarea
              id="input-3"
              required
              style="height: 150px;"
            />
          </b-form-group>
        </b-form>
        <b-button type="submit" variant="outline-secondary">提交</b-button>
      </div>
    </div>
    <div class="col-md-4 sidebar-bg">
      <sidebar />
    </div>
  </div>

</template>

<script>
// import { getPosts } from '@/api/posts'
import Sidebar from '@/components/Siderbar'

export default {
  name: 'Posts',
  components: {
    Sidebar
  },
  data() {
    return {
      total: 0,
      items: [],
      query: {
        page: 1,
        limit: 10
      }
    }
  },
  created() {
  },
  methods: {
    getData() {
      // getPosts(this.query).then(response => {
      //   this.total = response.data.total
      //   this.items = response.data.items
      // })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /*div {*/
    /*display: block;*/
  /*}*/
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
  #main h3 {
    font-size: 150%;
    font-weight: normal;
  }
  #main h4 {
    font-size: 120%;
    font-weight: normal;
  }
  #main h4 a {
    color: #66a;
  }

  #main p {
    font-size: 120%;
    line-height: 150%;
    margin-bottom: 20px;
  }
  #main .post {
    margin-bottom: 20px;
  }
  .main h1.post-title {
    color: #666;
    padding-bottom: 0;
    margin-bottom: 0;
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
  #main .post_more a {
    color: #66a;
  }
  #main .posted span a {
    color: #eee;
  }
  #main .comment {
    padding: 4px 4px 8px 4px;
    border-top: 1px solid #ddd;
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
    margin-left: 70px;
    overflow: auto;
  }
  /*#main .comment pre {*/
    /*padding: 0px 0px;*/
    /*font-size: 95%;*/
    /*white-space: pre-wrap;*/
    /*word-break: break-word;*/
    /*color: #222;*/
    /*background-color: inherit;*/
    /*border: 0px;*/
  /*}*/
  #main .comment p {
    margin-bottom: 5px;
  }

  /*#main p {*/
    /*font-size: 120%;*/
    /*line-height: 150%;*/
    /*margin-bottom: 20px;*/
  /*}*/
  /*p {*/
    /*margin: 0 0 10px;*/
  /*}*/

  img {
    vertical-align: middle;
  }
  .sidebar-bg {
    background-color: #f0f0f0;
    margin-top: 10px;
    height: 100%;
    padding-bottom: 16px;
    padding-top: 16px;
  }
</style>
